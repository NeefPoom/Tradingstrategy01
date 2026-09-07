"""Score completed Phase H bars and append forward observations.

This script never retrains, never enables TF, never opens a Runner from FLAT,
and never writes outcome fields. It backfills missed scheduler runs by scoring
all completed Phase H bars that do not already have observation IDs.
"""
from __future__ import annotations

from pathlib import Path
import json
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.bar_control import bar_meta, completed_bars, get_latest_completed_bar, observation_id
from hybrid_ml.config import asset_items, load_config
from hybrid_ml.features import build_features
from hybrid_ml.forward_mr import append_mr_candidate
from hybrid_ml.forward_store import append_observation, empty_outcomes, load_observations
from hybrid_ml.freeze import ensure_baseline, get_model_version, verify_freeze
from hybrid_ml.mr_policy import detect_mr_setup, evaluate_mr
from hybrid_ml.positions import MR_STATES, get_state, load_positions
from hybrid_ml.price_io import find_asset_price_file, load_price_csv


MR_FAIL_THRESHOLD = 0.45


def _model_evidence(feat_row, models_dir):
    """Score one feature row with frozen models."""
    import joblib

    md = Path(models_dir)
    cols = json.loads((md / "feature_columns.json").read_text(encoding="utf-8"))
    x = feat_row.to_frame().T.reindex(columns=cols)
    ev = {
        "p_mr_win": None,
        "p_mr_fail": None,
        "pred_mr_return_pct": None,
        "p_runner_win": None,
        "pred_runner_return_pct": None,
    }
    try:
        ev["p_mr_win"] = float(joblib.load(md / "mr_win_classifier.joblib").predict_proba(x)[0, 1])
        ev["pred_mr_return_pct"] = float(joblib.load(md / "mr_return_regressor.joblib").predict(x)[0])
        ev["p_mr_fail"] = float(joblib.load(md / "mr_fail_classifier.joblib").predict_proba(x)[0, 1])
    except Exception:
        pass
    try:
        ev["p_runner_win"] = float(joblib.load(md / "runner_win_classifier.joblib").predict_proba(x)[0, 1])
        ev["pred_runner_return_pct"] = float(joblib.load(md / "runner_return_regressor.joblib").predict(x)[0])
    except Exception:
        pass
    return ev


def detect_runner_transition(prev_state: dict, feat_row) -> bool:
    """MR to Runner transition: MR position reached oscillator zero."""
    state = prev_state.get("state")
    if state not in MR_STATES:
        return False
    osc = float(feat_row["osc"])
    if state == "MR_LONG" and osc >= 0:
        return True
    if state == "MR_SHORT" and osc <= 0:
        return True
    return False


def _phase_start_floor(baseline) -> pd.Timestamp | None:
    raw = baseline.get("phase_h_start")
    if not raw:
        return None
    ts = pd.Timestamp(raw)
    if getattr(ts, "tzinfo", None) is not None:
        ts = ts.tz_convert(None)
    return ts.floor("h")


def _asset_forward_start_floor(asset_meta, baseline) -> pd.Timestamp | None:
    raw = (asset_meta or {}).get("forward_start_utc")
    if not raw:
        return _phase_start_floor(baseline)
    ts = pd.Timestamp(raw)
    if getattr(ts, "tzinfo", None) is not None:
        ts = ts.tz_convert(None)
    return ts.floor("h")


def bars_to_score(asset, prices, baseline, existing_observations, current_time=None, asset_meta=None) -> pd.DataFrame:
    """Return completed Phase H bars without existing observations.

    This fills missed hourly scheduler runs but does not backfill the entire
    historical price file. For an asset with no post-start market bars yet,
    the first baseline observation may use the latest completed pre-start bar.
    """
    done = completed_bars(prices, current_time=current_time)
    if done.empty:
        return done

    has_explicit_forward_start = bool((asset_meta or {}).get("forward_start_utc"))
    forward_start = _asset_forward_start_floor(asset_meta, baseline)
    timestamps = pd.to_datetime(done["timestamp"], errors="coerce")
    candidates = done[timestamps >= forward_start].copy() if forward_start is not None else done.tail(1).copy()
    if candidates.empty:
        if has_explicit_forward_start:
            return candidates
        candidates = done.tail(1).copy()

    existing_ids = set()
    if len(existing_observations) and "observation_id" in existing_observations:
        existing_ids = set(existing_observations["observation_id"].astype(str))

    mask = [observation_id(asset, row["timestamp"]) not in existing_ids for _, row in candidates.iterrows()]
    return candidates.loc[mask].sort_values("timestamp").reset_index(drop=True)


def _feature_row_for_timestamp(feats: pd.DataFrame, timestamp):
    fidx = feats.index[feats["timestamp"] == pd.Timestamp(timestamp)]
    if len(fidx) == 0:
        raise ValueError("feature row missing")
    i = int(fidx[-1])
    if i < 1:
        raise ValueError("insufficient feature history")
    fr = feats.iloc[i].copy()
    fr["osc_prev"] = feats.iloc[i - 1]["osc"]
    fr["signal_prev"] = feats.iloc[i - 1]["signal"]
    return fr


def process_completed_bar(asset, cfg, positions, model_version, feats, target_row):
    """Score one completed bar and write append-only research rows."""
    timestamp = target_row["timestamp"]
    meta = bar_meta(asset, timestamp, status="OK")
    fr = _feature_row_for_timestamp(feats, timestamp)
    ev = _model_evidence(fr, ROOT / "models")
    state = get_state(positions, asset)
    oid = observation_id(asset, timestamp)
    mr = evaluate_mr(asset, fr, ev, cfg, meta["status"])

    obs = {
        "observation_id": oid,
        "asset": asset,
        "timestamp": meta["source_bar_timestamp"],
        "scored_at": meta["scored_at"],
        "data_source": "yahoo",
        "position_state": state["state"],
        **{
            c: float(fr[c]) if pd.notna(fr.get(c)) else None
            for c in [
                "open",
                "high",
                "low",
                "close",
                "volume",
                "er_10",
                "er_20",
                "er_40",
                "atr",
                "natr",
                "vol_ratio",
                "cross_count",
                "osc",
                "signal",
                "osc_minus_signal",
                "osc_slope_1",
                "osc_slope_3",
                "osc_abs",
                "price_direction_12",
                "price_direction_24",
            ]
        },
        "p_mr_win": ev.get("p_mr_win"),
        "p_mr_fail": ev.get("p_mr_fail"),
        "pred_mr_return_pct": ev.get("pred_mr_return_pct"),
        "p_runner_win": ev.get("p_runner_win"),
        "pred_runner_return_pct": ev.get("pred_runner_return_pct"),
        "mr_fail_threshold": MR_FAIL_THRESHOLD,
        "mr_eligible": mr["decision"] == "MR_ELIGIBLE",
        "runner_model_positive": (ev.get("pred_runner_return_pct") or 0) > 0,
        "asset_policy": "RESEARCH_ONLY" if asset == "US500" else "ACTIVE",
        "decision": mr["decision"],
        "runner_exit_policy_a": "FIXED_2ATR",
        "runner_exit_policy_b": "OSC_CROSS",
        "model_version": model_version,
        "config_version": "phase_h_2026-08-30",
        **empty_outcomes(),
    }
    append_result = append_observation(row=obs)
    if append_result == "APPENDED":
        print(f"{asset}: observation appended ({meta['source_bar_timestamp']})")

    setup = detect_mr_setup(fr)
    if setup["setup"]:
        cand = {
            "candidate_id": f"{asset}_{pd.Timestamp(timestamp).isoformat()}",
            "asset": asset,
            "timestamp": timestamp,
            "direction": setup["direction"],
            "entry_price": float(fr["close"]),
            "p_mr_win": ev.get("p_mr_win"),
            "p_mr_fail": ev.get("p_mr_fail"),
            "pred_mr_return_pct": ev.get("pred_mr_return_pct"),
            "threshold": MR_FAIL_THRESHOLD,
            "decision": mr["decision"],
            "decision_reason": mr["reason"],
            "mr_outcome": None,
            "mr_return_pct": None,
            "mr_failure_realized": None,
            "blocked_winner": None,
            "blocked_loser": None,
            "resolved_at": None,
        }
        append_mr_candidate(cand)

    if state["state"] in MR_STATES and detect_runner_transition(state, fr):
        print(f"{asset}: MR TP1 transition detected -> RUNNER state (research)")

    return {
        "asset": asset,
        "status": meta["status"],
        "decision": mr["decision"],
        "observation_id": oid,
        "append_result": append_result,
    }


def process_asset(asset, cfg, positions, baseline, model_version, asset_meta=None):
    """Backfill all unscored completed Phase H bars for one asset."""
    try:
        price_path = find_asset_price_file(ROOT / "data/prices", asset)
        prices = load_price_csv(price_path)
    except Exception as exc:
        return {"asset": asset, "status": "FAILED", "reason": str(exc)}

    latest = get_latest_completed_bar(prices, asset)
    if not latest.get("is_completed"):
        return {"asset": asset, "status": "STALE_DATA", "reason": latest.get("reason")}
    if latest["meta"]["status"] == "STALE_DATA":
        print(f"{asset}: STALE_DATA (bar age {latest['meta']['bar_age_hours']}h) - no action")
        return {"asset": asset, "status": "STALE_DATA"}

    targets = bars_to_score(asset, prices, baseline, load_observations(), asset_meta=asset_meta)
    if targets.empty:
        return {"asset": asset, "status": latest["meta"]["status"], "decision": "NO_NEW_COMPLETED_BAR"}

    feats = build_features(prices, cfg)
    results = []
    for _, target_row in targets.iterrows():
        results.append(process_completed_bar(asset, cfg, positions, model_version, feats, target_row))

    appended = sum(1 for r in results if r.get("append_result") == "APPENDED")
    print(f"{asset}: backfill checked {len(targets)} completed bar(s), appended {appended}")
    last = results[-1]
    last["appended_count"] = appended
    return last


def main():
    cfg = load_config()
    baseline = ensure_baseline(cfg)
    freeze = verify_freeze(baseline)
    if freeze["status"] == "VIOLATION":
        print("WARNING: PHASE H MODEL FREEZE VIOLATION - investigate before continuing")

    positions = load_positions()
    model_version = get_model_version()
    results = {}
    for asset, asset_meta in asset_items(cfg, forward_research=True):
        try:
            results[asset] = process_asset(asset, cfg, positions, baseline, model_version, asset_meta)
            print(f"{asset}: {results[asset]['status']} ({results[asset].get('decision', '')})")
        except Exception as exc:
            results[asset] = {"asset": asset, "status": "FAILED", "reason": str(exc)}
            print(f"{asset}: FAILED - {exc}")
    return results


if __name__ == "__main__":
    main()
