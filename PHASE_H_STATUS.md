# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-25T17:12:38.063832

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
26

## 5. Observation count by asset
- ADAUSD: 432
- AUDCAD: 334
- AUDCHF: 334
- AUDJPY: 334
- AUDNZD: 334
- AUDUSD: 334
- AUS200: 98
- AVAXUSD: 432
- BCHUSD: 432
- BNBUSD: 432
- BRENT: 312
- BTCUSD: 630
- CADCHF: 334
- CADJPY: 334
- CHFJPY: 334
- DOGEUSD: 432
- DOTUSD: 432
- ETHUSD: 630
- EU50: 126
- EURAUD: 334
- EURCAD: 472
- EURCHF: 334
- EURGBP: 334
- EURJPY: 334
- EURUSD: 334
- FRA40: 126
- GBPAUD: 334
- GBPCAD: 334
- GBPCHF: 334
- GBPJPY: 334
- GBPUSD: 334
- GER40: 126
- GOLD: 432
- HK50: 98
- JPN225: 77
- LINKUSD: 432
- LTCUSD: 432
- NAS100: 94
- NATGAS: 313
- NZDCAD: 334
- NZDCHF: 334
- NZDJPY: 334
- NZDUSD: 334
- SILVER: 313
- SOLUSD: 432
- UK100: 126
- US30: 94
- US500: 130
- USDCAD: 334
- USDCHF: 333
- USDJPY: 470
- WTI: 312
- XRPUSD: 432

## 6. MR candidates / resolved
- 308 candidates, 0 resolved

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