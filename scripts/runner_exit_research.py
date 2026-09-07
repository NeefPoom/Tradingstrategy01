"""Phase G7 — Runner exit research (A/B/C methods).

Runner is a position-management state, NOT an entry engine. This research
simulates exit management only, starting from the MR TP1 transition point.

Methods:
  A — Fixed 2 ATR: exit at 2xATR(14) from runner start
  B — Oscillator cross: long exits when Osc crosses below Signal;
      short exits when Osc crosses above Signal (TradingView/M7 logic)
  C — Hybrid: half position exits at 2 ATR, remainder at oscillator cross

Simulation: bar-by-bar on 1H Yahoo data, entry-time info only, no look-ahead.
"""
from pathlib import Path
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import load_config
from hybrid_ml.price_io import load_price_csv
from hybrid_ml.features import build_features

MAX_BARS = 200
TP_MULT = 2.0  # method A / partial C target: 2 x ATR


def simulate(px, entry_idx, direction, entry_price, atr_val, method):
    """Simulate one runner from the MR TP1 transition point.

    direction: +1 long, -1 short. Runner start = entry_price + 1*ATR
    (MR TP1). Stop = original MR stop (entry - 1 ATR against direction).
    Returns dict(return_pct, duration_bars, exit_reason).
    """
    n = len(px)
    high, low, close = px["high"].values, px["low"].values, px["close"].values
    osc, sig = px["osc"].values, px["signal"].values

    run_entry = entry_price + direction * atr_val          # runner start (TP1)
    stop = entry_price - direction * 1.0 * atr_val         # original MR stop
    tp_full = run_entry + direction * TP_MULT * atr_val    # method A target

    end = min(entry_idx + MAX_BARS, n - 1)
    for j in range(entry_idx + 1, end + 1):
        # stop first (conservative)
        if (direction == 1 and low[j] <= stop) or (direction == -1 and high[j] >= stop):
            return {"return_pct": (stop - run_entry) / run_entry * 100 * 1.0,
                    "duration_bars": j - entry_idx, "exit_reason": "stop"}
        if method in ("A", "C"):
            hit_tp = (direction == 1 and high[j] >= tp_full) or \
                     (direction == -1 and low[j] >= tp_full)
            if hit_tp and method == "A":
                return {"return_pct": (tp_full - run_entry) / run_entry * 100,
                        "duration_bars": j - entry_idx, "exit_reason": "tp_2atr"}
        # oscillator cross (method B and C)
        if method in ("B", "C") and j > 0:
            crossed = ((direction == 1 and osc[j - 1] >= sig[j - 1] and osc[j] < sig[j]) or
                       (direction == -1 and osc[j - 1] <= sig[j - 1] and osc[j] > sig[j]))
            if crossed:
                px_exit = close[j]
                if method == "C":
                    part_tp = (tp_full - run_entry) / run_entry * 100
                    part_cross = (px_exit - run_entry) / run_entry * 100
                    return {"return_pct": 0.5 * part_tp + 0.5 * part_cross,
                            "duration_bars": j - entry_idx, "exit_reason": "hybrid"}
                return {"return_pct": (px_exit - run_entry) / run_entry * 100,
                        "duration_bars": j - entry_idx, "exit_reason": "osc_cross"}
    # timeout
    px_exit = close[end]
    return {"return_pct": (px_exit - run_entry) / run_entry * 100,
            "duration_bars": end - entry_idx, "exit_reason": "timeout"}


def summarize(g):
    """Trading metrics for a group of simulated runner exits."""
    ret = g["return_pct"]
    wins, losses = ret[ret > 0], ret[ret <= 0]
    eq = ret.cumsum()
    return pd.Series({
        "trades": len(g),
        "win_rate": round(float((ret > 0).mean()), 4),
        "avg_return_pct": round(float(ret.mean()), 4),
        "median_return_pct": round(float(ret.median()), 4),
        "profit_factor": round(float(wins.sum() / losses.abs().sum()), 3)
                         if losses.abs().sum() > 0 else None,
        "avg_winner_pct": round(float(wins.mean()), 4) if len(wins) else None,
        "avg_loser_pct": round(float(losses.mean()), 4) if len(losses) else None,
        "p90_winner": round(float(ret[ret > 0].quantile(0.9)), 4) if (ret > 0).any() else None,
        "p95_winner": round(float(ret[ret > 0].quantile(0.95)), 4) if (ret > 0).any() else None,
        "worst_trade": round(float(ret.min()), 4),
        "max_drawdown": round(float((eq.cummax() - eq).max()), 3),
        "avg_duration_bars": round(float(g["duration_bars"].mean()), 1),
    })


def main():
    cfg = load_config()
    d = pd.read_parquet(ROOT / "data/ml_dataset.parquet")
    runners = d[d.engine == "RUNNER"].dropna(subset=["return_pct"])
    print(f"Runner exit research: {len(runners)} runner trades across "
          f"{runners['asset'].nunique()} assets\n")

    rows = []
    for asset, trades in runners.groupby("asset"):
        try:
            p = sorted((ROOT / "data/prices").glob(f"{asset}_1h_yahoo.csv"))[-1]
            px = build_features(load_price_csv(p), cfg).reset_index(drop=True)
        except Exception as e:
            print(f"{asset}: skipped — {e}")
            continue
        ts = px["timestamp"]
        for _, t in trades.iterrows():
            idx = px.index[ts <= t.entry_time]
            if len(idx) == 0:
                continue
            i = int(idx[-1])
            if i >= len(px) - 2:
                continue
            direction = 1 if t.direction == "LONG" else -1
            for method in ["A", "B", "C"]:
                r = simulate(px, i, direction, float(t.entry_price), float(t["atr"]), method)
                rows.append({"method": method, "asset": asset,
                             "return_pct": round(r["return_pct"], 4),
                             "duration_bars": r["duration_bars"],
                             "exit_reason": r["exit_reason"]})

    if not rows:
        print("No runner trades simulated")
        return
    sim = pd.DataFrame(rows)

    summary = sim.groupby(["method", "asset"]).apply(summarize, include_groups=False).reset_index()
    pooled = sim.groupby("method").apply(summarize, include_groups=False).reset_index()
    pooled["asset"] = "POOLED"
    out = pd.concat([summary, pooled], ignore_index=True)
    out.to_csv(ROOT / "reports" / "runner_exit_ab_test.csv", index=False)
    print("=== Runner exit A/B/C per asset ===")
    print(summary.to_string(index=False))
    print("\n=== Pooled cross-asset ===")
    print(pooled.to_string(index=False))
    print("\nSaved reports/runner_exit_ab_test.csv")


if __name__ == "__main__":
    main()
