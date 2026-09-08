"""Metrics and status helpers for the Phase H dashboard."""
from __future__ import annotations

import math
from typing import Any

import numpy as np
import pandas as pd

from .data_loader import ASSETS, MR_FAIL_THRESHOLD, US500_STATUS


def sample_label(n: int) -> str:
    if n < 10:
        return "VERY LOW SAMPLE"
    if n < 20:
        return "LOW SAMPLE"
    if n < 50:
        return "EARLY EVIDENCE"
    if n < 100:
        return "USABLE SAMPLE"
    return "STRONGER SAMPLE"


def runner_sample_label(n: int) -> str:
    if n < 20:
        return "LOW_SAMPLE"
    if n < 50:
        return "EARLY"
    return "USABLE_SAMPLE"


def pct(value: Any) -> str:
    try:
        if value is None or pd.isna(value):
            return "n/a"
        return f"{float(value):.2%}"
    except Exception:
        return "n/a"


def num(value: Any, digits: int = 3) -> str:
    try:
        if value is None or pd.isna(value):
            return "n/a"
        return f"{float(value):.{digits}f}"
    except Exception:
        return "n/a"


def profit_factor(returns: pd.Series) -> float | None:
    vals = pd.to_numeric(returns, errors="coerce").dropna()
    if vals.empty:
        return None
    gains = vals[vals > 0].sum()
    losses = vals[vals < 0].sum()
    if losses == 0:
        return math.inf if gains > 0 else None
    return float(gains / abs(losses))


def max_drawdown(returns: pd.Series) -> float | None:
    vals = pd.to_numeric(returns, errors="coerce").fillna(0)
    if vals.empty:
        return None
    curve = vals.cumsum()
    dd = curve - curve.cummax()
    return float(dd.min())


def win_rate(returns: pd.Series) -> float | None:
    vals = pd.to_numeric(returns, errors="coerce").dropna()
    if vals.empty:
        return None
    return float((vals > 0).mean())


def auc_pairwise(y_true: pd.Series, y_score: pd.Series) -> float | None:
    frame = pd.DataFrame({"y": y_true, "score": y_score}).dropna()
    if len(frame) < 20 or frame["y"].nunique() < 2:
        return None
    pos = frame.loc[frame["y"] == 1, "score"].to_numpy()
    neg = frame.loc[frame["y"] == 0, "score"].to_numpy()
    total = len(pos) * len(neg)
    if total == 0:
        return None
    wins = sum((p > neg).sum() + 0.5 * (p == neg).sum() for p in pos)
    return float(wins / total)


def brier_score(y_true: pd.Series, y_prob: pd.Series) -> float | None:
    frame = pd.DataFrame({"y": y_true, "p": y_prob}).dropna()
    if len(frame) < 20:
        return None
    return float(np.mean((frame["p"] - frame["y"]) ** 2))


def calibration_table(df: pd.DataFrame, prob_col: str = "p_mr_fail", actual_col: str = "mr_failure_realized") -> pd.DataFrame:
    if df.empty or prob_col not in df or actual_col not in df:
        return pd.DataFrame(columns=["Probability Bin", "N", "Mean Predicted", "Actual Fail Rate", "Error", "Sample"])
    frame = df[[prob_col, actual_col]].copy()
    frame[prob_col] = pd.to_numeric(frame[prob_col], errors="coerce")
    frame[actual_col] = pd.to_numeric(frame[actual_col], errors="coerce")
    frame = frame.dropna()
    if frame.empty:
        return pd.DataFrame(columns=["Probability Bin", "N", "Mean Predicted", "Actual Fail Rate", "Error", "Sample"])
    frame["Probability Bin"] = pd.cut(frame[prob_col], bins=np.linspace(0, 1, 6), include_lowest=True)
    grouped = frame.groupby("Probability Bin", observed=True).agg(
        N=(actual_col, "size"),
        **{"Mean Predicted": (prob_col, "mean"), "Actual Fail Rate": (actual_col, "mean")},
    ).reset_index()
    grouped["Error"] = (grouped["Mean Predicted"] - grouped["Actual Fail Rate"]).abs()
    grouped["Sample"] = grouped["N"].apply(lambda n: "LOW SAMPLE" if n < 10 else "OK")
    grouped["Probability Bin"] = grouped["Probability Bin"].astype(str)
    return grouped


def mr_forward_metrics(candidates: pd.DataFrame, observations: pd.DataFrame | None = None) -> dict[str, Any]:
    source = candidates
    resolved_col = "resolved_at" if "resolved_at" in source.columns else None
    actual_col = "mr_failure_realized" if "mr_failure_realized" in source.columns else None
    resolved = source[source[resolved_col].notna()] if resolved_col else pd.DataFrame()
    auc = auc_pairwise(resolved[actual_col], resolved["p_mr_fail"]) if actual_col in resolved and "p_mr_fail" in resolved else None
    brier = brier_score(resolved[actual_col], resolved["p_mr_fail"]) if actual_col in resolved and "p_mr_fail" in resolved else None
    if auc is None:
        status = "INSUFFICIENT"
    elif auc >= 0.65:
        status = "GREEN"
    elif auc > 0.55:
        status = "YELLOW"
    else:
        status = "RED"
    return {
        "candidates": len(source),
        "resolved": len(resolved),
        "roc_auc": auc,
        "pr_auc": None,
        "brier": brier,
        "ece": None,
        "status": status,
        "confidence": sample_label(len(resolved)),
    }


def yahoo_quality_summary(price_quality: pd.DataFrame) -> tuple[str, str, pd.DataFrame]:
    if price_quality.empty or "status" not in price_quality:
        return "UNKNOWN", "No price-quality report is available yet.", pd.DataFrame()

    statuses = price_quality["status"].astype(str).str.upper()
    if (statuses == "FAIL").any():
        overall = "FAILED"
    elif (statuses == "WARNING").any():
        overall = "WARNING"
    elif (statuses == "PASS").all():
        overall = "PASS"
    else:
        overall = "UNKNOWN"

    warning_rows = price_quality[statuses.isin(["WARNING", "FAIL"])].copy()
    if warning_rows.empty:
        return overall, "All Yahoo price-quality checks are currently PASS.", warning_rows

    details = []
    critical_assets = []
    for _, row in warning_rows.iterrows():
        asset = row.get("asset", "UNKNOWN")
        parts = []
        missing = pd.to_numeric(row.get("missing_bar_estimate"), errors="coerce")
        zero_volume = pd.to_numeric(row.get("zero_volume_count"), errors="coerce")
        bad_ohlc = pd.to_numeric(row.get("bad_ohlc_count"), errors="coerce")
        duplicates = pd.to_numeric(row.get("duplicate_count"), errors="coerce")
        max_gap = pd.to_numeric(row.get("max_bar_gap_hours"), errors="coerce")
        if missing > 0:
            parts.append(f"{int(missing)} estimated missing/session bars")
        if zero_volume > 0:
            parts.append(f"{int(zero_volume)} zero-volume bars")
        if bad_ohlc > 0:
            parts.append(f"{int(bad_ohlc)} bad OHLC rows")
            critical_assets.append(str(asset))
        if duplicates > 0:
            parts.append(f"{int(duplicates)} duplicates")
            critical_assets.append(str(asset))
        if max_gap > 24:
            parts.append(f"max closed-market/session gap {max_gap:g}h")
        details.append(f"{asset}: " + (", ".join(parts) if parts else str(row.get("status"))))

    note = "; ".join(details)
    if critical_assets:
        note += f". Check carefully: duplicate or bad OHLC rows detected for {', '.join(sorted(set(critical_assets)))}."
    else:
        note += ". No duplicate rows or bad OHLC rows were detected in the warning assets."
    return overall, note, warning_rows


def data_completeness_summary(completeness: pd.DataFrame) -> tuple[str, str, pd.DataFrame]:
    if completeness.empty or "status" not in completeness:
        return "UNKNOWN", "No session-aware completeness report is available yet.", pd.DataFrame()

    frame = completeness.copy()
    missing = pd.to_numeric(frame.get("missing_open_bars", 0), errors="coerce").fillna(0).astype(int)
    ignored = pd.to_numeric(frame.get("ignored_provider_calendar_mismatch", 0), errors="coerce").fillna(0).astype(int)
    status = "RED" if (missing > 0).any() else "GREEN"
    total_missing = int(missing.sum())
    total_ignored = int(ignored.sum())
    recoverable = int(pd.to_numeric(frame.get("missing_recoverable_by_yahoo_730d", 0), errors="coerce").fillna(0).sum())
    problem_rows = frame[missing > 0].copy()
    if problem_rows.empty:
        start = value_from(frame, "report_start_timestamp_utc", "the report start")
        note = f"All required open-market hourly bars are present since {start}."
        if total_ignored:
            note += f" Ignored {total_ignored} provider/calendar mismatch bar(s) that are not actionable backfill gaps."
        return status, note, problem_rows

    start = value_from(frame, "report_start_timestamp_utc", "the report start")
    note = (
        f"{total_missing} open-market hourly bar(s) are missing since {start} across {len(problem_rows)} asset(s); "
        f"{recoverable} are still inside Yahoo's approximate 730-day 1H window."
    )
    return status, note, problem_rows


def data_completeness_asset_cards(completeness: pd.DataFrame) -> pd.DataFrame:
    if completeness.empty:
        return pd.DataFrame(
            columns=["Asset", "Signal", "Missing open bars", "Recoverable", "Coverage", "Calendar", "Ignored"]
        )

    frame = completeness.copy()
    missing = pd.to_numeric(frame.get("missing_open_bars", 0), errors="coerce").fillna(0).astype(int)
    recoverable = pd.to_numeric(frame.get("missing_recoverable_by_yahoo_730d", 0), errors="coerce").fillna(0).astype(int)
    ignored = pd.to_numeric(frame.get("ignored_provider_calendar_mismatch", 0), errors="coerce").fillna(0).astype(int)
    coverage = pd.to_numeric(frame.get("open_session_coverage_pct", 0), errors="coerce").fillna(0)
    return pd.DataFrame(
        {
            "Asset": frame.get("asset", ""),
            "Signal": missing.map(lambda n: "GREEN" if n == 0 else "RED"),
            "Missing open bars": missing,
            "Recoverable": recoverable,
            "Coverage": coverage.map(lambda v: f"{v:.2f}%"),
            "Calendar": frame.get("calendar", ""),
            "Ignored": ignored,
        }
    )


def data_completeness_gap_details(gaps: pd.DataFrame, limit: int = 30) -> pd.DataFrame:
    if gaps.empty:
        return pd.DataFrame(
            columns=[
                "Asset",
                "First missing open bar",
                "Last missing open bar",
                "Missing open bars",
                "Recoverable by Yahoo 730d",
                "Calendar",
            ]
        )
    frame = gaps.copy()
    for col in ["first_missing_open_bar_utc", "last_missing_open_bar_utc"]:
        if col in frame:
            frame[col] = pd.to_datetime(frame[col], errors="coerce").dt.strftime("%Y-%m-%d %H:%M UTC")
    frame["missing_open_bars"] = pd.to_numeric(frame.get("missing_open_bars", 0), errors="coerce").fillna(0).astype(int)
    frame = frame.sort_values(["asset", "first_missing_open_bar_utc"]).head(limit)
    return frame.rename(
        columns={
            "asset": "Asset",
            "first_missing_open_bar_utc": "First missing open bar",
            "last_missing_open_bar_utc": "Last missing open bar",
            "missing_open_bars": "Missing open bars",
            "recoverable_by_yahoo_730d": "Recoverable by Yahoo 730d",
            "calendar": "Calendar",
        }
    )


def simulation_trade_frame(candidates: pd.DataFrame, observations: pd.DataFrame) -> pd.DataFrame:
    """Build resolved forward MR setup simulations from candidates plus future returns."""
    columns = [
        "timestamp",
        "asset",
        "direction",
        "decision",
        "p_mr_win",
        "p_mr_fail",
        "pred_mr_return_pct",
        "future_return_24h",
        "sim_return_pct",
        "outcome",
        "why",
        "trade_bucket",
    ]
    if candidates.empty or observations.empty:
        return pd.DataFrame(columns=columns)
    required = {"asset", "timestamp", "direction", "decision"}
    if not required.issubset(candidates.columns) or "future_return_24h" not in observations.columns:
        return pd.DataFrame(columns=columns)

    cand = candidates.copy()
    obs_cols = [
        "asset",
        "timestamp",
        "future_return_24h",
        "close",
        "atr",
        "natr",
        "vol_ratio",
        "cross_count",
        "osc",
        "signal",
        "osc_minus_signal",
        "osc_slope_1",
        "osc_slope_3",
        "price_direction_12",
        "price_direction_24",
    ]
    obs_cols = [c for c in obs_cols if c in observations]
    if "resolved_at" in observations:
        obs_cols.append("resolved_at")
    obs = observations[obs_cols].copy()
    cand["timestamp"] = pd.to_datetime(cand["timestamp"], errors="coerce")
    obs["timestamp"] = pd.to_datetime(obs["timestamp"], errors="coerce")
    merged = cand.merge(obs, on=["asset", "timestamp"], how="left")
    merged["future_return_24h"] = pd.to_numeric(merged["future_return_24h"], errors="coerce")
    merged = merged.dropna(subset=["timestamp", "future_return_24h"])
    if merged.empty:
        return pd.DataFrame(columns=columns)

    direction = merged["direction"].astype(str).str.upper().map({"LONG": 1.0, "SHORT": -1.0}).fillna(0.0)
    merged["sim_return_pct"] = merged["future_return_24h"] * direction
    merged["outcome"] = merged["sim_return_pct"].map(lambda x: "Win" if x > 0 else ("Loss" if x < 0 else "Flat"))
    decisions = merged["decision"].astype(str).str.upper()
    merged["trade_bucket"] = np.select(
        [
            decisions.eq("MR_ELIGIBLE"),
            decisions.eq("RESEARCH_ONLY"),
            decisions.eq("MR_BLOCK"),
        ],
        ["Gate allowed", "Research only", "Gate blocked"],
        default="Other",
    )
    merged["why"] = merged.apply(explain_trade_row, axis=1)
    present = [c for c in columns if c in merged]
    extra = [
        "decision_reason",
        "close",
        "atr",
        "natr",
        "vol_ratio",
        "cross_count",
        "osc",
        "signal",
        "osc_minus_signal",
        "osc_slope_1",
        "osc_slope_3",
        "price_direction_12",
        "price_direction_24",
    ]
    present = present + [c for c in extra if c in merged and c not in present]
    return merged[present].sort_values("timestamp").reset_index(drop=True)


def explain_trade_row(row: pd.Series) -> str:
    reasons = []
    outcome = str(row.get("outcome", "")).lower()
    direction = str(row.get("direction", "")).upper()
    sim_return = pd.to_numeric(row.get("sim_return_pct"), errors="coerce")
    future_return = pd.to_numeric(row.get("future_return_24h"), errors="coerce")
    p_fail = pd.to_numeric(row.get("p_mr_fail"), errors="coerce")
    p_win = pd.to_numeric(row.get("p_mr_win"), errors="coerce")
    pred = pd.to_numeric(row.get("pred_mr_return_pct"), errors="coerce")
    osc_gap = pd.to_numeric(row.get("osc_minus_signal"), errors="coerce")
    vol_ratio = pd.to_numeric(row.get("vol_ratio"), errors="coerce")
    price_dir = pd.to_numeric(row.get("price_direction_24"), errors="coerce")

    if pd.notna(sim_return) and pd.notna(future_return):
        if outcome == "win":
            reasons.append(f"{direction} matched the next 24h move ({sim_return:.2f}%).")
        elif outcome == "loss":
            reasons.append(f"{direction} was against the next 24h move ({sim_return:.2f}%).")
        else:
            reasons.append("The next 24h move was nearly flat.")
    if pd.notna(p_fail):
        reasons.append(f"MR_FAIL risk was {p_fail:.2f}.")
    if pd.notna(p_win):
        reasons.append(f"MR win probability was {p_win:.2f}.")
    if pd.notna(pred):
        reasons.append(f"Model expected return was {pred:.2f}%.")
    if pd.notna(osc_gap):
        reasons.append(f"Oscillator gap was {osc_gap:.2f}.")
    if pd.notna(vol_ratio):
        reasons.append(f"Volatility ratio was {vol_ratio:.2f}.")
    if pd.notna(price_dir):
        reasons.append(f"24-bar direction persistence was {price_dir:.2f}.")
    return " ".join(reasons)


def win_loss_reason_table(trades: pd.DataFrame) -> pd.DataFrame:
    if trades.empty or "outcome" not in trades:
        return pd.DataFrame(columns=["Outcome", "Asset", "Orders", "Win rate", "Avg return", "Avg p_mr_fail", "Avg p_mr_win"])
    frame = trades.copy()
    frame["sim_return_pct"] = pd.to_numeric(frame.get("sim_return_pct"), errors="coerce")
    frame["p_mr_fail"] = pd.to_numeric(frame.get("p_mr_fail"), errors="coerce")
    frame["p_mr_win"] = pd.to_numeric(frame.get("p_mr_win"), errors="coerce")
    grouped = frame.groupby(["outcome", "asset"], dropna=False).agg(
        Orders=("sim_return_pct", "size"),
        WinRate=("sim_return_pct", lambda s: (s > 0).mean()),
        AvgReturn=("sim_return_pct", "mean"),
        AvgFail=("p_mr_fail", "mean"),
        AvgWin=("p_mr_win", "mean"),
    ).reset_index()
    return pd.DataFrame(
        {
            "Outcome": grouped["outcome"],
            "Asset": grouped["asset"],
            "Orders": grouped["Orders"],
            "Win rate": grouped["WinRate"].map(pct),
            "Avg return": grouped["AvgReturn"].map(lambda v: pct(v / 100)),
            "Avg p_mr_fail": grouped["AvgFail"].map(lambda v: num(v, 2)),
            "Avg p_mr_win": grouped["AvgWin"].map(lambda v: num(v, 2)),
        }
    ).sort_values(["Outcome", "Orders"], ascending=[True, False]).reset_index(drop=True)


def asset_selection_score_table(trades: pd.DataFrame) -> pd.DataFrame:
    if trades.empty or "asset" not in trades:
        return pd.DataFrame(columns=["Rank", "Asset", "Orders", "Score", "PF", "Win rate", "Net return", "Max DD", "Usefulness"])
    rows = []
    for asset, frame in trades.groupby("asset", dropna=False):
        stats = performance_summary(frame, str(asset))
        orders = stats["orders"]
        pf = stats["profit_factor"]
        pf_score = 2.0 if pf == math.inf else float(pf or 0)
        win = float(stats["win_rate"] or 0)
        net = float(stats["net_return"] or 0)
        dd = abs(float(stats["max_drawdown"] or 0))
        sample_weight = min(orders / 30, 1)
        score = sample_weight * (pf_score * 0.45 + win * 0.35 + max(net, 0) / 20 * 0.20) - dd / 20
        rows.append(
            {
                "Asset": asset,
                "Orders": orders,
                "Score": round(score, 3),
                "PF": "inf" if pf == math.inf else num(pf, 2),
                "Win rate": pct(stats["win_rate"]),
                "Net return": pct(stats["net_return"] / 100),
                "Max DD": pct((stats["max_drawdown"] or 0) / 100),
                "Usefulness": "Watchlist candidate" if orders >= 20 and score > 0.5 else "Need more forward sample",
            }
        )
    out = pd.DataFrame(rows).sort_values("Score", ascending=False).reset_index(drop=True)
    out.insert(0, "Rank", range(1, len(out) + 1))
    return out


def strategy_return_matrix(trades: pd.DataFrame) -> pd.DataFrame:
    if trades.empty or not {"timestamp", "asset", "sim_return_pct"}.issubset(trades.columns):
        return pd.DataFrame()
    frame = trades[["timestamp", "asset", "sim_return_pct"]].copy()
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    frame["sim_return_pct"] = pd.to_numeric(frame["sim_return_pct"], errors="coerce")
    frame = frame.dropna(subset=["timestamp", "asset", "sim_return_pct"])
    if frame.empty:
        return pd.DataFrame()
    return frame.pivot_table(
        index="timestamp",
        columns="asset",
        values="sim_return_pct",
        aggfunc="mean",
        fill_value=0.0,
    ).sort_index()


def strategy_return_correlation(trades: pd.DataFrame) -> pd.DataFrame:
    matrix = strategy_return_matrix(trades)
    if matrix.empty or matrix.shape[1] < 2:
        return pd.DataFrame()
    return matrix.corr().fillna(0.0)


def _asset_registry_lookup(asset_registry: pd.DataFrame) -> dict[str, dict[str, Any]]:
    if asset_registry.empty or "asset" not in asset_registry:
        return {}
    return asset_registry.set_index("asset").to_dict(orient="index")


def _completeness_lookup(completeness: pd.DataFrame) -> dict[str, dict[str, Any]]:
    if completeness.empty or "asset" not in completeness:
        return {}
    return completeness.set_index("asset").to_dict(orient="index")


def strategy_fit_table(
    trades: pd.DataFrame,
    asset_registry: pd.DataFrame | None = None,
    completeness: pd.DataFrame | None = None,
) -> pd.DataFrame:
    columns = [
        "Rank",
        "Asset",
        "Class",
        "Role",
        "Pepperstone",
        "Orders",
        "Score",
        "Decision",
        "PF",
        "Win rate",
        "Net return",
        "Max DD",
        "Avg abs corr",
        "Data",
        "Cost",
    ]
    registry = _asset_registry_lookup(asset_registry if asset_registry is not None else pd.DataFrame())
    complete = _completeness_lookup(completeness if completeness is not None else pd.DataFrame())
    assets = sorted(set(registry) | (set(trades["asset"].dropna()) if not trades.empty and "asset" in trades else set()))
    if not assets:
        return pd.DataFrame(columns=columns)

    corr = strategy_return_correlation(trades)
    rows = []
    for asset in assets:
        meta = registry.get(asset, {})
        asset_trades = trades[trades["asset"] == asset] if not trades.empty and "asset" in trades else pd.DataFrame()
        stats = performance_summary(asset_trades, asset)
        orders = int(stats["orders"])
        pf = stats["profit_factor"]
        wr = float(stats["win_rate"] or 0)
        net = float(stats["net_return"] or 0)
        dd = abs(float(stats["max_drawdown"] or 0))
        cost = float(meta.get("estimated_round_trip_cost_pct", 0) or 0)
        selection_enabled = bool(meta.get("selection_enabled", True))
        forward_enabled = bool(meta.get("forward_research_enabled", True))
        missing = int(pd.to_numeric(complete.get(asset, {}).get("missing_open_bars", 0), errors="coerce") or 0)
        data_ready = missing == 0
        if asset in corr:
            others = corr[asset].drop(labels=[asset], errors="ignore").abs()
            avg_abs_corr = float(others.mean()) if not others.empty else 0.0
        else:
            avg_abs_corr = 0.0
        sample_component = min(orders / 30, 1.0)
        pf_component = min((3.0 if pf == math.inf else float(pf or 0)) / 3.0, 1.0)
        win_component = min(max(wr, 0.0), 1.0)
        return_component = min(max(net, 0.0) / 8.0, 1.0)
        dd_penalty = min(dd / 8.0, 1.0)
        diversifier = max(0.0, 1.0 - avg_abs_corr)
        data_component = 1.0 if data_ready and selection_enabled else 0.0
        cost_penalty = min(max(cost, 0.0) / 0.20, 1.0)
        if orders == 0 or not forward_enabled or not selection_enabled:
            score = 0.0
        else:
            raw_score = (
                sample_component * 28
                + pf_component * 24
                + win_component * 16
                + return_component * 14
                + diversifier * 12
                + data_component * 6
                - dd_penalty * 18
                - cost_penalty * 10
            )
            score = max(0.0, min(100.0, raw_score))
        if not forward_enabled or not selection_enabled:
            decision = "Data only"
        elif not data_ready:
            decision = "Data gap"
        elif orders < 20:
            decision = "Needs forward sample"
        elif score >= 65:
            decision = "Core candidate"
        elif score >= 50:
            decision = "Diversifier watch"
        elif score >= 35:
            decision = "Observe only"
        else:
            decision = "Avoid for now"
        rows.append(
            {
                "Asset": asset,
                "Class": meta.get("asset_class") or asset_class(asset),
                "Role": meta.get("universe_role", "core"),
                "Pepperstone": meta.get("pepperstone_symbol", asset),
                "Orders": orders,
                "Score": round(score, 1),
                "Decision": decision,
                "PF": "inf" if pf == math.inf else num(pf, 2),
                "Win rate": pct(stats["win_rate"]),
                "Net return": pct(net / 100),
                "Max DD": pct((stats["max_drawdown"] or 0) / 100),
                "Avg abs corr": num(avg_abs_corr, 2),
                "Data": "Complete" if data_ready else f"{missing} missing",
                "Cost": pct(cost / 100),
            }
        )
    out = pd.DataFrame(rows).sort_values(["Score", "Orders"], ascending=[False, False]).reset_index(drop=True)
    out.insert(0, "Rank", range(1, len(out) + 1))
    return out[columns]


def expansion_candidate_table(
    fit: pd.DataFrame,
    asset_registry: pd.DataFrame,
    latest_scores: pd.DataFrame,
    min_orders: int = 30,
) -> pd.DataFrame:
    columns = [
        "Priority",
        "Asset",
        "Class",
        "Role",
        "Stage",
        "Forward start",
        "Orders",
        "Score",
        "PF",
        "Win rate",
        "Net return",
        "Data",
        "Latest action",
        "Why",
    ]
    if asset_registry.empty or "asset" not in asset_registry:
        return pd.DataFrame(columns=columns)

    fit_map = fit.set_index("Asset").to_dict(orient="index") if not fit.empty and "Asset" in fit else {}
    latest_map = latest_scores.set_index("asset").to_dict(orient="index") if not latest_scores.empty and "asset" in latest_scores else {}
    rows = []
    for _, meta in asset_registry.iterrows():
        asset = str(meta.get("asset"))
        row = fit_map.get(asset, {})
        latest = latest_map.get(asset, {})
        role = str(meta.get("universe_role", "candidate"))
        orders = int(pd.to_numeric(row.get("Orders", 0), errors="coerce") or 0)
        score = float(pd.to_numeric(row.get("Score", 0), errors="coerce") or 0)
        data_state = str(row.get("Data", "Unknown"))
        action = str(latest.get("recommended_action", "WAIT_SAMPLE"))
        reasons = []

        if role == "core":
            stage = "Phase H core"
            priority = 0
            reasons.append("Already inside the frozen Phase H forward cohort.")
        elif data_state != "Complete":
            stage = "Fix data first"
            priority = 5
            reasons.append(f"Price coverage is not complete: {data_state}.")
        elif orders < min_orders:
            stage = "Collect forward sample"
            priority = 2
            reasons.append(f"Needs {min_orders - orders} more resolved setup(s) before promotion scoring is reliable.")
        elif score >= 65:
            stage = "Promote candidate"
            priority = 1
            reasons.append("Forward evidence is strong enough for the next review bucket.")
        elif score >= 50:
            stage = "Watchlist"
            priority = 3
            reasons.append("Evidence is useful but not yet strong enough for promotion.")
        else:
            stage = "Do not promote yet"
            priority = 4
            reasons.append("Forward score is still weak versus the current strategy.")

        if action in {"MR_ELIGIBLE", "WATCH_MR", "MR_BLOCK"}:
            reasons.append(f"Latest model state: {action}.")
        rows.append(
            {
                "Priority": priority,
                "Asset": asset,
                "Class": meta.get("asset_class", row.get("Class", "OTHER")),
                "Role": role,
                "Stage": stage,
                "Forward start": meta.get("forward_start_utc") or "Phase H start",
                "Orders": orders,
                "Score": round(score, 1),
                "PF": row.get("PF", "n/a"),
                "Win rate": row.get("Win rate", "n/a"),
                "Net return": row.get("Net return", "n/a"),
                "Data": data_state,
                "Latest action": action,
                "Why": " ".join(reasons),
            }
        )

    out = pd.DataFrame(rows).sort_values(["Priority", "Score", "Orders"], ascending=[True, False, False]).reset_index(drop=True)
    return out[columns]


def common_forward_window(trades: pd.DataFrame, assets: list[str] | None = None) -> dict[str, Any]:
    if trades.empty or not {"timestamp", "asset"}.issubset(trades.columns):
        return {"start": None, "end": None, "assets": 0, "usable": False}
    frame = trades.copy()
    if assets is not None:
        frame = frame[frame["asset"].isin(assets)]
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    frame = frame.dropna(subset=["timestamp", "asset"])
    if frame.empty:
        return {"start": None, "end": None, "assets": 0, "usable": False}
    spans = frame.groupby("asset")["timestamp"].agg(["min", "max"])
    if spans.empty:
        return {"start": None, "end": None, "assets": 0, "usable": False}
    start = spans["min"].max()
    end = spans["max"].min()
    return {
        "start": start,
        "end": end,
        "assets": int(len(spans)),
        "usable": bool(pd.notna(start) and pd.notna(end) and start <= end and len(spans) >= 2),
    }


def portfolio_equity_frame(trades: pd.DataFrame, assets: list[str], label: str) -> pd.DataFrame:
    if trades.empty or not assets:
        return pd.DataFrame(columns=["timestamp", "portfolio", "portfolio_return_pct", "equity_pct", "active_assets"])
    frame = trades[trades["asset"].isin(assets)].copy()
    if frame.empty or "timestamp" not in frame or "sim_return_pct" not in frame:
        return pd.DataFrame(columns=["timestamp", "portfolio", "portfolio_return_pct", "equity_pct", "active_assets"])
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    frame["sim_return_pct"] = pd.to_numeric(frame["sim_return_pct"], errors="coerce")
    frame = frame.dropna(subset=["timestamp", "sim_return_pct"]).sort_values("timestamp")
    grouped = frame.groupby("timestamp").agg(
        portfolio_return_pct=("sim_return_pct", "mean"),
        active_assets=("asset", "nunique"),
    ).reset_index()
    grouped["equity_pct"] = grouped["portfolio_return_pct"].cumsum()
    grouped["portfolio"] = label
    return grouped[["timestamp", "portfolio", "portfolio_return_pct", "equity_pct", "active_assets"]]


def _portfolio_row(trades: pd.DataFrame, name: str, assets: list[str]) -> dict[str, Any]:
    equity = portfolio_equity_frame(trades, assets, name)
    returns = equity["portfolio_return_pct"] if not equity.empty else pd.Series(dtype=float)
    pf = profit_factor(returns)
    return {
        "Portfolio": name,
        "Assets": ", ".join(assets) if assets else "None",
        "Asset count": len(assets),
        "Orders": int(len(trades[trades["asset"].isin(assets)])) if not trades.empty and assets else 0,
        "Periods": int(len(returns)),
        "PF": "inf" if pf == math.inf else num(pf, 2),
        "Win rate": pct(win_rate(returns)),
        "Net return": pct(float(returns.sum() if len(returns) else 0) / 100),
        "Max DD": pct(float((max_drawdown(returns) or 0)) / 100),
        "Avg period return": pct(float(returns.mean() if len(returns) else 0) / 100),
    }


def portfolio_candidate_sets(
    trades: pd.DataFrame,
    fit: pd.DataFrame,
    top_n: int = 5,
    max_avg_corr: float = 0.65,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if fit.empty or "Asset" not in fit:
        return pd.DataFrame(), pd.DataFrame()
    ranked = fit[fit["Orders"] > 0].copy().sort_values("Score", ascending=False)
    usable = ranked[~ranked["Decision"].isin(["Data gap", "Avoid for now"])].copy()
    if usable.empty:
        usable = ranked
    top_assets = usable["Asset"].head(top_n).tolist()

    corr = strategy_return_correlation(trades)
    low_corr_assets: list[str] = []
    for asset in usable["Asset"].tolist():
        if len(low_corr_assets) >= top_n:
            break
        if not low_corr_assets or corr.empty or asset not in corr:
            low_corr_assets.append(asset)
            continue
        avg_corr = corr.loc[asset, [a for a in low_corr_assets if a in corr]].abs().mean()
        if pd.isna(avg_corr) or float(avg_corr) <= max_avg_corr:
            low_corr_assets.append(asset)

    class_balanced = []
    if "Class" in usable:
        for _, row in usable.groupby("Class", sort=False).head(1).sort_values("Score", ascending=False).iterrows():
            class_balanced.append(row["Asset"])
        for asset in usable["Asset"].tolist():
            if len(class_balanced) >= top_n:
                break
            if asset not in class_balanced:
                class_balanced.append(asset)

    all_assets = usable["Asset"].tolist()
    rows = [
        _portfolio_row(trades, "Top score", top_assets),
        _portfolio_row(trades, "Low correlation", low_corr_assets),
        _portfolio_row(trades, "Class balanced", class_balanced[:top_n]),
        _portfolio_row(trades, "All usable", all_assets),
    ]
    summary = pd.DataFrame(rows)
    curves = pd.concat(
        [
            portfolio_equity_frame(trades, top_assets, "Top score"),
            portfolio_equity_frame(trades, low_corr_assets, "Low correlation"),
            portfolio_equity_frame(trades, class_balanced[:top_n], "Class balanced"),
            portfolio_equity_frame(trades, all_assets, "All usable"),
        ],
        ignore_index=True,
    )
    return summary, curves


def performance_summary(trades: pd.DataFrame, label: str = "All setups") -> dict[str, Any]:
    if trades.empty or "sim_return_pct" not in trades:
        return {
            "label": label,
            "orders": 0,
            "win_rate": None,
            "profit_factor": None,
            "net_return": 0.0,
            "avg_return": None,
            "max_drawdown": None,
            "status": "INSUFFICIENT",
        }
    returns = pd.to_numeric(trades["sim_return_pct"], errors="coerce").dropna()
    if returns.empty:
        return {
            "label": label,
            "orders": 0,
            "win_rate": None,
            "profit_factor": None,
            "net_return": 0.0,
            "avg_return": None,
            "max_drawdown": None,
            "status": "INSUFFICIENT",
        }
    pf = profit_factor(returns)
    wr = win_rate(returns)
    net = float(returns.sum())
    dd = max_drawdown(returns)
    if len(returns) < 10:
        status = "EARLY"
    elif pf is not None and pf >= 1.25 and net > 0:
        status = "GREEN"
    elif pf is not None and pf >= 1.0:
        status = "YELLOW"
    else:
        status = "RED"
    return {
        "label": label,
        "orders": int(len(returns)),
        "win_rate": wr,
        "profit_factor": pf,
        "net_return": net,
        "avg_return": float(returns.mean()),
        "max_drawdown": dd,
        "status": status,
    }


def performance_table(trades: pd.DataFrame, group_col: str = "asset") -> pd.DataFrame:
    if trades.empty or group_col not in trades:
        return pd.DataFrame(columns=["Group", "Orders", "Win rate", "Profit factor", "Net return", "Avg return", "Max drawdown", "Status"])
    rows = []
    for group, frame in trades.groupby(group_col, dropna=False):
        stats = performance_summary(frame, str(group))
        rows.append(
            {
                "Group": group,
                "Orders": stats["orders"],
                "Win rate": pct(stats["win_rate"]),
                "Profit factor": "inf" if stats["profit_factor"] == math.inf else num(stats["profit_factor"], 2),
                "Net return": pct(stats["net_return"] / 100),
                "Avg return": pct((stats["avg_return"] or 0) / 100),
                "Max drawdown": pct((stats["max_drawdown"] or 0) / 100),
                "Status": stats["status"],
            }
        )
    return pd.DataFrame(rows).sort_values(["Orders", "Group"], ascending=[False, True]).reset_index(drop=True)


def return_diagnostics(returns: pd.Series) -> dict[str, Any]:
    vals = pd.to_numeric(returns, errors="coerce").dropna()
    if vals.empty:
        return {
            "orders": 0,
            "profit_factor": None,
            "win_rate": None,
            "net_return": 0.0,
            "avg_return": None,
            "avg_win": None,
            "avg_loss": None,
            "expectancy": None,
            "max_drawdown": None,
            "current_drawdown": None,
            "top_3_profit_share": None,
        }
    curve = vals.cumsum()
    running_high = curve.cummax()
    dd = curve - running_high
    gains = vals[vals > 0]
    top_profit_share = None
    if gains.sum() > 0:
        top_profit_share = float(gains.sort_values(ascending=False).head(3).sum() / gains.sum())
    return {
        "orders": int(len(vals)),
        "profit_factor": profit_factor(vals),
        "win_rate": win_rate(vals),
        "net_return": float(vals.sum()),
        "avg_return": float(vals.mean()),
        "avg_win": float(gains.mean()) if not gains.empty else None,
        "avg_loss": float(vals[vals < 0].mean()) if (vals < 0).any() else None,
        "expectancy": float(vals.mean()),
        "max_drawdown": float(dd.min()) if not dd.empty else None,
        "current_drawdown": float(dd.iloc[-1]) if not dd.empty else None,
        "top_3_profit_share": top_profit_share,
    }


def strategy_health_status(diag: dict[str, Any]) -> str:
    orders = int(diag.get("orders") or 0)
    pf = diag.get("profit_factor")
    net = float(diag.get("net_return") or 0)
    dd = abs(float(diag.get("max_drawdown") or 0))
    if orders < 20:
        return "INSUFFICIENT SAMPLE"
    if pf is not None and pf >= 1.25 and net > 0 and dd < 8:
        return "HEALTHY"
    if pf is not None and pf >= 1.0 and net >= 0:
        return "WATCH"
    return "WEAK"


def strategy_window_table(trades: pd.DataFrame) -> pd.DataFrame:
    columns = ["Metric", "7D", "14D", "Since Phase H"]
    if trades.empty or not {"timestamp", "sim_return_pct"}.issubset(trades.columns):
        return pd.DataFrame(columns=columns)
    frame = trades.copy()
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    frame["sim_return_pct"] = pd.to_numeric(frame["sim_return_pct"], errors="coerce")
    frame = frame.dropna(subset=["timestamp", "sim_return_pct"])
    if frame.empty:
        return pd.DataFrame(columns=columns)
    end = frame["timestamp"].max()
    windows = {
        "7D": frame[frame["timestamp"] >= end - pd.Timedelta(days=7)],
        "14D": frame[frame["timestamp"] >= end - pd.Timedelta(days=14)],
        "Since Phase H": frame,
    }

    def diag(label: str) -> dict[str, Any]:
        return return_diagnostics(windows[label]["sim_return_pct"])

    diags = {label: diag(label) for label in windows}
    rows = [
        ("Trades", lambda d: str(d["orders"])),
        ("PF", lambda d: "inf" if d["profit_factor"] == math.inf else num(d["profit_factor"], 2)),
        ("Win rate", lambda d: pct(d["win_rate"])),
        ("Avg return", lambda d: pct((d["avg_return"] or 0) / 100)),
        ("Avg win", lambda d: pct((d["avg_win"] or 0) / 100)),
        ("Avg loss", lambda d: pct((d["avg_loss"] or 0) / 100)),
        ("Expectancy", lambda d: pct((d["expectancy"] or 0) / 100)),
        ("Max DD", lambda d: pct((d["max_drawdown"] or 0) / 100)),
        ("Current DD", lambda d: pct((d["current_drawdown"] or 0) / 100)),
    ]
    return pd.DataFrame(
        [{"Metric": name, **{label: formatter(diags[label]) for label in windows}} for name, formatter in rows]
    )[columns]


def investor_warning_table(
    trades: pd.DataFrame,
    fit: pd.DataFrame,
    completeness: pd.DataFrame,
    latest_scores: pd.DataFrame,
    observations: pd.DataFrame,
) -> pd.DataFrame:
    rows = []
    if trades.empty or len(trades) < 20:
        rows.append({"Warning": "LOW SAMPLE", "Detail": f"Only {len(trades)} resolved simulation trade(s). Treat PF and win rate as early evidence."})
    if not fit.empty and "Orders" in fit:
        low = fit[(pd.to_numeric(fit["Orders"], errors="coerce").fillna(0) > 0) & (pd.to_numeric(fit["Orders"], errors="coerce").fillna(0) < 20)]
        for _, row in low.head(5).iterrows():
            rows.append({"Warning": "LOW SAMPLE", "Detail": f"{row['Asset']} has only {row['Orders']} resolved setup(s)."})
    if not completeness.empty and "missing_open_bars" in completeness:
        missing = completeness[pd.to_numeric(completeness["missing_open_bars"], errors="coerce").fillna(0) > 0]
        for _, row in missing.head(5).iterrows():
            rows.append({"Warning": "DATA GAP", "Detail": f"{row.get('asset')} has {row.get('missing_open_bars')} real missing open-market bar(s)."})
        ignored = int(pd.to_numeric(completeness.get("ignored_provider_calendar_mismatch", 0), errors="coerce").fillna(0).sum())
        if ignored:
            rows.append({"Warning": "PROVIDER GAP", "Detail": f"{ignored} calendar/provider gap(s) are ignored as non-actionable market/session gaps."})
    window = common_forward_window(observations)
    if not window.get("usable"):
        rows.append({"Warning": "TIMELINE MISMATCH", "Detail": "Assets do not yet share a usable common observation window."})
    if not latest_scores.empty and "data_status" in latest_scores:
        bad = latest_scores[~latest_scores["data_status"].astype(str).str.upper().eq("OK")]
        for _, row in bad.head(5).iterrows():
            rows.append({"Warning": "DATA STALE", "Detail": f"{row.get('asset')} latest status is {row.get('data_status')}."})
    if trades.empty:
        return pd.DataFrame(rows, columns=["Warning", "Detail"])
    diag = return_diagnostics(trades["sim_return_pct"])
    if diag.get("top_3_profit_share") is not None and diag["top_3_profit_share"] > 0.6:
        rows.append({"Warning": "PF CONCENTRATION", "Detail": f"Top 3 winning trades explain {diag['top_3_profit_share']:.0%} of gross profit."})
    return pd.DataFrame(rows or [{"Warning": "NONE", "Detail": "No high-priority research warning from current forward data."}])


def gate_impact(df: pd.DataFrame) -> dict[str, Any]:
    if df.empty:
        return {"status": "INSUFFICIENT SAMPLE", "blocked_losers": 0, "blocked_winners": 0, "avoided_loss": 0.0, "missed_profit": 0.0, "benefit": 0.0}
    frame = df.copy()
    if "p_mr_fail" in frame:
        blocked = pd.to_numeric(frame["p_mr_fail"], errors="coerce") > MR_FAIL_THRESHOLD
    elif "mr_gate_pass" in frame:
        blocked = ~frame["mr_gate_pass"].astype(bool)
    else:
        blocked = pd.Series(False, index=frame.index)
    ret_col = next((c for c in ["hypothetical_return", "actual_return", "future_return_24h", "pred_mr_return_pct"] if c in frame.columns), None)
    returns = pd.to_numeric(frame[ret_col], errors="coerce").fillna(0) if ret_col else pd.Series(0, index=frame.index)
    blocked_returns = returns[blocked]
    blocked_losers = int((blocked_returns < 0).sum())
    blocked_winners = int((blocked_returns > 0).sum())
    avoided_loss = float(abs(blocked_returns[blocked_returns < 0].sum()))
    missed_profit = float(blocked_returns[blocked_returns > 0].sum())
    benefit = avoided_loss - missed_profit
    status = "INSUFFICIENT SAMPLE" if len(frame) < 10 else ("POSITIVE" if benefit > 0 else "NEGATIVE")
    return {
        "status": status,
        "blocked_losers": blocked_losers,
        "blocked_winners": blocked_winners,
        "avoided_loss": avoided_loss,
        "missed_profit": missed_profit,
        "benefit": benefit,
    }


def asset_summary(latest_scores: pd.DataFrame, observations: pd.DataFrame, runner_events: pd.DataFrame) -> pd.DataFrame:
    rows = []
    latest = latest_scores.copy()
    for asset in ASSETS:
        score = latest[latest["asset"] == asset].tail(1) if not latest.empty and "asset" in latest else pd.DataFrame()
        obs = observations[observations["asset"] == asset] if not observations.empty and "asset" in observations else pd.DataFrame()
        runners = runner_events[runner_events["asset"] == asset] if not runner_events.empty and "asset" in runner_events else pd.DataFrame()
        row = {
            "Asset": asset,
            "Asset Class": asset_class(asset),
            "Data Status": value_from(score, "data_status", "NOT YET AVAILABLE"),
            "Latest Completed Bar": value_from(score, "timestamp", value_from(obs.tail(1), "timestamp", "NOT YET AVAILABLE")),
            "Current Position State": value_from(score, "position_state", "FLAT"),
            "MR Candidates": int((obs.get("mr_eligible", pd.Series(dtype=bool)).fillna(False).astype(bool)).sum()) if not obs.empty else 0,
            "Resolved MR": int(obs["resolved_at"].notna().sum()) if not obs.empty and "resolved_at" in obs else 0,
            "MR_FAIL AUC": "INSUFFICIENT DATA",
            "Eligible MR Avg Return": "n/a",
            "Runner Events": len(runners),
            "Runner Avg Return": "n/a",
            "Research Status": US500_STATUS if asset == "US500" else ("INSUFFICIENT_DATA" if len(obs) < 10 else "WATCH"),
        }
        rows.append(row)
    return pd.DataFrame(rows)


def asset_class(asset: str) -> str:
    return {
        "GOLD": "METALS",
        "SILVER": "METALS",
        "USDJPY": "FX",
        "EURCAD": "FX",
        "EURUSD": "FX",
        "GBPUSD": "FX",
        "AUDUSD": "FX",
        "NZDUSD": "FX",
        "USDCAD": "FX",
        "USDCHF": "FX",
        "EURJPY": "FX",
        "GBPJPY": "FX",
        "AUDJPY": "FX",
        "CADJPY": "FX",
        "CHFJPY": "FX",
        "EURGBP": "FX",
        "EURCHF": "FX",
        "EURAUD": "FX",
        "GBPAUD": "FX",
        "GBPCAD": "FX",
        "GBPCHF": "FX",
        "AUDCAD": "FX",
        "AUDNZD": "FX",
        "AUDCHF": "FX",
        "NZDJPY": "FX",
        "NZDCAD": "FX",
        "NZDCHF": "FX",
        "CADCHF": "FX",
        "US500": "INDEX",
        "NAS100": "INDEX",
        "US30": "INDEX",
        "GER40": "INDEX",
        "UK100": "INDEX",
        "JPN225": "INDEX",
        "AUS200": "INDEX",
        "HK50": "INDEX",
        "FRA40": "INDEX",
        "EU50": "INDEX",
        "WTI": "ENERGY",
        "BRENT": "ENERGY",
        "NATGAS": "ENERGY",
        "BTCUSD": "CRYPTO",
        "ETHUSD": "CRYPTO",
        "SOLUSD": "CRYPTO",
        "XRPUSD": "CRYPTO",
        "ADAUSD": "CRYPTO",
        "DOGEUSD": "CRYPTO",
        "LTCUSD": "CRYPTO",
        "BCHUSD": "CRYPTO",
        "DOTUSD": "CRYPTO",
        "LINKUSD": "CRYPTO",
        "BNBUSD": "CRYPTO",
        "AVAXUSD": "CRYPTO",
    }.get(asset, "OTHER")


def value_from(df: pd.DataFrame, col: str, default: Any = "n/a") -> Any:
    if df.empty or col not in df:
        return default
    val = df.iloc[-1][col]
    return default if pd.isna(val) else val


def current_state_table(latest_scores: pd.DataFrame) -> pd.DataFrame:
    if latest_scores.empty:
        return pd.DataFrame(columns=["Asset", "Latest Completed Bar", "Data Status", "Position State", "MR Setup", "p_mr_win", "p_mr_fail", "MR Gate", "MR Eligible", "Runner Active", "p_runner_win", "Pred Runner Return", "Action", "Reason"])
    cols = {
        "asset": "Asset",
        "timestamp": "Latest Completed Bar",
        "data_status": "Data Status",
        "position_state": "Position State",
        "mr_setup": "MR Setup",
        "p_mr_win": "p_mr_win",
        "p_mr_fail": "p_mr_fail",
        "mr_gate_pass": "MR Gate",
        "mr_eligible": "MR Eligible",
        "runner_state_active": "Runner Active",
        "p_runner_win": "p_runner_win",
        "pred_runner_return_pct": "Pred Runner Return",
        "recommended_action": "Action",
        "reason": "Reason",
    }
    present = [c for c in cols if c in latest_scores]
    out = latest_scores[present].rename(columns=cols)
    if "Action" in out:
        out["Action"] = out["Action"].replace({"TF_ENTRY": "NO_ACTION", "RUNNER_ENTRY": "NO_ACTION"})
    return out
