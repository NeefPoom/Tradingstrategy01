# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-23T11:41:26.324386

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
85

## 5. Observation count by asset
- ADAUSD: 1842
- AUDCAD: 1302
- AUDCHF: 1302
- AUDJPY: 1301
- AUDNZD: 1302
- AUDUSD: 1302
- AUS200: 385
- AVAXUSD: 1842
- BCHUSD: 1842
- BNBUSD: 1842
- BRENT: 1248
- BTCUSD: 2040
- CADCHF: 1305
- CADJPY: 1301
- CHFJPY: 1301
- DOGEUSD: 1842
- DOTUSD: 1842
- ETHUSD: 2040
- EU50: 489
- EURAUD: 1301
- EURCAD: 1440
- EURCHF: 1301
- EURGBP: 1302
- EURJPY: 1300
- EURUSD: 1301
- FRA40: 489
- GBPAUD: 1302
- GBPCAD: 1302
- GBPCHF: 1302
- GBPJPY: 1301
- GBPUSD: 1302
- GER40: 489
- GOLD: 1373
- HK50: 371
- JPN225: 343
- LINKUSD: 1842
- LTCUSD: 1842
- NAS100: 378
- NATGAS: 1253
- NZDCAD: 1302
- NZDCHF: 1302
- NZDJPY: 1301
- NZDUSD: 1302
- SILVER: 1250
- SOLUSD: 1842
- UK100: 489
- US30: 378
- US500: 414
- USDCAD: 1303
- USDCHF: 1297
- USDJPY: 1431
- WTI: 1252
- XRPUSD: 1842

## 6. MR candidates / resolved
- 1602 candidates, 0 resolved

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