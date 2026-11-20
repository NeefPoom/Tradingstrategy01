# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-20T16:24:50.276723

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
82

## 5. Observation count by asset
- ADAUSD: 1775
- AUDCAD: 1284
- AUDCHF: 1284
- AUDJPY: 1283
- AUDNZD: 1284
- AUDUSD: 1284
- AUS200: 378
- AVAXUSD: 1775
- BCHUSD: 1775
- BNBUSD: 1775
- BRENT: 1230
- BTCUSD: 1973
- CADCHF: 1286
- CADJPY: 1283
- CHFJPY: 1283
- DOGEUSD: 1775
- DOTUSD: 1775
- ETHUSD: 1973
- EU50: 485
- EURAUD: 1283
- EURCAD: 1422
- EURCHF: 1283
- EURGBP: 1284
- EURJPY: 1282
- EURUSD: 1283
- FRA40: 485
- GBPAUD: 1284
- GBPCAD: 1284
- GBPCHF: 1284
- GBPJPY: 1283
- GBPUSD: 1284
- GER40: 485
- GOLD: 1355
- HK50: 364
- JPN225: 343
- LINKUSD: 1775
- LTCUSD: 1775
- NAS100: 372
- NATGAS: 1235
- NZDCAD: 1284
- NZDCHF: 1284
- NZDJPY: 1283
- NZDUSD: 1284
- SILVER: 1232
- SOLUSD: 1775
- UK100: 485
- US30: 372
- US500: 408
- USDCAD: 1285
- USDCHF: 1279
- USDJPY: 1414
- WTI: 1234
- XRPUSD: 1775

## 6. MR candidates / resolved
- 1572 candidates, 0 resolved

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