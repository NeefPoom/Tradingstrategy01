from pathlib import Path
import sys, pandas as pd
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from hybrid_ml.config import load_config
from hybrid_ml.dataset import feature_columns
from hybrid_ml.modeling import train
cfg=load_config(); d=pd.read_parquet(ROOT/"data/ml_dataset.parquet")
m=train(d,feature_columns(d),ROOT/"models",ROOT/"reports",cfg)
print(m.to_string(index=False))
