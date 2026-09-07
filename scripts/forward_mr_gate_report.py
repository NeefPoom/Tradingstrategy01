"""Phase H15 — forward MR gate report.

Measures whether the MR_FAIL gate reduces left-tail losses without destroying
positive expectancy. Includes counterfactual analysis of blocked candidates.
"""
from pathlib import Path
import sys
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.forward_mr import load_mr_candidates


def summarize(d):
    ret = d["mr_return_pct"].astype(float)
    wins, losses = ret[ret > 0], ret[ret <= 0]
    eq = ret.cumsum()
    return {
        "n": len(d),
        "win_rate": round(float((ret > 0).mean()), 4) if len(ret) else None,
        "avg_return_pct": round(float(ret.mean()), 4) if len(ret) else None,
        "profit_factor": round(float(wins.sum() / losses.abs().sum()), 3)
                         if losses.abs().sum() > 0 else None,
        "worst_trade_pct": round(float(ret.min()), 4) if len(ret) else None,
        "max_drawdown": round(float((eq.cummax() - eq).max()), 3) if len(eq) else 0.0,
    }


def main():
    cands = load_mr_candidates()
    if not len(cands):
        print("INSUFFICIENT FORWARD SAMPLE — no MR candidates logged yet")
        return
    d = cands[cands["mr_outcome"].notna()]
    if len(d) < 10:
        print(f"INSUFFICIENT FORWARD SAMPLE — {len(d)} resolved candidates")
        return

    elig = d[d.decision == "MR_ELIGIBLE"]
    blocked = d[d.decision != "MR_ELIGIBLE"]

    s_elig = summarize(elig) if len(elig) else {}
    s_all = summarize(d)
    blocked_winners = int(((blocked.mr_return_pct > 0).sum())) if len(blocked) else 0
    blocked_losers = int(((blocked.mr_return_pct <= 0).sum())) if len(blocked) else 0
    resolved_blocked = blocked[blocked.mr_return_pct.notna()] if len(blocked) else pd.DataFrame()
    resolved_elig = elig[elig.mr_return_pct.notna()] if len(elig) else pd.DataFrame()

    true_block = int((blocked.mr_outcome == "FAIL").sum()) if len(blocked) else 0
    false_block = int(((blocked.mr_return_pct > 0)).sum()) if len(blocked) else 0
    avoided_loss = float(blocked.loc[blocked.mr_return_pct < 0, "mr_return_pct"].sum()) if len(blocked) else 0.0
    missed_profit = float(blocked.loc[blocked.mr_return_pct > 0, "mr_return_pct"].sum()) if len(blocked) else 0.0

    summary = {
        "total_mr_setups": len(d),
        "eligible": len(elig),
        "blocked": len(blocked),
        "eligible_winners": int((elig.mr_return_pct > 0).sum()) if len(elig) else 0,
        "eligible_losers": int((elig.mr_return_pct <= 0).sum()) if len(elig) else 0,
        "blocked_winners": int((blocked.mr_return_pct > 0).sum()) if len(blocked) else 0,
        "blocked_losers": int((blocked.mr_return_pct <= 0).sum()) if len(blocked) else 0,
        "true_block_rate": round(blocked_losers / max(1, len(resolved_blocked)), 4) if len(blocked) else None,
        "false_block_rate": round(blocked_winners / max(1, len(resolved_blocked)), 4) if len(resolved_elig) else None,
        "avg_eligible_return": round(float(elig.mr_return_pct.mean()), 4) if len(elig) else None,
        "avg_blocked_hypothetical_return": round(float(blocked.mr_return_pct.mean()), 4) if len(blocked) else None,
        "avoided_loss": round(float(blocked[blocked.mr_return_pct < 0].mr_return_pct.sum()), 3) if len(blocked) else 0.0,
        "missed_profit": round(float(blocked[blocked.mr_return_pct > 0].mr_return_pct.sum()), 4) if len(blocked) else 0.0,
    }
    # profit factors
    def pf(x):
        w, l = x[x > 0].sum(), x[x <= 0].abs().sum()
        return round(float(w / l), 3) if l > 0 else None
    summary = {
        **{k: v for k, v in summarize(d).items() if k != "win_rate"},
        "total_mr_setups": len(d),
        "eligible": len(elig),
        "blocked": len(blocked),
        "profit_factor_eligible": pf(elig.mr_return_pct) if len(elig) else None,
        "profit_factor_unfiltered": pf(d.mr_return_pct),
        "avg_eligible_return": round(float(elig.mr_return_pct.mean()), 4) if len(elig) else None,
        "avg_blocked_hypothetical_return": round(float(blocked.mr_return_pct.mean()), 4) if len(blocked) else None,
        "avoided_loss": round(float(blocked[blocked.mr_return_pct < 0].mr_return_pct.sum()), 3),
        "missed_profit": round(float(blocked[blocked.mr_return_pct > 0].mr_return_pct.sum()), 4),
    }
    pd.DataFrame([summary]).to_csv(ROOT / "reports" / "forward_mr_gate.csv", index=False)

    lines = ["# Forward MR Gate Report (Phase H)", "",
             f"- Total MR setups: {summary['total_mr_setups']}",
             f"- Eligible: {len(elig)} | Blocked: {len(blocked)}",
             f"- Eligible avg return: {summary['avg_eligible_return']}%",
             f"- Blocked hypothetical avg return: {summary['avg_blocked_hypothetical_return']}%",
             f"- True block rate (blocked would have lost): {summary['true_block_rate']}",
             f"- False block rate: {summary['false_block_rate']}",
             f"- Avoided loss (sum of blocked losers): {summary['avoided_loss']}%",
             f"- Missed profit: {summary['missed_profit']}%",
             f"- PF eligible: {summary['profit_factor_eligible']} | "
             f"PF unfiltered: {summary['profit_factor_unfiltered']}",
             "",
             "Research question: does MR_FAIL reduce left-tail losses without",
             "destroying positive expectancy?"]
    (ROOT / "reports" / "forward_mr_gate_summary.md").write_text("\n".join(lines), encoding="utf-8")
    print(summary)
    print("\nSaved reports/forward_mr_gate.csv + forward_mr_gate_summary.md")


if __name__ == "__main__":
    main()
