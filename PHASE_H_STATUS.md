# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-23T23:20:02.370488

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
85

## 5. Observation count by asset
- ADAUSD: 1854
- AUDCAD: 1314
- AUDCHF: 1314
- AUDJPY: 1313
- AUDNZD: 1314
- AUDUSD: 1313
- AUS200: 385
- AVAXUSD: 1854
- BCHUSD: 1854
- BNBUSD: 1854
- BRENT: 1259
- BTCUSD: 2051
- CADCHF: 1317
- CADJPY: 1313
- CHFJPY: 1313
- DOGEUSD: 1854
- DOTUSD: 1854
- ETHUSD: 2051
- EU50: 495
- EURAUD: 1313
- EURCAD: 1451
- EURCHF: 1313
- EURGBP: 1314
- EURJPY: 1312
- EURUSD: 1312
- FRA40: 495
- GBPAUD: 1314
- GBPCAD: 1314
- GBPCHF: 1314
- GBPJPY: 1313
- GBPUSD: 1313
- GER40: 495
- GOLD: 1384
- HK50: 371
- JPN225: 343
- LINKUSD: 1854
- LTCUSD: 1854
- NAS100: 385
- NATGAS: 1264
- NZDCAD: 1314
- NZDCHF: 1314
- NZDJPY: 1313
- NZDUSD: 1313
- SILVER: 1261
- SOLUSD: 1854
- UK100: 495
- US30: 385
- US500: 421
- USDCAD: 1314
- USDCHF: 1308
- USDJPY: 1442
- WTI: 1263
- XRPUSD: 1854

## 6. MR candidates / resolved
- 1615 candidates, 0 resolved

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