"""Phase D — walk-forward validation.

Rolling train/test windows instead of one fixed chronological split.
For each fold: train on all data before the window, test on the window.
Reports per-fold and aggregate metrics for MR win, MR fail risk, and Runner.
"""
from pathlib import Path
import sys
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import load_config
from hybrid_ml.dataset import feature_columns
from hybrid_ml.modeling import cls, reg, cmetrics
from sklearn.metrics import mean_absolute_error

N_FOLDS = 5          # number of walk-forward folds
MIN_TRAIN = 150      # minimum training rows before first fold


def walk_forward(df, features, engine_filter, target, kind, seed=42):
    """Run walk-forward for one engine/target. Returns list of fold metrics."""
    d = df[df.engine == engine_filter].dropna(subset=["return_pct"]).copy()
    d = d.sort_values("entry_time").reset_index(drop=True)
    n = len(d)
    if n < MIN_TRAIN + 20:
        return [{"engine": engine_filter, "target": target, "fold": "SKIP",
                 "train_rows": n, "test_rows": 0}]

    folds = []
    # fold windows: each fold tests on the last slice; expanding train window
    test_size = (n - MIN_TRAIN) // N_FOLDS
    for k in range(N_FOLDS):
        te_start = MIN_TRAIN + k * test_size
        te_end = te_start + test_size if k < N_FOLDS - 1 else n
        tr, te = d.iloc[:te_start], d.iloc[te_start:te_end]
        if len(te) == 0 or tr[target].nunique() < 2:
            continue
        if kind == "cls":
            m = cls(seed)
        else:
            m = reg(seed)
        m.fit(tr[features], tr[target])
        if kind == "cls":
            met = cmetrics(m, te[features], te[target].astype(int))
        else:
            pred = m.predict(te[features])
            met = {"mae_return_pct": mean_absolute_error(te[target], pred),
                   "mean_actual": float(te[target].mean()),
                   "mean_pred": float(pred.mean())}
        met.update({"fold": k, "train_rows": len(tr), "test_rows": len(te),
                    "test_start": str(te.entry_time.iloc[0].date()),
                    "test_end": str(te.entry_time.iloc[-1].date())})
        folds.append({"engine": engine_filter, "target": target, **met})
    return folds


def main():
    from hybrid_ml.config import load_config
    cfg = load_config()
    d = pd.read_parquet(ROOT / "data/ml_dataset.parquet")
    feats = [c for c in d.columns if c not in
             {"asset","trade_number","entry_time","exit_time","engine","direction",
              "entry_regime","exit_regime","outcome_type","entry_price","exit_price",
              "return_pct","net_pnl","mfe_pct","mae_pct","duration_bars",
              "is_win","is_mr_fail","timestamp","open","high","low","close","volume"}]

    jobs = [
        ("MR", "is_win", "cls"),
        ("MR", "is_mr_fail", "cls"),
        ("RUNNER", "is_win", "cls"),
        ("RUNNER", "return_pct", "reg"),
        ("MR", "return_pct", "reg"),
    ]

    all_rows = []
    seed = int(cfg["model"]["random_state"])
    for eng, tgt, kind in jobs:
        all_rows += walk_forward(d, feats, eng, tgt, kind, seed)

    res = pd.DataFrame(all_rows)
    res.to_csv(ROOT / "reports" / "walk_forward_metrics.csv", index=False)

    # aggregate: mean across folds per engine/target
    agg = (res[res.fold != "SKIP"]
           .groupby(["engine", "target"])[["roc_auc", "pr_auc", "brier",
                                           "balanced_accuracy", "mae_return_pct",
                                           "mean_actual", "mean_pred"]]
           .mean().round(4))
    print("=== Per-fold ===")
    print(res.to_string(index=False))
    print("\n=== Walk-forward mean across folds ===")
    print(agg.to_string())


if __name__ == "__main__":
    main()
