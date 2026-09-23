# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-23T21:32:28.410066

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
24

## 5. Observation count by asset
- ADAUSD: 388
- AUDCAD: 290
- AUDCHF: 290
- AUDJPY: 290
- AUDNZD: 290
- AUDUSD: 290
- AUS200: 84
- AVAXUSD: 388
- BCHUSD: 388
- BNBUSD: 388
- BRENT: 270
- BTCUSD: 586
- CADCHF: 290
- CADJPY: 290
- CHFJPY: 290
- DOGEUSD: 388
- DOTUSD: 388
- ETHUSD: 586
- EU50: 108
- EURAUD: 290
- EURCAD: 428
- EURCHF: 290
- EURGBP: 290
- EURJPY: 290
- EURUSD: 290
- FRA40: 108
- GBPAUD: 290
- GBPCAD: 290
- GBPCHF: 290
- GBPJPY: 290
- GBPUSD: 290
- GER40: 108
- GOLD: 389
- HK50: 84
- JPN225: 63
- LINKUSD: 388
- LTCUSD: 388
- NAS100: 84
- NATGAS: 271
- NZDCAD: 290
- NZDCHF: 290
- NZDJPY: 290
- NZDUSD: 290
- SILVER: 271
- SOLUSD: 388
- UK100: 108
- US30: 84
- US500: 120
- USDCAD: 290
- USDCHF: 289
- USDJPY: 426
- WTI: 270
- XRPUSD: 388

## 6. MR candidates / resolved
- 259 candidates, 0 resolved

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