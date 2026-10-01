# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-01T23:30:56.009645

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
32

## 5. Observation count by asset
- ADAUSD: 582
- AUDCAD: 435
- AUDCHF: 435
- AUDJPY: 435
- AUDNZD: 435
- AUDUSD: 435
- AUS200: 126
- AVAXUSD: 582
- BCHUSD: 582
- BNBUSD: 582
- BRENT: 409
- BTCUSD: 780
- CADCHF: 435
- CADJPY: 435
- CHFJPY: 435
- DOGEUSD: 582
- DOTUSD: 582
- ETHUSD: 780
- EU50: 162
- EURAUD: 435
- EURCAD: 573
- EURCHF: 435
- EURGBP: 435
- EURJPY: 435
- EURUSD: 435
- FRA40: 162
- GBPAUD: 435
- GBPCAD: 435
- GBPCHF: 435
- GBPJPY: 435
- GBPUSD: 435
- GER40: 162
- GOLD: 529
- HK50: 119
- JPN225: 105
- LINKUSD: 582
- LTCUSD: 582
- NAS100: 126
- NATGAS: 410
- NZDCAD: 435
- NZDCHF: 435
- NZDJPY: 435
- NZDUSD: 435
- SILVER: 410
- SOLUSD: 582
- UK100: 162
- US30: 126
- US500: 162
- USDCAD: 435
- USDCHF: 433
- USDJPY: 571
- WTI: 409
- XRPUSD: 582

## 6. MR candidates / resolved
- 438 candidates, 0 resolved

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