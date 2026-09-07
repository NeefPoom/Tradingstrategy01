from pathlib import Path
import argparse, sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from hybrid_ml.config import load_config
from ib_async import IB, Forex, Index, Crypto, Contract
import pandas as pd

def make_contract(m):
    sec=m["secType"].upper()
    if sec=="CASH": return Forex(m["symbol"]+m["currency"],exchange=m["exchange"])
    if sec=="IND": return Index(m["symbol"],m["exchange"],m["currency"])
    if sec=="CRYPTO": return Crypto(m["symbol"],m["exchange"],m["currency"])
    c=Contract(); c.secType=sec; c.symbol=m["symbol"]; c.exchange=m["exchange"]; c.currency=m["currency"]; return c

ap=argparse.ArgumentParser()
ap.add_argument("--asset",required=True); ap.add_argument("--years",type=int,default=3)
ap.add_argument("--host",default="127.0.0.1"); ap.add_argument("--port",type=int,default=7497); ap.add_argument("--client-id",type=int,default=17)
a=ap.parse_args(); cfg=load_config(); asset=a.asset.upper()
m=cfg["assets"][asset]["ibkr"]; ib=IB(); ib.connect(a.host,a.port,clientId=a.client_id)
try:
    con=make_contract(m); q=ib.qualifyContracts(con)
    if not q: raise RuntimeError("Could not qualify contract; edit config.yaml")
    con=q[0]
    bars=ib.reqHistoricalData(con,endDateTime="",durationStr=f"{a.years} Y",barSizeSetting="1 hour",
        whatToShow="MIDPOINT" if con.secType=="CASH" else "TRADES",useRTH=False,formatDate=1,keepUpToDate=False)
    d=pd.DataFrame([{"timestamp":b.date,"open":b.open,"high":b.high,"low":b.low,"close":b.close,"volume":getattr(b,"volume",0)} for b in bars])
    out=ROOT/"data/prices"/f"{asset}_1h_ibkr.csv"; d.to_csv(out,index=False); print("saved",len(d),"rows to",out)
finally:
    ib.disconnect()
