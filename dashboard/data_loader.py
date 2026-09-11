"""Read-only Phase H dashboard data loading."""
from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

import pandas as pd
import yaml


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
DATA = ROOT / "data"
LOG_DIR = ROOT / "logs"
LOG_FILE = LOG_DIR / "dashboard.log"
GITHUB_ACTIONS_RUNS_URL = "https://api.github.com/repos/NeefPoom/Tradingstrategy01/actions/runs?branch=main&per_page=100"


def _configured_asset_names() -> list[str]:
    try:
        config = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8")) or {}
    except Exception:
        return ["GOLD", "USDJPY", "US500", "BTCUSD", "ETHUSD", "EURCAD"]
    return list((config.get("assets") or {}).keys())


ASSETS = _configured_asset_names()
MR_FAIL_THRESHOLD = 0.45
MODEL_VERSION = "H1.0"
TF_STATUS = "OFF"
BROKER_EXECUTION = "OFF"
US500_STATUS = "RESEARCH_ONLY"
THAILAND_TZ = ZoneInfo("Asia/Bangkok")
FORBIDDEN_ACTIONS = {"BUY", "SELL", "CLOSE", "TF_ENTRY", "RUNNER_ENTRY"}
FORBIDDEN_SCRIPTS = {
    "scripts/train_models.py",
    "scripts/walk_forward.py",
    "scripts/run_phase_h.py",
}


def setup_logging() -> None:
    LOG_DIR.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )


def log_event(message: str) -> None:
    setup_logging()
    logging.info(message)


def now_iso() -> str:
    return datetime.now(THAILAND_TZ).replace(microsecond=0).isoformat()


def format_thailand_timestamp(value: Any) -> str:
    """Format timestamps for dashboard display in Thailand time."""
    if value in (None, "", "NOT YET AVAILABLE", "UNKNOWN"):
        return str(value or "NOT YET AVAILABLE")
    ts = pd.to_datetime(value, errors="coerce")
    if pd.isna(ts):
        return str(value)
    if ts.tzinfo is None:
        ts = ts.tz_localize(timezone.utc)
    return ts.tz_convert(THAILAND_TZ).strftime("%Y-%m-%d %H:%M:%S ICT (+07:00)")


def _safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size <= 2:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def load_parquet_or_csv(parquet_path: Path, csv_path: Path | None = None) -> pd.DataFrame:
    """Prefer Parquet and fall back to CSV without writing anything."""
    csv_path = csv_path or parquet_path.with_suffix(".csv")
    if parquet_path.exists():
        try:
            return pd.read_parquet(parquet_path)
        except Exception as exc:  # pragma: no cover - exact engine errors vary
            log_event(f"parse error: {parquet_path}: {exc}")
    if csv_path.exists():
        try:
            return _safe_read_csv(csv_path)
        except Exception as exc:  # pragma: no cover
            log_event(f"parse error: {csv_path}: {exc}")
    log_event(f"missing file warning: {parquet_path} / {csv_path}")
    return pd.DataFrame()


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        log_event(f"missing file warning: {path}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        log_event(f"parse error: {path}: {exc}")
        return {}


def load_text(path: Path) -> str:
    if not path.exists():
        log_event(f"missing file warning: {path}")
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        log_event(f"parse error: {path}: {exc}")
        return ""


def load_report_csv(name: str) -> pd.DataFrame:
    return _safe_read_csv(REPORTS / name)


def load_asset_registry() -> pd.DataFrame:
    config_path = ROOT / "config.yaml"
    if not config_path.exists():
        return pd.DataFrame()
    try:
        config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        log_event(f"parse error: {config_path}: {exc}")
        return pd.DataFrame()

    assets = config.get("assets", {}) or {}
    class_map = config.get("asset_classes", {}) or {}
    rows = []
    for asset, meta in assets.items():
        meta = meta or {}
        rows.append(
            {
                "asset": asset,
                "asset_class": meta.get("asset_class") or class_map.get(asset, "OTHER"),
                "universe_role": meta.get("universe_role", "core"),
                "yahoo_symbol": meta.get("yahoo", ""),
                "pepperstone_symbol": meta.get("pepperstone", asset),
                "calendar": meta.get("calendar", ""),
                "forward_start_utc": meta.get("forward_start_utc", ""),
                "data_collection_enabled": bool(meta.get("data_collection_enabled", True)),
                "forward_research_enabled": bool(meta.get("forward_research_enabled", True)),
                "selection_enabled": bool(meta.get("selection_enabled", True)),
                "estimated_round_trip_cost_pct": float(meta.get("estimated_round_trip_cost_pct", 0) or 0),
            }
        )
    return pd.DataFrame(rows)


def load_observations() -> pd.DataFrame:
    return load_parquet_or_csv(
        DATA / "forward" / "phase_h_observations.parquet",
        DATA / "forward" / "phase_h_observations.csv",
    )


def load_mr_candidates() -> pd.DataFrame:
    return load_parquet_or_csv(
        DATA / "forward" / "mr_candidates.parquet",
        DATA / "forward" / "mr_candidates.csv",
    )


def load_runner_events() -> pd.DataFrame:
    return load_parquet_or_csv(
        DATA / "forward" / "runner_events.parquet",
        DATA / "forward" / "runner_events.csv",
    )


def file_mtime(path: Path) -> datetime | None:
    if not path.exists():
        return None
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).astimezone(THAILAND_TZ)


def latest_file_mtime(paths: list[Path]) -> datetime | None:
    mtimes = [mtime for path in paths if (mtime := file_mtime(path))]
    return max(mtimes) if mtimes else None


def _extract_status_value(text: str, label: str) -> str | None:
    pattern = rf"{re.escape(label)}\s*\n([^\n]+)"
    match = re.search(pattern, text, flags=re.IGNORECASE)
    if not match:
        return None
    return match.group(1).strip().strip("*")


def parse_phase_h_status(text: str) -> dict[str, Any]:
    decision = _extract_status_value(text, "## 15. Decision") or "INSUFFICIENT_FORWARD_DATA"
    generated_match = re.search(r"\*\*Generated:\*\*\s*([^\n]+)", text)
    days_match = re.search(r"## 4\. Days observed\s*\n(\d+)", text)
    mr_match = re.search(r"(\d+)\s+candidates,\s+(\d+)\s+resolved", text)
    runner_match = re.search(r"## 7\. Runner events / resolved\s*\n(\d+)\s+events", text)
    return {
        "decision": decision,
        "generated_at": generated_match.group(1).strip() if generated_match else "NOT YET AVAILABLE",
        "days_observed": int(days_match.group(1)) if days_match else 0,
        "mr_candidates": int(mr_match.group(1)) if mr_match else 0,
        "mr_resolved": int(mr_match.group(2)) if mr_match else 0,
        "runner_events": int(runner_match.group(1)) if runner_match else 0,
        "model_freeze_violation": "violation\nNone".lower() not in text.lower()
        and "PHASE H MODEL FREEZE VIOLATION" in text,
    }


def model_freeze_status(baseline: dict[str, Any], registry: dict[str, Any] | None = None) -> dict[str, Any]:
    registry = registry or {}
    config = baseline.get("config_snapshot", {})
    phase_h = config.get("phase_h", {})
    threshold = baseline.get("mr_fail_threshold") or registry.get("phase_h_baseline", {}).get("mr_fail_threshold")
    model_version = baseline.get("model_version") or registry.get("phase_h_baseline", {}).get("version") or MODEL_VERSION
    automatic_retraining = phase_h.get("automatic_retraining", baseline.get("automatic_retraining", False))
    tf_enabled = phase_h.get("tf_enabled", baseline.get("tf_enabled", False))
    status = "PASS"
    if model_version != MODEL_VERSION or float(threshold or 0) != MR_FAIL_THRESHOLD or automatic_retraining or tf_enabled:
        status = "FAIL"
    return {
        "model_version": model_version,
        "expected_hash": "recorded in baseline" if baseline.get("models") else "NOT YET AVAILABLE",
        "current_hash": "not recalculated by dashboard",
        "freeze_status": status,
        "mr_fail_threshold": MR_FAIL_THRESHOLD,
        "automatic_retraining": bool(automatic_retraining),
        "tf": "ON" if tf_enabled else TF_STATUS,
    }


def scheduler_status(health: dict[str, Any]) -> dict[str, Any]:
    if not health:
        return {"status": "UNKNOWN"}
    status = str(health.get("status") or health.get("last_status") or "UNKNOWN").upper()
    exit_code = health.get("exit_code", health.get("last_exit_code"))
    if exit_code not in (None, 0, "0"):
        status = "FAILED"
    return {
        "last_start": health.get("last_start") or health.get("last_started_at") or "NOT YET AVAILABLE",
        "last_finish": health.get("last_finish") or health.get("last_finished_at") or "NOT YET AVAILABLE",
        "exit_code": exit_code if exit_code is not None else "NOT YET AVAILABLE",
        "status": status,
        "duration": health.get("duration") or health.get("duration_seconds") or "NOT YET AVAILABLE",
        "last_successful_run": health.get("last_successful_run") or health.get("last_success_at") or (health.get("last_finish") if status == "SUCCESS" else None) or "NOT YET AVAILABLE",
        "next_scheduled_run": health.get("next_scheduled_run") or "NOT YET AVAILABLE",
    }


def _scheduler_history_from_runs(runs: list[dict[str, Any]], now: datetime | None = None, hours: int = 72) -> pd.DataFrame:
    now = now or datetime.now(timezone.utc)
    start = now - timedelta(hours=hours)
    end_hour = pd.Timestamp(now).tz_convert(THAILAND_TZ).floor("h")
    hourly = pd.DataFrame(
        {
            "Hour": [
                ts.strftime("%Y-%m-%d %H:00 ICT")
                for ts in pd.date_range(end=end_hour, periods=hours, freq="h").sort_values(ascending=False)
            ]
        }
    )
    rows = []
    for run in runs:
        finished = pd.to_datetime(run.get("updated_at") or run.get("created_at"), utc=True, errors="coerce")
        if pd.isna(finished) or finished.to_pydatetime() < start:
            continue
        status = str(run.get("status") or "").lower()
        conclusion = str(run.get("conclusion") or "").lower()
        display_status = "SUCCESS" if status == "completed" and conclusion == "success" else (conclusion or status or "unknown").upper()
        rows.append(
            {
                "_finished": finished,
                "_successful_finished": finished if display_status == "SUCCESS" else pd.NaT,
                "Run finished": format_thailand_timestamp(finished),
                "Hour": finished.tz_convert(THAILAND_TZ).floor("h").strftime("%Y-%m-%d %H:00 ICT"),
                "Status": display_status,
                "Workflow": run.get("name", "Update trading dashboard"),
                "Commit": str(run.get("head_sha", ""))[:7],
                "URL": run.get("html_url", ""),
            }
        )
    if not rows:
        hourly["Successful runs"] = 0
        hourly["Last successful run"] = "n/a"
        hourly["Other runs"] = 0
        hourly["Latest status"] = "NO RUN"
        hourly["Latest commit"] = ""
        return hourly

    frame = pd.DataFrame(rows).sort_values("_finished", ascending=False)
    grouped = (
        frame.groupby("Hour", sort=False)
        .agg(
            **{
                "Successful runs": ("Status", lambda s: int((s == "SUCCESS").sum())),
                "Last successful run": (
                    "_successful_finished",
                    lambda s: format_thailand_timestamp(s.dropna().max()) if not s.dropna().empty else "n/a",
                ),
                "Other runs": ("Status", lambda s: int((s != "SUCCESS").sum())),
                "Latest status": ("Status", "first"),
                "Latest commit": ("Commit", "first"),
            }
        )
        .reset_index()
    )
    history = hourly.merge(grouped, on="Hour", how="left")
    history["Successful runs"] = history["Successful runs"].fillna(0).astype(int)
    history["Last successful run"] = history["Last successful run"].fillna("n/a")
    history["Other runs"] = history["Other runs"].fillna(0).astype(int)
    history["Latest status"] = history["Latest status"].fillna("NO RUN")
    history["Latest commit"] = history["Latest commit"].fillna("")
    return history


def load_scheduler_history(hours: int = 72) -> pd.DataFrame:
    try:
        request = Request(GITHUB_ACTIONS_RUNS_URL, headers={"User-Agent": "Hybrid-MR-TF-dashboard"})
        with urlopen(request, timeout=8) as response:
            payload = json.loads(response.read().decode("utf-8"))
        return _scheduler_history_from_runs(payload.get("workflow_runs", []), hours=hours)
    except Exception as exc:
        log_event(f"scheduler history API warning: {exc}")
        return pd.DataFrame(columns=["Hour", "Successful runs", "Last successful run", "Other runs", "Latest status", "Latest commit"])


def normalize_actions(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    action_cols = [c for c in ["recommended_action", "action", "decision"] if c in df.columns]
    for col in action_cols:
        df[col] = df[col].astype(str).replace({"TF_ENTRY": "NO_ACTION", "RUNNER_ENTRY": "NO_ACTION"})
    return df


@dataclass(frozen=True)
class DashboardData:
    loaded_at: str
    status_text: str
    status: dict[str, Any]
    baseline: dict[str, Any]
    registry: dict[str, Any]
    scheduler: dict[str, Any]
    observations: pd.DataFrame
    mr_candidates: pd.DataFrame
    runner_events: pd.DataFrame
    latest_scores: pd.DataFrame
    trade_plan: pd.DataFrame
    price_quality: pd.DataFrame
    market_open_completeness: pd.DataFrame
    market_open_gaps: pd.DataFrame
    current_positions: dict[str, Any]
    forward_mr_gate: pd.DataFrame
    forward_runner_comparison: pd.DataFrame
    forward_calibration: pd.DataFrame
    asset_registry: pd.DataFrame
    scheduler_history: pd.DataFrame


def load_dashboard_data() -> DashboardData:
    log_event("dashboard start")
    status_text = load_text(ROOT / "PHASE_H_STATUS.md")
    status = parse_phase_h_status(status_text)
    baseline = load_json(REPORTS / "phase_h_baseline.json")
    registry = load_json(ROOT / "models" / "registry.json")
    scheduler_health = scheduler_status(load_json(REPORTS / "phase_h_scheduler_health.json"))
    observations = normalize_actions(load_observations())
    mr_candidates = normalize_actions(load_mr_candidates())
    runner_events = normalize_actions(load_runner_events())
    latest_scores = normalize_actions(load_report_csv("latest_scores.csv"))
    return DashboardData(
        loaded_at=now_iso(),
        status_text=status_text,
        status=status,
        baseline=baseline,
        registry=registry,
        scheduler=scheduler_health,
        observations=observations,
        mr_candidates=mr_candidates,
        runner_events=runner_events,
        latest_scores=latest_scores,
        trade_plan=normalize_actions(load_report_csv("trade_plan_latest.csv")),
        price_quality=load_report_csv("price_quality.csv"),
        market_open_completeness=load_report_csv("market_open_price_completeness.csv"),
        market_open_gaps=load_report_csv("market_open_price_gaps.csv"),
        current_positions=load_json(DATA / "state" / "current_positions.json"),
        forward_mr_gate=load_report_csv("forward_mr_gate.csv"),
        forward_runner_comparison=load_report_csv("forward_runner_comparison.csv"),
        forward_calibration=load_report_csv("mr_fail_forward_calibration.csv"),
        asset_registry=load_asset_registry(),
        scheduler_history=load_scheduler_history(),
    )


def latest_observation_timestamp(data: DashboardData) -> str:
    candidates = []
    for df in [data.observations, data.latest_scores]:
        if not df.empty and "timestamp" in df.columns:
            series = pd.to_datetime(df["timestamp"], errors="coerce").dropna()
            if not series.empty:
                candidates.append(series.max())
    if not candidates:
        return "NOT YET AVAILABLE"
    return format_thailand_timestamp(max(candidates))


def latest_scheduler_run(data: DashboardData) -> str:
    value = data.scheduler.get("last_finish") or data.scheduler.get("last_successful_run") or "UNKNOWN"
    return format_thailand_timestamp(value)
