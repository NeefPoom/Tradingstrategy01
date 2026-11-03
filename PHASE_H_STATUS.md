# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-03T02:28:32.530870

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
64

## 5. Observation count by asset
- ADAUSD: 1353
- AUDCAD: 960
- AUDCHF: 960
- AUDJPY: 959
- AUDNZD: 960
- AUDUSD: 960
- AUS200: 283
- AVAXUSD: 1353
- BCHUSD: 1353
- BNBUSD: 1353
- BRENT: 917
- BTCUSD: 1551
- CADCHF: 960
- CADJPY: 959
- CHFJPY: 959
- DOGEUSD: 1353
- DOTUSD: 1353
- ETHUSD: 1551
- EU50: 360
- EURAUD: 959
- EURCAD: 1098
- EURCHF: 959
- EURGBP: 960
- EURJPY: 959
- EURUSD: 959
- FRA40: 360
- GBPAUD: 960
- GBPCAD: 960
- GBPCHF: 960
- GBPJPY: 959
- GBPUSD: 960
- GER40: 360
- GOLD: 1039
- HK50: 266
- JPN225: 252
- LINKUSD: 1353
- LTCUSD: 1353
- NAS100: 280
- NATGAS: 922
- NZDCAD: 960
- NZDCHF: 960
- NZDJPY: 959
- NZDUSD: 960
- SILVER: 918
- SOLUSD: 1353
- UK100: 360
- US30: 280
- US500: 316
- USDCAD: 961
- USDCHF: 955
- USDJPY: 1091
- WTI: 918
- XRPUSD: 1353

## 6. MR candidates / resolved
- 1179 candidates, 0 resolved

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