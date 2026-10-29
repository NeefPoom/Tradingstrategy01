# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-29T17:01:50.859222

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
60

## 5. Observation count by asset
- ADAUSD: 1247
- AUDCAD: 903
- AUDCHF: 903
- AUDJPY: 903
- AUDNZD: 903
- AUDUSD: 903
- AUS200: 266
- AVAXUSD: 1248
- BCHUSD: 1248
- BNBUSD: 1248
- BRENT: 863
- BTCUSD: 1445
- CADCHF: 903
- CADJPY: 903
- CHFJPY: 903
- DOGEUSD: 1247
- DOTUSD: 1248
- ETHUSD: 1445
- EU50: 341
- EURAUD: 903
- EURCAD: 1041
- EURCHF: 903
- EURGBP: 904
- EURJPY: 903
- EURUSD: 903
- FRA40: 341
- GBPAUD: 903
- GBPCAD: 903
- GBPCHF: 903
- GBPJPY: 903
- GBPUSD: 904
- GER40: 341
- GOLD: 985
- HK50: 252
- JPN225: 238
- LINKUSD: 1248
- LTCUSD: 1247
- NAS100: 262
- NATGAS: 868
- NZDCAD: 903
- NZDCHF: 903
- NZDJPY: 903
- NZDUSD: 903
- SILVER: 864
- SOLUSD: 1247
- UK100: 341
- US30: 262
- US500: 298
- USDCAD: 903
- USDCHF: 898
- USDJPY: 1036
- WTI: 864
- XRPUSD: 1247

## 6. MR candidates / resolved
- 1105 candidates, 0 resolved

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