# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-30T20:17:40.072316

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
61

## 5. Observation count by asset
- ADAUSD: 1275
- AUDCAD: 931
- AUDCHF: 931
- AUDJPY: 931
- AUDNZD: 931
- AUDUSD: 931
- AUS200: 273
- AVAXUSD: 1275
- BCHUSD: 1275
- BNBUSD: 1275
- BRENT: 890
- BTCUSD: 1473
- CADCHF: 930
- CADJPY: 930
- CHFJPY: 930
- DOGEUSD: 1274
- DOTUSD: 1274
- ETHUSD: 1473
- EU50: 351
- EURAUD: 931
- EURCAD: 1069
- EURCHF: 931
- EURGBP: 932
- EURJPY: 931
- EURUSD: 931
- FRA40: 351
- GBPAUD: 931
- GBPCAD: 931
- GBPCHF: 931
- GBPJPY: 931
- GBPUSD: 932
- GER40: 351
- GOLD: 1012
- HK50: 259
- JPN225: 245
- LINKUSD: 1275
- LTCUSD: 1275
- NAS100: 272
- NATGAS: 895
- NZDCAD: 931
- NZDCHF: 931
- NZDJPY: 931
- NZDUSD: 931
- SILVER: 890
- SOLUSD: 1274
- UK100: 351
- US30: 272
- US500: 308
- USDCAD: 930
- USDCHF: 925
- USDJPY: 1064
- WTI: 890
- XRPUSD: 1275

## 6. MR candidates / resolved
- 1143 candidates, 0 resolved

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