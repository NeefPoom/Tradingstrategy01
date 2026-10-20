# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-20T06:42:52.176444

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
50

## 5. Observation count by asset
- ADAUSD: 1021
- AUDCAD: 727
- AUDCHF: 727
- AUDJPY: 727
- AUDNZD: 727
- AUDUSD: 727
- AUS200: 217
- AVAXUSD: 1021
- BCHUSD: 1021
- BNBUSD: 1021
- BRENT: 691
- BTCUSD: 1219
- CADCHF: 727
- CADJPY: 727
- CHFJPY: 727
- DOGEUSD: 1021
- DOTUSD: 1021
- ETHUSD: 1219
- EU50: 270
- EURAUD: 727
- EURCAD: 865
- EURCHF: 727
- EURGBP: 728
- EURJPY: 727
- EURUSD: 727
- FRA40: 270
- GBPAUD: 727
- GBPCAD: 727
- GBPCHF: 727
- GBPJPY: 727
- GBPUSD: 728
- GER40: 270
- GOLD: 814
- HK50: 201
- JPN225: 188
- LINKUSD: 1021
- LTCUSD: 1021
- NAS100: 210
- NATGAS: 695
- NZDCAD: 727
- NZDCHF: 727
- NZDJPY: 727
- NZDUSD: 727
- SILVER: 693
- SOLUSD: 1021
- UK100: 270
- US30: 210
- US500: 246
- USDCAD: 727
- USDCHF: 722
- USDJPY: 861
- WTI: 692
- XRPUSD: 1021

## 6. MR candidates / resolved
- 859 candidates, 0 resolved

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