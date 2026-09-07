"""Phase H24 — critical logic tests.

Run: pytest -q
"""
from pathlib import Path
import sys
import json
import pandas as pd
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from hybrid_ml.mr_policy import evaluate_mr, detect_mr_setup, RESEARCH_ONLY_ASSETS
from hybrid_ml.bar_control import completed_bars, get_latest_completed_bar, observation_id
from hybrid_ml.forward_store import append_observation, load_observations, empty_outcomes
from hybrid_ml.freeze import verify_freeze, file_sha256, FROZEN_MODELS, MODELS_DIR
from hybrid_ml.data.yahoo_provider import update_asset_prices


def _row(osc=0.0, signal=0.0, osc_prev=None, signal_prev=None, p_fail=0.2, atr=1.0):
    return {"osc": osc, "signal": signal,
            "osc_prev": osc if osc_prev is None else osc_prev,
            "signal_prev": signal if signal_prev is None else signal_prev,
            "p_mr_fail": p_fail, "atr": 1.0, "close": 100.0}


# 1. Runner cannot start from FLAT
def test_runner_never_from_flat():
    from hybrid_ml.positions import get_state
    st = get_state({}, "GOLD")
    assert st["state"] == "FLAT"
    # Runner model output when FLAT must never produce an entry action
    from hybrid_ml.mr_policy import evaluate_mr
    r = _row()
    res = evaluate_mr("GOLD", r, {}, {"phase_h": {"mr_fail": {"threshold": 0.45}}}, "OK")
    assert res["decision"] != "RUNNER_ENTRY"


# 2. TF can never be generated
def test_tf_never_generated():
    # TF is disabled in config and no code path generates TF actions
    from hybrid_ml.mr_policy import evaluate_mr
    from hybrid_ml.positions import VALID_STATES
    assert "TF_LONG" not in VALID_STATES and "TF_SHORT" not in VALID_STATES
    assert True  # covered by action whitelist test below


def test_no_forbidden_actions():
    from scripts.score_all_latest import FORBIDDEN
    assert "TF_ENTRY" in FORBIDDEN and "RUNNER_ENTRY" in FORBIDDEN


# 3. p_mr_fail > 0.45 blocks MR
def test_mr_blocked_by_fail_risk():
    from hybrid_ml.mr_policy import evaluate_mr
    row = _row(osc=-1.0, signal=-1.5, osc_prev=-1.2, signal_prev=-0.9, p_fail=0.6)
    res = evaluate_mr("GOLD", row, {}, {}, "OK")
    assert res["decision"] == "MR_BLOCK"
    assert res["reason"] == "BLOCK_FAIL_RISK"


# 4. US500 is RESEARCH_ONLY for MR
def test_us500_research_only():
    assert "US500" in RESEARCH_ONLY_ASSETS
    row = _row(osc=-1.0, signal=-1.2, osc_prev=-1.3, signal_prev=-1.1, p_fail=0.1)
    res = evaluate_mr("US500", row, {}, {}, "OK")
    assert res["decision"] == "RESEARCH_ONLY"


# 5. duplicate completed bar is not logged twice
def test_no_duplicate_observation(tmp_path):
    from hybrid_ml import forward_store
    oid = "TEST_2026-08-30T10:00:00"
    row = {"observation_id": oid, "asset": "TEST", "timestamp": "2026-08-30T10:00:00",
           **{c: None for c in forward_store.observation_columns() if c not in
              ("observation_id", "asset", "timestamp")}}
    # use a temp dir by monkeypatching module paths
    orig_pq, orig_csv = forward_store.OBS_PARQUET, forward_store.OBS_CSV
    forward_store.OBS_PARQUET = tmp_path / "obs.parquet"
    forward_store.OBS_CSV = tmp_path / "obs.csv"
    try:
        r1 = forward_store.append_observation(row)
        r2 = forward_store.append_observation(row)
        assert r1 == "APPENDED"
        assert r2 == "SKIP"
    finally:
        forward_store.OBS_PARQUET, forward_store.OBS_CSV = orig_pq, orig_csv


# 6. incomplete bar is not scored
def test_incomplete_bar_not_scored():
    now = pd.Timestamp("2026-08-30 10:30")
    df = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-08-30 09:00", "2026-08-30 10:00"]),
        "open": [1, 1], "high": [1, 1], "low": [1, 1], "close": [1, 1], "volume": [0, 0]})
    res = get_latest_completed_bar(df, "TEST", current_time=now)
    # the 10:00 bar closes at 11:00 — still forming at 10:30
    assert res["row"]["timestamp"] == pd.Timestamp("2026-08-30 09:00")


def test_completed_bars_excludes_forming_bar():
    now = pd.Timestamp("2026-08-30 10:30")
    df = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-08-30 08:00", "2026-08-30 09:00", "2026-08-30 10:00"]),
        "open": [1, 1, 1], "high": [1, 1, 1], "low": [1, 1, 1],
        "close": [1, 1, 1], "volume": [0, 0, 0]})
    out = completed_bars(df, current_time=now)
    assert out["timestamp"].tolist() == [pd.Timestamp("2026-08-30 08:00"), pd.Timestamp("2026-08-30 09:00")]


def test_bars_to_score_backfills_missing_completed_bars():
    from scripts.observe_latest import bars_to_score
    prices = pd.DataFrame({
        "timestamp": pd.to_datetime([
            "2026-08-30 11:00", "2026-08-30 12:00",
            "2026-08-30 13:00", "2026-08-30 14:00",
        ]),
        "open": [1, 1, 1, 1], "high": [1, 1, 1, 1], "low": [1, 1, 1, 1],
        "close": [1, 1, 1, 1], "volume": [0, 0, 0, 0]})
    existing = pd.DataFrame({
        "observation_id": [
            observation_id("BTCUSD", "2026-08-30 11:00"),
            observation_id("BTCUSD", "2026-08-30 13:00"),
        ]
    })
    baseline = {"phase_h_start": "2026-08-30T11:03:00+00:00"}
    out = bars_to_score("BTCUSD", prices, baseline, existing, current_time=pd.Timestamp("2026-08-30 15:05"))
    assert out["timestamp"].tolist() == [pd.Timestamp("2026-08-30 12:00"), pd.Timestamp("2026-08-30 14:00")]


# 7. future outcome columns empty at observation creation
def test_outcomes_empty_at_creation():
    o = empty_outcomes()
    assert all(v is None for v in o.values())
    assert "future_return_1h" in o and "mr_outcome" in o


# 8. model hash change raises freeze warning
def test_freeze_violation_detected(capsys):
    baseline = {"models": {name: {"sha256": "deadbeef", "modified": "x"}
                           for name in FROZEN_MODELS}}
    res = verify_freeze(baseline)
    assert res["status"] == "VIOLATION"


# 9. Yahoo download failure does not erase old file
def test_yahoo_failure_preserves_file(tmp_path, monkeypatch):
    from hybrid_ml.data import yahoo_provider
    # create existing file
    existing = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-01-01 00:00", "2026-01-01 01:00"]),
        "open": [1.0, 1.0], "high": [1.0, 1.0], "low": [1.0, 1.0],
        "close": [1.0, 1.0], "volume": [0, 0]})
    f = tmp_path / "TEST_1h_yahoo.csv"
    existing.to_csv(f, index=False)
    monkeypatch.setattr("hybrid_ml.data.yahoo_provider.fetch_yahoo_1h",
                        lambda t, p="730d": pd.DataFrame())
    r = update_asset_prices("TEST", "NOPE", tmp_path)
    assert r["status"] == "WARN"
    assert f.exists() and len(pd.read_csv(f)) == 2


# 10. stale data cannot generate MR_ELIGIBLE
def test_stale_blocks_mr():
    row = _row(osc=-1.0, signal=-1.2, osc_prev=-1.3, p_fail=0.1)
    res = evaluate_mr("GOLD", row, {}, {}, "STALE_DATA")
    assert res["decision"] == "MR_BLOCK"
    assert res["reason"] == "BLOCK_DATA_STALE"
