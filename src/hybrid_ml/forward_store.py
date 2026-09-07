"""Phase H3/H4 — forward observation database.

Append-only store: one row per ASSET x COMPLETED 1H BAR.
Parquet is primary; CSV kept for inspection. Outcome fields are written as
NA at observation time and filled only by resolve_forward_outcomes.py.
Duplicate observation_ids are skipped (safe to run repeatedly).
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

FWD_DIR = ROOT / "data" / "forward"
OBS_PARQUET = FWD_DIR / "phase_h_observations.parquet"
OBS_CSV = FWD_DIR / "phase_h_observations.csv"

OUTCOME_COLS = ["future_return_1h", "future_return_3h", "future_return_6h",
                "future_return_12h", "future_return_24h",
                "mr_outcome", "mr_failure_realized",
                "runner_return_osc_cross", "runner_return_hybrid",
                "resolved_at"]

FEATURE_COLS = ["er_10", "er_20", "er_40", "atr", "natr", "vol_ratio",
                "cross_count", "osc", "signal", "osc_minus_signal",
                "osc_slope_1", "osc_slope_3", "osc_abs",
                "price_direction_12", "price_direction_24"]

OHLCV = ["open", "high", "low", "close", "volume"]


def observation_columns() -> list:
    """Full ordered column list for the observation store."""
    base = ["observation_id", "asset", "timestamp", "scored_at", "data_source",
            "position_state", "open", "high", "low", "close", "volume"]
    feats = FEATURE_COLS
    model = ["p_mr_win", "p_mr_fail", "pred_mr_return_pct",
             "p_runner_win", "pred_runner_return_pct",
             "mr_fail_threshold", "mr_eligible", "runner_model_positive",
             "asset_policy", "decision",
             "runner_exit_policy_a", "runner_exit_policy_b",
             "model_version", "config_version"]
    outcomes = ["future_return_1h", "future_return_3h", "future_return_6h",
                "future_return_12h", "future_return_24h",
                "mr_outcome", "mr_failure_realized",
                "runner_return_osc_cross", "runner_return_hybrid", "resolved_at"]
    return base + feats + model + outcomes


def load_observations() -> "pd.DataFrame":
    """Load existing observations (parquet preferred, CSV fallback)."""
    if OBS_PARQUET.exists():
        return pd.read_parquet(OBS_PARQUET)
    if OBS_CSV.exists():
        return pd.read_csv(OBS_CSV)
    return pd.DataFrame()


def append_observation(row: dict) -> str:
    """Append one observation row. Skips duplicates by observation_id.

    Returns "APPENDED" | "SKIP — already scored".
    """
    import json
    FWD_DIR.mkdir(parents=True, exist_ok=True)
    oid = row["observation_id"]
    existing = load_observations()
    if len(existing) and oid in set(existing["observation_id"]):
        print(f"SKIP — already scored: {oid}")
        return "SKIP"
    new = pd.DataFrame([row])
    if existing.empty:
        df = new
    else:
        df = pd.concat([existing, new], ignore_index=True)
    # normalize timestamp column to tz-naive strings for consistent parquet
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True) \
            .dt.tz_convert(None).astype(str)
    df.to_parquet(OBS_PARQUET, index=False)
    df.to_csv(OBS_CSV, index=False)
    return "APPENDED"


def empty_outcomes() -> dict:
    """Outcome columns initialized to NA — never populated at write time."""
    return {c: None for c in
            ["future_return_1h", "future_return_3h", "future_return_6h",
             "future_return_12h", "future_return_24h",
             "mr_outcome", "mr_failure_realized",
             "runner_return_osc_cross", "runner_return_hybrid", "resolved_at"]}
