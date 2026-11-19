# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-19T08:10:14.957013

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
80

## 5. Observation count by asset
- ADAUSD: 1743
- AUDCAD: 1252
- AUDCHF: 1252
- AUDJPY: 1250
- AUDNZD: 1252
- AUDUSD: 1251
- AUS200: 371
- AVAXUSD: 1743
- BCHUSD: 1743
- BNBUSD: 1743
- BRENT: 1199
- BTCUSD: 1940
- CADCHF: 1254
- CADJPY: 1250
- CHFJPY: 1250
- DOGEUSD: 1743
- DOTUSD: 1743
- ETHUSD: 1940
- EU50: 468
- EURAUD: 1250
- EURCAD: 1389
- EURCHF: 1250
- EURGBP: 1251
- EURJPY: 1249
- EURUSD: 1250
- FRA40: 468
- GBPAUD: 1251
- GBPCAD: 1251
- GBPCHF: 1252
- GBPJPY: 1250
- GBPUSD: 1251
- GER40: 468
- GOLD: 1321
- HK50: 356
- JPN225: 336
- LINKUSD: 1743
- LTCUSD: 1743
- NAS100: 364
- NATGAS: 1204
- NZDCAD: 1252
- NZDCHF: 1252
- NZDJPY: 1251
- NZDUSD: 1251
- SILVER: 1200
- SOLUSD: 1743
- UK100: 468
- US30: 364
- US500: 400
- USDCAD: 1252
- USDCHF: 1246
- USDJPY: 1381
- WTI: 1203
- XRPUSD: 1743

## 6. MR candidates / resolved
- 1531 candidates, 0 resolved

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