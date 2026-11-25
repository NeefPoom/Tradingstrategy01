# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-25T13:01:44.753326

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
87

## 5. Observation count by asset
- ADAUSD: 1891
- AUDCAD: 1351
- AUDCHF: 1351
- AUDJPY: 1350
- AUDNZD: 1351
- AUDUSD: 1351
- AUS200: 399
- AVAXUSD: 1891
- BCHUSD: 1891
- BNBUSD: 1891
- BRENT: 1295
- BTCUSD: 2089
- CADCHF: 1354
- CADJPY: 1350
- CHFJPY: 1350
- DOGEUSD: 1891
- DOTUSD: 1891
- ETHUSD: 2089
- EU50: 508
- EURAUD: 1350
- EURCAD: 1489
- EURCHF: 1350
- EURGBP: 1351
- EURJPY: 1349
- EURUSD: 1350
- FRA40: 508
- GBPAUD: 1351
- GBPCAD: 1351
- GBPCHF: 1351
- GBPJPY: 1350
- GBPUSD: 1351
- GER40: 508
- GOLD: 1420
- HK50: 385
- JPN225: 357
- LINKUSD: 1891
- LTCUSD: 1891
- NAS100: 392
- NATGAS: 1300
- NZDCAD: 1351
- NZDCHF: 1351
- NZDJPY: 1350
- NZDUSD: 1351
- SILVER: 1297
- SOLUSD: 1891
- UK100: 508
- US30: 392
- US500: 428
- USDCAD: 1352
- USDCHF: 1346
- USDJPY: 1480
- WTI: 1299
- XRPUSD: 1891

## 6. MR candidates / resolved
- 1656 candidates, 0 resolved

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