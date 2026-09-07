"""Phase G6 — Leave-One-Asset-Out (LOAO) validation.

For each asset: train on all other assets, test only on the held-out asset.
Research question: does the model learn market-state structure, or just
memorize asset behavior? Asset name is NOT a feature (per project rules).

Models evaluated: MR win, MR_FAIL, RUNNER win, RUNNER return. TF excluded.
"""
from pathlib import Path
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import load_config
from hybrid_ml.modeling import cls, reg, cmetrics
from sklearn.metrics import mean_absolute_error

META_COLS = {"asset", "trade_number", "entry_time", "exit_time", "engine", "direction",
             "entry_regime", "exit_regime", "outcome_type", "entry_price", "exit_price",
             "return_pct", "net_pnl", "mfe_pct", "mae_pct", "duration_bars",
             "is_win", "is_mr_fail", "timestamp", "open", "high", "low", "close", "volume"}

JOBS = [("MR", "is_win", "cls"), ("MR", "is_mr_fail", "cls"),
        ("RUNNER", "is_win", "cls"), ("RUNNER", "return_pct", "reg")]


def evaluate(df, features, engine, target, kind, held_out, seed):
    """Train on all assets except held_out, test on held_out."""
    tr = df[(df.engine == engine) & (df.asset != held_out)].dropna(subset=["return_pct"])
    te = df[(df.engine == engine) & (df.asset == held_out)].dropna(subset=["return_pct"])
    target_col = "is_mr_fail" if kind_target_is_fail(target) else target
    if len(tr) < 100 or te.empty:
        return {"held_out_asset": held_out, "model": f"{engine}/{target}",
                "train_rows": len(tr), "test_rows": len(te), "status": "SKIP"}
    if tr[target].nunique() < 2:
        return {"held_out_asset": held_out, "model": f"{engine}/{target}",
                "train_rows": len(tr), "test_rows": len(te), "status": "SKIP_SINGLE_CLASS"}

    m = cls(seed) if kind_of(target) == "cls" else reg(seed)
    y_tr = tr[target].astype(int) if kind_of(target) == "cls" else tr[target].astype(float)
    m.fit(tr[features], y_tr := y_tr_safe(tr, target))

    row = {"held_out_asset": held_out, "model": f"{engine}/{target}",
           "train_rows": len(tr), "test_rows": len(te)}
    if kind_of(target) == "cls":
        met = cmetrics(m, te[features], te[target].astype(int))
        row.update({k: round(v, 4) if pd.notna(k) else k for k, v in met.items()})
        row["avg_actual_return"] = round(float(te["return_pct"].mean()), 4)
        row["avg_predicted_return"] = None
        row["return_mae"] = None
    else:
        pred = m.predict(te[features])
        row.update({"roc_auc": None, "pr_auc": None, "brier": None,
                    "balanced_accuracy": None,
                    "avg_actual_return": round(float(te["return_pct"].mean()), 4),
                    "avg_predicted_return": round(float(pred.mean()), 4),
                    "return_mae": round(float(mean_absolute_error(te["return_pct"], pred)), 4)})
    row["status"] = "OK"
    return row


def kind_of(target):
    return "cls" if target.startswith("is_") else "reg"


def kind_target_is_fail(target):
    return target == "is_mr_fail"


def y_tr_safe(tr, target):
    return tr[target]


def main():
    cfg = load_config()
    seed = int(cfg["model"]["random_state"])
    d = pd.read_parquet(ROOT / "data/ml_dataset.parquet")
    feats = [c for c in d.columns if c not in META_COLS]

    rows = []
    for asset in cfg["assets"]:
        for eng, tgt, kind in JOBS:
            tr = d[(d.engine == eng) & (d.asset != asset)].dropna(subset=["return_pct"])
            te = d[(d.engine == eng) & (d.asset == asset)].dropna(subset=["return_pct"])
            base = {"held_out_asset": asset, "model": f"{eng}/{tgt}",
                    "train_rows": len(tr), "test_rows": len(te)}
            if len(tr) < 100 or te.empty or tr[tgt].nunique() < 2:
                rows.append({**base, "status": "SKIP"})
                print(f"{asset} {eng}/{tgt}: SKIP (train={len(tr)}, test={len(te)})")
                continue
            m = cls(seed) if kind == "cls" else reg(seed)
            y = tr[tgt].astype(int) if kind == "cls" else tr[tgt].astype(float)
            m.fit(tr[feats], y)
            if kind == "cls":
                met = cmetrics(m, te[feats], te[tgt].astype(int))
                rows.append({**base, "roc_auc": round(met["roc_auc"], 4),
                             "pr_auc": round(met["pr_auc"], 4),
                             "brier": round(met["brier"], 4),
                             "balanced_accuracy": round(met["balanced_accuracy"], 4),
                             "avg_actual_return": round(float(te["return_pct"].mean()), 4),
                             "avg_predicted_return": None,
                             "return_mae": None, "status": "OK"})
                print(f"{asset} {eng}/{tgt}: roc={met['roc_auc']:.3f} pr={met['pr_auc']:.3f}")
            else:
                pred = m.predict(te[feats])
                rows.append({**base,
                             "roc_auc": None, "pr_auc": None, "brier": None,
                             "balanced_accuracy": None,
                             "avg_actual_return": round(float(te["return_pct"].mean()), 4),
                             "avg_predicted_return": round(float(pred.mean()), 4),
                             "return_mae": round(float(mean_absolute_error(te[tgt], pred)), 4),
                             "status": "OK"})
                print(f"{asset} {eng}/{tgt}: mae={rows[-1]['return_mae']:.3f} "
                      f"actual={rows[-1]['avg_actual_return']:.3f} pred={rows[-1]['avg_predicted_return']:.3f}")

    res = pd.DataFrame(rows)
    res.to_csv(ROOT / "reports" / "asset_holdout.csv", index=False)
    print(f"\nSaved reports/asset_holdout.csv ({len(rows)} rows)")


if __name__ == "__main__":
    from sklearn.metrics import mean_absolute_error
    main()
