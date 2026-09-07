"""Generate PHASE_H_STATUS.md for Phase H forward validation.

Decision is one of:
INSUFFICIENT_FORWARD_DATA | CONTINUE_FORWARD_VALIDATION |
MODEL_WARNING | CANDIDATE_FOR_PAPER_TRADING.

This script never emits PRODUCTION_READY.
"""
from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from hybrid_ml.config import load_config
from hybrid_ml.forward_mr import load_mr_candidates, load_runner_events
from hybrid_ml.forward_store import load_observations
from hybrid_ml.freeze import ensure_baseline, verify_freeze


def _days_observed(phase_h_start) -> int:
    start = pd.Timestamp(phase_h_start or pd.Timestamp.now())
    if getattr(start, "tzinfo", None) is not None:
        start = start.tz_convert(None)
    return int((pd.Timestamp.now() - start).days)


def main() -> None:
    cfg = load_config()
    baseline = ensure_baseline(cfg)
    freeze = verify_freeze(baseline)
    obs = load_observations()
    cands = load_mr_candidates()
    runners = load_runner_events()

    days = _days_observed(baseline.get("phase_h_start"))
    resolved_obs = obs[obs["mr_failure_realized"].notna()] if len(obs) and "mr_failure_realized" in obs else pd.DataFrame()

    auc = brier = ece = None
    if len(resolved_obs) >= 20 and resolved_obs["mr_failure_realized"].nunique() > 1:
        from sklearn.metrics import roc_auc_score
        from scripts.forward_calibration_report import brier_ece

        y = resolved_obs["mr_failure_realized"].astype(int)
        p = resolved_obs["p_mr_fail"].astype(float)
        auc = roc_auc_score(y, p)
        brier, ece = brier_ece(y.values, p.values)

    n_obs = len(obs)
    n_cands = len(cands)
    n_res = int(cands["resolved_at"].notna().sum()) if len(cands) and "resolved_at" in cands else 0
    n_runners = len(runners)
    n_runners_res = int(runners["resolved_at"].notna().sum()) if len(runners) and "resolved_at" in runners else 0

    if n_obs < 30 or n_cands < 10:
        decision = "INSUFFICIENT_FORWARD_DATA"
    elif freeze["status"] == "VIOLATION":
        decision = "MODEL_WARNING"
    elif len(resolved_obs) >= 20 and auc is not None and auc >= 0.65:
        decision = "CANDIDATE_FOR_PAPER_TRADING"
    else:
        decision = "CONTINUE_FORWARD_VALIDATION"

    lines = [
        "# Phase H Status - Frozen Forward Validation",
        "",
        f"**Generated:** {pd.Timestamp.now().isoformat()}",
        "",
        "## 1. Phase H start date",
        str(baseline.get("phase_h_start", "n/a"))[:10],
        "",
        "## 2. Frozen model version",
        str(baseline.get("model_version")),
        "",
        "## 3. Frozen MR_FAIL threshold",
        "0.45 (locked)",
        "",
        "## 4. Days observed",
        str(days),
        "",
        "## 5. Observation count by asset",
    ]
    if len(obs) and "asset" in obs:
        for asset, group in obs.groupby("asset"):
            lines.append(f"- {asset}: {len(group)}")
    else:
        lines.append("- (none yet)")

    lines += [
        "",
        "## 6. MR candidates / resolved",
        f"- {n_cands} candidates, {n_res} resolved",
        "",
        "## 7. Runner events / resolved",
        f"{n_runners} events, {n_runners_res} resolved "
        "(Runner lifecycle starts only after a live MR position reaches TP1)",
        "",
        "## 8. Forward MR_FAIL discrimination",
        f"ROC-AUC: {auc if len(resolved_obs) >= 20 else 'insufficient sample'}",
        "",
        "## 9. Forward calibration",
        f"Brier: {brier if len(resolved_obs) >= 20 else 'n/a'} | ECE: {ece if len(resolved_obs) >= 20 else 'n/a'}",
        "",
        "## 10. MR gate performance",
        "See reports/forward_mr_gate.csv (populated as candidates resolve)",
        "",
        "## 11. Runner B vs C",
        "Parallel research - see reports/forward_runner_comparison.csv",
        "",
        "## 12. US500 research status",
        "RESEARCH_ONLY for MR (Phase G holdout failure 0.487)",
        "",
        "## 13. Data-quality issues",
        "Weekend/session gaps expected for FX/futures/index (see price_quality.csv)",
        "",
        "## 14. Model freeze violation",
        "None" if freeze["status"] == "PASS" else "**VIOLATION DETECTED**",
        "",
        "## 15. Decision",
        f"**{decision}**",
        "",
        "Phase H never outputs PRODUCTION_READY.",
    ]
    (ROOT / "PHASE_H_STATUS.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"PHASE_H_STATUS.md written - decision: {decision}")


if __name__ == "__main__":
    main()
