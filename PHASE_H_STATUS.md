# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-03T17:58:41.100275

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
65

## 5. Observation count by asset
- ADAUSD: 1368
- AUDCAD: 975
- AUDCHF: 975
- AUDJPY: 974
- AUDNZD: 975
- AUDUSD: 975
- AUS200: 287
- AVAXUSD: 1368
- BCHUSD: 1368
- BNBUSD: 1368
- BRENT: 932
- BTCUSD: 1566
- CADCHF: 975
- CADJPY: 974
- CHFJPY: 974
- DOGEUSD: 1368
- DOTUSD: 1368
- ETHUSD: 1566
- EU50: 369
- EURAUD: 974
- EURCAD: 1113
- EURCHF: 974
- EURGBP: 975
- EURJPY: 974
- EURUSD: 974
- FRA40: 369
- GBPAUD: 975
- GBPCAD: 975
- GBPCHF: 975
- GBPJPY: 974
- GBPUSD: 975
- GER40: 369
- GOLD: 1054
- HK50: 273
- JPN225: 252
- LINKUSD: 1368
- LTCUSD: 1368
- NAS100: 283
- NATGAS: 937
- NZDCAD: 975
- NZDCHF: 975
- NZDJPY: 974
- NZDUSD: 975
- SILVER: 933
- SOLUSD: 1368
- UK100: 369
- US30: 283
- US500: 319
- USDCAD: 976
- USDCHF: 970
- USDJPY: 1106
- WTI: 933
- XRPUSD: 1368

## 6. MR candidates / resolved
- 1210 candidates, 0 resolved

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