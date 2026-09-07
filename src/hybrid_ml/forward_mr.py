"""Phase H7/H10 — MR candidate log and Runner event store.

MR candidates: every MR setup is logged (eligible AND blocked) so forward
evaluation can measure counterfactuals (did MR_FAIL block bad trades? did it
block winners?).

Runner events: parallel forward A/B test of OSC_CROSS vs HYBRID exits.
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

FWD_DIR = ROOT / "data" / "forward"
MR_CAND_PARQUET = FWD_DIR / "mr_candidates.parquet"
MR_CAND_CSV = FWD_DIR / "mr_candidates.csv"
RUNNER_PARQUET = FWD_DIR / "runner_events.parquet"
RUNNER_CSV = FWD_DIR / "runner_events.csv"

MR_CANDIDATE_COLS = [
    "candidate_id", "asset", "timestamp", "direction", "entry_price",
    "p_mr_win", "p_mr_fail", "pred_mr_return_pct",
    "threshold", "decision", "decision_reason",
    # outcome fields (NA until resolved)
    "mr_outcome", "mr_return_pct", "mr_failure_realized",
    "blocked_winner", "blocked_loser", "resolved_at",
]

RUNNER_EVENT_COLS = [
    "runner_id", "asset", "direction", "runner_start_time", "runner_start_price",
    "p_runner_win_at_start", "pred_runner_return_pct_at_start",
    "osc_exit_time", "osc_exit_price", "osc_return_pct",
    "hybrid_exit_time", "hybrid_exit_price", "hybrid_return_pct",
    "mae_pct", "mfe_pct", "duration_osc", "duration_hybrid", "resolved_at",
]


def load_mr_candidates() -> "pd.DataFrame":
    if MR_CAND_PARQUET.exists():
        return pd.read_parquet(MR_CAND_PARQUET)
    if MR_CAND_CSV.exists():
        return pd.read_csv(MR_CAND_CSV)
    return pd.DataFrame()


def append_mr_candidate(row: dict) -> str:
    """Append one MR candidate. Skips duplicates by candidate_id."""
    FWD_DIR.mkdir(parents=True, exist_ok=True)
    cid = row["candidate_id"]
    existing = load_mr_candidates()
    if len(existing) and cid in set(existing["candidate_id"]):
        print(f"SKIP — already scored: {cid}")
        return "SKIP"
    df = pd.concat([existing, pd.DataFrame([row])], ignore_index=True) if len(existing) else pd.DataFrame([row])
    df.to_parquet(MR_CAND_PARQUET, index=False)
    df.to_csv(MR_CAND_CSV, index=False)
    return "APPENDED"


def load_runner_events() -> "pd.DataFrame":
    if RUNNER_PARQUET.exists():
        return pd.read_parquet(RUNNER_PARQUET)
    if RUNNER_CSV.exists():
        return pd.read_csv(RUNNER_CSV)
    return pd.DataFrame()


def append_runner_event(row: dict) -> str:
    """Append one runner lifecycle event. Skips duplicates by runner_id."""
    FWD_DIR.mkdir(parents=True, exist_ok=True)
    rid = row["runner_id"]
    existing = load_runner_events()
    if len(existing) and rid in set(existing["runner_id"]):
        print(f"SKIP — already scored: {rid}")
        return "SKIP"
    df = pd.concat([existing, pd.DataFrame([row])], ignore_index=True) if len(existing) else pd.DataFrame([row])
    df.to_parquet(RUNNER_PARQUET, index=False)
    df.to_csv(RUNNER_CSV, index=False)
    return "APPENDED"
