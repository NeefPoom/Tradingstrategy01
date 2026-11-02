# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-02T20:07:29.691100

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
64

## 5. Observation count by asset
- ADAUSD: 1347
- AUDCAD: 953
- AUDCHF: 953
- AUDJPY: 952
- AUDNZD: 953
- AUDUSD: 953
- AUS200: 280
- AVAXUSD: 1347
- BCHUSD: 1347
- BNBUSD: 1347
- BRENT: 911
- BTCUSD: 1544
- CADCHF: 953
- CADJPY: 952
- CHFJPY: 952
- DOGEUSD: 1347
- DOTUSD: 1347
- ETHUSD: 1544
- EU50: 360
- EURAUD: 952
- EURCAD: 1091
- EURCHF: 952
- EURGBP: 953
- EURJPY: 952
- EURUSD: 952
- FRA40: 360
- GBPAUD: 953
- GBPCAD: 953
- GBPCHF: 953
- GBPJPY: 952
- GBPUSD: 953
- GER40: 360
- GOLD: 1033
- HK50: 266
- JPN225: 252
- LINKUSD: 1347
- LTCUSD: 1347
- NAS100: 278
- NATGAS: 916
- NZDCAD: 953
- NZDCHF: 953
- NZDJPY: 952
- NZDUSD: 953
- SILVER: 912
- SOLUSD: 1347
- UK100: 360
- US30: 278
- US500: 314
- USDCAD: 954
- USDCHF: 948
- USDJPY: 1084
- WTI: 912
- XRPUSD: 1347

## 6. MR candidates / resolved
- 1176 candidates, 0 resolved

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