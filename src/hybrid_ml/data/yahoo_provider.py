"""Yahoo Finance data provider (Phase G1).

Primary historical price source for the project. Replaces IBKR as the
planned primary source (IBKR scripts remain deprecated/optional).

Responsibilities:
- download 1H OHLCV via yfinance
- append-only merge with existing CSVs (preserve history)
- deduplicate by timestamp, sort ascending, normalize timestamps
- validate OHLC integrity (numeric, high >= low, close > 0)
- never overwrite an existing file with empty data
"""
from pathlib import Path
import pandas as pd
import yfinance as yf

REQUIRED_COLS = ["timestamp", "open", "high", "low", "close", "volume"]

# Yahoo intraday limits: 1h bars are only available for ~730 days.
YAHOO_1H_LIMIT_DAYS = 730


def normalize_ohlcv(df: "pd.DataFrame") -> "pd.DataFrame":
    """Normalize a raw OHLCV frame to canonical columns/dtypes/tz-naive UTC."""
    import pandas as pd

    x = df.copy()
    x.columns = [str(c).strip().lower().replace(" ", "_") for c in x.columns]
    if "timestamp" not in x.columns:
        for c in ["datetime", "date", "time", "index"]:
            if c in x.columns:
                x = x.rename(columns={c: "timestamp"})
                break
    if "volume" not in x.columns:
        x["volume"] = 0.0
    req = ["timestamp", "open", "high", "low", "close", "volume"]
    miss = [c for c in req if c not in x.columns]
    if miss:
        raise ValueError(f"Missing columns: {miss}")
    x["timestamp"] = pd.to_datetime(x["timestamp"], errors="coerce", utc=True).dt.tz_convert(None)
    for c in req[1:]:
        x[c] = pd.to_numeric(x[c], errors="coerce")
    return x[req].dropna(subset=req[:5]).sort_values("timestamp").drop_duplicates("timestamp")


def validate_ohlcv(df, asset=""):
    """Validate OHLC integrity. Returns (ok: bool, problems: list[str])."""
    problems = []
    if df["timestamp"].duplicated().any():
        problems.append(f"duplicate timestamps: {int(df['timestamp'].duplicated().sum())}")
    for c in ["open", "high", "low", "close"]:
        if not df[c].notna().all():
            problems.append(f"NaN values in {c}")
    bad_hl = (df["high"] < df["low"]).sum()
    if bad_hl:
        problems.append(f"{bad_hl} rows with high < low")
    nonpos = (df["close"] <= 0).sum()
    if nonpos:
        problems.append(f"{nonpos} rows with close <= 0")
    return (len(problems) == 0, problems)


def fetch_yahoo_1h(ticker: str, period: str = "730d") -> "pd.DataFrame":
    """Download 1h OHLCV from Yahoo. Returns normalized DataFrame (may be empty)."""
    import pandas as pd

    d = yf.download(ticker, period=period, interval="1h",
                    auto_adjust=False, progress=False, threads=False)
    if d is None or d.empty:
        return pd.DataFrame(columns=REQUIRED_COLS)
    if isinstance(d.columns, pd.MultiIndex):
        d.columns = [c[0] for c in d.columns]
    d = d.reset_index()
    d = d.rename(columns={d.columns[0]: "timestamp", "Open": "open", "High": "high",
                          "Low": "low", "Close": "close", "Volume": "volume"})
    if "volume" not in d.columns:
        d["volume"] = 0
    return normalize_ohlcv(d)


def fetch_yahoo_1h_range(ticker: str, start, end) -> "pd.DataFrame":
    """Download 1h OHLCV from Yahoo for an explicit UTC date/time range."""
    import pandas as pd

    d = yf.download(
        ticker,
        start=pd.Timestamp(start).to_pydatetime(),
        end=pd.Timestamp(end).to_pydatetime(),
        interval="1h",
        auto_adjust=False,
        progress=False,
        threads=False,
    )
    if d is None or d.empty:
        return pd.DataFrame(columns=REQUIRED_COLS)
    if isinstance(d.columns, pd.MultiIndex):
        d.columns = [c[0] for c in d.columns]
    d = d.reset_index()
    d = d.rename(
        columns={
            d.columns[0]: "timestamp",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume",
        }
    )
    if "volume" not in d.columns:
        d["volume"] = 0
    return normalize_ohlcv(d)


def merge_append(existing: "pd.DataFrame", new: "pd.DataFrame"):
    """Append-only merge: keep history, add new bars, dedupe, sort.

    Returns (merged_df, n_new_rows).
    """
    import pandas as pd

    if new.empty:
        return existing.copy(), 0
    combined = pd.concat([existing, new], ignore_index=True)
    combined = (combined.sort_values("timestamp")
                .drop_duplicates("timestamp", keep="last")
                .reset_index(drop=True))
    n_new = len(combined) - len(existing)
    return combined, max(0, n_new)


def update_asset_prices(asset: str, ticker: str, prices_dir: Path,
                        period: str = "730d") -> dict:
    """Download and merge new bars for one asset. Never overwrites on empty download.

    Returns summary dict with keys: asset, previous_rows, downloaded_rows,
    new_rows, final_rows, latest_timestamp, status, message.
    """
    import pandas as pd

    out_path = Path(prices_dir) / f"{asset}_1h_yahoo.csv"
    prev = None
    if out_path.exists():
        try:
            prev = normalize_ohlcv(pd.read_csv(out_path))
        except Exception as e:
            return {"asset": asset, "status": "FAIL",
                    "message": f"existing file unreadable: {e}"}

    new = fetch_yahoo_1h(ticker, period)
    if new.empty:
        return {"asset": asset, "status": "WARN",
                "message": "Yahoo returned no data; existing file preserved",
                "previous_rows": len(prev) if prev is not None else 0}

    if prev is None:
        merged, n_new = new, len(new)
    else:
        merged, n_new = merge_append(prev, new)

    ok, problems = validate_ohlcv(merged)
    if not ok:
        return {"asset": asset, "status": "FAIL",
                "message": "; ".join(problems), "previous_rows": len(prev or []),
                "downloaded_rows": len(new), "new_rows": n_new,
                "final_rows": len(merged)}

    merged.to_csv(out_path, index=False)
    return {"asset": asset, "status": "OK",
            "previous_rows": len(prev) if prev is not None else 0,
            "downloaded_rows": len(new), "new_rows": n_new,
            "final_rows": len(merged),
            "latest_timestamp": str(merged["timestamp"].iloc[-1]),
            "message": "ok" if n_new else "no new bars"}
