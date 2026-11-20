# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-20T22:56:37.986368

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
82

## 5. Observation count by asset
- ADAUSD: 1781
- AUDCAD: 1290
- AUDCHF: 1290
- AUDJPY: 1289
- AUDNZD: 1290
- AUDUSD: 1290
- AUS200: 378
- AVAXUSD: 1781
- BCHUSD: 1781
- BNBUSD: 1781
- BRENT: 1236
- BTCUSD: 1979
- CADCHF: 1292
- CADJPY: 1289
- CHFJPY: 1289
- DOGEUSD: 1781
- DOTUSD: 1781
- ETHUSD: 1979
- EU50: 486
- EURAUD: 1289
- EURCAD: 1428
- EURCHF: 1289
- EURGBP: 1290
- EURJPY: 1288
- EURUSD: 1289
- FRA40: 486
- GBPAUD: 1290
- GBPCAD: 1290
- GBPCHF: 1290
- GBPJPY: 1289
- GBPUSD: 1290
- GER40: 486
- GOLD: 1361
- HK50: 364
- JPN225: 343
- LINKUSD: 1781
- LTCUSD: 1781
- NAS100: 378
- NATGAS: 1241
- NZDCAD: 1290
- NZDCHF: 1290
- NZDJPY: 1289
- NZDUSD: 1290
- SILVER: 1238
- SOLUSD: 1781
- UK100: 486
- US30: 378
- US500: 414
- USDCAD: 1291
- USDCHF: 1285
- USDJPY: 1420
- WTI: 1240
- XRPUSD: 1781

## 6. MR candidates / resolved
- 1573 candidates, 0 resolved

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