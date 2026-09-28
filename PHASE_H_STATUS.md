# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-28T05:20:02.637646

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
28

## 5. Observation count by asset
- ADAUSD: 492
- AUDCAD: 345
- AUDCHF: 345
- AUDJPY: 345
- AUDNZD: 345
- AUDUSD: 345
- AUS200: 103
- AVAXUSD: 492
- BCHUSD: 492
- BNBUSD: 492
- BRENT: 321
- BTCUSD: 690
- CADCHF: 345
- CADJPY: 345
- CHFJPY: 345
- DOGEUSD: 492
- DOTUSD: 492
- ETHUSD: 690
- EU50: 126
- EURAUD: 345
- EURCAD: 483
- EURCHF: 345
- EURGBP: 345
- EURJPY: 345
- EURUSD: 345
- FRA40: 126
- GBPAUD: 345
- GBPCAD: 345
- GBPCHF: 345
- GBPJPY: 345
- GBPUSD: 345
- GER40: 126
- GOLD: 441
- HK50: 101
- JPN225: 82
- LINKUSD: 492
- LTCUSD: 492
- NAS100: 98
- NATGAS: 322
- NZDCAD: 345
- NZDCHF: 345
- NZDJPY: 345
- NZDUSD: 345
- SILVER: 322
- SOLUSD: 492
- UK100: 126
- US30: 98
- US500: 134
- USDCAD: 345
- USDCHF: 343
- USDJPY: 481
- WTI: 321
- XRPUSD: 492

## 6. MR candidates / resolved
- 334 candidates, 0 resolved

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