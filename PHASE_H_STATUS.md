# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-11T01:06:09.678922

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
11

## 5. Observation count by asset
- ADAUSD: 80
- AUDCAD: 80
- AUDCHF: 80
- AUDJPY: 80
- AUDNZD: 80
- AUDUSD: 80
- AUS200: 22
- AVAXUSD: 80
- BCHUSD: 80
- BNBUSD: 80
- BRENT: 66
- BTCUSD: 278
- CADCHF: 80
- CADJPY: 80
- CHFJPY: 80
- DOGEUSD: 80
- DOTUSD: 80
- ETHUSD: 278
- EU50: 27
- EURAUD: 80
- EURCAD: 218
- EURCHF: 80
- EURGBP: 80
- EURJPY: 80
- EURUSD: 80
- FRA40: 27
- GBPAUD: 80
- GBPCAD: 80
- GBPCHF: 80
- GBPJPY: 80
- GBPUSD: 80
- GER40: 27
- GOLD: 185
- HK50: 21
- JPN225: 22
- LINKUSD: 80
- LTCUSD: 80
- NAS100: 21
- NATGAS: 66
- NZDCAD: 80
- NZDCHF: 80
- NZDJPY: 80
- NZDUSD: 80
- SILVER: 66
- SOLUSD: 80
- UK100: 27
- US30: 21
- US500: 57
- USDCAD: 80
- USDCHF: 80
- USDJPY: 217
- WTI: 66
- XRPUSD: 80

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