# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-23T21:26:36.043130

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
54

## 5. Observation count by asset
- ADAUSD: 1108
- AUDCAD: 814
- AUDCHF: 814
- AUDJPY: 814
- AUDNZD: 814
- AUDUSD: 814
- AUS200: 238
- AVAXUSD: 1108
- BCHUSD: 1108
- BNBUSD: 1108
- BRENT: 776
- BTCUSD: 1306
- CADCHF: 814
- CADJPY: 814
- CHFJPY: 814
- DOGEUSD: 1108
- DOTUSD: 1108
- ETHUSD: 1306
- EU50: 306
- EURAUD: 814
- EURCAD: 952
- EURCHF: 814
- EURGBP: 815
- EURJPY: 814
- EURUSD: 814
- FRA40: 306
- GBPAUD: 814
- GBPCAD: 814
- GBPCHF: 814
- GBPJPY: 814
- GBPUSD: 815
- GER40: 306
- GOLD: 898
- HK50: 224
- JPN225: 210
- LINKUSD: 1108
- LTCUSD: 1108
- NAS100: 238
- NATGAS: 780
- NZDCAD: 814
- NZDCHF: 814
- NZDJPY: 814
- NZDUSD: 814
- SILVER: 777
- SOLUSD: 1108
- UK100: 306
- US30: 238
- US500: 274
- USDCAD: 814
- USDCHF: 809
- USDJPY: 948
- WTI: 777
- XRPUSD: 1108

## 6. MR candidates / resolved
- 976 candidates, 0 resolved

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