# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-24T19:09:07.805117

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
25

## 5. Observation count by asset
- ADAUSD: 410
- AUDCAD: 312
- AUDCHF: 312
- AUDJPY: 312
- AUDNZD: 312
- AUDUSD: 312
- AUS200: 91
- AVAXUSD: 410
- BCHUSD: 410
- BNBUSD: 410
- BRENT: 291
- BTCUSD: 608
- CADCHF: 312
- CADJPY: 312
- CHFJPY: 312
- DOGEUSD: 410
- DOTUSD: 410
- ETHUSD: 608
- EU50: 117
- EURAUD: 312
- EURCAD: 450
- EURCHF: 312
- EURGBP: 312
- EURJPY: 312
- EURUSD: 312
- FRA40: 117
- GBPAUD: 312
- GBPCAD: 312
- GBPCHF: 312
- GBPJPY: 312
- GBPUSD: 312
- GER40: 117
- GOLD: 411
- HK50: 91
- JPN225: 70
- LINKUSD: 410
- LTCUSD: 410
- NAS100: 89
- NATGAS: 292
- NZDCAD: 312
- NZDCHF: 312
- NZDJPY: 312
- NZDUSD: 312
- SILVER: 292
- SOLUSD: 410
- UK100: 117
- US30: 89
- US500: 125
- USDCAD: 312
- USDCHF: 311
- USDJPY: 448
- WTI: 291
- XRPUSD: 410

## 6. MR candidates / resolved
- 288 candidates, 0 resolved

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