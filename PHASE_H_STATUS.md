# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-16T05:07:14.474314

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
46

## 5. Observation count by asset
- ADAUSD: 924
- AUDCAD: 679
- AUDCHF: 679
- AUDJPY: 678
- AUDNZD: 679
- AUDUSD: 678
- AUS200: 202
- AVAXUSD: 924
- BCHUSD: 924
- BNBUSD: 924
- BRENT: 645
- BTCUSD: 1121
- CADCHF: 679
- CADJPY: 678
- CHFJPY: 678
- DOGEUSD: 924
- DOTUSD: 924
- ETHUSD: 1121
- EU50: 252
- EURAUD: 679
- EURCAD: 816
- EURCHF: 679
- EURGBP: 680
- EURJPY: 678
- EURUSD: 678
- FRA40: 252
- GBPAUD: 679
- GBPCAD: 679
- GBPCHF: 679
- GBPJPY: 678
- GBPUSD: 678
- GER40: 252
- GOLD: 766
- HK50: 192
- JPN225: 173
- LINKUSD: 924
- LTCUSD: 924
- NAS100: 196
- NATGAS: 649
- NZDCAD: 679
- NZDCHF: 679
- NZDJPY: 679
- NZDUSD: 678
- SILVER: 646
- SOLUSD: 924
- UK100: 252
- US30: 196
- US500: 232
- USDCAD: 678
- USDCHF: 674
- USDJPY: 813
- WTI: 646
- XRPUSD: 924

## 6. MR candidates / resolved
- 789 candidates, 0 resolved

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