"""Phase H8 — resolve forward outcomes.

For observations whose future price path is now known, resolve:
  - future returns (1h/3h/6h/12h/24h)
  - hypothetical MR outcomes for BOTH accepted and blocked candidates
    (counterfactual analysis: did MR_FAIL block bad trades? did it block winners?)

Never touches observation rows whose future window is not yet complete.
"""
from pathlib import Path
import sys
import pandas as pd
import numpy as np
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import load_config
from hybrid_ml.price_io import find_asset_price_file, load_price_csv
from hybrid_ml.forward_store import load_observations, OBS_PARQUET, OBS_CSV, FWD_DIR
from hybrid_ml.forward_mr import (load_mr_candidates, MR_CAND_PARQUET,
                                  MR_CAND_CSV, load_runner_events,
                                  RUNNER_PARQUET, RUNNER_CSV)

HORIZONS = {"future_return_1h": 1, "future_return_3h": 3, "future_return_6h": 6,
            "future_return_12h": 12, "future_return_24h": 24}


def future_return(px: "pd.DataFrame", ts: pd.Timestamp, hours: int):
    """Close-to-close return over `hours` bars after ts. None if unavailable."""
    x = px.sort_values("timestamp").reset_index(drop=True)
    idx = x.index[x["timestamp"] == ts]
    if len(idx) == 0:
        return None
    i = int(idx[-1])
    j = i + hours
    if j >= len(x):
        return None
    p0, p1 = float(x.iloc[i]["close"]), float(x.iloc[j]["close"])
    return (p1 - p0) / p0 * 100.0


def resolve_mr_outcome(px, row):
    """Resolve hypothetical MR outcome using frozen original MR logic.

    MR lifecycle (deterministic): entry at candidate close; stop = 1 ATR
    against direction; TP1 = 1 ATR in direction (MR success); failure when
    stop hit before TP1. Resolved bar-by-bar, no look-ahead.
    """
    i = px.index[px["timestamp"] >= pd.Timestamp(row["timestamp"])]
    if len(i) == 0:
        return None
    i0 = int(i[0])
    if i0 + 1 >= len(px):
        return None  # not enough future bars yet
    direction = 1 if row["direction"] == "LONG" else -1
    entry = float(row["entry_price"])
    atr_val = float(row["atr"]) if pd.notna(row.get("atr")) else None
    if not atr_val or atr_val <= 0:
        return None
    tp = entry + direction * atr_val
    stop = entry - direction * 1.0 * atr_val
    high, low, close = px["high"].values, px["low"].values, px["close"].values
    for j in range(i0 + 1, min(i0 + 200, len(px))):
        if (direction == 1 and low[j] <= stop) or (direction == -1 and high[j] >= stop):
            return {"mr_outcome": "FAIL", "mr_return_pct": (stop - entry) / entry * 100,
                    "mr_failure_realized": True}
        if (direction == 1 and high[j] >= tp) or (direction == -1 and low[j] <= tp):
            return {"mr_outcome": "TP1", "mr_return_pct": (tp - entry) / entry * 100,
                    "mr_failure_realized": False}
    # timeout at last available bar
    j = len(px) - 1
    return {"mr_outcome": "TIMEOUT", "mr_return_pct": (close[j] - entry) / entry * 100,
            "mr_failure_realized": False}


def main():
    from datetime import datetime, timezone
    cfg = load_config()
    obs = load_observations()
    cands = load_mr_candidates()
    resolved = 0

    # --- resolve observation future returns ---
    if len(obs):
        obs = obs.copy()
        obs["timestamp"] = pd.to_datetime(obs["timestamp"])
        for idx, r in obs.iterrows():
            if r.get("resolved_at") is not None and pd.notna(r.get("resolved_at")):
                continue
            try:
                p = find_asset_price_file(ROOT / "data/prices", r["asset"])
                px = load_price_csv(p)
            except Exception:
                continue
            ts = pd.Timestamp(r["timestamp"])
            updates = {}
            for col, h in HORIZONS.items():
                fr = future_return(px, ts, h)
                if fr is not None:
                    obs.at[idx, col] = fr
            # mark resolved when 24h path available
            if pd.notna(obs.at[idx, "future_return_24h"]):
                obs.at[idx, "resolved_at"] = datetime.now(timezone.utc).isoformat()
        obs.to_parquet(OBS_PARQUET, index=False)
        obs.to_csv(OBS_CSV, index=False)

    # --- resolve MR candidates (counterfactual for accepted AND blocked) ---
    cands = load_mr_candidates()
    n_res = 0
    if len(cands):
        for idx, r in cands.iterrows():
            if r.get("resolved_at") is not None and pd.notna(r.get("resolved_at")):
                continue
            try:
                p = find_asset_price_file(ROOT / "data/prices", r["asset"])
                px = load_price_csv(p)
            except Exception:
                continue
            out = resolve_mr_outcome(px, r)
            if out is None:
                continue
            for k, v in out.items():
                cands.at[idx, k] = v
            cands.at[idx, "resolved_at"] = datetime.now(timezone.utc).isoformat()
            n_res += 1
        cands.to_parquet(MR_CAND_PARQUET, index=False)
        cands.to_csv(MR_CAND_CSV, index=False)
    print(f"MR candidates resolved this pass: {n_res}")
    print(f"Total candidates: {len(cands)}")


if __name__ == "__main__":
    main()
