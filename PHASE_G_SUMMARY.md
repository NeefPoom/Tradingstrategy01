# Phase G Summary — Production Research Hardening

**Date:** 2026-08-30
**Project:** `E:\hybrid_mr_tf_ml_rading`
**Architecture change:** Yahoo Finance is now the primary data source. IBKR deprecated/optional. No broker connection. Manual execution only.

---

## Files Changed / Created

### Created (Phase G)
| File | Purpose |
|---|---|
| `src/hybrid_ml/data/yahoo_provider.py` | Reusable Yahoo data module (append-only merge, validation) |
| `src/hybrid_ml/data/__init__.py` | Data package |
| `src/hybrid_ml/positions.py` | Position state management (G3) |
| `data/state/current_positions.json` | Position state file (FLAT default) |
| `scripts/update_prices.py` | G1: incremental Yahoo refresh |
| `scripts/check_price_quality.py` | G2: price quality report |
| `scripts/threshold_research.py` | G4: MR_FAIL threshold research |
| `scripts/calibration_research.py` | G5: probability calibration |
| `scripts/asset_holdout.py` | G6: leave-one-asset-out validation |
| `scripts/runner_exit_research.py` | G7: Runner exit A/B/C |
| `PHASE_G_SUMMARY.md` | This file |

### Modified
- `scripts/score_all_latest.py` — G8: evidence output + state-aware actions → `latest_scores.csv`
- `scripts/make_trade_plan.py` — G9: state-driven actions, no Runner/TF entry, MANUAL_STOP_REQUIRED flag

### Deprecated (kept, not deleted)
- `scripts/download_ibkr.py` — optional, requires TWS/IB Gateway; not in active flow
- Old versions of rewritten scripts backed up in `reports/_old_*.bak`

### Preserved (unchanged)
- `scripts/check_trades.py`, `build_dataset.py`, `train_models.py`, `walk_forward.py`, `predict_latest.py`
- `src/hybrid_ml/` core modules (config, dataset, features, modeling, price_io, scoring, trades)
- All Phase A–F research conclusions

---

## Yahoo Finance Data Status (per asset)

| Asset | Ticker | Rows | Coverage | Latest bar |
|---|---|---|---|---|
| GOLD | GC=F | 13,736 | 2024-04 → 2026-08-28 | 2026-08-28 20:00 |
| USDJPY | JPY=X | 17,144 | 2023-11 → 2026-08 | 2026-08-28 20:00 |
| US500 | ^GSPC | 5,073 | 2023-10 → 2026-08 | 2026-08-28 19:30 |
| BTCUSD | BTC-USD | 17,474 | 2024-08 → 2026-08 | 2026-08-30 10:00 |
| ETHUSD | ETH-USD | 17,471 | 2024-08 → 2026-08 | 2026-08-30 10:00 |
| EURCAD | EURCAD=X | 17,264 | 2023-11 → 2026-08 | 2026-08-28 22:00 |

**Yahoo intraday limit:** 1h bars limited to ~730 days. GOLD (13.7K rows) and US500 (5.1K rows) have shorter history than FX/crypto (~17K). This is a Yahoo platform limit — reported, not silently filled.

---

## Price Quality Findings (`reports/price_quality.csv`)

| Asset | Rows | Duplicates | Bad OHLC | Missing~ | Max Gap | Status |
|---|---|---|---|---|---|---|
| GOLD | 13,736 | 0 | 0 | 619 | 80h | WARNING (weekend gaps) |
| USDJPY | 17,144 | 0 | 0 | 155 | 77h | WARNING (weekend gaps) |
| US500 | 5,073 | 0 | 0 | 729 | 94h | WARNING (session breaks) |
| BTCUSD | 17,474 | 0 | 0 | 4 | 21h | **PASS** |
| ETHUSD | 17,471 | 0 | 0 | 6 | 21h | **PASS** |
| EURCAD | 17,264 | 0 | 0 | 156 | 76h | WARNING (weekend gaps) |

**Interpretation:** WARNINGs for FX/futures/index are expected — they reflect weekends and session breaks, not data corruption. Zero bad OHLC, zero duplicates across all assets. Crypto (24/7) is cleanest. The `missing_bar_estimate` counts session gaps; this is expected for non-24/7 markets.

---

## MR_FAIL Threshold Research (G4)

Out-of-sample walk-forward predictions, 885 MR candidates. Keep MR trade if `p_mr_fail <= threshold`:

| Threshold | Kept | Win rate | Avg ret | PF | Max DD |
|---|---|---|---|---|---|
| 0.25 | 37.9% | 0.681 | +0.335% | 1.676 | −0.26 |
| 0.30 | 43.6% | 0.674 | 0.290 | 1.583 | 0.00 |
| 0.35 | 47.7% | 0.659 | 0.263 | 1.508 | 0.00 |
| **0.40** | 52.8% | 0.642 | 0.267 | 1.529 | −1.37 |
| **0.45 (current)** | 56.7% | 0.634 | 0.250 | 1.483 | −1.91 |
| 0.50 | 61.1% | 0.625 | 0.203 | 1.380 | −2.06 |
| 0.55 | 65.8% | 0.612 | 0.200 | 1.374 | −6.21 |
| 0.65 | 75.3% | 0.589 | 0.181 | 1.347 | −9.67 |

**Findings:**
- Broad stable plateau: **0.25–0.45** — PF stays 1.48–1.68, win rate 0.63–0.68, drawdowns small
- Best single value 0.25 (PF 1.676) but only keeps 38% of trades
- **Recommended research threshold: 0.40–0.45** (current production 0.45 sits inside the plateau — no change needed)
- Thresholds > 0.55 degrade drawdown sharply (−6 to −10)

**Production threshold NOT changed** (per instructions).

---

## Calibration Results (G5)

| Model | Brier | ECE | ROC-AUC |
|---|---|---|---|
| **raw** | **0.2117** | **0.0982** | 0.7401 |
| isotonic | 0.2840 | 0.2647 | 0.7148 |
| sigmoid | 0.2386 | 0.1780 | 0.7401 |

**Verdict: keep the raw model.** Isotonic calibration made things worse (higher Brier, lower AUC). Sigmoid matched raw discrimination but with worse calibration. The raw model is already reasonably calibrated (ECE 0.098); slight over-confidence at high probabilities (predicts 0.85, actual 0.69) — acceptable for a gate.

---

## Asset Holdout (G6 — Leave-One-Asset-Out)

MR_FAIL model tested on each unseen asset:

| Held-out | MR win AUC | MR_FAIL AUC | Runner win AUC |
|---|---|---|---|
| GOLD | 0.711 | 0.752 | 0.613 |
| USDJPY | 0.747 | 0.831 | 0.672 |
| US500 | 0.548 | **0.487** | 0.566 |
| BTCUSD | 0.793 | 0.814 | 0.795 |
| ETHUSD | 0.719 | 0.778 | 0.686 |
| EURCAD | 0.758 | 0.854 | 0.727 |

**Answer to the research question:** the models learn **market-state structure, not asset memorization** — 5 of 6 held-out assets show strong MR_FAIL performance (0.75–0.85) with zero asset identity features. **Exception: US500** degrades badly OOS (MR_FAIL 0.487, MR win 0.548) — its market state behaves differently from the other five. This is a genuine finding: US500 MR signals may need asset-specific treatment or exclusion.

---

## Runner Exit A/B/C Results (G7)

Pooled cross-asset (604 runner trades):

| Method | Win rate | Avg ret | Median | PF | Max DD | Avg bars |
|---|---|---|---|---|---|---|
| A — Fixed 2 ATR | 0.397 | **−0.206%** | −0.227 | 0.663 | 136.5 | 8.8 |
| B — Osc cross | 0.545 | +0.114% | 0.150 | 1.210 | 47.7 | 19.7 |
| **C — Hybrid** | 0.545 | **+0.119%** | 0.180 | **1.259** | **32.3** | 19.7 |

**Findings:**
- **Fixed 2 ATR (A) is clearly worst** — negative expectancy pooled (−0.21%), PF 0.66. The current production assumption of a fixed 2 ATR Runner TP is NOT supported.
- **Oscillator cross (B)** — positive, matches the original TradingView logic.
- **Hybrid (C)** — best PF (1.26), lowest drawdown (32 vs 48), same win rate as B. Slightly better than B on every pooled metric.
- Per-asset: B/C positive on BTCUSD, ETHUSD, GOLD, US500; negative on EURCAD, USDJPY (low-vol FX — oscillator exits too slow).
- **Live Runner exit NOT changed** — research only, pending review.

---

## Model Degradation Check

Re-ran full training + walk-forward after all changes — **no degradation**:
- MR_FAIL: 0.743 walk-forward (unchanged)
- MR win: 0.686 | RUNNER win: 0.632 | RUNNER return positive in all folds
- TF still rejected (0.500)

---

## Current Recommended Research Thresholds

| Parameter | Current | Research recommendation |
|---|---|---|
| `max_mr_fail_probability` | 0.45 | **0.40–0.45 plateau confirmed** — keep 0.45 for now |
| `min_probability` (MR win) | 0.55 | unchanged — not re-tested this phase |
| Runner exit | 2 ATR (implicit) | **Research favors B/C (oscillator cross)** — do NOT change live until reviewed |
| Stop mode | `research_only` | 1.5 ATR NOT validated cross-asset (G7 showed asset-dependent behavior) — MANUAL_STOP_REQUIRED stays |

## Actions Intentionally OFF

- **TF engine**: permanently OFF (41 rows, ROC-AUC 0.500)
- **Runner standalone entry**: removed — Runner is position management only
- **All assets currently FLAT → NO_ACTION** (no MR eligibility at latest bar)
- **Broker execution**: none; manual only

---

## Remaining Risks / Limitations

1. **Yahoo intraday limit**: 1H history capped ~730 days; GOLD/US500 have shorter effective history. No silent backfill.
2. **US500 is an outlier** — MR_FAIL fails on held-out US500 (0.487). Consider excluding US500 from MR or gathering more data.
3. **FX assets (EURCAD, USDJPY)** show weak Runner exits under oscillator logic — exit method may need per-asset-class tuning.
4. **Calibration drift**: model slightly over-confident at high p_fail bins (0.85 pred vs 0.69 actual). Raw model retained; recalibration not justified yet.
5. **Stop research incomplete**: no validated cross-asset stop → all entry plans flag MANUAL_STOP_REQUIRED.
6. **Runner exit change pending review** — B/C look better than A pooled, but FX assets disagree; do not change live logic yet.
7. **Sample sizes**: TF (41 rows) unusable; Runner per-asset folds are 90–177 rows — modest.

---

## Verdict

**NOT READY — production trading.**

Reasons:
- No validated cross-asset stop method (MANUAL_STOP_REQUIRED active)
- US500 MR_FAIL fails asset-holdout (0.487) — model not universal
- Runner exit method not yet decided (A vs B vs C research just completed)
- TF disabled; MR threshold plateau identified but not production-validated forward

**READY FOR NEXT RESEARCH PHASE**

The research infrastructure (G1–G9) is complete and operational. All Phase A–F conclusions preserved: MR_FAIL primary gate (0.743 walk-forward), Runner alpha (positive in all folds), TF OFF, OFF allowed, deterministic risk rules, manual execution only.
