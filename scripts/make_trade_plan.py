"""Phase H13 — manual paper trade plan.

MANUAL/PAPER ONLY. No broker API. Trade-plan entries are created ONLY for
action == MR_ELIGIBLE. Stop status is MANUAL_STOP_REQUIRED (no validated
cross-asset stop). Position size is POSITION_SIZE_PENDING_STOP.
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import asset_items, load_config
from hybrid_ml.positions import load_positions

sys.path.insert(0, str(ROOT / "scripts"))
from score_all_latest import latest_evidence_row

RISK_PER_TRADE_PCT = 0.5  # hard cap % equity per trade


def main():
    cfg = load_config()
    positions = load_positions()
    plans = []
    print("PHASE H — MANUAL PAPER TRADE PLAN (no broker, no auto-execution)\n")
    print("Only MR_ELIGIBLE actions produce a plan entry. "
          "Stop status: MANUAL_STOP_REQUIRED (no validated universal stop).\n")

    for asset, _ in asset_items(cfg, forward_research=True):
        try:
            r = latest_evidence_row(asset, cfg, positions)
        except Exception as e:
            print(f"[{asset}] ERROR: {e}")
            continue
        if r["recommended_action"] != "MR_ELIGIBLE":
            print(f"[{asset}] {r['recommended_action']} — no plan entry")
            continue
        # MR setup direction from reason
        direction = "LONG" if "LONG" in r.get("reason", "").upper() or "cross_up" in r.get("reason", "") else "SHORT"
        plans.append({
            "asset": asset, "direction": direction,
            "signal_time": r["timestamp"],
            "reference_entry_price": None,  # filled from price data below
            "p_mr_win": r["p_mr_win"], "p_mr_fail": r["p_mr_fail"],
            "pred_mr_return_pct": r["pred_mr_return_pct"],
            "risk_status": f"max {RISK_PER_TRADE_PCT}% equity",
            "stop_status": "MANUAL_STOP_REQUIRED",
            "position_size": "POSITION_SIZE_PENDING_STOP",
        })
        print(f"[{asset}] MR_ELIGIBLE {direction} — MANUAL_STOP_REQUIRED, "
              f"POSITION_SIZE_PENDING_STOP")

    # fill reference entry price
    from hybrid_ml.price_io import find_asset_price_file, load_price_csv
    for pl in plans:
        try:
            p = find_asset_price_file(ROOT / "data/prices", pl["asset"])
            px = load_price_csv(p)
            pl["reference_entry_price"] = float(px.iloc[-1]["close"])
        except Exception:
            pl["reference_entry_price"] = None

    df = pd.DataFrame(plans)
    df.to_csv(ROOT / "reports" / "trade_plan_latest.csv", index=False)
    print(f"\nSaved reports/trade_plan_latest.csv ({len(df)} paper entries)")


if __name__ == "__main__":
    main()
