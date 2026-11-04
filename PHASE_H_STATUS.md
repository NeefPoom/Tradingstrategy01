# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-04T03:17:15.917797

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
65

## 5. Observation count by asset
- ADAUSD: 1378
- AUDCAD: 985
- AUDCHF: 985
- AUDJPY: 984
- AUDNZD: 985
- AUDUSD: 985
- AUS200: 291
- AVAXUSD: 1378
- BCHUSD: 1378
- BNBUSD: 1378
- BRENT: 941
- BTCUSD: 1576
- CADCHF: 985
- CADJPY: 984
- CHFJPY: 984
- DOGEUSD: 1378
- DOTUSD: 1378
- ETHUSD: 1576
- EU50: 369
- EURAUD: 984
- EURCAD: 1123
- EURCHF: 984
- EURGBP: 985
- EURJPY: 984
- EURUSD: 984
- FRA40: 369
- GBPAUD: 985
- GBPCAD: 985
- GBPCHF: 985
- GBPJPY: 984
- GBPUSD: 985
- GER40: 369
- GOLD: 1063
- HK50: 274
- JPN225: 255
- LINKUSD: 1378
- LTCUSD: 1378
- NAS100: 287
- NATGAS: 946
- NZDCAD: 985
- NZDCHF: 985
- NZDJPY: 984
- NZDUSD: 985
- SILVER: 942
- SOLUSD: 1378
- UK100: 369
- US30: 287
- US500: 323
- USDCAD: 986
- USDCHF: 980
- USDJPY: 1116
- WTI: 942
- XRPUSD: 1378

## 6. MR candidates / resolved
- 1222 candidates, 0 resolved

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