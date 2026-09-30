# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-30T15:22:35.657326

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
31

## 5. Observation count by asset
- ADAUSD: 550
- AUDCAD: 403
- AUDCHF: 403
- AUDJPY: 403
- AUDNZD: 403
- AUDUSD: 403
- AUS200: 119
- AVAXUSD: 550
- BCHUSD: 550
- BNBUSD: 550
- BRENT: 379
- BTCUSD: 748
- CADCHF: 403
- CADJPY: 403
- CHFJPY: 403
- DOGEUSD: 550
- DOTUSD: 550
- ETHUSD: 748
- EU50: 152
- EURAUD: 403
- EURCAD: 541
- EURCHF: 403
- EURGBP: 403
- EURJPY: 403
- EURUSD: 403
- FRA40: 152
- GBPAUD: 403
- GBPCAD: 403
- GBPCHF: 403
- GBPJPY: 403
- GBPUSD: 403
- GER40: 152
- GOLD: 499
- HK50: 119
- JPN225: 98
- LINKUSD: 550
- LTCUSD: 550
- NAS100: 113
- NATGAS: 380
- NZDCAD: 403
- NZDCHF: 403
- NZDJPY: 403
- NZDUSD: 403
- SILVER: 380
- SOLUSD: 550
- UK100: 152
- US30: 113
- US500: 149
- USDCAD: 403
- USDCHF: 401
- USDJPY: 539
- WTI: 379
- XRPUSD: 550

## 6. MR candidates / resolved
- 403 candidates, 0 resolved

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