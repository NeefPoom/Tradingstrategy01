# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-03T23:28:21.628057

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
65

## 5. Observation count by asset
- ADAUSD: 1374
- AUDCAD: 981
- AUDCHF: 981
- AUDJPY: 980
- AUDNZD: 981
- AUDUSD: 981
- AUS200: 287
- AVAXUSD: 1374
- BCHUSD: 1374
- BNBUSD: 1374
- BRENT: 937
- BTCUSD: 1572
- CADCHF: 981
- CADJPY: 980
- CHFJPY: 980
- DOGEUSD: 1374
- DOTUSD: 1374
- ETHUSD: 1572
- EU50: 369
- EURAUD: 980
- EURCAD: 1119
- EURCHF: 980
- EURGBP: 981
- EURJPY: 980
- EURUSD: 980
- FRA40: 369
- GBPAUD: 981
- GBPCAD: 981
- GBPCHF: 981
- GBPJPY: 980
- GBPUSD: 981
- GER40: 369
- GOLD: 1059
- HK50: 273
- JPN225: 252
- LINKUSD: 1374
- LTCUSD: 1374
- NAS100: 287
- NATGAS: 942
- NZDCAD: 981
- NZDCHF: 981
- NZDJPY: 980
- NZDUSD: 981
- SILVER: 938
- SOLUSD: 1374
- UK100: 369
- US30: 287
- US500: 323
- USDCAD: 982
- USDCHF: 976
- USDJPY: 1112
- WTI: 938
- XRPUSD: 1374

## 6. MR candidates / resolved
- 1216 candidates, 0 resolved

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