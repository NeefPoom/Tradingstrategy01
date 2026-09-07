# Hybrid MR-TF ML Research — VS Code Implementation Guide

# Hybrid MR-TF ML Research — VS Code Ready

This project converts your TradingView M10 exports into a machine-learning research pipeline connected to 1H historical prices.

## Core idea retained from the research

- `MR Failed` is treated as a **risk target**.
- `Runner` is treated as its own **alpha engine**.
- `TF` is modeled independently instead of assuming `TREND => TF`.
- The model may return `OFF`; it does not have to trade every asset/state.
- Asset name is not used as an ML feature by default. The model learns from market state.

## Pipeline

```text
TradingView M10 trade CSV
        +
Historical 1H OHLCV
        ↓
Entry-time feature join
        ↓
MR / Runner / TF datasets
        ↓
Win classifier + Expected-return regressor
        +
MR-failure classifier
        ↓
Latest market state
        ↓
TRADE / CAUTION / OFF
```

## Quick start

### 1) Open this folder in VS Code

### 2) Create environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3) Check the TradingView exports

```powershell
python scripts/check_trades.py
```

The six M10 CSVs from this chat are already in `data/trades/`.

### 4) Download historical 1H prices

Fast prototype:

```powershell
python scripts/download_yfinance.py
```

Or IBKR after TWS/IB Gateway is running and API access is enabled:

```powershell
python scripts/download_ibkr.py --asset GOLD --years 3
python scripts/download_ibkr.py --asset USDJPY --years 3
```

You can also drop your own `GOLD_1h.csv`, `BTCUSD_1h.csv`, etc. into `data/prices/`.

Required columns:

```text
timestamp,open,high,low,close,volume
```

### 5) Build dataset

```powershell
python scripts/build_dataset.py
```

Creates:

```text
data/ml_dataset.parquet
reports/dataset_summary.csv
```

### 6) Train

```powershell
python scripts/train_models.py
```

Creates separate models:

```text
models/mr_win_classifier.joblib
models/mr_return_regressor.joblib
models/mr_fail_classifier.joblib
models/runner_win_classifier.joblib
models/runner_return_regressor.joblib
models/tf_win_classifier.joblib
models/tf_return_regressor.joblib
```

Plus:

```text
reports/model_metrics.csv
reports/feature_importance_*.csv
```

### 7) Score current state

```powershell
python scripts/predict_latest.py --asset GOLD
python scripts/predict_latest.py --asset BTCUSD
python scripts/predict_latest.py --asset USDJPY
```

## Features

The code computes only information available at or before the trade-entry bar:

- ER 10/20/40
- ATR / NATR
- volatility ratio
- realized volatility 12/24/72
- momentum 3/6/12/24
- normalized price slopes
- causal Nadaraya-Watson oscillator
- oscillator signal
- cross density
- oscillator persistence
- price directional persistence
- candle/range structure

## Leakage protection

- Historical features are joined backward to the trade entry timestamp.
- No exit values/MFE/MAE are used as input features.
- Train/test split is chronological.
- Models are separated by MR / Runner / TF.
- `MR_FAIL` is a separate binary risk model.
- Asset name is not part of the feature vector.

## What to evaluate first

Do not judge only by accuracy. Prioritize:

1. chronological test ROC-AUC / PR-AUC;
2. Brier score/calibration;
3. expected return on selected trades;
4. whether MR-failure probability isolates large-loss states;
5. whether Runner keeps its positive expectancy;
6. portfolio drawdown after `OFF` decisions.

## Recommended development path

1. Make this static pipeline run.
2. Inspect out-of-sample metrics.
3. Add more historical periods/assets.
4. Add walk-forward retraining.
5. Switch historical source to IBKR.
6. Run model once per completed 1H bar.
7. Keep execution manual initially.
8. Only later connect signals to broker execution.

The ML is a **research/selection layer**, not a promise of future returns.


---

# Next Steps

# Next steps for VS Code

## Phase A — validate data
- Run `check_trades.py`.
- Download/import 1H OHLCV.
- Run `build_dataset.py`.
- Confirm every asset has price matches.

## Phase B — baseline ML
- Run `train_models.py`.
- Inspect `reports/model_metrics.csv`.
- Reject any engine model that is weak out of sample.

## Phase C — focus on what the research found
Priority:
1. MR failure-risk model.
2. Runner model.
3. TF model.
4. Market eligibility / OFF decision.

## Phase D — walk-forward
Use rolling train/test windows rather than one fixed split.

## Phase E — IBKR
Run the same feature engine on IBKR 1H bars and score the latest completed bar.

## Phase F — execution
Keep risk rules deterministic. ML decides engine quality; it should not freely invent stop/TP parameters.

