"""Phase H27 — clean exports for future Phase I research.

Copies raw forward data into resolved research datasets under
data/forward/export/. Raw observations are never overwritten.
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.forward_store import load_observations
from hybrid_ml.forward_mr import load_mr_candidates, load_runner_events

EXPORT_DIR = ROOT / "data" / "forward" / "export"


def main():
    out = ROOT / "data" / "forward" / "export"
    out.mkdir(parents=True, exist_ok=True)

    obs = load_observations()
    if len(obs):
        obs.to_parquet(out / "phase_h_features.parquet", index=False)
    cands = load_mr_candidates()
    if len(cands):
        cands.to_parquet(out / "phase_h_mr_candidates.parquet", index=False)
    runners = load_runner_events()
    if len(runners):
        runners.to_parquet(out / "phase_h_runner_events.parquet", index=False)
    # resolved outcomes = observations with resolved_at
    if len(obs):
        res = obs[obs["resolved_at"].notna()]
        if len(res):
            res.to_parquet(out / "phase_h_resolved_outcomes.parquet", index=False)

    files = list(out.glob("*.parquet"))
    print(f"Exported {len(files)} research datasets to data/forward/export/:")
    for f in files:
        print(f"  {f.name}")
    if not len(obs):
        print("(raw observations preserved separately — nothing overwritten)")


if __name__ == "__main__":
    main()
