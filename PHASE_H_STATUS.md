# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-03T10:17:24.573642

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
64

## 5. Observation count by asset
- ADAUSD: 1361
- AUDCAD: 968
- AUDCHF: 968
- AUDJPY: 967
- AUDNZD: 968
- AUDUSD: 968
- AUS200: 287
- AVAXUSD: 1361
- BCHUSD: 1361
- BNBUSD: 1361
- BRENT: 925
- BTCUSD: 1559
- CADCHF: 968
- CADJPY: 967
- CHFJPY: 967
- DOGEUSD: 1361
- DOTUSD: 1361
- ETHUSD: 1559
- EU50: 362
- EURAUD: 967
- EURCAD: 1106
- EURCHF: 967
- EURGBP: 968
- EURJPY: 967
- EURUSD: 967
- FRA40: 362
- GBPAUD: 968
- GBPCAD: 968
- GBPCHF: 968
- GBPJPY: 967
- GBPUSD: 968
- GER40: 362
- GOLD: 1047
- HK50: 273
- JPN225: 252
- LINKUSD: 1361
- LTCUSD: 1361
- NAS100: 280
- NATGAS: 930
- NZDCAD: 968
- NZDCHF: 968
- NZDJPY: 967
- NZDUSD: 968
- SILVER: 926
- SOLUSD: 1361
- UK100: 362
- US30: 280
- US500: 316
- USDCAD: 969
- USDCHF: 963
- USDJPY: 1099
- WTI: 926
- XRPUSD: 1361

## 6. MR candidates / resolved
- 1192 candidates, 0 resolved

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