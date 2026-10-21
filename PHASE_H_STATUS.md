# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-21T13:23:35.193086

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
52

## 5. Observation count by asset
- ADAUSD: 1052
- AUDCAD: 758
- AUDCHF: 758
- AUDJPY: 758
- AUDNZD: 758
- AUDUSD: 758
- AUS200: 224
- AVAXUSD: 1052
- BCHUSD: 1052
- BNBUSD: 1052
- BRENT: 722
- BTCUSD: 1250
- CADCHF: 758
- CADJPY: 758
- CHFJPY: 758
- DOGEUSD: 1052
- DOTUSD: 1052
- ETHUSD: 1250
- EU50: 285
- EURAUD: 758
- EURCAD: 896
- EURCHF: 758
- EURGBP: 759
- EURJPY: 758
- EURUSD: 758
- FRA40: 285
- GBPAUD: 758
- GBPCAD: 758
- GBPCHF: 758
- GBPJPY: 758
- GBPUSD: 759
- GER40: 285
- GOLD: 844
- HK50: 210
- JPN225: 196
- LINKUSD: 1052
- LTCUSD: 1052
- NAS100: 217
- NATGAS: 726
- NZDCAD: 758
- NZDCHF: 758
- NZDJPY: 758
- NZDUSD: 758
- SILVER: 723
- SOLUSD: 1052
- UK100: 285
- US30: 217
- US500: 253
- USDCAD: 758
- USDCHF: 753
- USDJPY: 892
- WTI: 723
- XRPUSD: 1052

## 6. MR candidates / resolved
- 901 candidates, 0 resolved

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