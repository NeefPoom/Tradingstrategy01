# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-18T18:15:25.225301

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
80

## 5. Observation count by asset
- ADAUSD: 1729
- AUDCAD: 1238
- AUDCHF: 1238
- AUDJPY: 1237
- AUDNZD: 1238
- AUDUSD: 1238
- AUS200: 364
- AVAXUSD: 1729
- BCHUSD: 1729
- BNBUSD: 1729
- BRENT: 1186
- BTCUSD: 1926
- CADCHF: 1240
- CADJPY: 1237
- CHFJPY: 1237
- DOGEUSD: 1729
- DOTUSD: 1729
- ETHUSD: 1927
- EU50: 468
- EURAUD: 1237
- EURCAD: 1376
- EURCHF: 1237
- EURGBP: 1238
- EURJPY: 1236
- EURUSD: 1237
- FRA40: 468
- GBPAUD: 1238
- GBPCAD: 1238
- GBPCHF: 1238
- GBPJPY: 1237
- GBPUSD: 1238
- GER40: 468
- GOLD: 1308
- HK50: 350
- JPN225: 329
- LINKUSD: 1729
- LTCUSD: 1729
- NAS100: 360
- NATGAS: 1191
- NZDCAD: 1238
- NZDCHF: 1238
- NZDJPY: 1237
- NZDUSD: 1238
- SILVER: 1187
- SOLUSD: 1729
- UK100: 468
- US30: 360
- US500: 396
- USDCAD: 1239
- USDCHF: 1233
- USDJPY: 1367
- WTI: 1189
- XRPUSD: 1729

## 6. MR candidates / resolved
- 1521 candidates, 0 resolved

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