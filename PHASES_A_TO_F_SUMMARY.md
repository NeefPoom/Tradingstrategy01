# Hybrid MR-TF ML — Phase A–F Execution Summary

**Date:** 2026-08-30
**Project:** `E:\hybrid_mr_tf_ml_rading`
**Status:** All phases complete. Pipeline operational end-to-end.

---

## Phase A — Data Validation ✅

**Environment setup:**
- Installed Python 3.12 (winget) → `.venv` created
- Installed `requirements.txt` (pandas 3.0.5, numpy 2.5.2, scikit-learn 1.9, yfinance 1.7, etc.)

**Trade validation (`scripts/check_trades.py`):**

| Asset | MR TP1 (n, win%) | MR Fail (n, avg ret) | Runner (n, win%) | TF (n) |
|---|---|---|---|---|
| BTCUSD | 73, 93.2% | 57, −1.98% | 73, 69.9% | 4 |
| ETHUSD | 147, 83.7% | 91, −2.73% | 147, 61.9% | 12 |
| EURCAD | 104, 84.6% | 78, −0.27% | 103, 57.3% | 5 |
| GOLD | 145, 89.7% | 108, −0.84% | 145, 69.0% | 12 |
| US500 | 135, 87.4% | 111, −0.61% | 135, 68.2% | 6 |
| USDJPY | 91, 90.1% | 68, −0.35% | 91, 67.0% | 7 |

**Prices:** 6 × 1H Yahoo CSVs downloaded (5K–17.5K rows each) → `data/prices/`

**Dataset (`scripts/build_dataset.py`):** 1,680 rows × 34 features → `data/ml_dataset.parquet`
- MR: 1,035 rows | RUNNER: 604 | TF: 41 (too thin)

---

## Phase B — Baseline ML ✅

**Fix applied:** sklearn 1.9 removed `loss="huber"` from `HistGradientBoostingRegressor` → changed to `loss="absolute_error"` in `src/hybrid_ml/modeling.py`.

**Out-of-sample test metrics (`reports/model_metrics.csv`):**

| Engine | Rows | ROC-AUC | PR-AUC | Brier | Verdict |
|---|---|---|---|---|---|
| MR win | 1035 | 0.665 | 0.695 | 0.240 | Decent signal |
| RUNNER win | 604 | 0.602 | 0.729 | 0.238 | Positive expectancy holds |
| TF win | 41 | 0.500 | 0.375 | 0.243 | **No signal — rejected** |
| **MR_FAIL risk** | 1035 | **0.770** | 0.678 | 0.196 | **Best model** |

---

## Phase C — Research Priorities ✅

| Priority | Result |
|---|---|
| 1. MR failure-risk model | ✅ ROC-AUC 0.770 — isolates large-loss states |
| 2. Runner model | ✅ Keeps positive expectancy OOS (+0.91% actual vs +0.51% pred) |
| 3. TF model | ❌ Rejected — 41 rows, ROC-AUC 0.500. Stays OFF permanently |
| 4. OFF decision | ✅ Working — 5/6 assets OFF, MR blocked when fail-risk high |

---

## Phase D — Walk-Forward Validation ✅

**Script:** `scripts/walk_forward.py` (5 expanding-window folds, chronological)
**Output:** `reports/walk_forward_metrics.csv`

| Engine / Target | Mean ROC-AUC | PR-AUC | Brier | Verdict |
|---|---|---|---|---|
| **MR fail risk** | **0.743** | 0.658 | 0.212 | ✅ Robust — never below 0.70 in any fold |
| MR win | 0.686 | 0.709 | 0.238 | ✅ Holds up |
| RUNNER win | 0.632 | 0.757 | 0.240 | ✅ Acceptable |
| RUNNER return | MAE 1.24 | — | — | ✅ Positive in ALL 5 folds (+0.70% to +1.29%) |
| MR return | MAE 1.10 | — | — | ⚠️ Conservative filter, not forecaster |

**Key findings:**
- MR_FAIL model stable across all folds (0.70–0.77) — most trustworthy model
- Runner alpha engine thesis holds out-of-sample across time
- No fold collapse — models not overfit to one regime

---

## Phase E — Latest-Bar Scoring ✅

**Script:** `scripts/score_all_latest.py` (Yahoo as live proxy; IBKR-ready — `download_ibkr.py` output auto-prioritized when TWS/Gateway available)

**Latest signals (2026-08-28/30 bars):**

| Asset | MR | Runner | Portfolio |
|---|---|---|---|
| GOLD | OFF (fail 0.77) | **TRADE** (p 0.71, +1.42%) | RUNNER |
| USDJPY | OFF (fail 0.53) | **TRADE** (p 0.68, +0.29%) | RUNNER |
| ETHUSD | OFF | **TRADE** (p 0.58, +0.10%) | RUNNER |
| US500 | OFF | OFF | OFF |
| BTCUSD | OFF | OFF | OFF |
| EURCAD | OFF (fail 0.67) | OFF | OFF |

---

## Phase F — Execution (Manual) ✅

**Script:** `scripts/make_trade_plan.py` — deterministic trade-plan generator, no broker connection.

**Deterministic risk rules:**
- Stop = 1.5 × ATR(14)
- MR TP = 1.0 × ATR (TP1) | Runner TP = 2.0 × ATR
- Risk = 0.5% of equity ($50 per trade on $10,000)
- Direction: MR fades oscillator extremes; Runner follows osc/signal momentum
- TF hard-excluded; MR gated by p_mr_fail ≤ 0.45

**Current plan (`reports/trade_plan_latest.csv`):**

| Engine | Asset | Dir | Entry | Stop | TP | Size | p_win | E[r] |
|---|---|---|---|---|---|---|---|---|
| RUNNER | GOLD | SHORT | 4529.90 | 4572.04 | 4473.71 | 1.19 | 0.708 | +1.42% |
| RUNNER | USDJPY | LONG | 160.038 | 159.838 | 160.304 | 250.3 | 0.68 | +0.29% |
| RUNNER | ETHUSD | LONG | 2453.23 | 2441.36 | 2469.05 | 4.21 | 0.58 | +0.10% |

---

## Daily Operating Loop

```powershell
# 1. Refresh prices
python scripts/download_yfinance.py

# 2. Score latest completed 1H bar (all assets)
python scripts/score_all_latest.py

# 3. Generate trade plan (manual execution)
python scripts/make_trade_plan.py
```

**Periodic:** re-run `build_dataset.py` + `train_models.py` when new TradingView exports arrive; re-run `walk_forward.py` to confirm stability.

---

## Key Conclusions

1. **MR_FAIL is the primary gate** (ROC-AUC 0.743 walk-forward) — blocks MR trades in high-risk states
2. **Runner is the alpha engine** — positive expectancy in every walk-forward fold
3. **TF stays OFF** — insufficient data (41 rows)
4. **System is selective** — mostly OFF; only trades when expectancy is positive and fail-risk is low
5. **ETHUSD Runner signal is marginal** (E[r] +0.10%) — consider raising `min_expected_return_pct` to 0.10 in `config.yaml`

## Next Steps (beyond Phase F)

- Add more historical periods/assets to strengthen TF and MR models
- Walk-forward retraining on a schedule
- Switch to IBKR data when TWS/Gateway available (`download_ibkr.py` ready)
- Only later: connect signals to broker execution

> The ML is a **research/selection layer**, not a promise of future returns.
