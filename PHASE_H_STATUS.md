# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-05T07:41:22.666858

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
66

## 5. Observation count by asset
- ADAUSD: 1406
- AUDCAD: 1013
- AUDCHF: 1013
- AUDJPY: 1012
- AUDNZD: 1013
- AUDUSD: 1013
- AUS200: 301
- AVAXUSD: 1406
- BCHUSD: 1406
- BNBUSD: 1406
- BRENT: 968
- BTCUSD: 1604
- CADCHF: 1013
- CADJPY: 1012
- CHFJPY: 1012
- DOGEUSD: 1406
- DOTUSD: 1406
- ETHUSD: 1604
- EU50: 378
- EURAUD: 1012
- EURCAD: 1151
- EURCHF: 1012
- EURGBP: 1013
- EURJPY: 1012
- EURUSD: 1012
- FRA40: 378
- GBPAUD: 1013
- GBPCAD: 1013
- GBPCHF: 1013
- GBPJPY: 1012
- GBPUSD: 1013
- GER40: 378
- GOLD: 1090
- HK50: 286
- JPN225: 266
- LINKUSD: 1406
- LTCUSD: 1406
- NAS100: 294
- NATGAS: 973
- NZDCAD: 1013
- NZDCHF: 1013
- NZDJPY: 1012
- NZDUSD: 1013
- SILVER: 969
- SOLUSD: 1406
- UK100: 378
- US30: 294
- US500: 330
- USDCAD: 1014
- USDCHF: 1008
- USDJPY: 1144
- WTI: 969
- XRPUSD: 1406

## 6. MR candidates / resolved
- 1259 candidates, 0 resolved

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