# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-06T17:41:38.623457

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
68

## 5. Observation count by asset
- ADAUSD: 1440
- AUDCAD: 1047
- AUDCHF: 1047
- AUDJPY: 1046
- AUDNZD: 1047
- AUDUSD: 1047
- AUS200: 308
- AVAXUSD: 1440
- BCHUSD: 1440
- BNBUSD: 1440
- BRENT: 1001
- BTCUSD: 1638
- CADCHF: 1047
- CADJPY: 1046
- CHFJPY: 1046
- DOGEUSD: 1440
- DOTUSD: 1440
- ETHUSD: 1638
- EU50: 396
- EURAUD: 1046
- EURCAD: 1185
- EURCHF: 1046
- EURGBP: 1047
- EURJPY: 1046
- EURUSD: 1046
- FRA40: 396
- GBPAUD: 1047
- GBPCAD: 1047
- GBPCHF: 1047
- GBPJPY: 1046
- GBPUSD: 1047
- GER40: 396
- GOLD: 1123
- HK50: 294
- JPN225: 273
- LINKUSD: 1440
- LTCUSD: 1440
- NAS100: 304
- NATGAS: 1006
- NZDCAD: 1047
- NZDCHF: 1047
- NZDJPY: 1046
- NZDUSD: 1047
- SILVER: 1002
- SOLUSD: 1440
- UK100: 396
- US30: 304
- US500: 339
- USDCAD: 1048
- USDCHF: 1042
- USDJPY: 1178
- WTI: 1002
- XRPUSD: 1440

## 6. MR candidates / resolved
- 1306 candidates, 0 resolved

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