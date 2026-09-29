# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-29T13:24:26.008717

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
30

## 5. Observation count by asset
- ADAUSD: 524
- AUDCAD: 377
- AUDCHF: 377
- AUDJPY: 377
- AUDNZD: 377
- AUDUSD: 377
- AUS200: 112
- AVAXUSD: 524
- BCHUSD: 524
- BNBUSD: 524
- BRENT: 354
- BTCUSD: 722
- CADCHF: 377
- CADJPY: 377
- CHFJPY: 377
- DOGEUSD: 524
- DOTUSD: 524
- ETHUSD: 722
- EU50: 141
- EURAUD: 377
- EURCAD: 515
- EURCHF: 377
- EURGBP: 377
- EURJPY: 377
- EURUSD: 377
- FRA40: 141
- GBPAUD: 377
- GBPCAD: 377
- GBPCHF: 377
- GBPJPY: 377
- GBPUSD: 377
- GER40: 141
- GOLD: 474
- HK50: 112
- JPN225: 91
- LINKUSD: 524
- LTCUSD: 524
- NAS100: 105
- NATGAS: 355
- NZDCAD: 377
- NZDCHF: 377
- NZDJPY: 377
- NZDUSD: 377
- SILVER: 355
- SOLUSD: 524
- UK100: 141
- US30: 105
- US500: 141
- USDCAD: 377
- USDCHF: 375
- USDJPY: 513
- WTI: 354
- XRPUSD: 524

## 6. MR candidates / resolved
- 373 candidates, 0 resolved

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