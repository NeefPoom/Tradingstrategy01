"""Phase H22 — Phase H orchestrator.

Runs the full frozen forward-validation loop. NEVER retrains, never
optimizes, never connects to a broker, never enables TF.

Steps:
 1. verify model freeze
 2. update Yahoo prices
 3. backfill missing open-market price bars
 4. check data quality
 5. score latest completed bars (append observations)
 5. detect MR candidates
 6. resolve outcomes whose future data is now available
 7. generate latest scoring report
 8. generate manual paper trade plan
 9. refresh forward reports
10. print forward status
"""
from pathlib import Path
import sys
import subprocess

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from hybrid_ml.config import load_config
from hybrid_ml.freeze import ensure_baseline, verify_freeze

PY = sys.executable


def run_step(name, script):
    """Run one orchestrator step; continue on failure (H23)."""
    print(f"\n--- {name} ---")
    try:
        r = subprocess.run([PY, str(ROOT / "scripts" / name)],
                           capture_output=True, text=True, timeout=600)
        out = (r.stdout or "").strip()
        if out:
            print(out[-2000:])
        if r.returncode != 0:
            print(f"  [{name}] WARNING — exit {r.returncode}")
            return "WARNING"
        return "PASS"
    except Exception as e:
        print(f"  ERROR: {e}")
        return "FAILED"


def main():
    cfg = load_config()
    print("=" * 62)
    print("PHASE H OPERATING LOOP (frozen models, manual paper only)")
    print("=" * 62)

    # 1. model freeze
    from hybrid_ml.freeze import ensure_baseline, verify_freeze
    baseline = ensure_baseline(cfg)
    freeze = verify_freeze(baseline)
    print(f"\n[1] Model freeze: {freeze['status']}")
    if freeze["status"] == "VIOLATION":
        print("WARNING: PHASE H MODEL FREEZE VIOLATION — continuing to log, "
              "but investigate before drawing conclusions")

    steps = [
        ("[2] Yahoo price update", "scripts/update_prices.py"),
        ("[3a] Market-open completeness", "scripts/check_market_open_completeness.py"),
        ("[3b] Missing open-market price backfill", "scripts/backfill_market_open_prices.py"),
        ("[3c] Market-open completeness recheck", "scripts/check_market_open_completeness.py"),
        ("[3d] Data quality", "scripts/check_price_quality.py"),
        ("[4-7] Observations + MR candidates", "scripts/observe_latest.py"),
        ("[8] Outcome resolution", "scripts/resolve_forward_outcomes.py"),
        ("[10] Latest scores", "scripts/score_all_latest.py"),
        ("[11] Paper trade plan", "scripts/make_trade_plan.py"),
        ("[12a] Forward MR gate report", "scripts/forward_mr_gate_report.py"),
        ("[12b] Forward runner report", "scripts/forward_runner_report.py"),
        ("[12c] Forward calibration", "scripts/forward_calibration_report.py"),
    ]
    for name, script in steps:
        print(f"\n--- {name} ---")
        try:
            subprocess.run([PY, str(ROOT / script)], check=False, timeout=600)
        except Exception as e:
            print(f"WARNING: {name} failed: {e}")

    print("\n--- [13] Forward status ---")
    subprocess.run([PY, str(ROOT / "scripts" / "forward_status.py")], check=False)
    print("\n--- [14] Phase H status file ---")
    subprocess.run([PY, str(ROOT / "scripts" / "generate_phase_h_status.py")], check=False)


if __name__ == "__main__":
    main()
