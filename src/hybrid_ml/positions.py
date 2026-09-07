"""Position state management (Phase G3).

Runner is a position-management state, NOT a standalone entry.
Lifecycle: MR ENTRY -> TP1 -> partial profit -> remaining becomes RUNNER
-> ML evaluates HOLD/EXIT.

Valid states: FLAT, MR_LONG, MR_SHORT, RUNNER_LONG, RUNNER_SHORT
"""
from pathlib import Path
import json

VALID_STATES = {"FLAT", "MR_LONG", "MR_SHORT", "RUNNER_LONG", "RUNNER_SHORT"}
RUNNER_STATES = {"RUNNER_LONG", "RUNNER_SHORT"}
MR_STATES = {"MR_LONG", "MR_SHORT"}

DEFAULT_STATE_PATH = Path(__file__).resolve().parents[2] / "data" / "state" / "current_positions.json"


def load_positions(path=None):
    """Load current positions state file. Returns dict asset -> info."""
    p = Path(path) if path else DEFAULT_STATE_PATH
    if not p.exists():
        return {}
    import json
    return json.loads(p.read_text(encoding="utf-8"))


def get_state(positions: dict, asset: str) -> dict:
    """Return normalized state dict for an asset. Defaults to FLAT."""
    info = positions.get(asset, {})
    state = str(info.get("state", "FLAT")).upper()
    if state not in VALID_STATES:
        state = "FLAT"
    return {"state": state,
            "entry_price": info.get("entry_price"),
            "raw": info}


def save_positions(positions: dict, path=None):
    """Persist positions dict to JSON."""
    p = Path(path) if path else DEFAULT_STATE_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(positions, indent=2), encoding="utf-8")
