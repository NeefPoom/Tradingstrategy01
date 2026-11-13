# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-13T15:58:21.030083

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
75

## 5. Observation count by asset
- ADAUSD: 1606
- AUDCAD: 1164
- AUDCHF: 1164
- AUDJPY: 1163
- AUDNZD: 1164
- AUDUSD: 1164
- AUS200: 343
- AVAXUSD: 1606
- BCHUSD: 1606
- BNBUSD: 1606
- BRENT: 1114
- BTCUSD: 1804
- CADCHF: 1165
- CADJPY: 1163
- CHFJPY: 1163
- DOGEUSD: 1606
- DOTUSD: 1606
- ETHUSD: 1804
- EU50: 439
- EURAUD: 1163
- EURCAD: 1302
- EURCHF: 1163
- EURGBP: 1164
- EURJPY: 1163
- EURUSD: 1163
- FRA40: 439
- GBPAUD: 1164
- GBPCAD: 1164
- GBPCHF: 1164
- GBPJPY: 1163
- GBPUSD: 1164
- GER40: 439
- GOLD: 1237
- HK50: 329
- JPN225: 308
- LINKUSD: 1606
- LTCUSD: 1606
- NAS100: 337
- NATGAS: 1119
- NZDCAD: 1164
- NZDCHF: 1164
- NZDJPY: 1163
- NZDUSD: 1164
- SILVER: 1115
- SOLUSD: 1606
- UK100: 439
- US30: 337
- US500: 373
- USDCAD: 1165
- USDCHF: 1159
- USDJPY: 1295
- WTI: 1116
- XRPUSD: 1606

## 6. MR candidates / resolved
- 1446 candidates, 0 resolved

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