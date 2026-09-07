"""Phase G5 — MR_FAIL probability calibration research.

Evaluates predicted failure probability vs actual failure rate in decile bins.
Computes Brier score and ECE. Compares raw vs isotonic vs sigmoid calibration
on out-of-sample walk-forward predictions.

Does NOT replace the active model unless calibration demonstrably improves
out-of-sample calibration without harming discrimination.
"""
from pathlib import Path
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import load_config
from hybrid_ml.modeling import cls
from sklearn.metrics import brier_score_loss, roc_auc_score
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression

BINS = np.arange(0, 1.01, 0.1)


def oos_predictions(df, features, seed=42):
    """Out-of-sample (p_raw, y) plus in-fold calibration data, 5 folds."""
    mr = df[df.engine == "MR"].dropna(subset=["return_pct"]).copy()
    mr = mr.sort_values("entry_time").reset_index(drop=True)
    n = len(mr)
    min_train = 150
    if n < min_train + 40:
        return pd.DataFrame(), None, None

    oos, cal_p, cal_y = [], [], []
    for k in range(5):
        te_start = min_train + k * (n - min_train) // 5
        te_end = te_start + (n - min_train) // 5 if k < 4 else n
        tr, te = mr.iloc[:te_start], mr.iloc[te_start:te_end]
        if te.empty or tr["is_mr_fail"].nunique() < 2:
            continue
        m = cls(seed)
        m.fit(tr[features], tr["is_mr_fail"].astype(int))
        oos.append(pd.DataFrame({"p_raw": m.predict_proba(te[features])[:, 1],
                                 "y": te["is_mr_fail"].astype(int).values}))
        # in-fold calibration split: last 20% of train fold
        ntr = len(tr)
        cal = tr.iloc[int(ntr * 0.8):]
        if len(cal) > 30 and cal["is_mr_fail"].nunique() == 2:
            cal_p.append(m.predict_proba(cal[features])[:, 1])
            cal_y.append(cal["is_mr_fail"].astype(int).values)
    return (pd.concat(oos, ignore_index=True) if oos else pd.DataFrame(),
            (np.concatenate(cal_p) if cal_p else None),
            (np.concatenate(cal_y) if cal_y else None))


cal_p = []
cal_y_arr = []


def brier_ece(y, p, bins=BINS):
    """Brier score and expected calibration error."""
    y, p = np.asarray(y, float), np.asarray(p, float)
    ece = 0.0
    for i in range(len(bins) - 1):
        lo, hi = bins[i], bins[i + 1]
        m = (p >= lo) & (p < hi) if hi < 1 else (p >= lo) & (p <= hi)
        if m.sum():
            ece += m.mean() * abs(p[m].mean() - y[m].mean())
    return brier_score_loss(y, p), float(ece)


def main():
    global cal_p, cal_y_arr
    cfg = load_config()
    seed = int(cfg["model"]["random_state"])
    d = pd.read_parquet(ROOT / "data/ml_dataset.parquet")
    feats = [c for c in d.columns if c not in
             {"asset", "trade_number", "entry_time", "exit_time", "engine", "direction",
              "entry_regime", "exit_regime", "outcome_type", "entry_price", "exit_price",
              "return_pct", "net_pnl", "mfe_pct", "mae_pct", "duration_bars",
              "is_win", "is_mr_fail", "timestamp", "open", "high", "low", "close", "volume"}]

    mr = d[d.engine == "MR"].dropna(subset=["return_pct"]).sort_values("entry_time").reset_index(drop=True)
    n = len(mr)
    min_train = 150
    if n < min_train + 40:
        print("Not enough MR data for calibration research")
        return

    oos = []
    cal_p, cal_y = [], []
    for k in range(5):
        te_start = min_train + k * (n - min_train) // 5
        te_end = te_start + (n - min_train) // 5 if k < 4 else n
        tr, te = mr.iloc[:te_start], mr.iloc[te_start:te_end]
        if te.empty or tr["is_mr_fail"].nunique() < 2:
            continue
        m = cls(seed)
        m.fit(tr[features := feats], tr["is_mr_fail"].astype(int))
        oos.append(pd.DataFrame({"p_raw": m.predict_proba(te[feats])[:, 1],
                                 "y": te["is_mr_fail"].astype(int).values}))
        ntr = len(tr)
        cal = tr.iloc[int(ntr * 0.8):]
        if len(cal) > 30 and cal["is_mr_fail"].nunique() == 2:
            cal_p.append(m.predict_proba(cal[feats])[:, 1])
            cal_y.append(cal["is_mr_fail"].astype(int).values)

    if not oos:
        print("Not enough data for calibration research")
        return
    oos = pd.concat(oos, ignore_index=True)

    # fit calibrators on pooled in-fold holdout predictions
    if cal_p:
        cp, cy = np.concatenate(cal_p), np.concatenate(cal_y)
        if len(set(cy)) == 2:
            iso = IsotonicRegression(out_of_bounds="clip").fit(cp, cy)
            sig = LogisticRegression().fit(cp.reshape(-1, 1), cy)
            oos["p_isotonic"] = iso.predict(oos["p_raw"].values)
            oos["p_sigmoid"] = sig.predict_proba(oos["p_raw"].values.reshape(-1, 1))[:, 1]

    # decile bin report on raw probabilities
    rows = []
    for lo in np.arange(0, 1.0, 0.1):
        hi = lo + 0.1
        m = (oos.p_raw >= lo) & (oos.p_raw < hi) if hi < 1 else (oos.p_raw >= lo) & (oos.p_raw <= hi)
        if m.sum() == 0:
            continue
        sub = oos[m]
        rows.append({"probability_bin": f"{lo:.1f}-{hi:.1f}",
                     "count": int(m.sum()),
                     "mean_predicted_probability": round(float(sub.p_raw.mean()), 4),
                     "actual_failure_rate": round(float(sub.y.mean()), 4),
                     "calibration_error": round(float(sub.p_raw.mean() - sub.y.mean()), 4)})
    cal_df = pd.DataFrame(rows)
    cal_df.to_csv(ROOT / "reports" / "mr_fail_calibration.csv", index=False)
    print("=== MR_FAIL calibration bins (out-of-sample) ===")
    print(cal_df.to_string(index=False))

    print("\n=== Calibration comparison ===")
    b, e = brier_ece(oos.y.values, oos.p_raw.values)
    print(f"raw:      brier={b:.4f}  ece={e:.4f}  roc_auc={roc_auc_score(oos.y, oos.p_raw):.4f}")
    if "p_isotonic" in oos:
        b, e = brier_ece(oos.y.values, oos.p_isotonic.values)
        print(f"isotonic: brier={b:.4f}  ece={e:.4f}  roc_auc={roc_auc_score(oos.y, oos.p_isotonic):.4f}")
    if "p_sigmoid" in oos:
        b, e = brier_ece(oos.y.values, oos.p_sigmoid.values)
        print(f"sigmoid:  brier={b:.4f}  ece={e:.4f}  roc_auc={roc_auc_score(oos.y, oos.p_sigmoid):.4f}")

    print("\nSaved reports/mr_fail_calibration.csv")


if __name__ == "__main__":
    main()
