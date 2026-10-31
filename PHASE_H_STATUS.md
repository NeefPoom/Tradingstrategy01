# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-31T20:21:13.057669

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
62

## 5. Observation count by asset
- ADAUSD: 1299
- AUDCAD: 934
- AUDCHF: 934
- AUDJPY: 933
- AUDNZD: 934
- AUDUSD: 934
- AUS200: 273
- AVAXUSD: 1299
- BCHUSD: 1299
- BNBUSD: 1299
- BRENT: 891
- BTCUSD: 1497
- CADCHF: 934
- CADJPY: 933
- CHFJPY: 933
- DOGEUSD: 1299
- DOTUSD: 1299
- ETHUSD: 1497
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
- LINKUSD: 1299
- LTCUSD: 1299
- NAS100: 273
- NATGAS: 896
- NZDCAD: 934
- NZDCHF: 934
- NZDJPY: 933
- NZDUSD: 934
- SILVER: 892
- SOLUSD: 1299
- UK100: 351
- US30: 273
- US500: 309
- USDCAD: 935
- USDCHF: 929
- USDJPY: 1065
- WTI: 892
- XRPUSD: 1299

## 6. MR candidates / resolved
- 1151 candidates, 0 resolved

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