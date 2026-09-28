# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-28T12:07:08.439449

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
29

## 5. Observation count by asset
- ADAUSD: 499
- AUDCAD: 352
- AUDCHF: 352
- AUDJPY: 352
- AUDNZD: 352
- AUDUSD: 351
- AUS200: 105
- AVAXUSD: 499
- BCHUSD: 499
- BNBUSD: 499
- BRENT: 330
- BTCUSD: 696
- CADCHF: 352
- CADJPY: 352
- CHFJPY: 352
- DOGEUSD: 499
- DOTUSD: 499
- ETHUSD: 696
- EU50: 131
- EURAUD: 352
- EURCAD: 489
- EURCHF: 352
- EURGBP: 352
- EURJPY: 352
- EURUSD: 351
- FRA40: 131
- GBPAUD: 352
- GBPCAD: 352
- GBPCHF: 352
- GBPJPY: 352
- GBPUSD: 351
- GER40: 131
- GOLD: 449
- HK50: 105
- JPN225: 84
- LINKUSD: 499
- LTCUSD: 499
- NAS100: 98
- NATGAS: 331
- NZDCAD: 352
- NZDCHF: 352
- NZDJPY: 352
- NZDUSD: 351
- SILVER: 331
- SOLUSD: 499
- UK100: 131
- US30: 98
- US500: 134
- USDCAD: 352
- USDCHF: 350
- USDJPY: 487
- WTI: 330
- XRPUSD: 499

## 6. MR candidates / resolved
- 340 candidates, 0 resolved

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