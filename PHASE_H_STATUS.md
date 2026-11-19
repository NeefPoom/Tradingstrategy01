# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-19T17:45:46.500990

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
81

## 5. Observation count by asset
- ADAUSD: 1752
- AUDCAD: 1261
- AUDCHF: 1261
- AUDJPY: 1260
- AUDNZD: 1261
- AUDUSD: 1261
- AUS200: 371
- AVAXUSD: 1752
- BCHUSD: 1752
- BNBUSD: 1752
- BRENT: 1208
- BTCUSD: 1950
- CADCHF: 1263
- CADJPY: 1260
- CHFJPY: 1260
- DOGEUSD: 1752
- DOTUSD: 1752
- ETHUSD: 1950
- EU50: 477
- EURAUD: 1260
- EURCAD: 1399
- EURCHF: 1260
- EURGBP: 1261
- EURJPY: 1259
- EURUSD: 1260
- FRA40: 477
- GBPAUD: 1261
- GBPCAD: 1261
- GBPCHF: 1261
- GBPJPY: 1260
- GBPUSD: 1261
- GER40: 477
- GOLD: 1331
- HK50: 357
- JPN225: 336
- LINKUSD: 1752
- LTCUSD: 1752
- NAS100: 367
- NATGAS: 1213
- NZDCAD: 1261
- NZDCHF: 1261
- NZDJPY: 1260
- NZDUSD: 1261
- SILVER: 1209
- SOLUSD: 1752
- UK100: 477
- US30: 367
- US500: 402
- USDCAD: 1262
- USDCHF: 1256
- USDJPY: 1391
- WTI: 1212
- XRPUSD: 1752

## 6. MR candidates / resolved
- 1548 candidates, 0 resolved

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