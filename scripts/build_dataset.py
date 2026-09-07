from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from hybrid_ml.config import load_config
from hybrid_ml.trades import load_all_trade_exports
from hybrid_ml.dataset import join_entry_features, feature_columns
cfg=load_config()
tr=load_all_trade_exports(ROOT/"data/trades")
print(tr.groupby(["asset","engine"]).size())
ds=join_entry_features(tr,ROOT/"data/prices",cfg).dropna(subset=["timestamp"]).copy()
ds.to_parquet(ROOT/"data/ml_dataset.parquet",index=False)
summary=ds.groupby(["asset","engine","entry_regime"],dropna=False).agg(rows=("trade_number","count"),win_rate=("is_win","mean"),avg_return_pct=("return_pct","mean"),avg_mfe_pct=("mfe_pct","mean"),avg_mae_pct=("mae_pct","mean")).reset_index()
summary.to_csv(ROOT/"reports/dataset_summary.csv",index=False)
print("dataset rows",len(ds),"features",len(feature_columns(ds)))
