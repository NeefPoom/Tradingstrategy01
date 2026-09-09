"""Educational strategy visual simulator for the dashboard."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import json
from pathlib import Path
import sys
from typing import Any

import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hybrid_ml.features import build_features
from hybrid_ml.mr_policy import MR_FAIL_THRESHOLD, detect_mr_setup

WARMUP_BARS = 260
VISIBLE_BARS = 200
MODEL_DIR = ROOT / "models"
INTERVALS = {
    "1H - real Phase H baseline": ("1h", 1),
    "30m - exploratory synthetic": ("30min", 2),
    "15m - exploratory synthetic": ("15min", 4),
}


REGIME_PARAMS = {
    "TREND UP": dict(drift=0.0009, volatility=0.005, mean_reversion=0.01, shock_probability=0.01, shock_size=0.025),
    "TREND DOWN": dict(drift=-0.0009, volatility=0.005, mean_reversion=0.01, shock_probability=0.01, shock_size=0.025),
    "MEAN REVERSION": dict(drift=0.0, volatility=0.006, mean_reversion=0.12, shock_probability=0.01, shock_size=0.018),
    "CHOP / WHIPSAW": dict(drift=0.0, volatility=0.009, mean_reversion=0.2, shock_probability=0.02, shock_size=0.02),
    "VOLATILITY SHOCK": dict(drift=0.0001, volatility=0.006, mean_reversion=0.03, shock_probability=0.08, shock_size=0.045),
    "MIXED": dict(drift=0.0002, volatility=0.007, mean_reversion=0.06, shock_probability=0.03, shock_size=0.03),
}


ASSET_PROFILES = {
    "GOLD": dict(start=2400.0, volatility_scale=0.9),
    "USDJPY": dict(start=150.0, volatility_scale=0.55),
    "US500": dict(start=5200.0, volatility_scale=0.7),
    "BTCUSD": dict(start=65000.0, volatility_scale=1.8),
    "ETHUSD": dict(start=3400.0, volatility_scale=1.65),
    "EURCAD": dict(start=1.48, volatility_scale=0.45),
}


@dataclass(frozen=True)
class SimulationResult:
    prices: pd.DataFrame
    features: pd.DataFrame
    events: pd.DataFrame
    trades: pd.DataFrame
    summary: dict[str, Any]


def _synthetic_close(seed: int, regime: str, asset_profile: str, bars: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    params = REGIME_PARAMS.get(regime, REGIME_PARAMS["MIXED"]).copy()
    profile = ASSET_PROFILES.get(asset_profile, ASSET_PROFILES["GOLD"])
    volatility = params["volatility"] * profile["volatility_scale"]
    close = np.zeros(bars)
    close[0] = profile["start"]
    anchor = close[0]
    trend_sign = 1.0

    for i in range(1, bars):
        if regime == "MIXED" and i % 85 == 0:
            trend_sign *= -1
        reversion = params["mean_reversion"] * (np.log(anchor) - np.log(close[i - 1]))
        drift = params["drift"] * (trend_sign if regime == "MIXED" else 1.0)
        shock = 0.0
        if rng.random() < params["shock_probability"]:
            shock = rng.normal(0, params["shock_size"])
        ret = drift + reversion + rng.normal(0, volatility) + shock
        close[i] = max(close[i - 1] * np.exp(ret), close[0] * 0.1)
    return close


def synthetic_prices(seed: int, regime: str, asset_profile: str, visible_bars: int = VISIBLE_BARS, freq: str = "1h") -> pd.DataFrame:
    bars = visible_bars + WARMUP_BARS
    close = _synthetic_close(seed, regime, asset_profile, bars)
    rng = np.random.default_rng(seed + 101)
    span = np.maximum(np.abs(rng.normal(0.0015, 0.001, bars)), 0.0002)
    open_ = np.r_[close[0], close[:-1]]
    high = np.maximum(open_, close) * (1 + span)
    low = np.minimum(open_, close) * (1 - span)
    volume = rng.integers(500, 5000, bars)
    timestamps = pd.date_range("2026-01-01", periods=bars, freq=freq)
    return pd.DataFrame({"timestamp": timestamps, "open": open_, "high": high, "low": low, "close": close, "volume": volume})


def historical_prices(asset: str, seed: int, visible_bars: int = VISIBLE_BARS) -> pd.DataFrame:
    path = ROOT / "data" / "prices" / f"{asset}_1h_yahoo.csv"
    if not path.exists():
        return synthetic_prices(seed, "MIXED", asset, visible_bars)
    prices = pd.read_csv(path)
    prices["timestamp"] = pd.to_datetime(prices["timestamp"], errors="coerce")
    prices = prices.dropna(subset=["timestamp", "open", "high", "low", "close"]).sort_values("timestamp")
    need = visible_bars + WARMUP_BARS
    if len(prices) <= need:
        return prices.tail(need).reset_index(drop=True)
    rng = np.random.default_rng(seed)
    start = int(rng.integers(0, len(prices) - need))
    return prices.iloc[start : start + need].reset_index(drop=True)


def _p_fail(row: pd.Series) -> float:
    vol = float(row.get("vol_ratio", 1.0) or 1.0)
    cross = float(row.get("cross_count", 0.0) or 0.0)
    direction_persistence = float(row.get("price_direction_24", 0.0) or 0.0)
    osc_slope = abs(float(row.get("osc_slope_3", 0.0) or 0.0))
    raw = 0.28 + max(vol - 1.0, 0) * 0.18 + min(cross / 12, 1) * 0.24 + direction_persistence * 0.16 - min(osc_slope, 1) * 0.08
    return float(np.clip(raw, 0.02, 0.95))


def _p_win(row: pd.Series) -> float:
    return float(np.clip(1.0 - _p_fail(row) + 0.05, 0.03, 0.97))


@lru_cache(maxsize=1)
def _load_probability_models() -> tuple[list[str], Any | None, Any | None]:
    try:
        columns = json.loads((MODEL_DIR / "feature_columns.json").read_text(encoding="utf-8"))
        fail_model = joblib.load(MODEL_DIR / "mr_fail_classifier.joblib")
        win_model = joblib.load(MODEL_DIR / "mr_win_classifier.joblib")
        return columns, fail_model, win_model
    except Exception:
        return [], None, None


def _model_probabilities(features: pd.DataFrame) -> tuple[pd.Series | None, pd.Series | None]:
    columns, fail_model, win_model = _load_probability_models()
    if not columns or fail_model is None or win_model is None:
        return None, None
    try:
        matrix = features.reindex(columns=columns)
        matrix = matrix.replace([np.inf, -np.inf], np.nan).ffill().bfill().fillna(0)
        p_fail = pd.Series(fail_model.predict_proba(matrix)[:, 1], index=features.index)
        p_win = pd.Series(win_model.predict_proba(matrix)[:, 1], index=features.index)
        return p_fail.clip(0.0, 1.0), p_win.clip(0.0, 1.0)
    except Exception:
        return None, None


def _add_prev_columns(features: pd.DataFrame) -> pd.DataFrame:
    out = features.copy()
    out["osc_prev"] = out["osc"].shift(1)
    out["signal_prev"] = out["signal"].shift(1)
    p_fail, p_win = _model_probabilities(out)
    out["p_mr_fail"] = p_fail if p_fail is not None else out.apply(_p_fail, axis=1)
    out["p_mr_win"] = p_win if p_win is not None else out.apply(_p_win, axis=1)
    return out


def simulate_strategy(prices: pd.DataFrame, cfg: dict[str, Any], apply_gate: bool, visible_bars: int = VISIBLE_BARS) -> SimulationResult:
    """Replay MR candidates with the same Phase H MR resolver assumptions.

    MR entry/setup/gate uses the frozen policy. Outcome resolution is bar-by-bar:
    stop = 1 ATR against entry, TP1 = 1 ATR in favor. After TP1, the remaining
    runner follows the oscillator-cross exit research method.
    """
    feats = _add_prev_columns(build_features(prices, cfg)).dropna(subset=["osc", "signal", "atr"]).reset_index(drop=True)
    feats = feats.tail(visible_bars).reset_index(drop=True)
    state = "FLAT"
    entry: dict[str, Any] | None = None
    events: list[dict[str, Any]] = []
    trades: list[dict[str, Any]] = []

    for i, row in feats.iterrows():
        setup = detect_mr_setup(row)
        close = float(row["close"])
        atr = float(row["atr"] or 0)
        p_fail = float(row["p_mr_fail"])
        gate_pass = p_fail <= MR_FAIL_THRESHOLD

        if state == "FLAT" and setup["setup"]:
            if apply_gate and not gate_pass:
                events.append(
                    {
                        "idx": i,
                        "timestamp": row["timestamp"],
                        "price": close,
                        "event": "BLOCKED",
                        "direction": setup["direction"],
                        "reason": f"p_mr_fail {p_fail:.2f} > {MR_FAIL_THRESHOLD:.2f}",
                    }
                )
                continue
            state = f"MR_{setup['direction']}"
            entry = {
                "idx": i,
                "timestamp": row["timestamp"],
                "price": close,
                "atr": atr,
                "direction": setup["direction"],
                "p_mr_fail": p_fail,
                "p_mr_win": float(row["p_mr_win"]),
                "gate": "PASS" if gate_pass else "OFF",
                "reason": setup["reason"],
                "state_path": f"FLAT -> MR_{setup['direction']}",
            }
            events.append({"idx": i, "timestamp": row["timestamp"], "price": close, "event": f"{setup['direction']} MR", "direction": setup["direction"], "reason": setup["reason"]})
            continue

        if state.startswith("MR_") and entry:
            direction = 1 if entry["direction"] == "LONG" else -1
            tp = float(entry["price"]) + direction * float(entry["atr"])
            stop = float(entry["price"]) - direction * float(entry["atr"])
            hit_fail = (direction == 1 and float(row["low"]) <= stop) or (direction == -1 and float(row["high"]) >= stop)
            hit_tp = (direction == 1 and float(row["high"]) >= tp) or (direction == -1 and float(row["low"]) <= tp)
            if hit_fail or hit_tp:
                exit_event = "MR FAIL" if hit_fail else "TP1"
                state_after = "FLAT" if hit_fail else f"RUNNER_{entry['direction']}"
                exit_price = stop if hit_fail else tp
                mr_ret = (exit_price / float(entry["price"]) - 1) * direction * 100
                events.append({"idx": i, "timestamp": row["timestamp"], "price": exit_price, "event": exit_event, "direction": entry["direction"], "reason": "1 ATR stop hit before TP1" if hit_fail else "1 ATR TP1 hit"})
                if hit_fail:
                    trades.append(_trade_row(entry, row, mr_ret, "MR_FAIL", entry["state_path"] + " -> MR_FAIL -> CLOSE", exit_price=exit_price, mr_return=mr_ret, runner_return=None))
                    entry = None
                    state = "FLAT"
                else:
                    entry["state_path"] += f" -> TP1_1ATR -> {state_after}"
                    entry["mr_return"] = mr_ret
                    entry["runner_entry_price"] = exit_price
                    entry["runner_stop"] = stop
                    events.append({"idx": i, "timestamp": row["timestamp"], "price": exit_price, "event": "RUNNER", "direction": entry["direction"], "reason": "runner position opened after 1 ATR TP1"})
                    state = state_after
                continue

        if state.startswith("RUNNER_") and entry:
            direction = 1 if entry["direction"] == "LONG" else -1
            runner_entry = float(entry["runner_entry_price"])
            stop = float(entry["runner_stop"])
            hit_stop = (direction == 1 and float(row["low"]) <= stop) or (direction == -1 and float(row["high"]) >= stop)
            cross_against = (
                (entry["direction"] == "LONG" and float(row["osc_prev"]) >= float(row["signal_prev"]) and float(row["osc"]) < float(row["signal"]))
                or (entry["direction"] == "SHORT" and float(row["osc_prev"]) <= float(row["signal_prev"]) and float(row["osc"]) > float(row["signal"]))
            )
            age = i - int(entry["idx"])
            if hit_stop or cross_against or age >= visible_bars:
                exit_price = stop if hit_stop else close
                runner_ret = (exit_price / runner_entry - 1) * direction * 100
                # A half TP1 / half runner blend mirrors the documented partial-profit lifecycle.
                total_ret = 0.5 * float(entry["mr_return"]) + 0.5 * runner_ret
                reason = "original 1 ATR stop hit" if hit_stop else "opposite oscillator/signal cross" if cross_against else "end of replay window"
                events.append({"idx": i, "timestamp": row["timestamp"], "price": exit_price, "event": "CLOSE", "direction": entry["direction"], "reason": reason})
                trades.append(_trade_row(entry, row, total_ret, "RUNNER_EXIT", entry["state_path"] + " -> EXIT_RUNNER -> FLAT", exit_price=exit_price, mr_return=entry["mr_return"], runner_return=runner_ret))
                entry = None
                state = "FLAT"

    if entry is not None and len(feats):
        row = feats.iloc[-1]
        direction = 1 if entry["direction"] == "LONG" else -1
        if "runner_entry_price" in entry:
            runner_ret = (float(row["close"]) / float(entry["runner_entry_price"]) - 1) * direction * 100
            ret = 0.5 * float(entry["mr_return"]) + 0.5 * runner_ret
            mr_ret = entry["mr_return"]
        else:
            runner_ret = None
            ret = (float(row["close"]) / entry["price"] - 1) * direction * 100
            mr_ret = ret
        events.append({"idx": len(feats) - 1, "timestamp": row["timestamp"], "price": float(row["close"]), "event": "CLOSE", "direction": entry["direction"], "reason": "end of 200h simulation"})
        trades.append(_trade_row(entry, row, ret, "END_OF_PATH", entry["state_path"] + " -> CLOSE", mr_return=mr_ret, runner_return=runner_ret))

    events_df = pd.DataFrame(events)
    trades_df = pd.DataFrame(trades)
    summary = _summary(trades_df)
    return SimulationResult(prices=feats, features=feats, events=events_df, trades=trades_df, summary=summary)


def _trade_row(entry: dict[str, Any], exit_row: pd.Series, ret: float, exit_reason: str, state_path: str, exit_price: float | None = None, mr_return: float | None = None, runner_return: float | None = None) -> dict[str, Any]:
    close = float(exit_row["close"]) if exit_price is None else float(exit_price)
    return {
        "Entry": entry["timestamp"],
        "Exit": exit_row["timestamp"],
        "Type": entry["direction"],
        "Gate": entry["gate"],
        "Entry price": round(float(entry["price"]), 5),
        "Exit price": round(close, 5),
        "Return %": round(float(ret), 3),
        "MR leg %": round(float(mr_return), 3) if mr_return is not None else None,
        "Runner leg %": round(float(runner_return), 3) if runner_return is not None else None,
        "p_mr_fail": round(float(entry["p_mr_fail"]), 3),
        "p_mr_win": round(float(entry["p_mr_win"]), 3),
        "Exit reason": exit_reason,
        "Setup reason": entry["reason"],
        "State path": state_path,
    }


def _summary(trades: pd.DataFrame) -> dict[str, Any]:
    if trades.empty:
        return {"Trades": 0, "Win rate": "n/a", "PF": "n/a", "Net P&L": "0.00%", "Max DD": "0.00%"}
    returns = pd.to_numeric(trades["Return %"], errors="coerce").fillna(0)
    wins = returns[returns > 0]
    losses = returns[returns < 0]
    pf = "inf" if abs(losses.sum()) == 0 and wins.sum() > 0 else f"{wins.sum() / abs(losses.sum()):.2f}" if abs(losses.sum()) > 0 else "n/a"
    equity = returns.cumsum()
    dd = equity - equity.cummax()
    return {
        "Trades": int(len(returns)),
        "Win rate": f"{(returns > 0).mean():.2%}",
        "PF": pf,
        "Net P&L": f"{returns.sum():.2f}%",
        "Max DD": f"{dd.min():.2f}%",
    }


def simulator_figure(result: SimulationResult) -> go.Figure:
    frame = result.features.copy().reset_index(drop=True)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[0.66, 0.34], vertical_spacing=0.05)
    fig.add_trace(go.Scatter(x=frame.index, y=frame["close"], mode="lines", name="Price", line=dict(color="#d1d5db", width=2)), row=1, col=1)
    fig.add_trace(go.Scatter(x=frame.index, y=frame["osc"], mode="lines", name="Osc", line=dict(color="#60a5fa", width=2)), row=2, col=1)
    fig.add_trace(go.Scatter(x=frame.index, y=frame["signal"], mode="lines", name="Signal", line=dict(color="#f59e0b", width=2)), row=2, col=1)
    fig.add_hline(y=0, row=2, col=1, line_dash="dot", line_color="#9ca3af")

    if not result.events.empty:
        styles = {
            "LONG MR": ("triangle-up", "#22c55e"),
            "SHORT MR": ("triangle-down", "#ef4444"),
            "TP1": ("circle", "#38bdf8"),
            "RUNNER": ("diamond", "#a78bfa"),
            "MR FAIL": ("x", "#fb7185"),
            "CLOSE": ("square", "#e5e7eb"),
            "BLOCKED": ("diamond", "#f59e0b"),
        }
        for event, rows in result.events.groupby("event"):
            symbol, color = styles.get(event, ("circle", "#a78bfa"))
            fig.add_trace(
                go.Scatter(
                    x=rows["idx"],
                    y=rows["price"],
                    mode="markers",
                    name=event,
                    marker=dict(symbol=symbol, color=color, size=12, line=dict(width=1, color="#0b0f17")),
                    text=rows["reason"],
                    hovertemplate="%{fullData.name}<br>Bar %{x}<br>Price %{y:.4f}<br>%{text}<extra></extra>",
                ),
                row=1,
                col=1,
            )
            osc_y = frame.loc[rows["idx"].astype(int), "osc"] if len(rows) else []
            fig.add_trace(
                go.Scatter(x=rows["idx"], y=osc_y, mode="markers", name=f"{event} osc", showlegend=False, marker=dict(symbol=symbol, color=color, size=9)),
                row=2,
                col=1,
            )

    fig.update_layout(
        template="plotly_dark",
        height=680,
        margin=dict(l=20, r=20, t=35, b=20),
        title="Price / position and oscillator replay",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="Osc / signal", row=2, col=1)
    fig.update_xaxes(title_text="Simulation hour", row=2, col=1)
    return fig
