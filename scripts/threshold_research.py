"""Phase G4 — MR_FAIL threshold research.

Uses ONLY out-of-sample predictions from walk-forward folds.
For each candidate threshold t: keep MR trade if p_mr_fail <= t.
Reports trading expectancy metrics per threshold. Does NOT update the
production threshold — goal is to find a broad stable plateau.
"""
from pathlib import Path
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import load_config
from hybrid_ml.modeling import cls, split_time

THRESHOLDS = [round(0.25 + 0.025 * i, 3) for i in range(17)]  # 0.25 .. 0.65


def oos_predictions(df, features, seed=42):
    """Out-of-sample p_mr_fail predictions via 5 expanding walk-forward folds."""
    mr = df[df.engine == "MR"].dropna(subset=["return_pct"]).copy()
    mr = mr.sort_values("entry_time").reset_index(drop=True)
    n = len(mr)
    min_train = 150
    if n < min_train + 20:
        return pd.DataFrame()

    out = []
    for k in range(5):
        te_start = min_train + k * (n - min_train) // 5
        te_end = te_start + (n - min_train) // 5 if k < 4 else n
        tr, te = mr.iloc[:te_start], mr.iloc[te_start:te_end]
        if te.empty or tr["is_mr_fail"].nunique() < 2:
            continue
        m = cls(seed)
        m.fit(tr[features], tr["is_mr_fail"].astype(int))
        proba = m.predict_proba(te[features])[:, 1]
        out.append(pd.DataFrame({
            "entry_time": te["entry_time"].values,
            "asset": te["asset"].values,
            "p_mr_fail": proba,
            "is_win": te["is_win"].astype(int).values,
            "return_pct": te["return_pct"].astype(float).values,
            "mae_pct": te["mae_pct"].astype(float).values,
        }))
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame()


def trade_metrics(d: "pd.DataFrame") -> dict:
    """Trading expectancy metrics for a set of kept MR trades."""
    ret = d["return_pct"].astype(float)
    wins = ret[ret > 0]
    losses = ret[ret <= 0]
    pf = float(wins.sum() / losses.abs().sum()) if losses.sum() != 0 else float("inf")
    eq = ret.cumsum()
    dd = float((eq.cummax() - eq).max()) if len(eq) else 0.0
    return {
        "trades_kept": len(d),
        "percent_kept": round(100.0 * len(d) / max(1, _total_candidates), 2),
        "win_rate": round(float((ret > 0).mean()), 4) if len(ret) else np.nan,
        "avg_return_pct": round(float(ret.mean()), 4) if len(ret) else np.nan,
        "median_return_pct": round(float(ret.median()), 4) if len(ret) else np.nan,
        "profit_factor": round(pf, 3) if np.isfinite(pf) else None,
        "cumulative_return": round(float(ret.sum()), 3),
        "worst_trade_pct": round(float(ret.min()), 4) if len(ret) else np.nan,
        "p05_return": round(float(ret.quantile(0.05)), 4) if len(ret) else np.nan,
        "average_mae": round(float(d["mae_pct"].mean()), 4) if len(d) else np.nan,
        "worst_mae": round(float(d["mae_pct"].min()), 4) if len(d) else np.nan,
        "max_drawdown": round(float(eq.min() - eq.cummax().min()), 3) if len(eq) else 0.0,
    }


_total_candidates = 0


def main():
    global _total_candidates
    cfg = load_config()
    seed = int(cfg["model"]["random_state"])
    d = pd.read_parquet(ROOT / "data/ml_dataset.parquet")
    feats = [c for c in d.columns if c not in
             {"asset", "trade_number", "entry_time", "exit_time", "engine", "direction",
              "entry_regime", "exit_regime", "outcome_type", "entry_price", "exit_price",
              "return_pct", "net_pnl", "mfe_pct", "mae_pct", "duration_bars",
              "is_win", "is_mr_fail", "timestamp", "open", "high", "low", "close", "volume"}]

    preds = oos_predictions(d, feats, seed)
    if preds.empty:
        print("Not enough MR data for threshold research")
        return

    _total_candidates = len(preds)
    rows = []
    for t in THRESHOLDS:
        kept = preds[preds.p_mr_fail <= t]
        m = trade_metrics(kept)
        m.update({"threshold": t, "total_candidates": len(preds)})
        rows.append(m)

    res = pd.DataFrame(rows)
    cols = ["threshold", "total_candidates", "trades_kept", "percent_kept",
            "win_rate", "avg_return_pct", "median_return_pct", "profit_factor",
            "cumulative_return", "worst_trade_pct", "p05_return",
            "average_mae", "worst_mae", "max_drawdown"]
    res = res[[c for c in cols if c in res.columns]]
    res.to_csv(ROOT / "reports" / "mr_fail_threshold_research.csv", index=False)
    print(res.to_string(index=False))

    # markdown summary: find broad plateau (thresholds within 10% of best PF)
    pf = res["profit_factor"].replace([np.inf], np.nan)
    best = res.loc[pf.idxmax()] if pf.notna().any() else None
    lines = ["# MR_FAIL Threshold Research (out-of-sample, walk-forward)", ""]
    lines.append(f"- Total MR candidates: {len(preds)}")
    if best is not None:
        plateau = res[pf >= pf.max() * 0.9]["threshold"].tolist()
        lines.append(f"- Best single threshold: {best['threshold']} "
                     f"(win_rate {res.loc[pf.idxmax(), 'win_rate']}, "
                     f"profit_factor {best['profit_factor']})")
        lines.append(f"- Broad plateau (>=90% of best PF): {plateau}")
    lines.append("")
    lines.append("```")
    lines.append(res.to_string(index=False))
    lines.append("```")
    lines.append("")
    lines.append("**Note:** research only — production threshold in config.yaml "
                 "was NOT changed automatically.")
    (ROOT / "reports" / "mr_fail_threshold_summary.md").write_text(
        "\n".join(lines), encoding="utf-8")
    print("\nSaved reports/mr_fail_threshold_research.csv + mr_fail_threshold_summary.md")


if __name__ == "__main__":
    main()
