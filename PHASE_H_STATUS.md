# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-11T15:14:32.707853

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
12

## 5. Observation count by asset
- ADAUSD: 92
- AUDCAD: 94
- AUDCHF: 94
- AUDJPY: 94
- AUDNZD: 94
- AUDUSD: 94
- AUS200: 28
- AVAXUSD: 94
- BCHUSD: 94
- BNBUSD: 94
- BRENT: 80
- BTCUSD: 292
- CADCHF: 94
- CADJPY: 94
- CHFJPY: 94
- DOGEUSD: 94
- DOTUSD: 94
- ETHUSD: 292
- EU50: 34
- EURAUD: 94
- EURCAD: 232
- EURCHF: 94
- EURGBP: 94
- EURJPY: 94
- EURUSD: 94
- FRA40: 34
- GBPAUD: 94
- GBPCAD: 94
- GBPCHF: 94
- GBPJPY: 91
- GBPUSD: 93
- GER40: 35
- GOLD: 197
- HK50: 28
- JPN225: 28
- LINKUSD: 93
- LTCUSD: 94
- NAS100: 22
- NATGAS: 80
- NZDCAD: 94
- NZDCHF: 94
- NZDJPY: 94
- NZDUSD: 94
- SILVER: 78
- SOLUSD: 94
- UK100: 35
- US30: 22
- US500: 58
- USDCAD: 94
- USDCHF: 94
- USDJPY: 229
- WTI: 80
- XRPUSD: 94

## 6. MR candidates / resolved
- 20 candidates, 0 resolved

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