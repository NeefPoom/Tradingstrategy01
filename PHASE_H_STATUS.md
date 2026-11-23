# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-23T02:41:22.946642

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
84

## 5. Observation count by asset
- ADAUSD: 1831
- AUDCAD: 1293
- AUDCHF: 1293
- AUDJPY: 1292
- AUDNZD: 1293
- AUDUSD: 1293
- AUS200: 381
- AVAXUSD: 1831
- BCHUSD: 1831
- BNBUSD: 1831
- BRENT: 1239
- BTCUSD: 2029
- CADCHF: 1296
- CADJPY: 1292
- CHFJPY: 1292
- DOGEUSD: 1831
- DOTUSD: 1831
- ETHUSD: 2029
- EU50: 486
- EURAUD: 1292
- EURCAD: 1431
- EURCHF: 1292
- EURGBP: 1293
- EURJPY: 1291
- EURUSD: 1292
- FRA40: 486
- GBPAUD: 1293
- GBPCAD: 1293
- GBPCHF: 1293
- GBPJPY: 1292
- GBPUSD: 1293
- GER40: 486
- GOLD: 1364
- HK50: 365
- JPN225: 343
- LINKUSD: 1831
- LTCUSD: 1831
- NAS100: 378
- NATGAS: 1244
- NZDCAD: 1293
- NZDCHF: 1293
- NZDJPY: 1292
- NZDUSD: 1293
- SILVER: 1241
- SOLUSD: 1831
- UK100: 486
- US30: 378
- US500: 414
- USDCAD: 1294
- USDCHF: 1288
- USDJPY: 1422
- WTI: 1243
- XRPUSD: 1831

## 6. MR candidates / resolved
- 1589 candidates, 0 resolved

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