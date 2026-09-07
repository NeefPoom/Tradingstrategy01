"""Phase H17 — daily forward dashboard.

Console summary of Phase H forward validation. Prints INSUFFICIENT FORWARD
SAMPLE when evidence is too thin to draw conclusions.
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import load_config
from hybrid_ml.forward_store import load_observations
from hybrid_ml.forward_mr import load_mr_candidates, load_runner_events
from hybrid_ml.freeze import ensure_baseline, verify_freeze


def main():
    cfg = load_config()
    baseline = ensure_baseline(cfg)
    freeze = verify_freeze(baseline)
    obs = load_observations()
    cands = load_mr_candidates()

    print("=" * 62)
    print("PHASE H FORWARD VALIDATION")
    print("=" * 62)
    print(f"\nForward start: {baseline.get('phase_h_start', 'n/a')[:10]}")
    print(f"Model version: {baseline.get('model_version')}")

    print("\nCompleted observation bars:")
    if len(obs):
        for a, g in obs.groupby("asset"):
            print(f"  {a:<10} {len(g)}")
    else:
        print("  (none yet)")

    print(f"\nMR Candidates:")
    print(f"  Total     {len(cands)}")
    if len(cands):
        print(f"  Eligible  {(cands.decision == 'MR_ELIGIBLE').sum()}")
        print(f"  Blocked   {(cands.decision != 'MR_ELIGIBLE').sum()}")
        print(f"  Resolved  {cands.resolved_at.notna().sum()}")

    print(f"\nModel freeze: {freeze['status']}")
    print(f"\nOverall status: "
          f"{'INSUFFICIENT FORWARD SAMPLE' if len(obs) < 30 else 'CONTINUE OBSERVATION'}")


if __name__ == "__main__":
    main()
