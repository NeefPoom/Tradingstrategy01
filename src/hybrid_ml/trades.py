from pathlib import Path
import re
import pandas as pd

ASSETS = ["GOLD","USDJPY","US500","BTCUSD","ETHUSD","EURCAD"]

def infer_asset(path):
    name = Path(path).name.upper()
    for a in ASSETS:
        if a in name:
            return a
    raise ValueError(f"Cannot infer asset from {name}")

def first_col(df, prefix):
    for c in df.columns:
        if c.startswith(prefix):
            return c
    raise KeyError(prefix)

def parse_signal(signal):
    s = str(signal)
    if s.startswith("MR-L"): engine, direction = "MR", "LONG"
    elif s.startswith("MR-S"): engine, direction = "MR", "SHORT"
    elif s.startswith("TF-L"): engine, direction = "TF", "LONG"
    elif s.startswith("TF-S"): engine, direction = "TF", "SHORT"
    elif s.startswith("RUN EXIT"): engine, direction = "RUNNER", None
    elif s.startswith("MR TP1"): engine, direction = "MR_TP1", None
    elif s.startswith("MR FAIL"): engine, direction = "MR_FAIL", None
    elif s.startswith("TF EXIT"): engine, direction = "TF_EXIT", None
    else: engine, direction = "OTHER", None
    rin = re.search(r"IN:([A-Z_]+)", s)
    rout = re.search(r"OUT:([A-Z_]+)", s)
    return engine, direction, rin.group(1) if rin else None, rout.group(1) if rout else None

def load_trade_export(path):
    df = pd.read_csv(path)
    asset = infer_asset(path)
    price_col = first_col(df, "Price ")
    pnl_col = first_col(df, "Net PnL ")
    df["asset"] = asset
    df["timestamp"] = pd.to_datetime(df["Date and time"], errors="coerce")
    df["price"] = pd.to_numeric(df[price_col], errors="coerce")
    df["net_pnl"] = pd.to_numeric(df[pnl_col], errors="coerce")
    return df

def reconstruct_legs(path):
    raw = load_trade_export(path)
    rows = []
    for trade_no, g in raw.groupby("Trade number", sort=False):
        ent = g[g["Type"].str.startswith("Entry", na=False)]
        ext = g[g["Type"].str.startswith("Exit", na=False)]
        if ent.empty or ext.empty:
            continue
        e, x = ent.iloc[0], ext.iloc[0]
        e_engine, direction, entry_regime, _ = parse_signal(e["Signal"])
        x_engine, _, _, exit_regime = parse_signal(x["Signal"])

        engine = e_engine
        outcome_type = x_engine
        if x_engine == "RUNNER":
            engine = "RUNNER"
        elif x_engine in ("MR_TP1","MR_FAIL"):
            engine = "MR"
        elif x_engine == "TF_EXIT":
            engine = "TF"

        ret = float(x["Return %"])
        rows.append({
            "asset": e["asset"],
            "trade_number": int(trade_no),
            "entry_time": e["timestamp"],
            "exit_time": x["timestamp"],
            "engine": engine,
            "direction": direction,
            "entry_regime": entry_regime,
            "exit_regime": exit_regime,
            "outcome_type": outcome_type,
            "entry_price": float(e["price"]),
            "exit_price": float(x["price"]),
            "return_pct": ret,
            "net_pnl": float(x["net_pnl"]),
            "mfe_pct": float(x["Favorable excursion %"]),
            "mae_pct": float(x["Adverse excursion %"]),
            "duration_bars": int(x["Duration (bars)"]),
            "is_win": int(ret > 0),
            "is_mr_fail": int(x_engine == "MR_FAIL"),
        })
    return pd.DataFrame(rows)

def load_all_trade_exports(folder):
    frames = []
    for p in sorted(Path(folder).glob("*.csv")):
        x = reconstruct_legs(p)
        if not x.empty:
            frames.append(x)
    if not frames:
        raise FileNotFoundError("No TradingView exports found")
    return pd.concat(frames, ignore_index=True).sort_values("entry_time").reset_index(drop=True)
