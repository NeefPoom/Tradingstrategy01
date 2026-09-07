"""Backfill missing open-market 1H Yahoo bars.

This script uses the session-aware gap report, fetches only gaps that are still
inside Yahoo's approximate 1H history window, and append-merges returned bars.
It never fabricates candles for gaps Yahoo does not provide.
"""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import load_config
from hybrid_ml.data.yahoo_provider import fetch_yahoo_1h_range, merge_append, normalize_ohlcv, validate_ohlcv


CHUNK_DAYS = 120


def ensure_gap_report() -> pd.DataFrame:
    gap_path = ROOT / "reports" / "market_open_price_gaps.csv"
    if not gap_path.exists():
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_market_open_completeness.py")],
            cwd=ROOT,
            check=True,
        )
    if not gap_path.exists() or gap_path.stat().st_size <= 2:
        return pd.DataFrame()
    return pd.read_csv(gap_path)


def fetch_window(ticker: str, start: pd.Timestamp, end: pd.Timestamp) -> pd.DataFrame:
    frames = []
    cursor = start
    while cursor < end:
        chunk_end = min(cursor + pd.Timedelta(days=CHUNK_DAYS), end)
        data = fetch_yahoo_1h_range(ticker, cursor, chunk_end)
        if not data.empty:
            frames.append(data)
        cursor = chunk_end
    if not frames:
        return pd.DataFrame()
    return normalize_ohlcv(pd.concat(frames, ignore_index=True))


def main() -> None:
    cfg = load_config()
    gaps = ensure_gap_report()
    if gaps.empty:
        print("No session-aware gaps found.")
        return

    recoverable = gaps[gaps["recoverable_by_yahoo_730d"].astype(str).str.lower().eq("true")].copy()
    if recoverable.empty:
        print("No gaps inside Yahoo's approximate 730-day 1H range.")
        return

    prices_dir = ROOT / "data" / "prices"
    for asset, asset_gaps in recoverable.groupby("asset", sort=False):
        ticker = cfg["assets"][asset].get("yahoo")
        if not ticker:
            print(f"{asset}: skipped, no Yahoo ticker")
            continue

        start = pd.to_datetime(asset_gaps["first_missing_open_bar_utc"]).min() - pd.Timedelta(hours=2)
        end = pd.to_datetime(asset_gaps["last_missing_open_bar_utc"]).max() + pd.Timedelta(hours=3)
        path = prices_dir / f"{asset}_1h_yahoo.csv"
        existing = normalize_ohlcv(pd.read_csv(path))
        before_rows = len(existing)
        before_missing = int(asset_gaps["missing_open_bars"].sum())

        downloaded = fetch_window(ticker, start, end)
        if downloaded.empty:
            print(f"{asset}: Yahoo returned 0 rows for {start} -> {end}")
            continue

        merged, added = merge_append(existing, downloaded)
        ok, problems = validate_ohlcv(merged, asset)
        if not ok:
            print(f"{asset}: merge rejected: {'; '.join(problems)}")
            continue

        merged.to_csv(path, index=False)
        print(
            f"{asset}: checked {before_missing} missing open bar(s), "
            f"downloaded {len(downloaded)} row(s), added {added}, rows {before_rows}->{len(merged)}"
        )


if __name__ == "__main__":
    main()
