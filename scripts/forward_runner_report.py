"""Phase H16 — forward Runner report (OSC_CROSS vs HYBRID).

Compares the two Phase H research exit policies overall and by asset class.
Sample-size flags: LOW_SAMPLE (<20), EARLY (20-49), USABLE_SAMPLE (>=50).
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import load_config
from hybrid_ml.forward_mr import load_runner_events


def sample_flag(n):
    return "LOW_SAMPLE" if n < 20 else ("EARLY" if n < 50 else "USABLE_SAMPLE")


def summarize(g):
    ret = g["return_pct"]
    wins, losses = ret[ret > 0], ret[ret <= 0]
    eq = ret.cumsum()
    return pd.Series({
        "runner_events": len(g),
        "win_rate": round(float((ret > 0).mean()), 4),
        "avg_return_pct": round(float(ret.mean()), 4),
        "median_return_pct": round(float(ret.median()), 4),
        "profit_factor": round(float(wins.sum() / losses.abs().sum()), 3)
                         if losses.abs().sum() > 0 else None,
        "avg_winner": round(float(wins.mean()), 4) if len(wins) else None,
        "avg_loser": round(float(losses.mean()), 4) if len(losses) else None,
        "p90_winner": round(float(ret[ret > 0].quantile(0.9)), 4) if (ret > 0).any() else None,
        "p95_winner": round(float(ret[ret > 0].quantile(0.95)), 4) if (ret > 0).any() else None,
        "worst_trade": round(float(ret.min()), 4),
        "max_drawdown": round(float((eq.cummax() - eq).max()), 3),
        "avg_duration_bars": round(float(g["duration_bars"].mean()), 1) if "duration_bars" in g else None,
    })


def main():
    from hybrid_ml.forward_mr import load_runner_events
    ev = load_runner_events()
    if len(ev) < 5:
        print(f"INSUFFICIENT FORWARD SAMPLE — {len(ev)} runner events")
        return

    rows = []
    for method, ret_col in [("OSC_CROSS", "osc_return_pct"),
                            ("HYBRID", "hybrid_return_pct")]:
        sub = ev[ev[method.lower().replace("_", "") + "_exit_time"].notna()] \
            if False else ev
        d = ev[ev[method.lower().replace("osc", "osc") + "_exit_time"].notna()] if False else ev
        # build long-form: one row per method per event
        for _, r in ev.iterrows():
            rows.append({"method": method, "asset": r["asset"],
                         "return_pct": r["osc_return_pct"] if method == "OSC_CROSS"
                         else r["hybrid_return_pct"],
                         "duration_bars": r.get("duration_osc" if method == "OSC_CROSS"
                                                else "duration_hybrid")})
    sim = pd.DataFrame(rows).dropna(subset=["return_pct"])
    if len(sim) < 5:
        print("INSUFFICIENT FORWARD SAMPLE — runner events not yet resolved")
        return

    def metrics(g):
        ret = g["return_pct"]
        wins, losses = ret[ret > 0], ret[ret <= 0]
        eq = ret.cumsum()
        return pd.Series({
            "runner_events": len(g),
            "win_rate": round(float((ret > 0).mean()), 4),
            "avg_return_pct": round(float(ret.mean()), 4),
            "median_return_pct": round(float(ret.median()), 4),
            "profit_factor": round(float(wins.sum() / losses.abs().sum()), 3)
                             if losses.abs().sum() > 0 else None,
            "avg_winner": round(float(wins.mean()), 4) if len(wins) else None,
            "avg_loser": round(float(losses.mean()), 4) if len(losses) else None,
            "p90_winner": round(float(ret[ret > 0].quantile(0.9)), 4) if (ret > 0).any() else None,
            "p95_winner": round(float(ret[ret > 0].quantile(0.95)), 4) if (ret > 0).any() else None,
            "worst_trade": round(float(ret.min()), 4),
            "max_drawdown": round(float((eq.cummax() - eq).max()), 3),
            "avg_duration_bars": round(float(g["duration"].mean()), 1) if "duration_bars" in g else None,
        })

    sim["method"] = sim["method"].where(sim["method"].isin(["OSC_CROSS", "HYBRID"]))
    by_asset = sim.groupby(["method", "asset"]).apply(
        lambda g: pd.Series({**{k: v for k, v in summarize(g).items()},
                             "sample_flag": ("LOW_SAMPLE" if len(g) < 20 else
                                             "EARLY" if len(g) < 50 else "USABLE_SAMPLE")}),
        include_groups=False).reset_index()
    by_asset.to_csv(ROOT / "reports" / "forward_runner_comparison.csv", index=False)

    lines = ["# Forward Runner Comparison (Phase H)", "",
             "Policies compared in parallel: OSC_CROSS vs HYBRID (Phase G definitions).",
             "No policy selected in real time.", ""]
    for method, g in sim.groupby("method"):
        n = len(g)
        flag = "LOW_SAMPLE" if len(g) < 20 else ("EARLY" if len(g) < 50 else "USABLE_SAMPLE")
        lines.append(f"## {method} ({n} events, {sample_flag})")
        lines.append(f"- win_rate: {round(float((g.return_pct > 0).mean()), 4)}")
        lines.append(f"- avg_return_pct: {round(float(g.return_pct.mean()), 4)}")
        lines.append(f"- profit_factor: {round(float(g[g.return_pct>0].return_pct.sum() / max(1e-9, g[g.return_pct<=0].abs().sum())), 3)}")
        lines.append("")
    (ROOT / "reports" / "forward_runner_summary.md").write_text("\n".join(lines), encoding="utf-8")
    print(sim.groupby("method").apply(
        lambda g: pd.Series({"n": len(g),
                             "win_rate": round(float((g.return_pct > 0).mean()), 4),
                             "avg_return_pct": round(float(g.return_pct.mean()), 4)}),
        include_groups=False))
    print("\nSaved reports/forward_runner_comparison.csv + forward_runner_summary.md")


if __name__ == "__main__":
    main()
