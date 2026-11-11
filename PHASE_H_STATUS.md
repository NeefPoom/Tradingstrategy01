# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-11T07:19:49.863675

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
72

## 5. Observation count by asset
- ADAUSD: 1550
- AUDCAD: 1108
- AUDCHF: 1108
- AUDJPY: 1107
- AUDNZD: 1108
- AUDUSD: 1108
- AUS200: 329
- AVAXUSD: 1550
- BCHUSD: 1550
- BNBUSD: 1550
- BRENT: 1060
- BTCUSD: 1748
- CADCHF: 1109
- CADJPY: 1107
- CHFJPY: 1107
- DOGEUSD: 1550
- DOTUSD: 1550
- ETHUSD: 1748
- EU50: 414
- EURAUD: 1107
- EURCAD: 1246
- EURCHF: 1107
- EURGBP: 1108
- EURJPY: 1107
- EURUSD: 1107
- FRA40: 414
- GBPAUD: 1108
- GBPCAD: 1108
- GBPCHF: 1108
- GBPJPY: 1107
- GBPUSD: 1108
- GER40: 414
- GOLD: 1183
- HK50: 313
- JPN225: 294
- LINKUSD: 1550
- LTCUSD: 1550
- NAS100: 322
- NATGAS: 1065
- NZDCAD: 1108
- NZDCHF: 1108
- NZDJPY: 1107
- NZDUSD: 1108
- SILVER: 1061
- SOLUSD: 1550
- UK100: 414
- US30: 322
- US500: 358
- USDCAD: 1109
- USDCHF: 1103
- USDJPY: 1239
- WTI: 1061
- XRPUSD: 1550

## 6. MR candidates / resolved
- 1392 candidates, 0 resolved

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