# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-10T03:39:59.971617

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
71

## 5. Observation count by asset
- ADAUSD: 1521
- AUDCAD: 1079
- AUDCHF: 1079
- AUDJPY: 1078
- AUDNZD: 1079
- AUDUSD: 1079
- AUS200: 319
- AVAXUSD: 1521
- BCHUSD: 1521
- BNBUSD: 1521
- BRENT: 1033
- BTCUSD: 1719
- CADCHF: 1080
- CADJPY: 1078
- CHFJPY: 1078
- DOGEUSD: 1521
- DOTUSD: 1521
- ETHUSD: 1719
- EU50: 405
- EURAUD: 1078
- EURCAD: 1217
- EURCHF: 1078
- EURGBP: 1079
- EURJPY: 1078
- EURUSD: 1078
- FRA40: 405
- GBPAUD: 1079
- GBPCAD: 1079
- GBPCHF: 1079
- GBPJPY: 1078
- GBPUSD: 1079
- GER40: 405
- GOLD: 1156
- HK50: 303
- JPN225: 283
- LINKUSD: 1521
- LTCUSD: 1521
- NAS100: 315
- NATGAS: 1038
- NZDCAD: 1079
- NZDCHF: 1079
- NZDJPY: 1078
- NZDUSD: 1079
- SILVER: 1034
- SOLUSD: 1521
- UK100: 405
- US30: 315
- US500: 351
- USDCAD: 1080
- USDCHF: 1074
- USDJPY: 1210
- WTI: 1034
- XRPUSD: 1521

## 6. MR candidates / resolved
- 1356 candidates, 0 resolved

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