# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-09T01:59:52.672961

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
70

## 5. Observation count by asset
- ADAUSD: 1495
- AUDCAD: 1054
- AUDCHF: 1054
- AUDJPY: 1053
- AUDNZD: 1054
- AUDUSD: 1054
- AUS200: 310
- AVAXUSD: 1495
- BCHUSD: 1495
- BNBUSD: 1495
- BRENT: 1008
- BTCUSD: 1693
- CADCHF: 1055
- CADJPY: 1053
- CHFJPY: 1053
- DOGEUSD: 1495
- DOTUSD: 1495
- ETHUSD: 1693
- EU50: 396
- EURAUD: 1053
- EURCAD: 1192
- EURCHF: 1053
- EURGBP: 1054
- EURJPY: 1053
- EURUSD: 1053
- FRA40: 396
- GBPAUD: 1054
- GBPCAD: 1054
- GBPCHF: 1054
- GBPJPY: 1053
- GBPUSD: 1054
- GER40: 396
- GOLD: 1130
- HK50: 294
- JPN225: 274
- LINKUSD: 1495
- LTCUSD: 1495
- NAS100: 308
- NATGAS: 1013
- NZDCAD: 1054
- NZDCHF: 1054
- NZDJPY: 1053
- NZDUSD: 1054
- SILVER: 1009
- SOLUSD: 1495
- UK100: 396
- US30: 308
- US500: 344
- USDCAD: 1055
- USDCHF: 1049
- USDJPY: 1185
- WTI: 1009
- XRPUSD: 1495

## 6. MR candidates / resolved
- 1327 candidates, 0 resolved

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