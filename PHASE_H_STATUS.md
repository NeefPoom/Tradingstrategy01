# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-24T04:45:11.231944

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
24

## 5. Observation count by asset
- ADAUSD: 395
- AUDCAD: 297
- AUDCHF: 297
- AUDJPY: 297
- AUDNZD: 297
- AUDUSD: 297
- AUS200: 88
- AVAXUSD: 395
- BCHUSD: 395
- BNBUSD: 395
- BRENT: 274
- BTCUSD: 593
- CADCHF: 297
- CADJPY: 297
- CHFJPY: 297
- DOGEUSD: 395
- DOTUSD: 395
- ETHUSD: 593
- EU50: 108
- EURAUD: 297
- EURCAD: 435
- EURCHF: 297
- EURGBP: 297
- EURJPY: 297
- EURUSD: 297
- FRA40: 108
- GBPAUD: 297
- GBPCAD: 297
- GBPCHF: 297
- GBPJPY: 297
- GBPUSD: 297
- GER40: 108
- GOLD: 394
- HK50: 87
- JPN225: 67
- LINKUSD: 395
- LTCUSD: 395
- NAS100: 84
- NATGAS: 275
- NZDCAD: 297
- NZDCHF: 297
- NZDJPY: 297
- NZDUSD: 297
- SILVER: 275
- SOLUSD: 395
- UK100: 108
- US30: 84
- US500: 120
- USDCAD: 297
- USDCHF: 296
- USDJPY: 433
- WTI: 274
- XRPUSD: 395

## 6. MR candidates / resolved
- 261 candidates, 0 resolved

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