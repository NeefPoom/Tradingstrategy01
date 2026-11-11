# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-11T15:24:42.282422

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
73

## 5. Observation count by asset
- ADAUSD: 1558
- AUDCAD: 1116
- AUDCHF: 1116
- AUDJPY: 1115
- AUDNZD: 1116
- AUDUSD: 1116
- AUS200: 329
- AVAXUSD: 1558
- BCHUSD: 1558
- BNBUSD: 1558
- BRENT: 1068
- BTCUSD: 1756
- CADCHF: 1117
- CADJPY: 1115
- CHFJPY: 1115
- DOGEUSD: 1558
- DOTUSD: 1558
- ETHUSD: 1756
- EU50: 421
- EURAUD: 1115
- EURCAD: 1254
- EURCHF: 1115
- EURGBP: 1116
- EURJPY: 1115
- EURUSD: 1115
- FRA40: 421
- GBPAUD: 1116
- GBPCAD: 1116
- GBPCHF: 1116
- GBPJPY: 1115
- GBPUSD: 1116
- GER40: 421
- GOLD: 1191
- HK50: 315
- JPN225: 294
- LINKUSD: 1558
- LTCUSD: 1558
- NAS100: 322
- NATGAS: 1073
- NZDCAD: 1116
- NZDCHF: 1116
- NZDJPY: 1115
- NZDUSD: 1116
- SILVER: 1069
- SOLUSD: 1558
- UK100: 421
- US30: 322
- US500: 358
- USDCAD: 1117
- USDCHF: 1111
- USDJPY: 1247
- WTI: 1069
- XRPUSD: 1558

## 6. MR candidates / resolved
- 1401 candidates, 0 resolved

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