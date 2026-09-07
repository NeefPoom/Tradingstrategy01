from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from hybrid_ml.trades import load_all_trade_exports
d=load_all_trade_exports(ROOT/"data/trades")
print(d.groupby(["asset","engine","outcome_type"]).agg(n=("trade_number","count"),win_rate=("is_win","mean"),avg_return=("return_pct","mean"),avg_mfe=("mfe_pct","mean"),avg_mae=("mae_pct","mean")).round(4).to_string())
