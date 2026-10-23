# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-23T17:57:55.385111

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
54

## 5. Observation count by asset
- ADAUSD: 1104
- AUDCAD: 810
- AUDCHF: 810
- AUDJPY: 810
- AUDNZD: 810
- AUDUSD: 810
- AUS200: 238
- AVAXUSD: 1104
- BCHUSD: 1104
- BNBUSD: 1104
- BRENT: 772
- BTCUSD: 1302
- CADCHF: 810
- CADJPY: 810
- CHFJPY: 810
- DOGEUSD: 1104
- DOTUSD: 1104
- ETHUSD: 1302
- EU50: 306
- EURAUD: 810
- EURCAD: 948
- EURCHF: 810
- EURGBP: 811
- EURJPY: 810
- EURUSD: 810
- FRA40: 306
- GBPAUD: 810
- GBPCAD: 810
- GBPCHF: 810
- GBPJPY: 810
- GBPUSD: 811
- GER40: 306
- GOLD: 894
- HK50: 224
- JPN225: 210
- LINKUSD: 1104
- LTCUSD: 1104
- NAS100: 235
- NATGAS: 776
- NZDCAD: 810
- NZDCHF: 810
- NZDJPY: 810
- NZDUSD: 810
- SILVER: 773
- SOLUSD: 1104
- UK100: 306
- US30: 235
- US500: 271
- USDCAD: 810
- USDCHF: 805
- USDJPY: 944
- WTI: 773
- XRPUSD: 1104

## 6. MR candidates / resolved
- 975 candidates, 0 resolved

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