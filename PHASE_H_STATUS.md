# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-01T19:37:55.588900

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
32

## 5. Observation count by asset
- ADAUSD: 578
- AUDCAD: 431
- AUDCHF: 431
- AUDJPY: 431
- AUDNZD: 431
- AUDUSD: 431
- AUS200: 126
- AVAXUSD: 578
- BCHUSD: 578
- BNBUSD: 578
- BRENT: 406
- BTCUSD: 776
- CADCHF: 431
- CADJPY: 431
- CHFJPY: 431
- DOGEUSD: 578
- DOTUSD: 578
- ETHUSD: 776
- EU50: 162
- EURAUD: 431
- EURCAD: 569
- EURCHF: 431
- EURGBP: 431
- EURJPY: 431
- EURUSD: 431
- FRA40: 162
- GBPAUD: 431
- GBPCAD: 431
- GBPCHF: 431
- GBPJPY: 431
- GBPUSD: 431
- GER40: 162
- GOLD: 526
- HK50: 119
- JPN225: 105
- LINKUSD: 578
- LTCUSD: 578
- NAS100: 125
- NATGAS: 407
- NZDCAD: 431
- NZDCHF: 431
- NZDJPY: 431
- NZDUSD: 431
- SILVER: 407
- SOLUSD: 578
- UK100: 162
- US30: 125
- US500: 161
- USDCAD: 431
- USDCHF: 429
- USDJPY: 567
- WTI: 406
- XRPUSD: 578

## 6. MR candidates / resolved
- 436 candidates, 0 resolved

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