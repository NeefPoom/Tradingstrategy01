from pathlib import Path
import pandas as pd

def normalize_ohlcv(df):
    x = df.copy()
    x.columns = [str(c).strip().lower().replace(" ", "_") for c in x.columns]
    if "timestamp" not in x.columns:
        for c in ["datetime","date","time"]:
            if c in x.columns:
                x = x.rename(columns={c:"timestamp"})
                break
    if "volume" not in x.columns:
        x["volume"] = 0.0
    req = ["timestamp","open","high","low","close","volume"]
    miss = [c for c in req if c not in x.columns]
    if miss:
        raise ValueError(f"Missing columns: {miss}")
    x["timestamp"] = pd.to_datetime(x["timestamp"], errors="coerce", utc=True).dt.tz_convert(None)
    for c in req[1:]:
        x[c] = pd.to_numeric(x[c], errors="coerce")
    return x[req].dropna(subset=req[:5]).sort_values("timestamp").drop_duplicates("timestamp")

def load_price_csv(path):
    return normalize_ohlcv(pd.read_csv(path))

def find_asset_price_file(folder, asset):
    matches = sorted(Path(folder).glob(f"{asset}*.csv"))
    if not matches:
        raise FileNotFoundError(f"No price CSV for {asset} in {folder}")
    return matches[-1]
