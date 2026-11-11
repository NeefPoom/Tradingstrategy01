# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-11T22:03:51.293105

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
73

## 5. Observation count by asset
- ADAUSD: 1565
- AUDCAD: 1122
- AUDCHF: 1122
- AUDJPY: 1121
- AUDNZD: 1122
- AUDUSD: 1122
- AUS200: 329
- AVAXUSD: 1565
- BCHUSD: 1565
- BNBUSD: 1565
- BRENT: 1075
- BTCUSD: 1762
- CADCHF: 1123
- CADJPY: 1121
- CHFJPY: 1121
- DOGEUSD: 1565
- DOTUSD: 1565
- ETHUSD: 1762
- EU50: 423
- EURAUD: 1121
- EURCAD: 1260
- EURCHF: 1121
- EURGBP: 1122
- EURJPY: 1121
- EURUSD: 1121
- FRA40: 423
- GBPAUD: 1122
- GBPCAD: 1122
- GBPCHF: 1122
- GBPJPY: 1121
- GBPUSD: 1122
- GER40: 423
- GOLD: 1197
- HK50: 315
- JPN225: 294
- LINKUSD: 1565
- LTCUSD: 1565
- NAS100: 329
- NATGAS: 1080
- NZDCAD: 1122
- NZDCHF: 1122
- NZDJPY: 1121
- NZDUSD: 1122
- SILVER: 1075
- SOLUSD: 1565
- UK100: 423
- US30: 329
- US500: 365
- USDCAD: 1123
- USDCHF: 1117
- USDJPY: 1253
- WTI: 1075
- XRPUSD: 1565

## 6. MR candidates / resolved
- 1403 candidates, 0 resolved

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