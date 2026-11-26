# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-26T04:34:58.058095

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
87

## 5. Observation count by asset
- ADAUSD: 1907
- AUDCAD: 1367
- AUDCHF: 1367
- AUDJPY: 1366
- AUDNZD: 1367
- AUDUSD: 1367
- AUS200: 404
- AVAXUSD: 1907
- BCHUSD: 1907
- BNBUSD: 1907
- BRENT: 1310
- BTCUSD: 2105
- CADCHF: 1370
- CADJPY: 1366
- CHFJPY: 1366
- DOGEUSD: 1907
- DOTUSD: 1907
- ETHUSD: 2105
- EU50: 513
- EURAUD: 1366
- EURCAD: 1505
- EURCHF: 1366
- EURGBP: 1367
- EURJPY: 1365
- EURUSD: 1366
- FRA40: 513
- GBPAUD: 1367
- GBPCAD: 1367
- GBPCHF: 1367
- GBPJPY: 1366
- GBPUSD: 1367
- GER40: 513
- GOLD: 1435
- HK50: 388
- JPN225: 361
- LINKUSD: 1907
- LTCUSD: 1907
- NAS100: 399
- NATGAS: 1315
- NZDCAD: 1367
- NZDCHF: 1367
- NZDJPY: 1366
- NZDUSD: 1367
- SILVER: 1312
- SOLUSD: 1907
- UK100: 513
- US30: 399
- US500: 435
- USDCAD: 1368
- USDCHF: 1362
- USDJPY: 1496
- WTI: 1314
- XRPUSD: 1907

## 6. MR candidates / resolved
- 1688 candidates, 0 resolved

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