# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-11T02:39:41.264615

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
11

## 5. Observation count by asset
- ADAUSD: 81
- AUDCAD: 81
- AUDCHF: 81
- AUDJPY: 81
- AUDNZD: 81
- AUDUSD: 81
- AUS200: 23
- AVAXUSD: 81
- BCHUSD: 81
- BNBUSD: 81
- BRENT: 67
- BTCUSD: 279
- CADCHF: 81
- CADJPY: 81
- CHFJPY: 81
- DOGEUSD: 81
- DOTUSD: 81
- ETHUSD: 279
- EU50: 27
- EURAUD: 81
- EURCAD: 219
- EURCHF: 81
- EURGBP: 81
- EURJPY: 81
- EURUSD: 81
- FRA40: 27
- GBPAUD: 81
- GBPCAD: 81
- GBPCHF: 81
- GBPJPY: 81
- GBPUSD: 81
- GER40: 27
- GOLD: 186
- HK50: 22
- JPN225: 23
- LINKUSD: 81
- LTCUSD: 81
- NAS100: 21
- NATGAS: 67
- NZDCAD: 81
- NZDCHF: 81
- NZDJPY: 81
- NZDUSD: 81
- SILVER: 67
- SOLUSD: 81
- UK100: 27
- US30: 21
- US500: 57
- USDCAD: 81
- USDCHF: 81
- USDJPY: 218
- WTI: 67
- XRPUSD: 81

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