"""Price data quality report.

Checks every data/prices/{ASSET}_1h_yahoo.csv for duplicates, missing bars,
zero volume, bad OHLC, and bar-gap statistics.
"""
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import asset_items, load_config
from hybrid_ml.price_io import load_price_csv

from check_market_open_completeness import expected_open_bars, non_actionable_missing, phase_h_start_floor


def _utc_naive_index(values) -> pd.DatetimeIndex:
    idx = pd.DatetimeIndex(pd.to_datetime(values, utc=True, errors="coerce")).dropna()
    return idx.tz_convert(None)


def quality_metrics(
    df: pd.DataFrame,
    asset: str | None = None,
    calendar_name: str | None = None,
    report_start: pd.Timestamp | None = None,
) -> dict:
    """Compute quality metrics for one normalized OHLCV frame."""
    x = df.sort_values("timestamp").reset_index(drop=True)
    n = len(x)
    dup = int(x["timestamp"].duplicated().sum())
    gaps = x["timestamp"].diff().dt.total_seconds().div(3600).dropna()
    if asset and n:
        observed = _utc_naive_index(x["timestamp"])
        effective_start = max(observed.min(), report_start) if report_start is not None else observed.min()
        expected = expected_open_bars(asset, effective_start, observed.max(), calendar_name)
        raw_missing = expected.difference(observed)
        ignored = non_actionable_missing(asset, raw_missing, observed)
        missing = len(raw_missing.difference(ignored))
    else:
        missing = int((gaps > 1.5).sum())
    bad_ohlc = int(
        (
            (x["high"] < x["low"])
            | (x["close"] <= 0)
            | x[["open", "high", "low", "close"]].isna().any(axis=1)
        ).sum()
    )
    max_gap = float(gaps.max()) if len(gaps) else 0.0
    med_gap = float(gaps.median()) if len(gaps) else 0.0

    if n == 0 or bad_ohlc > 0 or dup > 0:
        status = "FAIL"
    elif missing > max(10, n * 0.05):
        status = "WARNING"
    else:
        status = "PASS"

    return {
        "rows": n,
        "first_timestamp": str(x["timestamp"].iloc[0]) if n else "",
        "last_timestamp": str(x["timestamp"].iloc[-1]) if n else "",
        "duplicate_count": dup,
        "missing_bar_estimate": missing,
        "zero_volume_count": int((x["volume"] == 0).sum()),
        "bad_ohlc_count": bad_ohlc,
        "median_bar_gap_hours": round(med_gap, 3),
        "max_bar_gap_hours": round(max_gap, 2),
        "status": status,
    }


def main() -> None:
    cfg = load_config()
    report_start = phase_h_start_floor()
    prices = ROOT / "data" / "prices"
    rows = []
    for asset, meta in asset_items(cfg, data_collection=True):
        matches = sorted(prices.glob(f"{asset}_1h_yahoo.csv"))
        if not matches:
            rows.append({"asset": asset, "rows": 0, "status": "FAIL"})
            print(f"{asset}: NO PRICE FILE")
            continue
        try:
            df = load_price_csv(matches[-1])
        except Exception as exc:
            rows.append({"asset": asset, "rows": 0, "status": "FAIL"})
            print(f"{asset}: unreadable - {exc}")
            continue
        m = quality_metrics(df, asset, meta.get("calendar"), report_start)
        m["asset"] = asset
        rows.append(m)
        print(
            f"{asset}: {m['rows']} rows  {m['first_timestamp']} -> {m['last_timestamp']}  "
            f"dup={m['duplicate_count']} missing~{m['missing_bar_estimate']} "
            f"badOHLC={m['bad_ohlc_count']} maxGap={m['max_bar_gap_hours']}h  -> {m['status']}"
        )

    out = pd.DataFrame(rows)
    out.to_csv(ROOT / "reports" / "price_quality.csv", index=False)
    print(f"\nSaved reports/price_quality.csv ({len(out)} assets)")


if __name__ == "__main__":
    main()
