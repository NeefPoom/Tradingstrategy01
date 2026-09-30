# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-30T08:33:04.817761

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
30

## 5. Observation count by asset
- ADAUSD: 543
- AUDCAD: 396
- AUDCHF: 396
- AUDJPY: 396
- AUDNZD: 396
- AUDUSD: 396
- AUS200: 119
- AVAXUSD: 543
- BCHUSD: 543
- BNBUSD: 543
- BRENT: 372
- BTCUSD: 741
- CADCHF: 396
- CADJPY: 396
- CHFJPY: 396
- DOGEUSD: 543
- DOTUSD: 543
- ETHUSD: 741
- EU50: 145
- EURAUD: 396
- EURCAD: 534
- EURCHF: 396
- EURGBP: 396
- EURJPY: 396
- EURUSD: 396
- FRA40: 145
- GBPAUD: 396
- GBPCAD: 396
- GBPCHF: 396
- GBPJPY: 396
- GBPUSD: 396
- GER40: 145
- GOLD: 492
- HK50: 118
- JPN225: 98
- LINKUSD: 543
- LTCUSD: 543
- NAS100: 112
- NATGAS: 373
- NZDCAD: 396
- NZDCHF: 396
- NZDJPY: 396
- NZDUSD: 396
- SILVER: 373
- SOLUSD: 543
- UK100: 145
- US30: 112
- US500: 148
- USDCAD: 396
- USDCHF: 394
- USDJPY: 532
- WTI: 372
- XRPUSD: 543

## 6. MR candidates / resolved
- 388 candidates, 0 resolved

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