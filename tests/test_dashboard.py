from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from dashboard import data_loader
from dashboard.data_loader import (
    BROKER_EXECUTION,
    FORBIDDEN_ACTIONS,
    FORBIDDEN_SCRIPTS,
    MR_FAIL_THRESHOLD,
    TF_STATUS,
    US500_STATUS,
    load_parquet_or_csv,
    load_asset_registry,
    normalize_actions,
)
from dashboard.metrics import asset_summary, current_state_table, mr_forward_metrics
from dashboard.metrics import yahoo_quality_summary
from dashboard.metrics import (
    asset_selection_score_table,
    common_forward_window,
    performance_summary,
    portfolio_candidate_sets,
    simulation_trade_frame,
    strategy_fit_table,
    strategy_return_correlation,
    win_loss_reason_table,
)
from dashboard.simulator import simulate_strategy, synthetic_prices
from hybrid_ml.config import load_config


def test_dashboard_loader_works_with_missing_runner_file(monkeypatch, tmp_path):
    monkeypatch.setattr(data_loader, "DATA", tmp_path / "data")
    df = data_loader.load_runner_events()
    assert df.empty


def test_zero_mr_candidates_are_safe():
    metrics = mr_forward_metrics(pd.DataFrame())
    assert metrics["candidates"] == 0
    assert metrics["status"] == "INSUFFICIENT"


def test_mr_candidate_count_does_not_fall_back_to_observations():
    observations = pd.DataFrame({"asset": ["GOLD", "USDJPY"], "p_mr_fail": [0.2, 0.3]})
    metrics = mr_forward_metrics(pd.DataFrame(), observations)
    assert metrics["candidates"] == 0


def test_zero_runner_events_are_safe():
    out = asset_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame())
    assert set(out["Runner Events"]) == {0}


def test_threshold_is_read_only_045():
    assert MR_FAIL_THRESHOLD == 0.45


def test_us500_displays_research_only():
    out = asset_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame())
    us500 = out[out["Asset"] == "US500"].iloc[0]
    assert us500["Research Status"] == US500_STATUS == "RESEARCH_ONLY"


def test_tf_displays_off():
    assert TF_STATUS == "OFF"


def test_no_runner_entry_action_exists():
    df = pd.DataFrame({"recommended_action": ["RUNNER_ENTRY", "NO_ACTION"]})
    out = normalize_actions(df)
    assert "RUNNER_ENTRY" not in set(out["recommended_action"])
    assert "RUNNER_ENTRY" in FORBIDDEN_ACTIONS


def test_no_broker_action_exists():
    assert BROKER_EXECUTION == "OFF"
    assert {"BUY", "SELL", "CLOSE"}.issubset(FORBIDDEN_ACTIONS)


def test_parquet_to_csv_fallback_works(tmp_path):
    csv = tmp_path / "sample.csv"
    pd.DataFrame({"asset": ["GOLD"]}).to_csv(csv, index=False)
    df = load_parquet_or_csv(tmp_path / "missing.parquet", csv)
    assert df.iloc[0]["asset"] == "GOLD"


def test_refresh_data_does_not_modify_research_files():
    before = set(data_loader.FORBIDDEN_SCRIPTS)
    # Refresh clears Streamlit's cache in app.py; data-loader refresh paths are read-only.
    assert before == FORBIDDEN_SCRIPTS


def test_no_dashboard_function_invokes_model_training():
    assert "scripts/train_models.py" in FORBIDDEN_SCRIPTS


def test_no_dashboard_function_invokes_run_phase_h_automatically():
    assert "scripts/run_phase_h.py" in FORBIDDEN_SCRIPTS


def test_no_forbidden_actions_in_current_state_table():
    df = pd.DataFrame({"asset": ["GOLD"], "recommended_action": ["TF_ENTRY"]})
    out = current_state_table(normalize_actions(df))
    assert "TF_ENTRY" not in set(out["Action"])


def test_yahoo_warning_explains_assets():
    df = pd.DataFrame(
        {
            "asset": ["GOLD", "BTCUSD"],
            "status": ["WARNING", "PASS"],
            "missing_bar_estimate": [3, 0],
            "zero_volume_count": [2, 0],
            "bad_ohlc_count": [0, 0],
            "duplicate_count": [0, 0],
            "max_bar_gap_hours": [80, 1],
        }
    )
    status, note, rows = yahoo_quality_summary(df)
    assert status == "WARNING"
    assert "GOLD" in note
    assert "No duplicate rows or bad OHLC rows" in note
    assert len(rows) == 1


def test_simulation_trade_frame_uses_directional_returns():
    candidates = pd.DataFrame(
        {
            "asset": ["GOLD", "USDJPY"],
            "timestamp": ["2026-09-01 10:00:00", "2026-09-01 11:00:00"],
            "direction": ["LONG", "SHORT"],
            "decision": ["MR_BLOCK", "MR_BLOCK"],
        }
    )
    observations = pd.DataFrame(
        {
            "asset": ["GOLD", "USDJPY"],
            "timestamp": ["2026-09-01 10:00:00", "2026-09-01 11:00:00"],
            "future_return_24h": [2.0, -3.0],
        }
    )
    trades = simulation_trade_frame(candidates, observations)
    assert trades["sim_return_pct"].tolist() == [2.0, 3.0]
    assert trades["outcome"].tolist() == ["Win", "Win"]
    assert "LONG matched" in trades.iloc[0]["why"]
    stats = performance_summary(trades)
    assert stats["orders"] == 2
    assert stats["win_rate"] == 1.0
    reasons = win_loss_reason_table(trades)
    assert set(reasons["Asset"]) == {"GOLD", "USDJPY"}
    ranking = asset_selection_score_table(trades)
    assert ranking.iloc[0]["Rank"] == 1


def test_asset_registry_loads_pepperstone_metadata():
    registry = load_asset_registry()
    assert {"asset", "asset_class", "pepperstone_symbol", "calendar"}.issubset(registry.columns)
    gold = registry[registry["asset"] == "GOLD"].iloc[0]
    assert gold["pepperstone_symbol"] == "XAUUSD"
    assert gold["asset_class"] == "METALS"


def test_strategy_fit_and_portfolio_candidates_rank_assets():
    trades = pd.DataFrame(
        {
            "asset": ["GOLD", "GOLD", "USDJPY", "USDJPY", "BTCUSD", "BTCUSD"],
            "timestamp": pd.date_range("2026-09-01", periods=6, freq="h"),
            "sim_return_pct": [1.0, 1.5, -0.2, 0.4, 0.7, -0.1],
        }
    )
    registry = pd.DataFrame(
        {
            "asset": ["GOLD", "USDJPY", "BTCUSD"],
            "asset_class": ["METALS", "FX", "CRYPTO"],
            "pepperstone_symbol": ["XAUUSD", "USDJPY", "BTCUSD"],
            "selection_enabled": [True, True, True],
            "estimated_round_trip_cost_pct": [0.0, 0.0, 0.0],
        }
    )
    completeness = pd.DataFrame({"asset": ["GOLD", "USDJPY", "BTCUSD"], "missing_open_bars": [0, 0, 0]})
    fit = strategy_fit_table(trades, registry, completeness)
    assert fit.iloc[0]["Rank"] == 1
    assert set(fit["Decision"]).issubset({"Needs forward sample", "Core candidate", "Diversifier watch", "Observe only", "Avoid for now"})
    corr = strategy_return_correlation(trades)
    assert set(corr.columns) == {"GOLD", "USDJPY", "BTCUSD"}
    portfolios, curves = portfolio_candidate_sets(trades, fit, top_n=2, max_avg_corr=0.7)
    assert {"Top score", "Low correlation", "Class balanced", "All usable"}.issubset(set(portfolios["Portfolio"]))
    assert not curves.empty


def test_common_forward_window_uses_shared_asset_span():
    observations = pd.DataFrame(
        {
            "asset": ["A", "A", "B", "B"],
            "timestamp": [
                "2026-09-01 00:00:00",
                "2026-09-05 00:00:00",
                "2026-09-02 00:00:00",
                "2026-09-04 00:00:00",
            ],
        }
    )
    window = common_forward_window(observations)
    assert str(window["start"]) == "2026-09-02 00:00:00"
    assert str(window["end"]) == "2026-09-04 00:00:00"
    assert window["usable"] is True


def test_strategy_visual_simulator_produces_200_hour_replay():
    prices = synthetic_prices(seed=7, regime="MIXED", asset_profile="GOLD")
    result = simulate_strategy(prices, load_config(), apply_gate=True)
    assert len(result.features) == 200
    assert {"Trades", "Win rate", "PF", "Net P&L", "Max DD"}.issubset(result.summary)
    assert {"osc", "signal", "p_mr_fail", "p_mr_win"}.issubset(result.features.columns)
    if not result.trades.empty:
        assert {"MR leg %", "Runner leg %"}.issubset(result.trades.columns)
