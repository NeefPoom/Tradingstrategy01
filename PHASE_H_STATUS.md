# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-04T19:05:11.724171

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
66

## 5. Observation count by asset
- ADAUSD: 1394
- AUDCAD: 1000
- AUDCHF: 1000
- AUDJPY: 999
- AUDNZD: 1000
- AUDUSD: 1000
- AUS200: 294
- AVAXUSD: 1394
- BCHUSD: 1394
- BNBUSD: 1394
- BRENT: 956
- BTCUSD: 1591
- CADCHF: 1000
- CADJPY: 999
- CHFJPY: 999
- DOGEUSD: 1394
- DOTUSD: 1394
- ETHUSD: 1591
- EU50: 378
- EURAUD: 999
- EURCAD: 1138
- EURCHF: 999
- EURGBP: 1000
- EURJPY: 999
- EURUSD: 999
- FRA40: 378
- GBPAUD: 1000
- GBPCAD: 1000
- GBPCHF: 1000
- GBPJPY: 999
- GBPUSD: 1000
- GER40: 378
- GOLD: 1078
- HK50: 280
- JPN225: 259
- LINKUSD: 1394
- LTCUSD: 1394
- NAS100: 291
- NATGAS: 961
- NZDCAD: 1000
- NZDCHF: 1000
- NZDJPY: 999
- NZDUSD: 1000
- SILVER: 957
- SOLUSD: 1394
- UK100: 378
- US30: 291
- US500: 327
- USDCAD: 1001
- USDCHF: 995
- USDJPY: 1131
- WTI: 957
- XRPUSD: 1394

## 6. MR candidates / resolved
- 1247 candidates, 0 resolved

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