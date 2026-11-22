# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-22T15:45:01.299289

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
84

## 5. Observation count by asset
- ADAUSD: 1822
- AUDCAD: 1291
- AUDCHF: 1291
- AUDJPY: 1290
- AUDNZD: 1291
- AUDUSD: 1291
- AUS200: 378
- AVAXUSD: 1822
- BCHUSD: 1822
- BNBUSD: 1822
- BRENT: 1236
- BTCUSD: 2020
- CADCHF: 1294
- CADJPY: 1290
- CHFJPY: 1290
- DOGEUSD: 1822
- DOTUSD: 1822
- ETHUSD: 2020
- EU50: 486
- EURAUD: 1290
- EURCAD: 1429
- EURCHF: 1290
- EURGBP: 1291
- EURJPY: 1289
- EURUSD: 1290
- FRA40: 486
- GBPAUD: 1291
- GBPCAD: 1291
- GBPCHF: 1291
- GBPJPY: 1290
- GBPUSD: 1291
- GER40: 486
- GOLD: 1361
- HK50: 364
- JPN225: 343
- LINKUSD: 1822
- LTCUSD: 1822
- NAS100: 378
- NATGAS: 1241
- NZDCAD: 1291
- NZDCHF: 1291
- NZDJPY: 1290
- NZDUSD: 1291
- SILVER: 1238
- SOLUSD: 1822
- UK100: 486
- US30: 378
- US500: 414
- USDCAD: 1292
- USDCHF: 1286
- USDJPY: 1420
- WTI: 1240
- XRPUSD: 1822

## 6. MR candidates / resolved
- 1586 candidates, 0 resolved

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