import pandas as pd
from .price_io import find_asset_price_file, load_price_csv
from .features import build_features

META={"asset","trade_number","entry_time","exit_time","engine","direction","entry_regime",
      "exit_regime","outcome_type","entry_price","exit_price","return_pct","net_pnl",
      "mfe_pct","mae_pct","duration_bars","is_win","is_mr_fail","timestamp",
      "open","high","low","close","volume"}

def join_entry_features(trades, price_folder, cfg):
    frames=[]
    for asset,t in trades.groupby("asset"):
        px=load_price_csv(find_asset_price_file(price_folder,asset))
        feat=build_features(px,cfg).sort_values("timestamp")
        left=t.sort_values("entry_time").copy()
        left["entry_time"]=pd.to_datetime(left["entry_time"])
        merged=pd.merge_asof(left,feat,left_on="entry_time",right_on="timestamp",
                             direction="backward",tolerance=pd.Timedelta("2h"))
        frames.append(merged)
    return pd.concat(frames,ignore_index=True).sort_values("entry_time").reset_index(drop=True)

def feature_columns(df):
    return [c for c in df.columns if c not in META and pd.api.types.is_numeric_dtype(df[c])]
