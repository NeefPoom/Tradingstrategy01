from pathlib import Path
import argparse, sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from hybrid_ml.config import load_config
from hybrid_ml.price_io import find_asset_price_file, load_price_csv
from hybrid_ml.features import build_features
from hybrid_ml.scoring import score_latest
ap=argparse.ArgumentParser(); ap.add_argument("--asset",required=True); a=ap.parse_args()
cfg=load_config(); asset=a.asset.upper()
p=find_asset_price_file(ROOT/"data/prices",asset)
f=build_features(load_price_csv(p),cfg).dropna()
latest=f.iloc[[-1]]
print("Asset:",asset,"Time:",latest.iloc[0]["timestamp"],"Close:",latest.iloc[0]["close"])
print("ER20:",round(latest.iloc[0].get("er_20",float("nan")),3),"NATR:",round(latest.iloc[0]["natr"],3),"VolRatio:",round(latest.iloc[0]["vol_ratio"],3),"Osc:",round(latest.iloc[0]["osc"],3))
print(score_latest(latest,ROOT/"models",cfg).to_string(index=False))
