from __future__ import annotations

from pathlib import Path
import subprocess
import sys

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard import charts
from dashboard.components import dataframe_or_empty, frozen_controls_panel, inject_css, metric_card, progress, status_pill
from dashboard.data_loader import (
    ASSETS,
    BROKER_EXECUTION,
    MR_FAIL_THRESHOLD,
    TF_STATUS,
    US500_STATUS,
    load_dashboard_data,
    latest_observation_timestamp,
    latest_scheduler_run,
    log_event,
    format_thailand_timestamp,
    model_freeze_status,
)
from dashboard.metrics import (
    asset_summary,
    calibration_table,
    current_state_table,
    data_completeness_asset_cards,
    data_completeness_gap_details,
    data_completeness_summary,
    gate_impact,
    mr_forward_metrics,
    num,
    asset_selection_score_table,
    performance_summary,
    performance_table,
    pct,
    portfolio_candidate_sets,
    runner_sample_label,
    sample_label,
    simulation_trade_frame,
    common_forward_window,
    strategy_fit_table,
    strategy_return_correlation,
    win_loss_reason_table,
    yahoo_quality_summary,
)


st.set_page_config(page_title="Hybrid MR-TF - Phase H", layout="wide")
inject_css()


@st.cache_data(show_spinner=False)
def cached_data():
    return load_dashboard_data()


def run_price_backfill() -> subprocess.CompletedProcess[str]:
    command = f"""
import subprocess
import sys
from pathlib import Path

root = Path({str(ROOT)!r})
scripts = [
    "check_market_open_completeness.py",
    "backfill_market_open_prices.py",
    "check_market_open_completeness.py",
]
failed = 0
for script in scripts:
    print(f"--- {{script}} ---")
    result = subprocess.run([sys.executable, str(root / "scripts" / script)], cwd=root)
    failed = failed or result.returncode
sys.exit(failed)
"""
    return subprocess.run(
        [sys.executable, "-c", command],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=1200,
        check=False,
    )


def _scoped_completeness(data, *, compact: bool) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    completeness = data.market_open_completeness.copy()
    gaps = data.market_open_gaps.copy()
    if data.asset_registry.empty or "asset" not in data.asset_registry:
        return completeness, gaps, "All"

    registry = data.asset_registry.copy()
    if compact:
        scope = "Core"
    else:
        scope = st.segmented_control("Completeness scope", ["Core", "Candidates", "All"], default="Core")

    if scope == "All":
        return completeness, gaps, scope
    role = "core" if scope == "Core" else "candidate"
    assets = registry[registry["universe_role"].astype(str).str.lower().eq(role)]["asset"].tolist()
    completeness = completeness[completeness["asset"].isin(assets)] if "asset" in completeness else completeness
    gaps = gaps[gaps["asset"].isin(assets)] if "asset" in gaps else gaps
    return completeness, gaps, scope


def render_data_completeness(data, *, compact: bool = False) -> None:
    completeness, gaps, scope = _scoped_completeness(data, compact=compact)
    status, note, problem_rows = data_completeness_summary(completeness)
    st.subheader("Data Completeness Signal")
    if not compact:
        st.caption(f"Scope: {scope}")
    cards = data_completeness_asset_cards(completeness)
    if cards.empty:
        st.info("Run the session-aware completeness check to create the report.")
    else:
        cols = st.columns(3 if compact else 6)
        for idx, row in cards.iterrows():
            with cols[idx % len(cols)]:
                metric_card(
                    str(row["Asset"]),
                    f"{row['Missing open bars']} missing",
                    str(row["Signal"]),
                )
                caption = f"{row['Coverage']} | {row['Calendar']}"
                if int(row.get("Ignored", 0) or 0):
                    caption += f" | ignored {int(row['Ignored'])} provider mismatch"
                st.caption(caption)

    if status == "GREEN":
        st.success(note)
    elif status == "RED":
        st.error(note)
    else:
        st.warning(note)

    if st.button(
        "Check and backfill missing prices",
        icon=":material/sync:",
        type="primary",
        disabled=status != "RED",
        width="stretch" if compact else "content",
    ):
        with st.status("Backfilling missing open-market bars from Yahoo...", expanded=True) as status_box:
            result = run_price_backfill()
            if result.stdout:
                st.code(result.stdout[-4000:])
            if result.stderr:
                st.code(result.stderr[-2000:])
            if result.returncode == 0:
                status_box.update(label="Backfill finished. Refreshing dashboard data.", state="complete")
                st.cache_data.clear()
                st.rerun()
            else:
                status_box.update(label=f"Backfill failed with exit code {result.returncode}.", state="error")

    if not problem_rows.empty:
        details = data_completeness_gap_details(gaps)
        with st.expander("Missing open-market bar details", expanded=not compact):
            st.caption("Closed sessions, weekends, and exchange holidays are excluded. Rows here are only hours the selected market calendar expected to be open.")
            dataframe_or_empty(details, "No missing open-market bars.")


def sidebar(data):
    st.sidebar.title("Phase H Dashboard")
    if st.sidebar.button("Refresh Data", type="primary", width="stretch"):
        log_event("manual refresh")
        st.cache_data.clear()
        st.rerun()
    st.sidebar.caption("Dashboard Loaded (Thailand):")
    st.sidebar.write(data.loaded_at)
    st.sidebar.caption("Latest Phase H Observation (Thailand):")
    st.sidebar.write(latest_observation_timestamp(data))
    st.sidebar.caption("Scheduler Latest Run (Thailand):")
    st.sidebar.write(latest_scheduler_run(data))
    return st.sidebar.radio(
        "Navigation",
        [
            "Overview",
            "MR_FAIL Monitor",
            "Trade Simulation",
            "Asset Selection Lab",
            "MR Gate Analysis",
            "Runner Research",
            "Assets",
            "Latest Market State",
            "Data & Scheduler Health",
            "Forward Observations",
        ],
    )


def page_overview(data):
    freeze = model_freeze_status(data.baseline, data.registry)
    mr = mr_forward_metrics(data.mr_candidates, data.observations)
    yahoo_status, yahoo_note, yahoo_warnings = yahoo_quality_summary(data.price_quality)
    st.title("PHASE H - FROZEN FORWARD VALIDATION")
    st.markdown("**RESEARCH / FORWARD VALIDATION ONLY**  \n**NO BROKER EXECUTION**")
    st.caption(f"Model Version: {freeze['model_version']} | MR_FAIL Threshold: {MR_FAIL_THRESHOLD:.2f} LOCKED | TF: {TF_STATUS} | Data Source: Yahoo Finance")

    completeness_status, _, _ = data_completeness_summary(data.market_open_completeness)
    cols = st.columns(6)
    with cols[0]:
        metric_card("Phase H Decision", data.status["decision"], data.status["decision"])
    with cols[1]:
        metric_card("Model Freeze", freeze["freeze_status"], freeze["freeze_status"])
    with cols[2]:
        metric_card("Scheduler", data.scheduler.get("status", "UNKNOWN"), data.scheduler.get("status", "UNKNOWN"))
    with cols[3]:
        metric_card("Yahoo Data", yahoo_status, yahoo_status)
    with cols[4]:
        metric_card("Completeness", completeness_status, completeness_status)
    with cols[5]:
        days = data.status.get("days_observed", 0)
        metric_card("Days Observed", f"{days} / 28 minimum", "INSUFFICIENT" if days < 28 else "PASS")

    left, right = st.columns([1, 1])
    with left:
        st.subheader("Progress")
        days = int(data.status.get("days_observed", 0))
        progress("Days observed minimum", days, 28)
        progress("Days observed preferred", days, 56)
        progress("MR candidates first checkpoint", int(mr["candidates"]), 30)
        progress("MR candidates preferred", int(mr["candidates"]), 60)
        progress("Resolved MR", int(mr["resolved"]), max(int(mr["candidates"]), 1))
        runner_count = len(data.runner_events)
        progress("Runner events first checkpoint", runner_count, 20)
        progress("Runner events preferred", runner_count, 40)
    with right:
        st.subheader("Observations")
        st.plotly_chart(charts.observations_over_time(data.observations), width="stretch")

    if yahoo_status == "WARNING":
        with st.expander("Why Yahoo Data shows WARNING", expanded=True):
            st.warning(yahoo_note)
            st.caption("This is a data-quality warning, not a broker or model warning. If today is a weekend or the market/session is closed, empty new rows, missing-hour estimates, and large gaps can be expected. Yahoo often reports zero volume for FX, and that does not by itself change model results.")
            dataframe_or_empty(yahoo_warnings, "No warning rows.")

    render_data_completeness(data, compact=True)

    snapshot = pd.DataFrame(
        [
            {"Research Area": "MR_FAIL", "Status": mr["status"], "Key Metric": num(mr["roc_auc"]), "Interpretation": "Risk gate"},
            {"Research Area": "MR Gate", "Status": gate_impact(data.mr_candidates)["status"], "Key Metric": num(gate_impact(data.mr_candidates)["benefit"]), "Interpretation": "Gate value"},
            {"Research Area": "Runner Osc Cross", "Status": "WAITING", "Key Metric": "n/a", "Interpretation": "Exit research"},
            {"Research Area": "Runner Hybrid", "Status": "WAITING", "Key Metric": "n/a", "Interpretation": "Exit research"},
            {"Research Area": "US500", "Status": US500_STATUS, "Key Metric": "-", "Interpretation": "Holdout issue"},
            {"Research Area": "TF", "Status": TF_STATUS, "Key Metric": "historical n=41", "Interpretation": "Rejected"},
        ]
    )
    st.subheader("Research Snapshot")
    dataframe_or_empty(snapshot)
    frozen_controls_panel()
    st.info("A favorable ML score does not create an MR setup. MR requires the original oscillator setup, the locked MR_FAIL gate, model evidence, and asset policy. Runner requires an existing successful MR lifecycle.")


def page_mr_fail(data):
    mr = mr_forward_metrics(data.mr_candidates, data.observations)
    st.title("MR_FAIL Monitor")
    cols = st.columns(5)
    for col, label, value in [
        (cols[0], "ROC-AUC", num(mr["roc_auc"])),
        (cols[1], "PR-AUC", "n/a"),
        (cols[2], "Brier", num(mr["brier"])),
        (cols[3], "ECE", "n/a"),
        (cols[4], "Resolved MR", mr["resolved"]),
    ]:
        with col:
            metric_card(label, value, mr["status"] if label == "ROC-AUC" else None)
    st.caption("Phase G baseline: ROC-AUC approx 0.743 | Brier approx 0.212 | ECE approx 0.098")
    source = data.mr_candidates if not data.mr_candidates.empty else data.observations
    table = calibration_table(source)
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(charts.p_mr_fail_distribution(source), width="stretch")
    with col2:
        st.plotly_chart(charts.calibration_curve(table), width="stretch")
    st.subheader("Calibration Table")
    dataframe_or_empty(table, "WAITING FOR RESOLVED EVENTS")
    st.caption(f"Forward MR_FAIL status: {mr['status']} | Confidence: {mr['confidence']}")


def _metric_value(value, kind: str = "number") -> str:
    if kind == "percent":
        return pct(value)
    if kind == "return_pct":
        return pct((value or 0) / 100)
    if value == float("inf"):
        return "inf"
    return num(value, 2)


def page_trade_simulation(data):
    st.title("Trade Simulation")
    st.caption("Forward research simulation only. These are not broker orders and not realized account P&L.")
    trades = simulation_trade_frame(data.mr_candidates, data.observations)

    if trades.empty:
        st.info("No resolved MR setup simulations yet. The page will populate after candidates have 24h forward returns.", icon=":material/pending:")
        dataframe_or_empty(data.mr_candidates, "No MR candidates yet.", height=320)
        return

    bucket_options = ["All"] + sorted(trades["trade_bucket"].dropna().unique().tolist())
    selected_bucket = st.segmented_control("Simulation view", bucket_options, default="All")
    selected_outcome = st.segmented_control("Outcome", ["All", "Wins", "Losses", "Flat"], default="All")
    asset_options = sorted(trades["asset"].dropna().unique().tolist())
    selected_assets = st.pills("Assets", asset_options, selection_mode="multi", default=asset_options)

    filtered = trades.copy()
    if selected_bucket != "All":
        filtered = filtered[filtered["trade_bucket"] == selected_bucket]
    if selected_outcome != "All":
        outcome_map = {"Wins": "Win", "Losses": "Loss", "Flat": "Flat"}
        filtered = filtered[filtered["outcome"] == outcome_map[selected_outcome]]
    filtered = filtered[filtered["asset"].isin(selected_assets or [])]

    stats = performance_summary(filtered, str(selected_bucket))
    with st.container(horizontal=True):
        st.metric("Orders", stats["orders"], border=True)
        st.metric("Win rate", _metric_value(stats["win_rate"], "percent"), border=True)
        st.metric("Profit factor", _metric_value(stats["profit_factor"]), border=True)
        st.metric("Net return", _metric_value(stats["net_return"], "return_pct"), border=True)
        st.metric("Avg return", _metric_value(stats["avg_return"], "return_pct"), border=True)
        st.metric("Max drawdown", _metric_value(stats["max_drawdown"], "return_pct"), border=True)

    if stats["orders"] < 20:
        st.warning("Sample is still small, so PF and win rate can swing hard. Use this as early evidence only.", icon=":material/warning:")

    left, right = st.columns([1.5, 1])
    with left:
        st.plotly_chart(charts.simulation_equity_curve(filtered, "Cumulative simulation return"), width="stretch")
    with right:
        st.plotly_chart(charts.simulation_win_loss(filtered), width="stretch")

    left, right = st.columns([1, 1])
    with left:
        st.subheader("By asset")
        dataframe_or_empty(performance_table(filtered, "asset"), "No trades for this filter.", height=300)
    with right:
        st.plotly_chart(charts.simulation_return_by_asset(filtered), width="stretch")

    st.subheader("By gate bucket")
    dataframe_or_empty(performance_table(trades, "trade_bucket"), "No bucket summary yet.", height=240)

    st.subheader("Why trades won or lost")
    left, right = st.columns([1, 1])
    with left:
        dataframe_or_empty(win_loss_reason_table(filtered), "No win/loss detail for this filter.", height=300)
    with right:
        st.markdown("**Asset selection readout**")
        dataframe_or_empty(asset_selection_score_table(trades), "No asset ranking yet.", height=300)
        st.caption("Ranking is useful only after enough forward samples. It should shortlist assets, not replace the entry rules.")

    detail_frame = filtered.copy().sort_values("timestamp", ascending=False).reset_index(drop=True)
    if detail_frame.empty:
        st.info("No trade detail available for this filter.", icon=":material/info:")
    else:
        labels = []
        for i, row in detail_frame.iterrows():
            ts = pd.to_datetime(row["timestamp"], errors="coerce")
            ts_label = ts.strftime("%Y-%m-%d %H:%M UTC") if pd.notna(ts) else str(row.get("timestamp"))
            labels.append(
                f"{ts_label} | {row.get('asset')} | {row.get('direction')} | "
                f"{row.get('outcome')} | {float(row.get('sim_return_pct', 0)):.2f}%"
            )
        selected_trade = st.selectbox("Inspect one trade", labels)
        selected_idx = labels.index(selected_trade)
        row = detail_frame.iloc[selected_idx]
        with st.container(border=True):
            st.markdown(f"**{row.get('asset')} {row.get('direction')} - {row.get('outcome')}**")
            st.write(row.get("why", "No explanation available."))
            detail_cols = st.columns(4)
            with detail_cols[0]:
                st.metric("Sim return", pct(float(row.get("sim_return_pct", 0)) / 100), border=True)
            with detail_cols[1]:
                st.metric("p_mr_fail", num(row.get("p_mr_fail"), 2), border=True)
            with detail_cols[2]:
                st.metric("p_mr_win", num(row.get("p_mr_win"), 2), border=True)
            with detail_cols[3]:
                st.metric("Vol ratio", num(row.get("vol_ratio"), 2), border=True)
            fields = [
                "timestamp",
                "decision",
                "decision_reason",
                "trade_bucket",
                "future_return_24h",
                "pred_mr_return_pct",
                "osc",
                "signal",
                "osc_minus_signal",
                "osc_slope_1",
                "osc_slope_3",
                "price_direction_12",
                "price_direction_24",
                "atr",
                "natr",
                "close",
            ]
            detail = pd.DataFrame([{"Field": f, "Value": row.get(f, "")} for f in fields if f in row.index])
            dataframe_or_empty(detail, "No detail fields.", height=300)

    st.info(
        "Forward trade simulation can become an asset-selection engine: rank many assets by out-of-sample PF, win rate, drawdown, sample size, and data completeness, then trade only the strongest shortlist. The important rule is to freeze the selection formula first and validate it forward, otherwise it becomes curve fitting.",
        icon=":material/query_stats:",
    )

    st.subheader("Resolved simulation trades")
    display = filtered.copy()
    for col in ["timestamp"]:
        if col in display:
            display[col] = pd.to_datetime(display[col], errors="coerce").dt.strftime("%Y-%m-%d %H:%M UTC")
    ordered = [
        "timestamp",
        "asset",
        "direction",
        "decision",
        "trade_bucket",
        "p_mr_win",
        "p_mr_fail",
        "pred_mr_return_pct",
        "future_return_24h",
        "sim_return_pct",
    ]
    present = [c for c in ordered if c in display]
    dataframe_or_empty(display[present], "No resolved simulation trades for this filter.", height=360)


def page_asset_selection_lab(data):
    st.title("Asset Selection Lab")
    st.caption("Research-only portfolio selection from forward simulation results. Use this to shortlist assets before any live decision.")
    trades = simulation_trade_frame(data.mr_candidates, data.observations)
    if trades.empty:
        st.info("No resolved simulation trades yet. Asset selection will become meaningful after enough forward outcomes.", icon=":material/pending:")
        dataframe_or_empty(data.asset_registry, "No asset registry configured.", height=280)
        return

    registry = data.asset_registry.copy()
    universe_view = st.segmented_control("Universe", ["Forward cohort", "All registry"], default="Forward cohort")
    if not registry.empty and "forward_research_enabled" in registry and universe_view == "Forward cohort":
        registry = registry[registry["forward_research_enabled"].astype(bool)]

    classes = sorted(registry["asset_class"].dropna().unique().tolist()) if not registry.empty and "asset_class" in registry else []
    selected_classes = st.pills("Asset classes", classes, selection_mode="multi", default=classes) if classes else []
    selected_bucket = st.segmented_control("Trade set", ["All", "Gate allowed", "Gate blocked", "Research only"], default="All")
    timeline_mode = st.segmented_control("Comparison window", ["Common forward window", "All resolved samples"], default="Common forward window")
    max_corr = st.slider("Max average correlation for low-correlation set", min_value=0.0, max_value=1.0, value=0.65, step=0.05)

    filtered = trades.copy()
    window_source = data.observations.copy()
    if not registry.empty and "asset" in registry:
        registry_assets = registry["asset"].tolist()
        filtered = filtered[filtered["asset"].isin(registry_assets)]
        if not window_source.empty and "asset" in window_source:
            window_source = window_source[window_source["asset"].isin(registry_assets)]
    if selected_bucket != "All":
        filtered = filtered[filtered["trade_bucket"] == selected_bucket]
    if selected_classes and not registry.empty:
        class_assets = registry[registry["asset_class"].isin(selected_classes)]["asset"].tolist()
        filtered = filtered[filtered["asset"].isin(class_assets)]
        if not window_source.empty and "asset" in window_source:
            window_source = window_source[window_source["asset"].isin(class_assets)]

    window = common_forward_window(window_source)
    if timeline_mode == "Common forward window" and window["usable"]:
        filtered = filtered[
            (pd.to_datetime(filtered["timestamp"], errors="coerce") >= window["start"])
            & (pd.to_datetime(filtered["timestamp"], errors="coerce") <= window["end"])
        ]
    elif timeline_mode == "Common forward window":
        st.warning("Common forward window is not usable yet. Showing available resolved samples for now.", icon=":material/warning:")

    asset_count = max(1, int(filtered["asset"].nunique()) if not filtered.empty and "asset" in filtered else 1)
    top_n = st.slider("Portfolio size", min_value=1, max_value=max(1, min(12, asset_count)), value=min(5, asset_count))

    fit = strategy_fit_table(filtered, registry, data.market_open_completeness)
    portfolios, curves = portfolio_candidate_sets(filtered, fit, top_n=top_n, max_avg_corr=max_corr)
    best = portfolios.copy()
    if not best.empty:
        best["_net"] = best["Net return"].str.rstrip("%").replace("n/a", "0").astype(float)
        best = best.sort_values("_net", ascending=False).iloc[0]

    with st.container(horizontal=True):
        st.metric("Assets scored", len(fit), border=True)
        st.metric("Simulation orders", len(filtered), border=True)
        st.metric("Comparison", timeline_mode, border=True)
        st.metric("Best portfolio", best["Portfolio"] if not portfolios.empty else "n/a", border=True)
        st.metric("Best net return", best["Net return"] if not portfolios.empty else "n/a", border=True)
        st.metric("Best PF", best["PF"] if not portfolios.empty else "n/a", border=True)

    if window["usable"]:
        st.caption(
            f"Common forward window: {window['start'].strftime('%Y-%m-%d %H:%M UTC')} "
            f"to {window['end'].strftime('%Y-%m-%d %H:%M UTC')} across {window['assets']} asset(s)."
        )
    if universe_view == "All registry":
        st.info("Data-only candidates are shown for readiness, but their score stays 0 until forward research and selection are enabled.", icon=":material/info:")

    chart_rows = min(len(fit), 24) if not fit.empty else 0

    left, right = st.columns([1.4, 1])
    with left:
        st.plotly_chart(charts.portfolio_equity_curve(curves), width="stretch")
    with right:
        st.plotly_chart(charts.strategy_fit_score_bar(fit.head(chart_rows)), width="stretch")

    left, right = st.columns([1, 1])
    with left:
        st.subheader("Portfolio candidates")
        dataframe_or_empty(portfolios, "No portfolio candidate yet.", height=280)
    with right:
        st.subheader("Strategy-return correlation")
        st.plotly_chart(charts.strategy_correlation_heatmap(strategy_return_correlation(filtered)), width="stretch")

    st.subheader("Asset ranking")
    if fit.empty:
        st.info("No asset ranking yet.")
    else:
        st.dataframe(
            fit,
            hide_index=True,
            height=360,
            width="stretch",
            column_config={
                "Score": st.column_config.ProgressColumn("Score", min_value=0, max_value=100, format="%.1f"),
            },
        )

    st.subheader("Asset registry")
    data_only = data.asset_registry.copy()
    if not data_only.empty and "forward_research_enabled" in data_only:
        data_only = data_only[~data_only["forward_research_enabled"].astype(bool)]
    registry_tabs = st.tabs(["Data-only candidates", "Full registry"])
    with registry_tabs[0]:
        dataframe_or_empty(data_only, "No data-only candidates.", height=260)
    with registry_tabs[1]:
        dataframe_or_empty(data.asset_registry, "No asset registry configured.", height=260)
    st.info(
        "The score favors assets that make money alone, have enough forward samples, avoid large drawdown, have complete data, and diversify the other assets. It is a shortlist engine, not a new entry signal.",
        icon=":material/account_tree:",
    )


def page_mr_gate(data):
    st.title("MR Gate Analysis")
    impact = gate_impact(data.mr_candidates)
    cols = st.columns(5)
    with cols[0]:
        metric_card("Blocked Losers", impact["blocked_losers"])
    with cols[1]:
        metric_card("Blocked Winners", impact["blocked_winners"])
    with cols[2]:
        metric_card("Avoided Loss", num(impact["avoided_loss"]))
    with cols[3]:
        metric_card("Missed Profit", num(impact["missed_profit"]))
    with cols[4]:
        metric_card("Gate Benefit", num(impact["benefit"]), impact["status"])
    dataframe_or_empty(data.forward_mr_gate, "INSUFFICIENT DATA")
    st.plotly_chart(charts.cumulative_returns(data.forward_mr_gate, ["unfiltered_return", "gated_return", "hypothetical_return"], "Forward Research Simulation - Not Broker P&L"), width="stretch")


def page_runner(data):
    st.title("Runner Research")
    st.info("Runner is not a standalone entry engine. Runner begins only after a successful MR trade reaches the Runner transition point.")
    cols = st.columns(3)
    with cols[0]:
        metric_card("Runner Events", len(data.runner_events), runner_sample_label(len(data.runner_events)))
    with cols[1]:
        metric_card("OSC_CROSS", "WAITING")
    with cols[2]:
        metric_card("HYBRID", "WAITING")
    dataframe_or_empty(data.forward_runner_comparison, "No resolved Runner events yet.")
    st.plotly_chart(charts.cumulative_returns(data.runner_events, ["runner_return_osc_cross", "runner_return_hybrid"], "Parallel Forward Research"), width="stretch")
    st.plotly_chart(charts.count_by_asset(data.runner_events, "Runner Events by Asset"), width="stretch")


def page_assets(data):
    st.title("Assets")
    summary = asset_summary(data.latest_scores, data.observations, data.runner_events)
    dataframe_or_empty(summary)
    asset = st.selectbox("Asset", ASSETS)
    latest = data.latest_scores[data.latest_scores["asset"] == asset].tail(1) if not data.latest_scores.empty and "asset" in data.latest_scores else pd.DataFrame()
    obs = data.observations[data.observations["asset"] == asset].tail(20) if not data.observations.empty and "asset" in data.observations else pd.DataFrame()
    st.subheader(f"{asset} Detail")
    columns = ["er_10", "er_20", "er_40", "atr", "natr", "vol_ratio", "cross_count", "osc", "signal", "osc_minus_signal", "osc_slope_1", "p_mr_win", "p_mr_fail", "pred_mr_return_pct", "p_runner_win", "pred_runner_return_pct", "mr_setup", "mr_gate_pass", "asset_policy", "position_state", "recommended_action"]
    present = [c for c in columns if c in latest]
    dataframe_or_empty(latest[present] if present else latest, "NOT YET AVAILABLE")
    st.subheader("Recent Observations")
    dataframe_or_empty(obs, "NOT YET AVAILABLE", height=300)


def page_market_state(data):
    st.title("Latest Market State")
    table = current_state_table(data.latest_scores)
    dataframe_or_empty(table, "NOT YET AVAILABLE", height=420)
    st.plotly_chart(charts.latest_probability_bar(data.latest_scores, "p_mr_fail", "Latest p_mr_fail by Asset"), width="stretch")
    st.caption("Low p_mr_fail alone is NOT an entry signal. Original MR setup must also exist.")
    st.subheader("Position Lifecycle")
    positions = data.current_positions
    rows = [{"Asset": k, **v} for k, v in positions.items() if isinstance(v, dict) and v.get("state") != "FLAT"]
    dataframe_or_empty(pd.DataFrame(rows), "No non-FLAT positions.")


def page_health(data):
    st.title("Data & Scheduler Health")
    freeze = model_freeze_status(data.baseline, data.registry)
    left, right = st.columns(2)
    with left:
        st.subheader("Scheduler Health")
        dataframe_or_empty(pd.DataFrame([data.scheduler]))
    with right:
        st.subheader("Model Freeze Health")
        dataframe_or_empty(pd.DataFrame([freeze]))
        if freeze["freeze_status"] != "PASS":
            st.error("PHASE H MODEL FREEZE VIOLATION")
    st.subheader("Yahoo Data Quality")
    dataframe_or_empty(data.price_quality, "NOT YET AVAILABLE")
    render_data_completeness(data)
    st.subheader("Observation Freshness")
    if data.observations.empty or "asset" not in data.observations or "timestamp" not in data.observations:
        st.info("NOT YET AVAILABLE")
    else:
        fresh = data.observations.copy()
        fresh["timestamp"] = pd.to_datetime(fresh["timestamp"], errors="coerce")
        out = fresh.groupby("asset", as_index=False)["timestamp"].max().rename(columns={"timestamp": "Last Phase H Observation"})
        out["Last Phase H Observation"] = out["Last Phase H Observation"].apply(format_thailand_timestamp)
        dataframe_or_empty(out)


def page_forward_observations(data):
    st.title("Forward Observations")
    obs = data.observations.copy()
    if not obs.empty and "asset" in obs:
        assets = st.multiselect("Asset", sorted(obs["asset"].dropna().unique()), default=sorted(obs["asset"].dropna().unique()))
        obs = obs[obs["asset"].isin(assets)]
    dataframe_or_empty(obs, "WAITING FOR PHASE H OBSERVATIONS", height=420)
    st.download_button("Download selected observations CSV", obs.to_csv(index=False), "phase_h_observations_selected.csv", "text/csv", disabled=obs.empty)
    st.subheader("MR Candidates")
    dataframe_or_empty(data.mr_candidates, "No MR candidates yet.", height=320)
    st.subheader("Runner Events")
    dataframe_or_empty(data.runner_events, "No Runner events yet.", height=320)


def main():
    data = cached_data()
    page = sidebar(data)
    if page == "Overview":
        page_overview(data)
    elif page == "MR_FAIL Monitor":
        page_mr_fail(data)
    elif page == "Trade Simulation":
        page_trade_simulation(data)
    elif page == "Asset Selection Lab":
        page_asset_selection_lab(data)
    elif page == "MR Gate Analysis":
        page_mr_gate(data)
    elif page == "Runner Research":
        page_runner(data)
    elif page == "Assets":
        page_assets(data)
    elif page == "Latest Market State":
        page_market_state(data)
    elif page == "Data & Scheduler Health":
        page_health(data)
    else:
        page_forward_observations(data)

    st.sidebar.caption(f"Safety: model retraining disabled | threshold editing disabled | broker execution {BROKER_EXECUTION}")


if __name__ == "__main__":
    main()
