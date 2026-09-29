# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-29T06:18:09.741029

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
29

## 5. Observation count by asset
- ADAUSD: 517
- AUDCAD: 370
- AUDCHF: 370
- AUDJPY: 370
- AUDNZD: 370
- AUDUSD: 370
- AUS200: 111
- AVAXUSD: 517
- BCHUSD: 517
- BNBUSD: 517
- BRENT: 346
- BTCUSD: 715
- CADCHF: 370
- CADJPY: 370
- CHFJPY: 370
- DOGEUSD: 517
- DOTUSD: 517
- ETHUSD: 715
- EU50: 135
- EURAUD: 370
- EURCAD: 508
- EURCHF: 370
- EURGBP: 370
- EURJPY: 370
- EURUSD: 370
- FRA40: 135
- GBPAUD: 370
- GBPCAD: 370
- GBPCHF: 370
- GBPJPY: 370
- GBPUSD: 370
- GER40: 135
- GOLD: 466
- HK50: 109
- JPN225: 90
- LINKUSD: 517
- LTCUSD: 517
- NAS100: 105
- NATGAS: 347
- NZDCAD: 370
- NZDCHF: 370
- NZDJPY: 370
- NZDUSD: 370
- SILVER: 347
- SOLUSD: 517
- UK100: 135
- US30: 105
- US500: 141
- USDCAD: 370
- USDCHF: 368
- USDJPY: 506
- WTI: 346
- XRPUSD: 517

## 6. MR candidates / resolved
- 361 candidates, 0 resolved

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