# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-20T07:23:54.827944

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
81

## 5. Observation count by asset
- ADAUSD: 1766
- AUDCAD: 1275
- AUDCHF: 1275
- AUDJPY: 1274
- AUDNZD: 1275
- AUDUSD: 1275
- AUS200: 378
- AVAXUSD: 1766
- BCHUSD: 1766
- BNBUSD: 1766
- BRENT: 1219
- BTCUSD: 1964
- CADCHF: 1277
- CADJPY: 1274
- CHFJPY: 1274
- DOGEUSD: 1766
- DOTUSD: 1766
- ETHUSD: 1964
- EU50: 477
- EURAUD: 1274
- EURCAD: 1413
- EURCHF: 1274
- EURGBP: 1275
- EURJPY: 1273
- EURUSD: 1274
- FRA40: 477
- GBPAUD: 1275
- GBPCAD: 1275
- GBPCHF: 1275
- GBPJPY: 1274
- GBPUSD: 1275
- GER40: 477
- GOLD: 1344
- HK50: 362
- JPN225: 343
- LINKUSD: 1766
- LTCUSD: 1766
- NAS100: 371
- NATGAS: 1224
- NZDCAD: 1275
- NZDCHF: 1275
- NZDJPY: 1274
- NZDUSD: 1275
- SILVER: 1221
- SOLUSD: 1766
- UK100: 477
- US30: 371
- US500: 407
- USDCAD: 1276
- USDCHF: 1270
- USDJPY: 1405
- WTI: 1223
- XRPUSD: 1766

## 6. MR candidates / resolved
- 1562 candidates, 0 resolved

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