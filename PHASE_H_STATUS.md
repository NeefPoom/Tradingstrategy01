# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-09T09:55:54.391320

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
70

## 5. Observation count by asset
- ADAUSD: 1504
- AUDCAD: 1062
- AUDCHF: 1062
- AUDJPY: 1061
- AUDNZD: 1062
- AUDUSD: 1062
- AUS200: 315
- AVAXUSD: 1504
- BCHUSD: 1504
- BNBUSD: 1504
- BRENT: 1016
- BTCUSD: 1702
- CADCHF: 1063
- CADJPY: 1061
- CHFJPY: 1061
- DOGEUSD: 1504
- DOTUSD: 1504
- ETHUSD: 1702
- EU50: 397
- EURAUD: 1061
- EURCAD: 1200
- EURCHF: 1061
- EURGBP: 1062
- EURJPY: 1061
- EURUSD: 1061
- FRA40: 397
- GBPAUD: 1062
- GBPCAD: 1062
- GBPCHF: 1062
- GBPJPY: 1061
- GBPUSD: 1062
- GER40: 397
- GOLD: 1138
- HK50: 301
- JPN225: 280
- LINKUSD: 1504
- LTCUSD: 1504
- NAS100: 308
- NATGAS: 1021
- NZDCAD: 1062
- NZDCHF: 1062
- NZDJPY: 1061
- NZDUSD: 1062
- SILVER: 1017
- SOLUSD: 1504
- UK100: 397
- US30: 308
- US500: 344
- USDCAD: 1063
- USDCHF: 1057
- USDJPY: 1193
- WTI: 1017
- XRPUSD: 1504

## 6. MR candidates / resolved
- 1337 candidates, 0 resolved

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