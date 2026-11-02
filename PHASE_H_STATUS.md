# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-02T09:39:45.611305

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
63

## 5. Observation count by asset
- ADAUSD: 1336
- AUDCAD: 943
- AUDCHF: 943
- AUDJPY: 942
- AUDNZD: 943
- AUDUSD: 943
- AUS200: 280
- AVAXUSD: 1336
- BCHUSD: 1336
- BNBUSD: 1336
- BRENT: 901
- BTCUSD: 1534
- CADCHF: 943
- CADJPY: 942
- CHFJPY: 942
- DOGEUSD: 1336
- DOTUSD: 1336
- ETHUSD: 1534
- EU50: 352
- EURAUD: 942
- EURCAD: 1081
- EURCHF: 942
- EURGBP: 943
- EURJPY: 942
- EURUSD: 942
- FRA40: 352
- GBPAUD: 943
- GBPCAD: 943
- GBPCHF: 943
- GBPJPY: 942
- GBPUSD: 943
- GER40: 352
- GOLD: 1023
- HK50: 266
- JPN225: 252
- LINKUSD: 1336
- LTCUSD: 1336
- NAS100: 273
- NATGAS: 906
- NZDCAD: 943
- NZDCHF: 943
- NZDJPY: 942
- NZDUSD: 943
- SILVER: 902
- SOLUSD: 1336
- UK100: 352
- US30: 273
- US500: 309
- USDCAD: 944
- USDCHF: 938
- USDJPY: 1074
- WTI: 902
- XRPUSD: 1336

## 6. MR candidates / resolved
- 1170 candidates, 0 resolved

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