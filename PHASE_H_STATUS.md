# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-29T21:56:58.059231

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
60

## 5. Observation count by asset
- ADAUSD: 1252
- AUDCAD: 908
- AUDCHF: 908
- AUDJPY: 908
- AUDNZD: 908
- AUDUSD: 908
- AUS200: 266
- AVAXUSD: 1252
- BCHUSD: 1252
- BNBUSD: 1252
- BRENT: 868
- BTCUSD: 1450
- CADCHF: 908
- CADJPY: 908
- CHFJPY: 908
- DOGEUSD: 1252
- DOTUSD: 1252
- ETHUSD: 1450
- EU50: 342
- EURAUD: 908
- EURCAD: 1046
- EURCHF: 908
- EURGBP: 909
- EURJPY: 908
- EURUSD: 908
- FRA40: 342
- GBPAUD: 908
- GBPCAD: 908
- GBPCHF: 908
- GBPJPY: 908
- GBPUSD: 909
- GER40: 342
- GOLD: 990
- HK50: 252
- JPN225: 238
- LINKUSD: 1252
- LTCUSD: 1252
- NAS100: 266
- NATGAS: 873
- NZDCAD: 908
- NZDCHF: 908
- NZDJPY: 908
- NZDUSD: 908
- SILVER: 869
- SOLUSD: 1252
- UK100: 342
- US30: 266
- US500: 302
- USDCAD: 908
- USDCHF: 903
- USDJPY: 1041
- WTI: 869
- XRPUSD: 1252

## 6. MR candidates / resolved
- 1111 candidates, 0 resolved

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