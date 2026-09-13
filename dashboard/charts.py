"""Plotly charts for the Phase H dashboard."""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from .data_loader import MR_FAIL_THRESHOLD


def empty_figure(message: str = "NOT YET AVAILABLE") -> go.Figure:
    fig = go.Figure()
    fig.add_annotation(text=message, x=0.5, y=0.5, showarrow=False, font={"size": 16, "color": "#9ca3af"})
    fig.update_layout(height=260, template="plotly_dark", margin=dict(l=20, r=20, t=30, b=20))
    return fig


def observations_over_time(df: pd.DataFrame) -> go.Figure:
    if df.empty or "timestamp" not in df:
        return empty_figure("WAITING FOR PHASE H OBSERVATIONS")
    frame = df.copy()
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    frame = frame.dropna(subset=["timestamp"]).sort_values("timestamp")
    if frame.empty:
        return empty_figure("WAITING FOR PHASE H OBSERVATIONS")
    frame["count"] = range(1, len(frame) + 1)
    fig = px.line(frame, x="timestamp", y="count", color="asset" if "asset" in frame else None, markers=True)
    fig.update_layout(template="plotly_dark", height=290, margin=dict(l=20, r=20, t=35, b=20), title="Observations Accumulated")
    return fig


def latest_probability_bar(df: pd.DataFrame, column: str, title: str) -> go.Figure:
    if df.empty or "asset" not in df or column not in df:
        return empty_figure("NOT YET AVAILABLE")
    frame = df[["asset", column]].copy()
    frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame.dropna()
    if frame.empty:
        return empty_figure("NOT YET AVAILABLE")
    fig = px.bar(frame, x="asset", y=column, color=column, color_continuous_scale="RdYlGn_r")
    if column == "p_mr_fail":
        fig.add_hline(y=MR_FAIL_THRESHOLD, line_dash="dash", line_color="#f59e0b", annotation_text="0.45 LOCKED")
    fig.update_layout(template="plotly_dark", height=290, margin=dict(l=20, r=20, t=35, b=20), title=title, coloraxis_showscale=False)
    return fig


def p_mr_fail_distribution(df: pd.DataFrame) -> go.Figure:
    if df.empty or "p_mr_fail" not in df:
        return empty_figure("WAITING FOR MR CANDIDATES")
    frame = df.copy()
    frame["p_mr_fail"] = pd.to_numeric(frame["p_mr_fail"], errors="coerce")
    frame = frame.dropna(subset=["p_mr_fail"])
    if frame.empty:
        return empty_figure("WAITING FOR MR CANDIDATES")
    if "mr_eligible" in frame:
        frame["Gate"] = frame["mr_eligible"].map({True: "accepted", False: "blocked"}).fillna("all")
    else:
        frame["Gate"] = "all"
    fig = px.histogram(frame, x="p_mr_fail", color="Gate", nbins=20, barmode="overlay")
    fig.add_vline(x=MR_FAIL_THRESHOLD, line_dash="dash", line_color="#f59e0b", annotation_text="0.45 LOCKED")
    fig.update_layout(template="plotly_dark", height=310, margin=dict(l=20, r=20, t=35, b=20), title="p_mr_fail Distribution")
    return fig


def calibration_curve(table: pd.DataFrame) -> go.Figure:
    if table.empty or "Mean Predicted" not in table or "Actual Fail Rate" not in table:
        return empty_figure("WAITING FOR RESOLVED EVENTS")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", name="Ideal", line=dict(dash="dash", color="#94a3b8")))
    fig.add_trace(go.Scatter(x=table["Mean Predicted"], y=table["Actual Fail Rate"], mode="markers+lines", name="Forward bins"))
    fig.update_layout(template="plotly_dark", height=310, margin=dict(l=20, r=20, t=35, b=20), title="Calibration")
    return fig


def cumulative_returns(df: pd.DataFrame, columns: list[str], title: str) -> go.Figure:
    present = [c for c in columns if c in df]
    if df.empty or not present:
        return empty_figure("WAITING FOR RESOLVED EVENTS")
    frame = df.copy().reset_index(drop=True)
    fig = go.Figure()
    for col in present:
        vals = pd.to_numeric(frame[col], errors="coerce").fillna(0).cumsum()
        fig.add_trace(go.Scatter(x=list(range(1, len(vals) + 1)), y=vals, mode="lines+markers", name=col))
    fig.update_layout(template="plotly_dark", height=310, margin=dict(l=20, r=20, t=35, b=20), title=title)
    return fig


def count_by_asset(df: pd.DataFrame, title: str) -> go.Figure:
    if df.empty or "asset" not in df:
        return empty_figure("NOT YET AVAILABLE")
    frame = df.groupby("asset", dropna=False).size().reset_index(name="count")
    fig = px.bar(frame, x="asset", y="count")
    fig.update_layout(template="plotly_dark", height=280, margin=dict(l=20, r=20, t=35, b=20), title=title)
    return fig


def simulation_equity_curve(df: pd.DataFrame, title: str) -> go.Figure:
    if df.empty or "timestamp" not in df or "sim_return_pct" not in df:
        return empty_figure("WAITING FOR RESOLVED SIMULATION TRADES")
    frame = df.copy()
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    frame["sim_return_pct"] = pd.to_numeric(frame["sim_return_pct"], errors="coerce")
    frame = frame.dropna(subset=["timestamp", "sim_return_pct"]).sort_values("timestamp")
    if frame.empty:
        return empty_figure("WAITING FOR RESOLVED SIMULATION TRADES")
    color_col = "trade_bucket" if "trade_bucket" in frame else None
    if color_col:
        curves = []
        for bucket, bucket_df in frame.groupby(color_col):
            x = bucket_df.sort_values("timestamp").copy()
            x["equity"] = x["sim_return_pct"].cumsum()
            curves.append(x)
        frame = pd.concat(curves, ignore_index=True)
        fig = px.line(frame, x="timestamp", y="equity", color=color_col, markers=True)
    else:
        frame["equity"] = frame["sim_return_pct"].cumsum()
        fig = px.line(frame, x="timestamp", y="equity", markers=True)
    fig.update_layout(
        template="plotly_dark",
        height=340,
        margin=dict(l=20, r=20, t=35, b=20),
        title=title,
        yaxis_title="Cumulative return %",
        xaxis_title="Time",
    )
    return fig


def simulation_return_by_asset(df: pd.DataFrame) -> go.Figure:
    if df.empty or "asset" not in df or "sim_return_pct" not in df:
        return empty_figure("WAITING FOR RESOLVED SIMULATION TRADES")
    frame = df.copy()
    frame["sim_return_pct"] = pd.to_numeric(frame["sim_return_pct"], errors="coerce")
    frame = frame.dropna(subset=["sim_return_pct"])
    if frame.empty:
        return empty_figure("WAITING FOR RESOLVED SIMULATION TRADES")
    grouped = frame.groupby("asset", as_index=False).agg(
        net_return=("sim_return_pct", "sum"),
        orders=("sim_return_pct", "size"),
    )
    fig = px.bar(grouped, x="asset", y="net_return", color="net_return", text="orders", color_continuous_scale="RdYlGn")
    fig.update_layout(
        template="plotly_dark",
        height=300,
        margin=dict(l=20, r=20, t=35, b=20),
        title="Net return by asset",
        yaxis_title="Net return %",
        xaxis_title="Asset",
        coloraxis_showscale=False,
    )
    return fig


def simulation_win_loss(df: pd.DataFrame) -> go.Figure:
    if df.empty or "sim_return_pct" not in df:
        return empty_figure("WAITING FOR RESOLVED SIMULATION TRADES")
    frame = df.copy()
    frame["sim_return_pct"] = pd.to_numeric(frame["sim_return_pct"], errors="coerce")
    frame = frame.dropna(subset=["sim_return_pct"])
    if frame.empty:
        return empty_figure("WAITING FOR RESOLVED SIMULATION TRADES")
    frame["Outcome"] = frame["sim_return_pct"].map(lambda x: "Win" if x > 0 else ("Loss" if x < 0 else "Flat"))
    grouped = frame.groupby("Outcome", as_index=False).size().rename(columns={"size": "Orders"})
    fig = px.bar(grouped, x="Outcome", y="Orders", color="Outcome", color_discrete_map={"Win": "#16a34a", "Loss": "#dc2626", "Flat": "#6b7280"})
    fig.update_layout(template="plotly_dark", height=300, margin=dict(l=20, r=20, t=35, b=20), title="Win / loss count")
    return fig


def portfolio_equity_curve(df: pd.DataFrame) -> go.Figure:
    if df.empty or not {"timestamp", "portfolio", "equity_pct"}.issubset(df.columns):
        return empty_figure("WAITING FOR PORTFOLIO SIMULATION")
    frame = df.copy()
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    frame["equity_pct"] = pd.to_numeric(frame["equity_pct"], errors="coerce")
    frame = frame.dropna(subset=["timestamp", "equity_pct"]).sort_values("timestamp")
    if frame.empty:
        return empty_figure("WAITING FOR PORTFOLIO SIMULATION")
    fig = px.line(frame, x="timestamp", y="equity_pct", color="portfolio", markers=True)
    fig.update_layout(
        template="plotly_dark",
        height=350,
        margin=dict(l=20, r=20, t=35, b=20),
        title="Portfolio equity curve",
        yaxis_title="Cumulative return %",
        xaxis_title="Time",
    )
    return fig


def selected_portfolio_equity(equity: pd.DataFrame, title: str = "Selected portfolio P/L") -> go.Figure:
    if equity.empty or not {"timestamp", "equity_pct", "portfolio_return_pct"}.issubset(equity.columns):
        return empty_figure("WAITING FOR SELECTED PORTFOLIO TRADES")
    frame = equity.copy()
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    frame["equity_pct"] = pd.to_numeric(frame["equity_pct"], errors="coerce")
    frame["portfolio_return_pct"] = pd.to_numeric(frame["portfolio_return_pct"], errors="coerce")
    frame = frame.dropna(subset=["timestamp", "equity_pct"]).sort_values("timestamp")
    if frame.empty:
        return empty_figure("WAITING FOR SELECTED PORTFOLIO TRADES")
    colors = ["#22c55e" if value >= 0 else "#ef4444" for value in frame["portfolio_return_pct"]]
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=frame["timestamp"],
            y=frame["portfolio_return_pct"],
            marker_color=colors,
            name="Period P/L",
            opacity=0.45,
            yaxis="y2",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=frame["timestamp"],
            y=frame["equity_pct"],
            mode="lines+markers",
            name="Cumulative P/L",
            line=dict(color="#60a5fa", width=3),
        )
    )
    fig.update_layout(
        template="plotly_dark",
        height=380,
        margin=dict(l=20, r=20, t=35, b=20),
        title=title,
        yaxis_title="Cumulative return %",
        yaxis2=dict(title="Period return %", overlaying="y", side="right", showgrid=False),
        xaxis_title="Time",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    return fig


def portfolio_contribution_bar(df: pd.DataFrame) -> go.Figure:
    if df.empty or not {"Asset", "Net return"}.issubset(df.columns):
        return empty_figure("WAITING FOR ASSET CONTRIBUTION")
    frame = df.copy()
    frame["net_return_pct"] = pd.to_numeric(frame["Net return"].astype(str).str.rstrip("%"), errors="coerce")
    frame = frame.dropna(subset=["net_return_pct"]).sort_values("net_return_pct", ascending=True)
    if frame.empty:
        return empty_figure("WAITING FOR ASSET CONTRIBUTION")
    fig = px.bar(
        frame,
        x="net_return_pct",
        y="Asset",
        orientation="h",
        color="net_return_pct",
        text="Net return",
        color_continuous_scale="RdYlGn",
    )
    fig.update_layout(
        template="plotly_dark",
        height=max(280, min(560, 36 * len(frame) + 100)),
        margin=dict(l=20, r=20, t=35, b=20),
        title="Contribution by selected asset",
        xaxis_title="Net return %",
        yaxis_title="Asset",
        coloraxis_showscale=False,
    )
    return fig


def standardized_price_portfolio(prices: pd.DataFrame, trades: pd.DataFrame | None = None) -> go.Figure:
    if prices.empty or not {"timestamp", "asset", "standardized_close"}.issubset(prices.columns):
        return empty_figure("WAITING FOR STANDARDIZED PRICE HISTORY")
    frame = prices.copy()
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    frame["standardized_close"] = pd.to_numeric(frame["standardized_close"], errors="coerce")
    frame = frame.dropna(subset=["timestamp", "asset", "standardized_close"]).sort_values(["asset", "timestamp"])
    if frame.empty:
        return empty_figure("WAITING FOR STANDARDIZED PRICE HISTORY")
    fig = px.line(
        frame,
        x="timestamp",
        y="standardized_close",
        color="asset",
        title="Standardized price paths with strategy signals",
    )
    portfolio = frame.groupby("timestamp", as_index=False)["standardized_close"].mean()
    fig.add_trace(
        go.Scatter(
            x=portfolio["timestamp"],
            y=portfolio["standardized_close"],
            mode="lines",
            name="Equal-weight price blend",
            line=dict(color="#f8fafc", width=4),
        )
    )
    if trades is not None and not trades.empty and {"timestamp", "asset", "direction"}.issubset(trades.columns):
        signal_frame = trades.copy()
        signal_frame["timestamp"] = pd.to_datetime(signal_frame["timestamp"], errors="coerce")
        signal_frame = signal_frame.dropna(subset=["timestamp", "asset"])
        signal_rows = []
        for asset, group in signal_frame.groupby("asset", dropna=False):
            asset_prices = frame[frame["asset"].eq(asset)][["timestamp", "standardized_close"]].sort_values("timestamp")
            if asset_prices.empty:
                continue
            aligned = pd.merge_asof(
                group.sort_values("timestamp"),
                asset_prices,
                on="timestamp",
                direction="nearest",
                tolerance=pd.Timedelta("3h"),
            ).dropna(subset=["standardized_close"])
            if not aligned.empty:
                signal_rows.append(aligned)
        if signal_rows:
            markers = pd.concat(signal_rows, ignore_index=True)
            markers["Direction"] = markers["direction"].astype(str).str.upper()
            markers["Signal"] = markers.get("trade_bucket", markers.get("decision", "")).astype(str)
            symbol_map = {"LONG": "triangle-up", "SHORT": "triangle-down"}
            color_map = {"Gate allowed": "#22c55e", "Gate blocked": "#ef4444", "Research only": "#f59e0b"}
            for direction, direction_rows in markers.groupby("Direction", dropna=False):
                colors = direction_rows["Signal"].map(color_map).fillna("#e5e7eb")
                fig.add_trace(
                    go.Scatter(
                        x=direction_rows["timestamp"],
                        y=direction_rows["standardized_close"],
                        mode="markers",
                        name=f"{direction} signal",
                        marker=dict(size=12, symbol=symbol_map.get(str(direction), "circle"), color=colors, line=dict(width=1, color="#020617")),
                        text=direction_rows["asset"],
                        customdata=direction_rows[["Signal"]].to_numpy(),
                        hovertemplate="%{text}<br>%{x}<br>%{customdata[0]}<br>Standardized=%{y:.2f}<extra></extra>",
                    )
                )
    fig.update_layout(
        template="plotly_dark",
        height=460,
        margin=dict(l=20, r=20, t=35, b=20),
        yaxis_title="Standardized close (first visible bar = 100)",
        xaxis_title="Time",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    return fig


def strategy_fit_score_bar(df: pd.DataFrame) -> go.Figure:
    if df.empty or not {"Asset", "Score"}.issubset(df.columns):
        return empty_figure("WAITING FOR ASSET SCORES")
    frame = df.copy()
    frame["Score"] = pd.to_numeric(frame["Score"], errors="coerce")
    frame = frame.dropna(subset=["Score"]).sort_values("Score", ascending=False)
    if frame.empty:
        return empty_figure("WAITING FOR ASSET SCORES")
    fig = px.bar(
        frame,
        x="Asset",
        y="Score",
        color="Decision" if "Decision" in frame else None,
        text="Score",
    )
    fig.update_layout(
        template="plotly_dark",
        height=340,
        margin=dict(l=20, r=20, t=35, b=20),
        title="Strategy fit score",
        xaxis_title="Asset",
        yaxis_title="Score",
        dragmode="pan",
    )
    fig.update_xaxes(tickangle=-45, categoryorder="array", categoryarray=frame["Asset"].tolist())
    fig.update_yaxes(range=[0, max(100, float(frame["Score"].max()) * 1.12)])
    return fig


def strategy_correlation_heatmap(corr: pd.DataFrame) -> go.Figure:
    if corr.empty:
        return empty_figure("WAITING FOR MULTI-ASSET RETURNS")
    fig = go.Figure(
        data=go.Heatmap(
            z=corr.values,
            x=corr.columns.tolist(),
            y=corr.index.tolist(),
            zmin=-1,
            zmax=1,
            colorscale="RdBu",
            reversescale=True,
            colorbar=dict(title="corr"),
            text=corr.round(2).astype(str).values,
            texttemplate="%{text}",
        )
    )
    fig.update_layout(
        template="plotly_dark",
        height=360,
        margin=dict(l=20, r=20, t=35, b=20),
        title="Strategy return correlation",
    )
    return fig
