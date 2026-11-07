# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-07T23:58:01.318806

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
69

## 5. Observation count by asset
- ADAUSD: 1470
- AUDCAD: 1053
- AUDCHF: 1053
- AUDJPY: 1052
- AUDNZD: 1053
- AUDUSD: 1053
- AUS200: 308
- AVAXUSD: 1470
- BCHUSD: 1470
- BNBUSD: 1470
- BRENT: 1006
- BTCUSD: 1668
- CADCHF: 1054
- CADJPY: 1052
- CHFJPY: 1052
- DOGEUSD: 1470
- DOTUSD: 1470
- ETHUSD: 1668
- EU50: 396
- EURAUD: 1052
- EURCAD: 1191
- EURCHF: 1052
- EURGBP: 1053
- EURJPY: 1052
- EURUSD: 1052
- FRA40: 396
- GBPAUD: 1053
- GBPCAD: 1053
- GBPCHF: 1053
- GBPJPY: 1052
- GBPUSD: 1053
- GER40: 396
- GOLD: 1128
- HK50: 294
- JPN225: 273
- LINKUSD: 1470
- LTCUSD: 1470
- NAS100: 308
- NATGAS: 1011
- NZDCAD: 1053
- NZDCHF: 1053
- NZDJPY: 1052
- NZDUSD: 1053
- SILVER: 1007
- SOLUSD: 1470
- UK100: 396
- US30: 308
- US500: 344
- USDCAD: 1054
- USDCHF: 1048
- USDJPY: 1184
- WTI: 1007
- XRPUSD: 1470

## 6. MR candidates / resolved
- 1322 candidates, 0 resolved

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