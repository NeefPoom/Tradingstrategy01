# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-26T16:47:54.171305

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
27

## 5. Observation count by asset
- ADAUSD: 455
- AUDCAD: 339
- AUDCHF: 339
- AUDJPY: 339
- AUDNZD: 339
- AUDUSD: 339
- AUS200: 98
- AVAXUSD: 455
- BCHUSD: 455
- BNBUSD: 455
- BRENT: 316
- BTCUSD: 653
- CADCHF: 339
- CADJPY: 339
- CHFJPY: 339
- DOGEUSD: 455
- DOTUSD: 455
- ETHUSD: 653
- EU50: 126
- EURAUD: 339
- EURCAD: 477
- EURCHF: 339
- EURGBP: 339
- EURJPY: 339
- EURUSD: 339
- FRA40: 126
- GBPAUD: 339
- GBPCAD: 339
- GBPCHF: 339
- GBPJPY: 339
- GBPUSD: 339
- GER40: 126
- GOLD: 436
- HK50: 98
- JPN225: 77
- LINKUSD: 455
- LTCUSD: 455
- NAS100: 98
- NATGAS: 317
- NZDCAD: 339
- NZDCHF: 339
- NZDJPY: 339
- NZDUSD: 339
- SILVER: 317
- SOLUSD: 455
- UK100: 126
- US30: 98
- US500: 134
- USDCAD: 339
- USDCHF: 337
- USDJPY: 475
- WTI: 316
- XRPUSD: 455

## 6. MR candidates / resolved
- 313 candidates, 0 resolved

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