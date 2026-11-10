# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-10T12:03:24.413458

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
72

## 5. Observation count by asset
- ADAUSD: 1530
- AUDCAD: 1088
- AUDCHF: 1088
- AUDJPY: 1087
- AUDNZD: 1088
- AUDUSD: 1088
- AUS200: 322
- AVAXUSD: 1531
- BCHUSD: 1530
- BNBUSD: 1531
- BRENT: 1041
- BTCUSD: 1728
- CADCHF: 1089
- CADJPY: 1087
- CHFJPY: 1087
- DOGEUSD: 1530
- DOTUSD: 1530
- ETHUSD: 1728
- EU50: 408
- EURAUD: 1087
- EURCAD: 1226
- EURCHF: 1087
- EURGBP: 1088
- EURJPY: 1087
- EURUSD: 1087
- FRA40: 408
- GBPAUD: 1088
- GBPCAD: 1088
- GBPCHF: 1088
- GBPJPY: 1087
- GBPUSD: 1088
- GER40: 408
- GOLD: 1164
- HK50: 308
- JPN225: 287
- LINKUSD: 1531
- LTCUSD: 1530
- NAS100: 315
- NATGAS: 1046
- NZDCAD: 1088
- NZDCHF: 1088
- NZDJPY: 1087
- NZDUSD: 1088
- SILVER: 1042
- SOLUSD: 1530
- UK100: 408
- US30: 315
- US500: 351
- USDCAD: 1089
- USDCHF: 1083
- USDJPY: 1219
- WTI: 1042
- XRPUSD: 1530

## 6. MR candidates / resolved
- 1368 candidates, 0 resolved

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