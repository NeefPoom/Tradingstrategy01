# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-31T11:16:13.816517

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
62

## 5. Observation count by asset
- ADAUSD: 1290
- AUDCAD: 934
- AUDCHF: 934
- AUDJPY: 933
- AUDNZD: 934
- AUDUSD: 934
- AUS200: 273
- AVAXUSD: 1290
- BCHUSD: 1290
- BNBUSD: 1290
- BRENT: 891
- BTCUSD: 1488
- CADCHF: 934
- CADJPY: 933
- CHFJPY: 933
- DOGEUSD: 1290
- DOTUSD: 1290
- ETHUSD: 1488
- EU50: 351
- EURAUD: 933
- EURCAD: 1072
- EURCHF: 933
- EURGBP: 934
- EURJPY: 933
- EURUSD: 933
- FRA40: 351
- GBPAUD: 934
- GBPCAD: 934
- GBPCHF: 934
- GBPJPY: 933
- GBPUSD: 934
- GER40: 351
- GOLD: 1013
- HK50: 259
- JPN225: 245
- LINKUSD: 1290
- LTCUSD: 1290
- NAS100: 273
- NATGAS: 896
- NZDCAD: 934
- NZDCHF: 934
- NZDJPY: 933
- NZDUSD: 934
- SILVER: 892
- SOLUSD: 1290
- UK100: 351
- US30: 273
- US500: 309
- USDCAD: 935
- USDCHF: 929
- USDJPY: 1065
- WTI: 892
- XRPUSD: 1290

## 6. MR candidates / resolved
- 1150 candidates, 0 resolved

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