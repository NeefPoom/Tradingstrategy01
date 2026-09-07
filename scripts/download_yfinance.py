from pathlib import Path
import sys, pandas as pd, yfinance as yf
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from hybrid_ml.config import load_config
cfg=load_config(); out=ROOT/"data/prices"; out.mkdir(exist_ok=True)
for asset,meta in cfg["assets"].items():
    ticker=meta.get("yahoo")
    if not ticker: continue
    print("Downloading",asset,ticker)
    d=yf.download(ticker,period="730d",interval="1h",auto_adjust=False,progress=False,threads=False)
    if d.empty:
        print("  no data"); continue
    if isinstance(d.columns,pd.MultiIndex): d.columns=[c[0] for c in d.columns]
    d=d.reset_index()
    d=d.rename(columns={d.columns[0]:"timestamp","Open":"open","High":"high","Low":"low","Close":"close","Volume":"volume"})
    if "volume" not in d.columns: d["volume"]=0
    d[["timestamp","open","high","low","close","volume"]].to_csv(out/f"{asset}_1h_yahoo.csv",index=False)
    print(" ",len(d),"rows")
