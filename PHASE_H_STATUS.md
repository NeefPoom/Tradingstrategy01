# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-06T10:09:39.986489

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
67

## 5. Observation count by asset
- ADAUSD: 1433
- AUDCAD: 1039
- AUDCHF: 1039
- AUDJPY: 1038
- AUDNZD: 1039
- AUDUSD: 1039
- AUS200: 308
- AVAXUSD: 1433
- BCHUSD: 1433
- BNBUSD: 1433
- BRENT: 994
- BTCUSD: 1630
- CADCHF: 1040
- CADJPY: 1038
- CHFJPY: 1038
- DOGEUSD: 1433
- DOTUSD: 1433
- ETHUSD: 1630
- EU50: 389
- EURAUD: 1038
- EURCAD: 1177
- EURCHF: 1038
- EURGBP: 1039
- EURJPY: 1038
- EURUSD: 1038
- FRA40: 389
- GBPAUD: 1039
- GBPCAD: 1039
- GBPCHF: 1039
- GBPJPY: 1038
- GBPUSD: 1039
- GER40: 389
- GOLD: 1115
- HK50: 294
- JPN225: 273
- LINKUSD: 1433
- LTCUSD: 1433
- NAS100: 301
- NATGAS: 999
- NZDCAD: 1039
- NZDCHF: 1039
- NZDJPY: 1038
- NZDUSD: 1039
- SILVER: 995
- SOLUSD: 1433
- UK100: 389
- US30: 301
- US500: 337
- USDCAD: 1040
- USDCHF: 1034
- USDJPY: 1170
- WTI: 995
- XRPUSD: 1433

## 6. MR candidates / resolved
- 1294 candidates, 0 resolved

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