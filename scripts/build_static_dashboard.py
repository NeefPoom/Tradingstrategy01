"""Build a static GitHub Pages dashboard from the latest Phase H reports."""
from __future__ import annotations

from datetime import datetime, timezone
from html import escape
from pathlib import Path
import json
import sys

import pandas as pd
import plotly.io as pio

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from dashboard import charts
from dashboard.data_loader import load_dashboard_data
from dashboard.metrics import (
    common_forward_window,
    data_completeness_summary,
    expansion_candidate_table,
    performance_summary,
    portfolio_candidate_sets,
    simulation_trade_frame,
    strategy_fit_table,
    strategy_return_correlation,
)


DOCS = ROOT / "docs"


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size <= 2:
        return pd.DataFrame()
    return pd.read_csv(path)


def _fmt(value) -> str:
    if value is None:
        return "n/a"
    try:
        if pd.isna(value):
            return "n/a"
    except Exception:
        pass
    return escape(str(value))


def _table(df: pd.DataFrame, limit: int = 30) -> str:
    if df.empty:
        return '<div class="empty">No data yet</div>'
    frame = df.head(limit).copy()
    headers = "".join(f"<th>{escape(str(col))}</th>" for col in frame.columns)
    rows = []
    for _, row in frame.iterrows():
        cells = "".join(f"<td>{_fmt(row[col])}</td>" for col in frame.columns)
        rows.append(f"<tr>{cells}</tr>")
    return f'<div class="table-wrap"><table><thead><tr>{headers}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


def _filterable_table(df: pd.DataFrame, table_id: str, limit: int = 80) -> str:
    if df.empty:
        return '<div class="empty">No data yet</div>'
    frame = df.head(limit).copy()
    headers = "".join(f"<th>{escape(str(col))}</th>" for col in frame.columns)
    rows = []
    for _, row in frame.iterrows():
        role = str(row.get("Role", "")).lower()
        stage = str(row.get("Stage", "")).lower().replace(" ", "-")
        asset_class = str(row.get("Class", "")).lower()
        cells = "".join(f"<td>{_fmt(row[col])}</td>" for col in frame.columns)
        rows.append(f'<tr data-role="{escape(role)}" data-stage="{escape(stage)}" data-class="{escape(asset_class)}">{cells}</tr>')
    return (
        f'<div class="table-wrap"><table id="{escape(table_id)}">'
        f"<thead><tr>{headers}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>"
    )


def _fig_html(fig) -> str:
    return pio.to_html(fig, include_plotlyjs=False, full_html=False, config={"displayModeBar": False})


def _metric(label: str, value: str, status: str | None = None) -> str:
    css = (status or "").lower().replace(" ", "-")
    pill = f'<span class="pill {css}">{escape(status)}</span>' if status else ""
    return f"""
    <section class="metric">
      <div class="label">{escape(label)}</div>
      <div class="value">{escape(value)}</div>
      {pill}
    </section>
    """


def build() -> str:
    data = load_dashboard_data()
    completeness_status, completeness_note, _ = data_completeness_summary(data.market_open_completeness)
    trades = simulation_trade_frame(data.mr_candidates, data.observations)
    fit = strategy_fit_table(trades, data.asset_registry, data.market_open_completeness)
    expansion = expansion_candidate_table(fit, data.asset_registry, data.latest_scores)
    core_fit = fit[fit["Role"].astype(str).str.lower().eq("core")].copy() if not fit.empty and "Role" in fit else pd.DataFrame()
    candidate_fit = fit[fit["Role"].astype(str).str.lower().eq("candidate")].copy() if not fit.empty and "Role" in fit else pd.DataFrame()
    portfolios, curves = portfolio_candidate_sets(trades, fit, top_n=5, max_avg_corr=0.65)
    stats = performance_summary(trades)
    corr = strategy_return_correlation(trades)
    window = common_forward_window(data.observations)
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    registry_counts = {}
    if not data.asset_registry.empty and "universe_role" in data.asset_registry:
        registry_counts = data.asset_registry["universe_role"].value_counts().to_dict()

    latest_scores = data.latest_scores.copy()
    if not latest_scores.empty:
        keep = [
            "asset",
            "timestamp",
            "data_status",
            "position_state",
            "mr_setup",
            "p_mr_win",
            "p_mr_fail",
            "pred_mr_return_pct",
            "recommended_action",
        ]
        latest_scores = latest_scores[[c for c in keep if c in latest_scores]]

    promote_count = int((expansion["Stage"] == "Promote candidate").sum()) if not expansion.empty and "Stage" in expansion else 0
    watch_count = int((expansion["Stage"] == "Watchlist").sum()) if not expansion.empty and "Stage" in expansion else 0
    collect_count = int((expansion["Stage"] == "Collect forward sample").sum()) if not expansion.empty and "Stage" in expansion else 0

    common = ""
    if window["usable"]:
        common = (
            f"Common forward window: {window['start'].strftime('%Y-%m-%d %H:%M UTC')} "
            f"to {window['end'].strftime('%Y-%m-%d %H:%M UTC')} across {window['assets']} assets."
        )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="900">
  <title>Hybrid MR-TF Phase H Dashboard</title>
  <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #0b0f17;
      --panel: #111827;
      --muted: #9ca3af;
      --border: #243044;
      --green: #16a34a;
      --amber: #f59e0b;
      --red: #dc2626;
      --blue: #60a5fa;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Arial, sans-serif;
      background: var(--bg);
      color: #f8fafc;
      letter-spacing: 0;
    }}
    main {{ width: min(1440px, calc(100vw - 32px)); margin: 0 auto; padding: 24px 0 48px; }}
    header {{ display: flex; justify-content: space-between; gap: 16px; align-items: flex-start; margin-bottom: 18px; }}
    h1 {{ margin: 0; font-size: clamp(1.6rem, 2.5vw, 2.4rem); }}
    h2 {{ margin: 28px 0 12px; font-size: 1.1rem; }}
    .sub, .note {{ color: var(--muted); font-size: .9rem; }}
    .grid {{ display: grid; grid-template-columns: repeat(6, minmax(150px, 1fr)); gap: 12px; }}
    .metric, .panel {{
      border: 1px solid var(--border);
      background: var(--panel);
      border-radius: 8px;
      padding: 14px;
      min-width: 0;
    }}
    .label {{ color: var(--muted); font-size: .78rem; text-transform: uppercase; }}
    .value {{ font-size: 1.3rem; font-weight: 800; margin-top: 4px; overflow-wrap: anywhere; }}
    .pill {{ display: inline-block; margin-top: 8px; padding: 4px 8px; border-radius: 6px; font-size: .75rem; font-weight: 800; color: #020617; background: #64748b; }}
    .green, .pass, .continue-forward-validation {{ background: var(--green); }}
    .warning, .yellow, .early, .watchlist, .collect-forward-sample {{ background: var(--amber); }}
    .red, .failed, .fail {{ background: var(--red); }}
    .phase-h-core, .promote-candidate {{ background: var(--green); }}
    .do-not-promote-yet, .fix-data-first {{ background: var(--red); }}
    .controls {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0; }}
    button {{
      border: 1px solid var(--border);
      background: #182033;
      color: #f8fafc;
      border-radius: 6px;
      padding: 8px 11px;
      font-weight: 700;
      cursor: pointer;
    }}
    button.active {{ background: var(--blue); color: #06101f; border-color: var(--blue); }}
    .legend {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }}
    .mini {{ margin: 0; padding: 3px 7px; color: #020617; }}
    .charts {{ display: grid; grid-template-columns: 1.25fr .95fr; gap: 14px; align-items: start; }}
    .tables {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }}
    .table-wrap {{ overflow: auto; max-height: 520px; border: 1px solid var(--border); border-radius: 8px; }}
    table {{ width: 100%; border-collapse: collapse; font-size: .86rem; min-width: 720px; }}
    th, td {{ padding: 9px 10px; border-bottom: 1px solid var(--border); text-align: left; white-space: nowrap; }}
    th {{ position: sticky; top: 0; background: #182033; z-index: 1; }}
    .empty {{ color: var(--muted); padding: 18px; border: 1px solid var(--border); border-radius: 8px; }}
    footer {{ margin-top: 24px; color: var(--muted); font-size: .82rem; }}
    @media (max-width: 1100px) {{ .grid, .charts, .tables {{ grid-template-columns: 1fr 1fr; }} }}
    @media (max-width: 760px) {{ main {{ width: min(100vw - 20px, 720px); }} .grid, .charts, .tables {{ grid-template-columns: 1fr; }} header {{ display: block; }} }}
  </style>
</head>
<body>
<main>
  <header>
    <div>
      <h1>Hybrid MR-TF Phase H Dashboard</h1>
      <div class="sub">Research / forward validation only. No broker execution.</div>
    </div>
    <div class="sub">Data generated {escape(updated)}<br>Browser reloads every 15 minutes</div>
  </header>

  <div class="grid">
    {_metric("Phase H decision", str(data.status.get("decision", "UNKNOWN")), str(data.status.get("decision", "UNKNOWN")))}
    {_metric("Yahoo data", "PASS" if not data.price_quality.empty and data.price_quality["status"].astype(str).str.upper().eq("PASS").all() else "CHECK", "PASS" if not data.price_quality.empty and data.price_quality["status"].astype(str).str.upper().eq("PASS").all() else "WARNING")}
    {_metric("Completeness", completeness_status, completeness_status)}
    {_metric("Assets tracked", str(len(data.asset_registry)), "PASS")}
    {_metric("Core / candidate", f"{registry_counts.get('core', 0)} / {registry_counts.get('candidate', 0)}")}
    {_metric("Simulation orders", str(stats["orders"]), stats["status"])}
  </div>
  <div class="grid" style="margin-top: 12px;">
    {_metric("Promotion candidates", str(promote_count), "PROMOTE CANDIDATE" if promote_count else "COLLECT FORWARD SAMPLE")}
    {_metric("Watchlist", str(watch_count), "WATCHLIST" if watch_count else None)}
    {_metric("Collecting sample", str(collect_count), "COLLECT FORWARD SAMPLE")}
    {_metric("Forward cohort", str(len(fit[fit["Orders"] > 0]) if not fit.empty else 0))}
    {_metric("Expansion start", "2026-09-08 00:00 ICT")}
    {_metric("Minimum sample", "30 setups")}
  </div>

  <section class="panel" style="margin-top: 14px;">
    <strong>Data completeness</strong>
    <div class="note">{escape(completeness_note)}</div>
  </section>

  <h2>Portfolio simulation</h2>
  <div class="note">{escape(common)}</div>
  <div class="charts">
    <div class="panel">{_fig_html(charts.portfolio_equity_curve(curves))}</div>
    <div class="panel">{_fig_html(charts.strategy_fit_score_bar(fit.head(24)))}</div>
  </div>

  <h2>Asset selection</h2>
  <section class="panel">
    <strong>How to read this</strong>
    <div class="note">
      Phase H core is the original frozen forward test cohort. Expansion candidates are collected from 2026-09-08 00:00 ICT
      (2026-09-07 17:00 UTC) onward,
      so they are not promoted from historical backfill. A candidate needs complete data and at least 30 resolved setups before
      its strategy fit score should be treated as selection evidence.
    </div>
    <div class="legend">
      <span class="pill mini phase-h-core">Phase H core</span>
      <span class="pill mini promote-candidate">Promote candidate</span>
      <span class="pill mini watchlist">Watchlist</span>
      <span class="pill mini collect-forward-sample">Collect sample</span>
      <span class="pill mini fix-data-first">Fix data first</span>
    </div>
  </section>
  <div class="controls" data-table="promotion-table">
    <button class="active" data-filter="all">All</button>
    <button data-filter="role:core">Phase H core</button>
    <button data-filter="stage:promote-candidate">Promote</button>
    <button data-filter="stage:watchlist">Watchlist</button>
    <button data-filter="stage:collect-forward-sample">Collect sample</button>
    <button data-filter="class:fx">FX</button>
    <button data-filter="class:crypto">Crypto</button>
    <button data-filter="class:index">Index</button>
  </div>
  {_filterable_table(expansion, "promotion-table", limit=80)}

  <h2>Phase H core scoreboard</h2>
  {_table(core_fit, limit=20)}

  <h2>Expansion candidate scoreboard</h2>
  {_table(candidate_fit, limit=80)}

  <div class="tables">
    <div>
      <h2>Portfolio candidates</h2>
      {_table(portfolios, limit=20)}
    </div>
    <div>
      <h2>Strategy correlation</h2>
      <div class="panel">{_fig_html(charts.strategy_correlation_heatmap(corr))}</div>
    </div>
  </div>

  <h2>Full asset ranking</h2>
  {_table(fit, limit=60)}

  <h2>Latest market state</h2>
  {_table(latest_scores, limit=60)}

  <h2>Tracked universe</h2>
  {_table(data.asset_registry, limit=80)}

  <footer>
    Built by GitHub Actions from repository data. This page is research-only and does not place broker orders.
  </footer>
</main>
<script>
  document.querySelectorAll(".controls").forEach((group) => {{
    const table = document.getElementById(group.dataset.table);
    if (!table) return;
    const buttons = group.querySelectorAll("button");
    buttons.forEach((button) => {{
      button.addEventListener("click", () => {{
        buttons.forEach((b) => b.classList.remove("active"));
        button.classList.add("active");
        const filter = button.dataset.filter;
        table.querySelectorAll("tbody tr").forEach((row) => {{
          let show = true;
          if (filter && filter !== "all") {{
            const [key, value] = filter.split(":");
            show = row.dataset[key] === value;
          }}
          row.style.display = show ? "" : "none";
        }});
      }});
    }});
  }});
</script>
</body>
</html>
"""


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "index.html").write_text(build(), encoding="utf-8")
    meta = {"generated_at_utc": datetime.now(timezone.utc).isoformat()}
    (DOCS / "dashboard_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Saved {DOCS / 'index.html'}")


if __name__ == "__main__":
    main()
