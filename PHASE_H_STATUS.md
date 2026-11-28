# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-28T16:32:21.040183

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
90

## 5. Observation count by asset
- ADAUSD: 1967
- AUDCAD: 1411
- AUDCHF: 1410
- AUDJPY: 1409
- AUDNZD: 1411
- AUDUSD: 1411
- AUS200: 413
- AVAXUSD: 1967
- BCHUSD: 1967
- BNBUSD: 1967
- BRENT: 1315
- BTCUSD: 2165
- CADCHF: 1414
- CADJPY: 1409
- CHFJPY: 1409
- DOGEUSD: 1967
- DOTUSD: 1967
- ETHUSD: 2165
- EU50: 531
- EURAUD: 1409
- EURCAD: 1548
- EURCHF: 1409
- EURGBP: 1410
- EURJPY: 1408
- EURUSD: 1409
- FRA40: 531
- GBPAUD: 1411
- GBPCAD: 1411
- GBPCHF: 1410
- GBPJPY: 1409
- GBPUSD: 1410
- GER40: 531
- GOLD: 1440
- HK50: 399
- JPN225: 371
- LINKUSD: 1967
- LTCUSD: 1967
- NAS100: 403
- NATGAS: 1320
- NZDCAD: 1411
- NZDCHF: 1410
- NZDJPY: 1409
- NZDUSD: 1411
- SILVER: 1317
- SOLUSD: 1967
- UK100: 531
- US30: 403
- US500: 439
- USDCAD: 1412
- USDCHF: 1405
- USDJPY: 1539
- WTI: 1319
- XRPUSD: 1967

## 6. MR candidates / resolved
- 1729 candidates, 0 resolved

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