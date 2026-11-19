# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-19T00:23:03.134390

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
80

## 5. Observation count by asset
- ADAUSD: 1732
- AUDCAD: 1241
- AUDCHF: 1241
- AUDJPY: 1240
- AUDNZD: 1241
- AUDUSD: 1241
- AUS200: 365
- AVAXUSD: 1732
- BCHUSD: 1732
- BNBUSD: 1732
- BRENT: 1191
- BTCUSD: 1930
- CADCHF: 1243
- CADJPY: 1240
- CHFJPY: 1240
- DOGEUSD: 1732
- DOTUSD: 1732
- ETHUSD: 1930
- EU50: 468
- EURAUD: 1240
- EURCAD: 1379
- EURCHF: 1240
- EURGBP: 1241
- EURJPY: 1239
- EURUSD: 1240
- FRA40: 468
- GBPAUD: 1241
- GBPCAD: 1241
- GBPCHF: 1241
- GBPJPY: 1240
- GBPUSD: 1241
- GER40: 468
- GOLD: 1314
- HK50: 350
- JPN225: 329
- LINKUSD: 1732
- LTCUSD: 1732
- NAS100: 364
- NATGAS: 1196
- NZDCAD: 1241
- NZDCHF: 1241
- NZDJPY: 1240
- NZDUSD: 1241
- SILVER: 1192
- SOLUSD: 1732
- UK100: 468
- US30: 364
- US500: 400
- USDCAD: 1242
- USDCHF: 1236
- USDJPY: 1371
- WTI: 1195
- XRPUSD: 1732

## 6. MR candidates / resolved
- 1523 candidates, 0 resolved

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