# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-02T02:38:51.002191

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
32

## 5. Observation count by asset
- ADAUSD: 585
- AUDCAD: 438
- AUDCHF: 438
- AUDJPY: 438
- AUDNZD: 438
- AUDUSD: 438
- AUS200: 128
- AVAXUSD: 585
- BCHUSD: 585
- BNBUSD: 585
- BRENT: 412
- BTCUSD: 783
- CADCHF: 438
- CADJPY: 438
- CHFJPY: 438
- DOGEUSD: 585
- DOTUSD: 585
- ETHUSD: 783
- EU50: 162
- EURAUD: 438
- EURCAD: 576
- EURCHF: 438
- EURGBP: 438
- EURJPY: 438
- EURUSD: 438
- FRA40: 162
- GBPAUD: 438
- GBPCAD: 438
- GBPCHF: 438
- GBPJPY: 438
- GBPUSD: 438
- GER40: 162
- GOLD: 532
- HK50: 120
- JPN225: 107
- LINKUSD: 585
- LTCUSD: 585
- NAS100: 126
- NATGAS: 413
- NZDCAD: 438
- NZDCHF: 438
- NZDJPY: 438
- NZDUSD: 438
- SILVER: 413
- SOLUSD: 585
- UK100: 162
- US30: 126
- US500: 162
- USDCAD: 438
- USDCHF: 436
- USDJPY: 574
- WTI: 412
- XRPUSD: 585

## 6. MR candidates / resolved
- 442 candidates, 0 resolved

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