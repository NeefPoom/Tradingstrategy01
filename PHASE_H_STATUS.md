# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-26T14:43:30.918819

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
88

## 5. Observation count by asset
- ADAUSD: 1917
- AUDCAD: 1377
- AUDCHF: 1377
- AUDJPY: 1376
- AUDNZD: 1377
- AUDUSD: 1377
- AUS200: 406
- AVAXUSD: 1917
- BCHUSD: 1917
- BNBUSD: 1917
- BRENT: 1311
- BTCUSD: 2115
- CADCHF: 1380
- CADJPY: 1376
- CHFJPY: 1376
- DOGEUSD: 1917
- DOTUSD: 1917
- ETHUSD: 2115
- EU50: 519
- EURAUD: 1376
- EURCAD: 1515
- EURCHF: 1376
- EURGBP: 1377
- EURJPY: 1375
- EURUSD: 1376
- FRA40: 519
- GBPAUD: 1377
- GBPCAD: 1377
- GBPCHF: 1377
- GBPJPY: 1376
- GBPUSD: 1377
- GER40: 519
- GOLD: 1436
- HK50: 392
- JPN225: 364
- LINKUSD: 1917
- LTCUSD: 1917
- NAS100: 399
- NATGAS: 1316
- NZDCAD: 1377
- NZDCHF: 1377
- NZDJPY: 1376
- NZDUSD: 1377
- SILVER: 1313
- SOLUSD: 1917
- UK100: 519
- US30: 399
- US500: 435
- USDCAD: 1378
- USDCHF: 1372
- USDJPY: 1506
- WTI: 1315
- XRPUSD: 1917

## 6. MR candidates / resolved
- 1695 candidates, 0 resolved

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