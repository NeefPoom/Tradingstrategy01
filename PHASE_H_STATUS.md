# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-19T23:58:19.743078

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
81

## 5. Observation count by asset
- ADAUSD: 1758
- AUDCAD: 1267
- AUDCHF: 1267
- AUDJPY: 1266
- AUDNZD: 1267
- AUDUSD: 1267
- AUS200: 371
- AVAXUSD: 1758
- BCHUSD: 1758
- BNBUSD: 1758
- BRENT: 1213
- BTCUSD: 1956
- CADCHF: 1269
- CADJPY: 1266
- CHFJPY: 1266
- DOGEUSD: 1758
- DOTUSD: 1758
- ETHUSD: 1956
- EU50: 477
- EURAUD: 1266
- EURCAD: 1405
- EURCHF: 1266
- EURGBP: 1267
- EURJPY: 1265
- EURUSD: 1266
- FRA40: 477
- GBPAUD: 1267
- GBPCAD: 1267
- GBPCHF: 1267
- GBPJPY: 1266
- GBPUSD: 1267
- GER40: 477
- GOLD: 1337
- HK50: 357
- JPN225: 336
- LINKUSD: 1758
- LTCUSD: 1758
- NAS100: 371
- NATGAS: 1218
- NZDCAD: 1267
- NZDCHF: 1267
- NZDJPY: 1266
- NZDUSD: 1267
- SILVER: 1214
- SOLUSD: 1758
- UK100: 477
- US30: 371
- US500: 407
- USDCAD: 1268
- USDCHF: 1262
- USDJPY: 1397
- WTI: 1217
- XRPUSD: 1758

## 6. MR candidates / resolved
- 1556 candidates, 0 resolved

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