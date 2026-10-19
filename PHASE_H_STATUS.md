# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-19T00:15:14.262335

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
49

## 5. Observation count by asset
- ADAUSD: 990
- AUDCAD: 697
- AUDCHF: 697
- AUDJPY: 697
- AUDNZD: 697
- AUDUSD: 697
- AUS200: 204
- AVAXUSD: 990
- BCHUSD: 990
- BNBUSD: 990
- BRENT: 663
- BTCUSD: 1188
- CADCHF: 697
- CADJPY: 697
- CHFJPY: 697
- DOGEUSD: 990
- DOTUSD: 990
- ETHUSD: 1188
- EU50: 261
- EURAUD: 697
- EURCAD: 835
- EURCHF: 697
- EURGBP: 698
- EURJPY: 697
- EURUSD: 697
- FRA40: 261
- GBPAUD: 697
- GBPCAD: 697
- GBPCHF: 697
- GBPJPY: 697
- GBPUSD: 698
- GER40: 261
- GOLD: 785
- HK50: 196
- JPN225: 175
- LINKUSD: 990
- LTCUSD: 990
- NAS100: 203
- NATGAS: 667
- NZDCAD: 697
- NZDCHF: 697
- NZDJPY: 697
- NZDUSD: 697
- SILVER: 664
- SOLUSD: 990
- UK100: 261
- US30: 203
- US500: 239
- USDCAD: 697
- USDCHF: 692
- USDJPY: 831
- WTI: 664
- XRPUSD: 990

## 6. MR candidates / resolved
- 818 candidates, 0 resolved

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