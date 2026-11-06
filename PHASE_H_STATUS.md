# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-06T02:26:38.713615

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
67

## 5. Observation count by asset
- ADAUSD: 1423
- AUDCAD: 1030
- AUDCHF: 1030
- AUDJPY: 1029
- AUDNZD: 1030
- AUDUSD: 1030
- AUS200: 304
- AVAXUSD: 1423
- BCHUSD: 1423
- BNBUSD: 1423
- BRENT: 986
- BTCUSD: 1621
- CADCHF: 1030
- CADJPY: 1029
- CHFJPY: 1029
- DOGEUSD: 1423
- DOTUSD: 1423
- ETHUSD: 1621
- EU50: 387
- EURAUD: 1029
- EURCAD: 1168
- EURCHF: 1029
- EURGBP: 1030
- EURJPY: 1029
- EURUSD: 1029
- FRA40: 387
- GBPAUD: 1030
- GBPCAD: 1030
- GBPCHF: 1030
- GBPJPY: 1029
- GBPUSD: 1030
- GER40: 387
- GOLD: 1108
- HK50: 287
- JPN225: 268
- LINKUSD: 1423
- LTCUSD: 1423
- NAS100: 301
- NATGAS: 991
- NZDCAD: 1030
- NZDCHF: 1030
- NZDJPY: 1029
- NZDUSD: 1030
- SILVER: 987
- SOLUSD: 1423
- UK100: 387
- US30: 301
- US500: 337
- USDCAD: 1031
- USDCHF: 1025
- USDJPY: 1161
- WTI: 987
- XRPUSD: 1423

## 6. MR candidates / resolved
- 1290 candidates, 0 resolved

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