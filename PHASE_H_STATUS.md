# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-22T20:38:57.051024

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
53

## 5. Observation count by asset
- ADAUSD: 1083
- AUDCAD: 789
- AUDCHF: 789
- AUDJPY: 789
- AUDNZD: 789
- AUDUSD: 789
- AUS200: 231
- AVAXUSD: 1083
- BCHUSD: 1083
- BNBUSD: 1083
- BRENT: 752
- BTCUSD: 1281
- CADCHF: 789
- CADJPY: 789
- CHFJPY: 789
- DOGEUSD: 1083
- DOTUSD: 1083
- ETHUSD: 1281
- EU50: 297
- EURAUD: 789
- EURCAD: 927
- EURCHF: 789
- EURGBP: 790
- EURJPY: 789
- EURUSD: 789
- FRA40: 297
- GBPAUD: 789
- GBPCAD: 789
- GBPCHF: 789
- GBPJPY: 789
- GBPUSD: 790
- GER40: 297
- GOLD: 874
- HK50: 217
- JPN225: 203
- LINKUSD: 1083
- LTCUSD: 1083
- NAS100: 231
- NATGAS: 756
- NZDCAD: 789
- NZDCHF: 789
- NZDJPY: 789
- NZDUSD: 789
- SILVER: 753
- SOLUSD: 1083
- UK100: 297
- US30: 231
- US500: 267
- USDCAD: 789
- USDCHF: 784
- USDJPY: 923
- WTI: 753
- XRPUSD: 1083

## 6. MR candidates / resolved
- 939 candidates, 0 resolved

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