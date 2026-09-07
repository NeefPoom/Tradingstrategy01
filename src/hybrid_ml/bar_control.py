"""Completed 1H bar control for Phase H.

The system scores only completed 1H bars. Price timestamps are normalized to
UTC-naive values, so wall-clock comparisons must also use UTC-naive time.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

ALWAYS_OPEN = {"BTCUSD", "ETHUSD"}
STALE_HOURS = 72.0


def utc_now_naive() -> pd.Timestamp:
    """Current UTC time without tzinfo, matching normalized price files."""
    return pd.Timestamp.now(tz=timezone.utc).tz_convert(None)


def normalize_current_time(current_time=None) -> pd.Timestamp:
    """Convert an optional timestamp to UTC-naive for price-time comparison."""
    now = pd.Timestamp(current_time) if current_time is not None else utc_now_naive()
    if getattr(now, "tzinfo", None) is not None:
        now = now.tz_convert(None)
    return now


def completed_bars(df: pd.DataFrame, current_time=None) -> pd.DataFrame:
    """Return rows whose 1H candle has fully closed."""
    x = df.sort_values("timestamp").reset_index(drop=True).copy()
    if x.empty:
        return x
    now = normalize_current_time(current_time)
    ts = pd.to_datetime(x["timestamp"], errors="coerce")
    return x[(ts + pd.Timedelta(hours=1)) <= now].copy()


def bar_meta(asset: str, timestamp, current_time=None, status: str | None = None) -> dict:
    """Build freshness metadata for a selected completed bar."""
    now = normalize_current_time(current_time)
    ts = pd.Timestamp(timestamp)
    age_hours = (now - ts).total_seconds() / 3600.0
    computed_status = status or ("STALE_DATA" if age_hours > STALE_HOURS else "OK")
    return {
        "asset": asset,
        "source_bar_timestamp": str(ts),
        "scored_at": datetime.now(timezone.utc).isoformat(),
        "bar_age_minutes": round((now - ts).total_seconds() / 60.0, 1),
        "is_completed_bar": True,
        "data_source": "yahoo",
        "status": computed_status,
        "bar_age_hours": round(age_hours, 2),
    }


def get_latest_completed_bar(df, asset: str, current_time=None) -> dict:
    """Identify the latest fully completed 1H bar for an asset."""
    x = completed_bars(df, current_time=current_time)
    if x.empty:
        return {"is_completed": False, "reason": "NO_COMPLETED_BAR", "row": None}

    last = x.iloc[-1]
    meta = bar_meta(asset, last["timestamp"], current_time=current_time)
    return {"is_completed": True, "row": last, "meta": meta}


def observation_id(asset: str, timestamp) -> str:
    """Deterministic observation ID: ASSET + ISO timestamp."""
    return f"{asset}_{pd.Timestamp(timestamp).isoformat()}"


def is_stale(meta: dict) -> bool:
    return meta.get("status") == "STALE_DATA"
