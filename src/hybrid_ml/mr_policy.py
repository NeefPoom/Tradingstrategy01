"""Phase H6 — MR decision policy.

ML is a GATE, not the setup generator. The original MR technical setup
(oscillator state + cross) must exist first; MR_FAIL probability then gates
eligibility. US500 is RESEARCH_ONLY for MR (Phase G finding).
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

MR_FAIL_THRESHOLD = 0.45
RESEARCH_ONLY_ASSETS = {"US500"}  # poor cross-asset generalization (G6)


def detect_mr_setup(row) -> dict:
    """Detect the ORIGINAL MR technical setup at the latest completed bar.

    LONG MR candidate: oscillator below zero AND osc crosses UP its signal.
    SHORT MR candidate: oscillator above zero AND osc crosses DOWN signal.

    Uses the current and previous bar (entry-time info only).
    Returns {"setup": bool, "direction": "LONG"|"SHORT"|None, "reason": str}.
    """
    osc, sig = float(row["osc"]), float(row["signal"])
    osc_prev = float(row.get("osc_prev", osc))
    sig_prev = float(row.get("signal_prev", sig))

    cross_up = osc_prev <= sig_prev and osc > sig
    cross_down = osc_prev >= sig_prev and osc < sig

    if osc < 0 and osc > sig and osc_prev <= sig_prev:
        return {"setup": True, "direction": "LONG",
                "reason": "osc_below_zero_cross_up"}
    if osc > 0 and osc < sig and osc_prev >= sig_prev:
        return {"setup": True, "direction": "SHORT",
                "reason": "osc_above_zero_cross_down"}
    return {"setup": False, "direction": None, "reason": "no_setup"}


def evaluate_mr(asset: str, row, scores, cfg, data_status: str = "OK") -> dict:
    """Deterministic MR decision policy.

    Order of gates:
      1. data stale -> BLOCK_DATA_STALE
      2. asset policy (US500 research-only) -> BLOCK_ASSET_POLICY
      3. p_mr_fail > threshold -> BLOCK_FAIL_RISK
      4. no original setup -> NO_ACTION
      5. else -> MR_ELIGIBLE
    """
    threshold = float(cfg.get("phase_h", {}).get("mr_fail", {}).get("threshold", 0.45))
    p_fail = float(row.get("p_mr_fail", 1.0)) if pd.notna(row.get("p_mr_fail", None)) else 1.0

    if data_status == "STALE_DATA":
        return {"decision": "MR_BLOCK", "reason": "BLOCK_DATA_STALE"}
    if asset in RESEARCH_ONLY_ASSETS:
        return {"decision": "RESEARCH_ONLY",
                "reason": "BLOCK_ASSET_POLICY (US500 research-only)"}
    if p_fail > threshold:
        return {"decision": "MR_BLOCK", "reason": "BLOCK_FAIL_RISK"}
    setup = detect_mr_setup(row)
    if not setup["setup"]:
        return {"decision": "NO_ACTION", "reason": "no_original_setup"}
    return {"decision": "MR_ELIGIBLE", "reason": setup["reason"],
            "direction": setup["direction"]}


def mr_gate_pass(p_mr_fail, cfg) -> bool:
    """MR_FAIL gate: True when p_mr_fail <= threshold."""
    return float(p_mr_fail) <= float(cfg.get("phase_h", {}).get("mr_fail", {}).get("threshold", 0.45))
