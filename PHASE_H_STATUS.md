# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-11T21:44:26.842520

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
12

## 5. Observation count by asset
- ADAUSD: 100
- AUDCAD: 100
- AUDCHF: 100
- AUDJPY: 100
- AUDNZD: 98
- AUDUSD: 100
- AUS200: 28
- AVAXUSD: 100
- BCHUSD: 100
- BNBUSD: 100
- BRENT: 86
- BTCUSD: 298
- CADCHF: 100
- CADJPY: 100
- CHFJPY: 100
- DOGEUSD: 100
- DOTUSD: 100
- ETHUSD: 298
- EU50: 36
- EURAUD: 100
- EURCAD: 238
- EURCHF: 100
- EURGBP: 100
- EURJPY: 100
- EURUSD: 100
- FRA40: 36
- GBPAUD: 100
- GBPCAD: 100
- GBPCHF: 100
- GBPJPY: 100
- GBPUSD: 100
- GER40: 36
- GOLD: 205
- HK50: 28
- JPN225: 28
- LINKUSD: 100
- LTCUSD: 100
- NAS100: 28
- NATGAS: 86
- NZDCAD: 100
- NZDCHF: 100
- NZDJPY: 100
- NZDUSD: 100
- SILVER: 86
- SOLUSD: 100
- UK100: 36
- US30: 28
- US500: 64
- USDCAD: 100
- USDCHF: 100
- USDJPY: 237
- WTI: 86
- XRPUSD: 100

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