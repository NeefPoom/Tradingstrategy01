# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-24T22:24:18.490109

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
25

## 5. Observation count by asset
- ADAUSD: 413
- AUDCAD: 315
- AUDCHF: 315
- AUDJPY: 315
- AUDNZD: 315
- AUDUSD: 315
- AUS200: 91
- AVAXUSD: 413
- BCHUSD: 413
- BNBUSD: 413
- BRENT: 293
- BTCUSD: 611
- CADCHF: 315
- CADJPY: 315
- CHFJPY: 315
- DOGEUSD: 413
- DOTUSD: 413
- ETHUSD: 611
- EU50: 117
- EURAUD: 315
- EURCAD: 453
- EURCHF: 315
- EURGBP: 315
- EURJPY: 315
- EURUSD: 315
- FRA40: 117
- GBPAUD: 315
- GBPCAD: 315
- GBPCHF: 315
- GBPJPY: 315
- GBPUSD: 315
- GER40: 117
- GOLD: 413
- HK50: 91
- JPN225: 70
- LINKUSD: 413
- LTCUSD: 413
- NAS100: 91
- NATGAS: 294
- NZDCAD: 315
- NZDCHF: 315
- NZDJPY: 315
- NZDUSD: 315
- SILVER: 294
- SOLUSD: 413
- UK100: 117
- US30: 91
- US500: 127
- USDCAD: 315
- USDCHF: 314
- USDJPY: 451
- WTI: 293
- XRPUSD: 413

## 6. MR candidates / resolved
- 293 candidates, 0 resolved

## 7. Runner events / resolved
0 events, 0 resolved (Runner lifecycle starts only after a live MR position reaches TP1)

## 8. Forward MR_FAIL discrimination
ROC-AUC: insufficient sample

## 9. Forward calibration
Brier: n/a | ECE: n/a

## 10. MR gate performance
See reports/forward_mr_gate.csv (populated as candidates resolve)

## 11. Runner B vs C
Parallel research - see reports/forward_runner_comparison.csv

## 12. US500 research status
RESEARCH_ONLY for MR (Phase G holdout failure 0.487)

## 13. Data-quality issues
Weekend/session gaps expected for FX/futures/index (see price_quality.csv)

## 14. Model freeze violation
None

## 15. Decision
**CONTINUE_FORWARD_VALIDATION**

Phase H never outputs PRODUCTION_READY.