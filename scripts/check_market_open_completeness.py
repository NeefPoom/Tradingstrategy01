"""Session-aware hourly price completeness report.

Closed weekends, exchange breaks, and exchange holidays are excluded from the
expected bars. Missing rows are only reported when the relevant market calendar
expects an hourly bar to exist.
"""
from __future__ import annotations

from datetime import timezone
from pathlib import Path
import argparse
import json
import sys

import pandas as pd
import pandas_market_calendars as mcal

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import asset_items, load_config
from hybrid_ml.price_io import load_price_csv


YAHOO_1H_LIMIT_DAYS = 730

ASSET_CALENDARS = {
    "GOLD": "CMEGlobex_GC",
    "USDJPY": "24/5",
    "US500": "NYSE",
    "BTCUSD": "24/7",
    "ETHUSD": "24/7",
    "EURCAD": "24/5",
}

PROVIDER_OPEN_MISMATCH_ASSETS = {"GOLD", "SILVER", "WTI", "BRENT", "NATGAS"}

SPECIAL_PROVIDER_CLOSED_WINDOWS = {
    # CME Labor Day 2026 created a futures holiday session where Yahoo did not
    # publish continuous 1H bars for GC/SI/energy futures. Treat these as
    # non-actionable provider/holiday gaps, not data-collection failures.
    "CMEGlobex_GC": [
        ("2026-09-07 03:00:00", "2026-09-08 03:00:00", "CME Labor Day 2026 / Yahoo futures holiday session"),
    ],
    "CMEGlobex_Energy": [
        ("2026-09-07 03:00:00", "2026-09-08 03:00:00", "CME Labor Day 2026 / Yahoo futures holiday session"),
    ],
}


def _utc_naive_index(values) -> pd.DatetimeIndex:
    idx = pd.DatetimeIndex(pd.to_datetime(values, utc=True, errors="coerce")).dropna()
    return idx.tz_convert(None)


def _hourly_session_starts(schedule: pd.DataFrame) -> pd.DatetimeIndex:
    bars: list[pd.Timestamp] = []
    for _, row in schedule.iterrows():
        start = pd.Timestamp(row["market_open"]).tz_convert("UTC").tz_localize(None)
        end = pd.Timestamp(row["market_close"]).tz_convert("UTC").tz_localize(None)
        bars.extend(pd.date_range(start, end, freq="1h", inclusive="left"))
    return pd.DatetimeIndex(bars).drop_duplicates().sort_values()


def expected_open_bars(
    asset: str,
    first: pd.Timestamp,
    last: pd.Timestamp,
    calendar_name: str | None = None,
) -> pd.DatetimeIndex:
    calendar_name = calendar_name or ASSET_CALENDARS.get(asset, "24/5")
    if calendar_name == "24/7":
        return pd.date_range(first, last, freq="1h")
    if calendar_name == "24/5":
        expected = pd.date_range(first, last, freq="1h")
        # Yahoo spot-FX hourly bars generally trade from late Sunday through
        # Friday 20:00 UTC. Weekend tails are broker/source-closed, not gaps.
        open_mask = (
            (expected.dayofweek < 4)
            | ((expected.dayofweek == 4) & (expected.hour < 21))
            | ((expected.dayofweek == 6) & (expected.hour >= 23))
        )
        return expected[open_mask]

    calendar = mcal.get_calendar(calendar_name)
    # Include the prior date because Globex sessions can open on the prior UTC day.
    start_date = (first - pd.Timedelta(days=1)).date()
    end_date = (last + pd.Timedelta(days=1)).date()
    schedule = calendar.schedule(start_date=start_date, end_date=end_date)
    expected = _hourly_session_starts(schedule)
    return expected[(expected >= first) & (expected <= last)]


def non_actionable_missing(asset: str, missing: pd.DatetimeIndex, observed: pd.DatetimeIndex) -> pd.DatetimeIndex:
    if asset not in PROVIDER_OPEN_MISMATCH_ASSETS or missing.empty or observed.empty:
        return pd.DatetimeIndex([])
    ignored = []
    for ts in missing:
        next_obs = observed[observed > ts]
        if next_obs.empty:
            continue
        gap_hours = (next_obs[0] - ts).total_seconds() / 3600
        prev_obs = observed[observed < ts]
        prev_gap = (ts - prev_obs[-1]).total_seconds() / 3600 if not prev_obs.empty else 0
        if ts.dayofweek == 6 and ts.hour >= 22 and gap_hours <= 5 and prev_gap > 24:
            ignored.append(ts)
        elif ts.dayofweek == 0 and ts.hour <= 1 and gap_hours <= 2 and prev_gap > 24:
            ignored.append(ts)
    return pd.DatetimeIndex(ignored)


def special_provider_closed_missing(calendar_name: str, missing: pd.DatetimeIndex) -> pd.DatetimeIndex:
    if missing.empty:
        return pd.DatetimeIndex([])
    ignored = []
    for start_raw, end_raw, _reason in SPECIAL_PROVIDER_CLOSED_WINDOWS.get(calendar_name, []):
        start = pd.Timestamp(start_raw)
        end = pd.Timestamp(end_raw)
        ignored.extend(missing[(missing >= start) & (missing <= end)].tolist())
    return pd.DatetimeIndex(ignored).drop_duplicates().sort_values()


def phase_h_start_floor() -> pd.Timestamp | None:
    baseline_path = ROOT / "reports" / "phase_h_baseline.json"
    if not baseline_path.exists():
        return None
    try:
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
        raw = baseline.get("phase_h_start")
        if not raw:
            return None
        ts = pd.Timestamp(raw)
        if getattr(ts, "tzinfo", None) is not None:
            ts = ts.tz_convert(None)
        return ts.floor("h")
    except Exception:
        return None


def summarize_asset(
    asset: str,
    price_path: Path,
    now: pd.Timestamp,
    report_start: pd.Timestamp | None,
    calendar_name: str | None = None,
) -> tuple[dict, pd.DataFrame]:
    prices = load_price_csv(price_path)
    prices = prices.sort_values("timestamp").reset_index(drop=True)
    observed = _utc_naive_index(prices["timestamp"])
    first = observed.min()
    last = observed.max()
    effective_start = max(first, report_start) if report_start is not None else first
    calendar_name = calendar_name or ASSET_CALENDARS.get(asset, "24/5")
    expected = expected_open_bars(asset, effective_start, last, calendar_name)
    raw_missing = expected.difference(observed)
    ignored_missing = non_actionable_missing(asset, raw_missing, observed)
    special_ignored = special_provider_closed_missing(calendar_name, raw_missing)
    ignored_missing = ignored_missing.union(special_ignored)
    missing = raw_missing.difference(ignored_missing)
    recoverable_cutoff = now - pd.Timedelta(days=YAHOO_1H_LIMIT_DAYS)
    recoverable = missing[missing >= recoverable_cutoff]
    older = missing[missing < recoverable_cutoff]

    gap_rows = []
    if len(missing):
        groups = pd.Series(missing).diff().ne(pd.Timedelta(hours=1)).cumsum()
        for _, group in pd.Series(missing).groupby(groups):
            gap_rows.append(
                {
                    "asset": asset,
                    "first_missing_open_bar_utc": group.iloc[0],
                    "last_missing_open_bar_utc": group.iloc[-1],
                    "missing_open_bars": len(group),
                    "recoverable_by_yahoo_730d": bool(group.iloc[-1] >= recoverable_cutoff),
                    "calendar": calendar_name,
                }
            )

    summary = {
        "asset": asset,
        "calendar": calendar_name,
        "rows": len(prices),
        "first_timestamp_utc": first,
        "last_timestamp_utc": last,
        "report_start_timestamp_utc": effective_start,
        "expected_open_bars": len(expected),
        "missing_open_bars": len(missing),
        "raw_calendar_missing_open_bars": len(raw_missing),
        "ignored_provider_calendar_mismatch": len(ignored_missing),
        "missing_recoverable_by_yahoo_730d": len(recoverable),
        "missing_requires_alt_provider_or_archive": len(older),
        "open_session_coverage_pct": round((len(expected) - len(missing)) / len(expected) * 100, 2)
        if len(expected)
        else 0.0,
        "duplicate_timestamps": int(prices["timestamp"].duplicated().sum()),
        "nan_ohlc_rows": int(prices[["open", "high", "low", "close"]].isna().any(axis=1).sum()),
        "status": "PASS" if len(missing) == 0 else "MISSING_OPEN_BARS",
    }
    return summary, pd.DataFrame(gap_rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--full-history",
        action="store_true",
        help="Check from the first historical row instead of the Phase H start timestamp.",
    )
    args = parser.parse_args()

    cfg = load_config()
    prices_dir = ROOT / "data" / "prices"
    now = pd.Timestamp.now(tz=timezone.utc).tz_convert(None)
    report_start = None if args.full_history else phase_h_start_floor()
    summaries = []
    gaps = []

    for asset, meta in asset_items(cfg, data_collection=True):
        path = prices_dir / f"{asset}_1h_yahoo.csv"
        if not path.exists():
            summaries.append({"asset": asset, "status": "FAIL", "reason": "missing price file"})
            continue
        summary, asset_gaps = summarize_asset(asset, path, now, report_start, meta.get("calendar"))
        summaries.append(summary)
        if not asset_gaps.empty:
            gaps.append(asset_gaps)
        print(
            f"{asset}: {summary['status']} "
            f"missing_open={summary['missing_open_bars']} "
            f"recoverable_yahoo={summary['missing_recoverable_by_yahoo_730d']} "
            f"coverage={summary['open_session_coverage_pct']}% "
            f"calendar={summary['calendar']}"
        )

    summary_df = pd.DataFrame(summaries)
    gaps_df = pd.concat(gaps, ignore_index=True) if gaps else pd.DataFrame()
    summary_path = ROOT / "reports" / "market_open_price_completeness.csv"
    gaps_path = ROOT / "reports" / "market_open_price_gaps.csv"
    summary_df.to_csv(summary_path, index=False)
    gaps_df.to_csv(gaps_path, index=False)
    print(f"\nSaved {summary_path}")
    print(f"Saved {gaps_path}")


if __name__ == "__main__":
    main()
