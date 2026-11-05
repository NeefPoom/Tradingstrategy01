# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-05T16:06:48.013372

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
67

## 5. Observation count by asset
- ADAUSD: 1415
- AUDCAD: 1021
- AUDCHF: 1021
- AUDJPY: 1020
- AUDNZD: 1021
- AUDUSD: 1021
- AUS200: 301
- AVAXUSD: 1415
- BCHUSD: 1415
- BNBUSD: 1415
- BRENT: 976
- BTCUSD: 1612
- CADCHF: 1021
- CADJPY: 1020
- CHFJPY: 1020
- DOGEUSD: 1415
- DOTUSD: 1415
- ETHUSD: 1612
- EU50: 386
- EURAUD: 1020
- EURCAD: 1159
- EURCHF: 1020
- EURGBP: 1021
- EURJPY: 1020
- EURUSD: 1020
- FRA40: 386
- GBPAUD: 1021
- GBPCAD: 1021
- GBPCHF: 1021
- GBPJPY: 1020
- GBPUSD: 1021
- GER40: 385
- GOLD: 1098
- HK50: 287
- JPN225: 266
- LINKUSD: 1415
- LTCUSD: 1415
- NAS100: 295
- NATGAS: 981
- NZDCAD: 1021
- NZDCHF: 1021
- NZDJPY: 1020
- NZDUSD: 1021
- SILVER: 977
- SOLUSD: 1415
- UK100: 385
- US30: 295
- US500: 331
- USDCAD: 1022
- USDCHF: 1016
- USDJPY: 1152
- WTI: 977
- XRPUSD: 1415

## 6. MR candidates / resolved
- 1282 candidates, 0 resolved

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