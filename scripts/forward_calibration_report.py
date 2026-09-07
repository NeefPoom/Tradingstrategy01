"""Phase H14 — forward calibration report (Phase H observations ONLY).

Never mixes historical Phase A-G records. Compares forward MR_FAIL
discibration/calibration against the Phase G baseline and flags
GREEN / YELLOW / RED. Never retrains.
"""
from pathlib import Path
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.forward_store import load_observations
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss

BASELINE = {"roc_auc": 0.743, "brier": 0.212, "ece": 0.098}
BINS = np.arange(0, 1.01, 0.1)


def brier_ece(y, p):
    y, p = np.asarray(y, float), np.asarray(p, float)
    ece = 0.0
    for lo in np.arange(0, 1.0, 0.1):
        hi = lo + 0.1
        m = (p >= lo) & (p < hi) if hi < 1 else (p >= lo) & (p <= hi)
        if m.sum():
            ece += m.mean() * abs(p[m].mean() - y[m].mean())
    return brier_score_loss(y, p), float(ece)


def main():
    obs = load_observations()
    resolved = obs[obs["mr_failure_realized"].notna()] if len(obs) else pd.DataFrame()
    # MR_FAIL forward evaluation uses observations where MR was scored
    if len(obs) < 30:
        print("INSUFFICIENT FORWARD SAMPLE "
              f"({len(obs)} observations; need >= 30 for calibration report)")
        return
    # use observations with resolved MR failure outcome
    d = obs[obs["mr_failure_realized"].notna()] if len(obs) else pd.DataFrame()
    if len(d) < 20:
        print(f"INSUFFICIENT FORWARD SAMPLE — {len(d)} resolved MR outcomes")
        return

    y = d["mr_failure_realized"].astype(int)
    p = d["p_mr_fail"].astype(float)
    brier, ece = brier_ece(y.values, p.values)
    auc = roc_auc_score(y, p)
    pr = average_precision_score(y, p)

    rows = []
    for lo in np.arange(0, 1.0, 0.1):
        hi = lo + 0.1
        m = (d.p_mr_fail >= lo) & (d.p_mr_fail < hi) if hi < 1 else (d.p_mr_fail >= lo) & (d.p_mr_fail <= hi)
        if m.sum() == 0:
            continue
        sub = d[m]
        rows.append({"probability_bin": f"{lo:.1f}-{hi:.1f}", "n": int(m.sum()),
                     "mean_predicted": round(float(sub.p_mr_fail.mean()), 4),
                     "actual_failure_rate": round(float(sub.mr_failure_realized.mean()), 4),
                     "calibration_error": round(float(sub.p_mr_fail.mean() - sub.mr_failure_realized.mean()), 4)})
    cal = pd.DataFrame(rows)
    cal.to_csv(ROOT / "reports" / "mr_fail_forward_calibration.csv", index=False)
    print(cal.to_string(index=False))

    # status flag
    if auc >= 0.65 and brier < 0.30:
        flag = "GREEN"
    elif auc >= 0.55:
        flag = "YELLOW"
    else:
        flag = "RED"
    print(f"\nForward MR_FAIL: ROC-AUC={auc:.3f}  Brier={brier:.4f}  ECE={ece:.4f}")
    print(f"Phase G baseline: ROC-AUC 0.743  Brier 0.212  ECE 0.098")
    print(f"Status: {flag}")
    print("Saved reports/mr_fail_forward_calibration.csv")


if __name__ == "__main__":
    from sklearn.metrics import brier_score_loss, roc_auc_score, average_precision_score
    main()
