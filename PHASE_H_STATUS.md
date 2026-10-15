# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-15T21:53:14.139668

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
46

## 5. Observation count by asset
- ADAUSD: 916
- AUDCAD: 671
- AUDCHF: 671
- AUDJPY: 671
- AUDNZD: 671
- AUDUSD: 671
- AUS200: 196
- AVAXUSD: 916
- BCHUSD: 916
- BNBUSD: 916
- BRENT: 638
- BTCUSD: 1114
- CADCHF: 671
- CADJPY: 671
- CHFJPY: 671
- DOGEUSD: 916
- DOTUSD: 916
- ETHUSD: 1114
- EU50: 252
- EURAUD: 671
- EURCAD: 809
- EURCHF: 671
- EURGBP: 672
- EURJPY: 671
- EURUSD: 671
- FRA40: 252
- GBPAUD: 671
- GBPCAD: 671
- GBPCHF: 671
- GBPJPY: 671
- GBPUSD: 671
- GER40: 252
- GOLD: 760
- HK50: 189
- JPN225: 168
- LINKUSD: 916
- LTCUSD: 916
- NAS100: 196
- NATGAS: 642
- NZDCAD: 671
- NZDCHF: 671
- NZDJPY: 671
- NZDUSD: 671
- SILVER: 639
- SOLUSD: 916
- UK100: 252
- US30: 196
- US500: 232
- USDCAD: 671
- USDCHF: 667
- USDJPY: 806
- WTI: 639
- XRPUSD: 916

## 6. MR candidates / resolved
- 779 candidates, 0 resolved

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