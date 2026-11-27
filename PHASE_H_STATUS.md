# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-27T05:30:33.076106

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
88

## 5. Observation count by asset
- ADAUSD: 1932
- AUDCAD: 1392
- AUDCHF: 1392
- AUDJPY: 1391
- AUDNZD: 1392
- AUDUSD: 1392
- AUS200: 412
- AVAXUSD: 1932
- BCHUSD: 1932
- BNBUSD: 1932
- BRENT: 1311
- BTCUSD: 2130
- CADCHF: 1395
- CADJPY: 1391
- CHFJPY: 1391
- DOGEUSD: 1932
- DOTUSD: 1932
- ETHUSD: 2130
- EU50: 522
- EURAUD: 1391
- EURCAD: 1530
- EURCHF: 1391
- EURGBP: 1392
- EURJPY: 1390
- EURUSD: 1391
- FRA40: 522
- GBPAUD: 1392
- GBPCAD: 1392
- GBPCHF: 1392
- GBPJPY: 1391
- GBPUSD: 1392
- GER40: 522
- GOLD: 1436
- HK50: 395
- JPN225: 369
- LINKUSD: 1932
- LTCUSD: 1932
- NAS100: 399
- NATGAS: 1316
- NZDCAD: 1392
- NZDCHF: 1392
- NZDJPY: 1391
- NZDUSD: 1392
- SILVER: 1313
- SOLUSD: 1932
- UK100: 522
- US30: 399
- US500: 435
- USDCAD: 1393
- USDCHF: 1387
- USDJPY: 1521
- WTI: 1315
- XRPUSD: 1932

## 6. MR candidates / resolved
- 1701 candidates, 0 resolved

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