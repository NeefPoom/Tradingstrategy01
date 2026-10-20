# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-20T23:30:14.176521

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
51

## 5. Observation count by asset
- ADAUSD: 1038
- AUDCAD: 744
- AUDCHF: 744
- AUDJPY: 744
- AUDNZD: 744
- AUDUSD: 744
- AUS200: 217
- AVAXUSD: 1038
- BCHUSD: 1038
- BNBUSD: 1038
- BRENT: 708
- BTCUSD: 1236
- CADCHF: 744
- CADJPY: 744
- CHFJPY: 744
- DOGEUSD: 1038
- DOTUSD: 1038
- ETHUSD: 1236
- EU50: 279
- EURAUD: 744
- EURCAD: 882
- EURCHF: 744
- EURGBP: 745
- EURJPY: 744
- EURUSD: 744
- FRA40: 279
- GBPAUD: 744
- GBPCAD: 744
- GBPCHF: 744
- GBPJPY: 744
- GBPUSD: 745
- GER40: 279
- GOLD: 830
- HK50: 203
- JPN225: 189
- LINKUSD: 1038
- LTCUSD: 1038
- NAS100: 217
- NATGAS: 712
- NZDCAD: 744
- NZDCHF: 744
- NZDJPY: 744
- NZDUSD: 744
- SILVER: 709
- SOLUSD: 1038
- UK100: 279
- US30: 217
- US500: 253
- USDCAD: 744
- USDCHF: 739
- USDJPY: 878
- WTI: 709
- XRPUSD: 1038

## 6. MR candidates / resolved
- 887 candidates, 0 resolved

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