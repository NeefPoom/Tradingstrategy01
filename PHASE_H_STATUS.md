# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-24T07:09:16.784585

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
85

## 5. Observation count by asset
- ADAUSD: 1862
- AUDCAD: 1322
- AUDCHF: 1322
- AUDJPY: 1320
- AUDNZD: 1322
- AUDUSD: 1321
- AUS200: 392
- AVAXUSD: 1862
- BCHUSD: 1862
- BNBUSD: 1862
- BRENT: 1267
- BTCUSD: 2059
- CADCHF: 1325
- CADJPY: 1320
- CHFJPY: 1321
- DOGEUSD: 1862
- DOTUSD: 1862
- ETHUSD: 2059
- EU50: 495
- EURAUD: 1321
- EURCAD: 1459
- EURCHF: 1321
- EURGBP: 1322
- EURJPY: 1319
- EURUSD: 1320
- FRA40: 495
- GBPAUD: 1322
- GBPCAD: 1322
- GBPCHF: 1322
- GBPJPY: 1320
- GBPUSD: 1321
- GER40: 495
- GOLD: 1391
- HK50: 376
- JPN225: 350
- LINKUSD: 1862
- LTCUSD: 1862
- NAS100: 385
- NATGAS: 1272
- NZDCAD: 1322
- NZDCHF: 1322
- NZDJPY: 1321
- NZDUSD: 1321
- SILVER: 1269
- SOLUSD: 1862
- UK100: 495
- US30: 385
- US500: 421
- USDCAD: 1322
- USDCHF: 1316
- USDJPY: 1450
- WTI: 1271
- XRPUSD: 1862

## 6. MR candidates / resolved
- 1628 candidates, 0 resolved

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