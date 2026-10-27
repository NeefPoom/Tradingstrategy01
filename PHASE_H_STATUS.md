# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-27T05:45:49.702138

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
57

## 5. Observation count by asset
- ADAUSD: 1188
- AUDCAD: 844
- AUDCHF: 844
- AUDJPY: 844
- AUDNZD: 844
- AUDUSD: 844
- AUS200: 251
- AVAXUSD: 1188
- BCHUSD: 1188
- BNBUSD: 1188
- BRENT: 805
- BTCUSD: 1386
- CADCHF: 844
- CADJPY: 844
- CHFJPY: 844
- DOGEUSD: 1188
- DOTUSD: 1188
- ETHUSD: 1386
- EU50: 315
- EURAUD: 844
- EURCAD: 982
- EURCHF: 844
- EURGBP: 845
- EURJPY: 844
- EURUSD: 844
- FRA40: 315
- GBPAUD: 844
- GBPCAD: 844
- GBPCHF: 844
- GBPJPY: 844
- GBPUSD: 845
- GER40: 315
- GOLD: 928
- HK50: 235
- JPN225: 222
- LINKUSD: 1188
- LTCUSD: 1188
- NAS100: 245
- NATGAS: 810
- NZDCAD: 844
- NZDCHF: 844
- NZDJPY: 844
- NZDUSD: 844
- SILVER: 807
- SOLUSD: 1188
- UK100: 315
- US30: 245
- US500: 281
- USDCAD: 844
- USDCHF: 839
- USDJPY: 977
- WTI: 806
- XRPUSD: 1188

## 6. MR candidates / resolved
- 1029 candidates, 0 resolved

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