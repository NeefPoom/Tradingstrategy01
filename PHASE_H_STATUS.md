# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-26T23:29:17.910926

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
88

## 5. Observation count by asset
- ADAUSD: 1926
- AUDCAD: 1386
- AUDCHF: 1386
- AUDJPY: 1385
- AUDNZD: 1386
- AUDUSD: 1386
- AUS200: 406
- AVAXUSD: 1926
- BCHUSD: 1926
- BNBUSD: 1926
- BRENT: 1311
- BTCUSD: 2124
- CADCHF: 1389
- CADJPY: 1385
- CHFJPY: 1385
- DOGEUSD: 1926
- DOTUSD: 1926
- ETHUSD: 2124
- EU50: 522
- EURAUD: 1385
- EURCAD: 1524
- EURCHF: 1385
- EURGBP: 1386
- EURJPY: 1384
- EURUSD: 1385
- FRA40: 522
- GBPAUD: 1386
- GBPCAD: 1386
- GBPCHF: 1386
- GBPJPY: 1385
- GBPUSD: 1386
- GER40: 522
- GOLD: 1436
- HK50: 392
- JPN225: 364
- LINKUSD: 1926
- LTCUSD: 1926
- NAS100: 399
- NATGAS: 1316
- NZDCAD: 1386
- NZDCHF: 1386
- NZDJPY: 1385
- NZDUSD: 1386
- SILVER: 1313
- SOLUSD: 1926
- UK100: 522
- US30: 399
- US500: 435
- USDCAD: 1387
- USDCHF: 1381
- USDJPY: 1515
- WTI: 1315
- XRPUSD: 1926

## 6. MR candidates / resolved
- 1699 candidates, 0 resolved

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