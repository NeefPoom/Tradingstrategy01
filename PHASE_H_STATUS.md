# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-26T01:43:41.169888

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
56

## 5. Observation count by asset
- ADAUSD: 1160
- AUDCAD: 816
- AUDCHF: 816
- AUDJPY: 816
- AUDNZD: 816
- AUDUSD: 816
- AUS200: 240
- AVAXUSD: 1160
- BCHUSD: 1160
- BNBUSD: 1160
- BRENT: 779
- BTCUSD: 1358
- CADCHF: 816
- CADJPY: 816
- CHFJPY: 816
- DOGEUSD: 1160
- DOTUSD: 1160
- ETHUSD: 1358
- EU50: 306
- EURAUD: 816
- EURCAD: 954
- EURCHF: 816
- EURGBP: 817
- EURJPY: 816
- EURUSD: 816
- FRA40: 306
- GBPAUD: 816
- GBPCAD: 816
- GBPCHF: 816
- GBPJPY: 816
- GBPUSD: 817
- GER40: 306
- GOLD: 901
- HK50: 224
- JPN225: 211
- LINKUSD: 1160
- LTCUSD: 1160
- NAS100: 238
- NATGAS: 784
- NZDCAD: 816
- NZDCHF: 816
- NZDJPY: 816
- NZDUSD: 816
- SILVER: 780
- SOLUSD: 1160
- UK100: 306
- US30: 238
- US500: 274
- USDCAD: 816
- USDCHF: 811
- USDJPY: 949
- WTI: 780
- XRPUSD: 1160

## 6. MR candidates / resolved
- 996 candidates, 0 resolved

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