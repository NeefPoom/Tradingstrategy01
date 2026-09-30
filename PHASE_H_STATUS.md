# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-30T02:08:53.117572

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
30

## 5. Observation count by asset
- ADAUSD: 536
- AUDCAD: 390
- AUDCHF: 390
- AUDJPY: 390
- AUDNZD: 390
- AUDUSD: 390
- AUS200: 114
- AVAXUSD: 536
- BCHUSD: 536
- BNBUSD: 536
- BRENT: 366
- BTCUSD: 734
- CADCHF: 390
- CADJPY: 390
- CHFJPY: 390
- DOGEUSD: 536
- DOTUSD: 536
- ETHUSD: 734
- EU50: 144
- EURAUD: 390
- EURCAD: 528
- EURCHF: 390
- EURGBP: 390
- EURJPY: 390
- EURUSD: 390
- FRA40: 144
- GBPAUD: 390
- GBPCAD: 390
- GBPCHF: 390
- GBPJPY: 390
- GBPUSD: 390
- GER40: 144
- GOLD: 486
- HK50: 112
- JPN225: 93
- LINKUSD: 536
- LTCUSD: 536
- NAS100: 112
- NATGAS: 367
- NZDCAD: 390
- NZDCHF: 390
- NZDJPY: 390
- NZDUSD: 390
- SILVER: 367
- SOLUSD: 536
- UK100: 144
- US30: 112
- US500: 148
- USDCAD: 390
- USDCHF: 388
- USDJPY: 526
- WTI: 366
- XRPUSD: 536

## 6. MR candidates / resolved
- 385 candidates, 0 resolved

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