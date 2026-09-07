# Hybrid MR-TF ML Research — VS Code Ready

This project converts your TradingView M10 exports into a machine-learning research pipeline connected to 1H historical prices.

## Phase H — Frozen Forward Validation

Phase H freezes the Phase A–G research architecture and observes it prospectively on new 1H Yahoo data. **Research/paper observation only — no broker execution.**

### Why models are frozen
Forward validation requires an unchanged experiment. Models (`models/*.joblib`) are hash-frozen in `reports/phase_h_baseline.json` (version **H1.0**). Any hash change prints `WARNING: PHASE H MODEL FREEZE VIOLATION`. Retraining would start a NEW experiment version (`H1.1`, `H2.0`) — never silently replace the frozen model.

### Yahoo Finance workflow
Yahoo Finance is the only active price source (IBKR deprecated). `scripts/update_prices.py` appends new bars, never erases history, and validates OHLC. Yahoo's ~730-day 1H intraday limit means no silent backfill.

### Why TF is OFF
TF has only ~41 training samples and ROC-AUC ≈ 0.50. It stays disabled for the entire Phase H window.

### Why Runner cannot enter from flat
Runner is a **position-management state**, not an entry engine. Lifecycle: `MR ENTRY → TP1 → partial profit → RUNNER → HOLD/EXIT`. If state is FLAT, Runner model output is informational only.

### Why US500 is research-only
Leave-one-asset-out MR_FAIL ROC-AUC for US500 was 0.487 (Phase G) — poor cross-asset generalization. US500 MR signals are logged but never actionable.

### How forward outcome resolution works
Observations are written with outcome fields as NA. Later, `resolve_forward_outcomes.py` fills future returns and hypothetical MR outcomes (including **counterfactuals for blocked candidates**) once the future price path exists. This prevents leakage and lets us measure both true-block and false-block rates.

### Daily loop
```powershell
python scripts/run_phase_h.py        # full orchestrator (recommended)
# or individually:
python scripts/update_prices.py
python scripts/check_price_quality.py
python scripts/score_all_latest.py
python scripts/resolve_forward_outcomes.py
python scripts/make_trade_plan.py
python scripts/forward_status.py
```

### Inspecting reports
- `reports/latest_scores.csv` — per-asset evidence + recommended action
- `reports/trade_plan_latest.csv` — paper entries (MR_ELIGIBLE only, MANUAL_STOP_REQUIRED)
- `reports/forward_mr_gate.csv` / `forward_mr_gate_summary.md` — gate counterfactuals
- `reports/forward_runner_comparison.csv` — OSC_CROSS vs HYBRID
- `reports/mr_fail_forward_calibration.csv` — forward calibration vs Phase G baseline
- `PHASE_H_STATUS.md` — overall decision

### Stopping / restarting safely
All forward stores are append-only with deterministic IDs (`ASSET_timestamp`). Scripts are safe to re-run — duplicates are skipped (`SKIP — already scored`). To stop: just stop running the loop. To restart: run `run_phase_h.py` again; the freeze check confirms the same experiment continues. Retraining requires a NEW model version (`models/registry.json`) and must never silently replace H1.0.

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

## Phase H Dashboard

Launch the local read-only Phase H research dashboard with:

```powershell
streamlit run dashboard/app.py --server.address 127.0.0.1
```

or:

```powershell
run_phase_h_dashboard.bat
```

The dashboard does not auto-refresh. Press **Refresh Data** to load newly collected Phase H data. It does not train models, run Phase H, edit thresholds, place broker orders, enable TF, or create Runner standalone entries.

## Phase H Scheduler

Install the local Windows hourly scheduler with:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\install_phase_h_scheduler.ps1
```

The task name is `Hybrid MR-TF Phase H`. It runs once per hour at minute `05` using `.venv\Scripts\python.exe` and logs to `logs\phase_h_scheduler.log`. Check status with:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\check_phase_h_scheduler.ps1
```

Uninstall with:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\uninstall_phase_h_scheduler.ps1
```
