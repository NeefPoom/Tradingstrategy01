# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-28T19:47:10.201273

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
29

## 5. Observation count by asset
- ADAUSD: 506
- AUDCAD: 359
- AUDCHF: 359
- AUDJPY: 359
- AUDNZD: 359
- AUDUSD: 359
- AUS200: 105
- AVAXUSD: 506
- BCHUSD: 506
- BNBUSD: 506
- BRENT: 337
- BTCUSD: 704
- CADCHF: 359
- CADJPY: 359
- CHFJPY: 359
- DOGEUSD: 506
- DOTUSD: 506
- ETHUSD: 704
- EU50: 135
- EURAUD: 359
- EURCAD: 497
- EURCHF: 359
- EURGBP: 359
- EURJPY: 359
- EURUSD: 359
- FRA40: 135
- GBPAUD: 359
- GBPCAD: 359
- GBPCHF: 359
- GBPJPY: 359
- GBPUSD: 359
- GER40: 135
- GOLD: 457
- HK50: 105
- JPN225: 84
- LINKUSD: 506
- LTCUSD: 506
- NAS100: 104
- NATGAS: 338
- NZDCAD: 359
- NZDCHF: 359
- NZDJPY: 359
- NZDUSD: 359
- SILVER: 338
- SOLUSD: 506
- UK100: 135
- US30: 104
- US500: 140
- USDCAD: 359
- USDCHF: 357
- USDJPY: 495
- WTI: 337
- XRPUSD: 506

## 6. MR candidates / resolved
- 348 candidates, 0 resolved

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