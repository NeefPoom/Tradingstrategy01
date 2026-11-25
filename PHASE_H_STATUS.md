# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-25T22:55:59.230684

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
87

## 5. Observation count by asset
- ADAUSD: 1901
- AUDCAD: 1361
- AUDCHF: 1361
- AUDJPY: 1360
- AUDNZD: 1361
- AUDUSD: 1361
- AUS200: 399
- AVAXUSD: 1901
- BCHUSD: 1901
- BNBUSD: 1901
- BRENT: 1305
- BTCUSD: 2099
- CADCHF: 1364
- CADJPY: 1360
- CHFJPY: 1360
- DOGEUSD: 1901
- DOTUSD: 1901
- ETHUSD: 2099
- EU50: 513
- EURAUD: 1360
- EURCAD: 1499
- EURCHF: 1360
- EURGBP: 1361
- EURJPY: 1359
- EURUSD: 1360
- FRA40: 513
- GBPAUD: 1361
- GBPCAD: 1361
- GBPCHF: 1361
- GBPJPY: 1360
- GBPUSD: 1361
- GER40: 513
- GOLD: 1430
- HK50: 385
- JPN225: 357
- LINKUSD: 1901
- LTCUSD: 1901
- NAS100: 399
- NATGAS: 1310
- NZDCAD: 1361
- NZDCHF: 1361
- NZDJPY: 1360
- NZDUSD: 1361
- SILVER: 1307
- SOLUSD: 1901
- UK100: 513
- US30: 399
- US500: 435
- USDCAD: 1362
- USDCHF: 1356
- USDJPY: 1490
- WTI: 1309
- XRPUSD: 1901

## 6. MR candidates / resolved
- 1677 candidates, 0 resolved

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