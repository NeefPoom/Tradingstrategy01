# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-11T18:48:40.905106

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
12

## 5. Observation count by asset
- ADAUSD: 97
- AUDCAD: 97
- AUDCHF: 97
- AUDJPY: 97
- AUDNZD: 97
- AUDUSD: 97
- AUS200: 28
- AVAXUSD: 97
- BCHUSD: 97
- BNBUSD: 97
- BRENT: 83
- BTCUSD: 295
- CADCHF: 97
- CADJPY: 97
- CHFJPY: 97
- DOGEUSD: 97
- DOTUSD: 97
- ETHUSD: 295
- EU50: 36
- EURAUD: 97
- EURCAD: 235
- EURCHF: 97
- EURGBP: 97
- EURJPY: 97
- EURUSD: 97
- FRA40: 36
- GBPAUD: 97
- GBPCAD: 97
- GBPCHF: 97
- GBPJPY: 97
- GBPUSD: 97
- GER40: 36
- GOLD: 202
- HK50: 28
- JPN225: 28
- LINKUSD: 97
- LTCUSD: 97
- NAS100: 26
- NATGAS: 83
- NZDCAD: 97
- NZDCHF: 97
- NZDJPY: 97
- NZDUSD: 97
- SILVER: 83
- SOLUSD: 97
- UK100: 36
- US30: 26
- US500: 62
- USDCAD: 97
- USDCHF: 97
- USDJPY: 234
- WTI: 83
- XRPUSD: 97

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