# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-24T00:00:26.785324

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
24

## 5. Observation count by asset
- ADAUSD: 390
- AUDCAD: 292
- AUDCHF: 292
- AUDJPY: 292
- AUDNZD: 292
- AUDUSD: 292
- AUS200: 84
- AVAXUSD: 390
- BCHUSD: 390
- BNBUSD: 390
- BRENT: 271
- BTCUSD: 588
- CADCHF: 292
- CADJPY: 292
- CHFJPY: 292
- DOGEUSD: 390
- DOTUSD: 390
- ETHUSD: 588
- EU50: 108
- EURAUD: 292
- EURCAD: 430
- EURCHF: 292
- EURGBP: 292
- EURJPY: 292
- EURUSD: 292
- FRA40: 108
- GBPAUD: 292
- GBPCAD: 292
- GBPCHF: 292
- GBPJPY: 292
- GBPUSD: 292
- GER40: 108
- GOLD: 391
- HK50: 84
- JPN225: 63
- LINKUSD: 390
- LTCUSD: 390
- NAS100: 84
- NATGAS: 272
- NZDCAD: 292
- NZDCHF: 292
- NZDJPY: 292
- NZDUSD: 292
- SILVER: 272
- SOLUSD: 390
- UK100: 108
- US30: 84
- US500: 120
- USDCAD: 292
- USDCHF: 291
- USDJPY: 428
- WTI: 271
- XRPUSD: 390

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