"""Phase H12 — latest score report (evidence, not trade commands).

Reads the forward observation store and reports model evidence + deterministic
policy decision per asset. Actions never include TF_ENTRY or RUNNER_ENTRY.
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import asset_items, load_config
from hybrid_ml.price_io import find_asset_price_file, load_price_csv
from hybrid_ml.features import build_features
from hybrid_ml.bar_control import get_latest_completed_bar
from hybrid_ml.positions import load_positions, get_state
from hybrid_ml.mr_policy import evaluate_mr, detect_mr_setup
from hybrid_ml.freeze import get_model_version

VALID_ACTIONS = {"NO_ACTION", "WATCH_MR", "MR_ELIGIBLE", "MR_BLOCK", "HOLD_MR",
                 "MR_TP1_TRANSITION", "HOLD_RUNNER", "EXIT_RUNNER",
                 "RESEARCH_ONLY", "STALE_DATA"}
FORBIDDEN = {"TF_ENTRY", "RUNNER_ENTRY"}


def latest_evidence_row(asset, cfg, positions):
    """Build one evidence row for the asset's latest completed bar."""
    from hybrid_ml.scoring import score_latest
    from hybrid_ml.mr_policy import detect_mr_setup
    p = find_asset_price_file(ROOT / "data/prices", asset)
    px = load_price_csv(p)
    feats = build_features(px, cfg).reset_index(drop=True)
    ts = feats["timestamp"]
    i = len(feats) - 1
    fr = feats.iloc[i].copy()
    fr["osc_prev"] = feats.iloc[i - 1]["osc"]
    fr["signal_prev"] = feats.iloc[i - 1]["signal"]
    s = score_latest(feats.iloc[[i]], ROOT / "models", cfg)
    st = get_state(positions, asset)

    mr = s[s.engine == "MR"]
    rn = s[s.engine == "RUNNER"]
    p_mr_win = float(mr.iloc[0]["p_win"]) if len(mr) else None
    p_mr_fail = float(mr.iloc[0].get("p_mr_fail")) if len(mr) and pd.notna(mr.iloc[0].get("p_mr_fail")) else None
    pred_mr = float(mr.iloc[0]["expected_return_pct"]) if len(mr) else None
    p_run = float(rn.iloc[0]["p_win"]) if len(rn) else None
    pred_run = float(rn.iloc[0]["expected_return_pct"]) if len(rn) else None

    setup = detect_mr_setup(fr)
    gate_pass = p_mr_fail is not None and p_mr_fail <= 0.45
    mr_eligible = setup["setup"] and gate_pass and asset != "US500"

    # deterministic action
    st_state = st["state"]
    if st_state in ("MR_LONG", "MR_SHORT"):
        action = "HOLD_MR"
        reason = "position active"
    elif st_state in ("RUNNER_LONG", "RUNNER_SHORT"):
        action = "HOLD_RUNNER" if (pred_run or 0) > 0 else "EXIT_RUNNER"
        reason = "runner lifecycle (position management only)"
    elif asset == "US500":
        action, reason = "RESEARCH_ONLY", "US500 research-only for MR"
    elif mr_eligible:
        action, reason = "MR_ELIGIBLE", setup["reason"]
    elif setup["setup"] and not gate_pass:
        action, reason = "MR_BLOCK", "BLOCK_FAIL_RISK"
    elif setup["setup"]:
        action, reason = "MR_BLOCK", "BLOCK_ASSET_POLICY"
    else:
        action, reason = "NO_ACTION", "no setup"

    return {
        "asset": asset, "timestamp": str(fr["timestamp"]),
        "data_status": "OK", "position_state": st_state,
        "p_mr_win": p_mr_win, "p_mr_fail": p_mr_fail,
        "pred_mr_return_pct": pred_mr,
        "mr_setup": setup["setup"], "mr_gate_pass": gate_pass,
        "mr_eligible": mr_eligible,
        "p_runner_win": p_run, "pred_runner_return_pct": pred_run,
        "runner_state_active": st_state in ("RUNNER_LONG", "RUNNER_SHORT"),
        "asset_policy": "RESEARCH_ONLY" if asset == "US500" else "ACTIVE",
        "recommended_action": action, "reason": reason,
    }


def main():
    cfg = load_config()
    positions = load_positions()
    rows = []
    print("Phase H — latest-bar evidence report\n")
    for asset, _ in asset_items(cfg, forward_research=True):
        try:
            r = latest_evidence_row(asset, cfg, positions)
            rows.append(r)
            print(f"[{asset}] {r['data_status']}  state={r['position_state']}  "
                  f"p_fail={r['p_mr_fail'] if r['p_mr_fail'] is not None else 'n/a'}  "
                  f"setup={r['mr_setup']}  gate={r['mr_gate_pass']}  "
                  f"-> {r['recommended_action']}")
        except Exception as e:
            rows.append({"asset": asset, "data_status": "ERROR",
                         "recommended_action": "STALE_DATA", "reason": str(e)})
            print(f"{asset}: ERROR — {e}")
    df = pd.DataFrame(rows)
    assert not set(df.get("recommended_action", [])) & FORBIDDEN, "forbidden action generated"
    df.to_csv(ROOT / "reports" / "latest_scores.csv", index=False)
    print("\nSaved reports/latest_scores.csv")


if __name__ == "__main__":
    from hybrid_ml.positions import load_positions
    main()
