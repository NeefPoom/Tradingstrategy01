# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-24T19:30:20.846271

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
55

## 5. Observation count by asset
- ADAUSD: 1130
- AUDCAD: 815
- AUDCHF: 815
- AUDJPY: 815
- AUDNZD: 815
- AUDUSD: 815
- AUS200: 238
- AVAXUSD: 1130
- BCHUSD: 1130
- BNBUSD: 1130
- BRENT: 776
- BTCUSD: 1328
- CADCHF: 815
- CADJPY: 815
- CHFJPY: 815
- DOGEUSD: 1130
- DOTUSD: 1130
- ETHUSD: 1328
- EU50: 306
- EURAUD: 815
- EURCAD: 953
- EURCHF: 815
- EURGBP: 816
- EURJPY: 815
- EURUSD: 815
- FRA40: 306
- GBPAUD: 815
- GBPCAD: 815
- GBPCHF: 815
- GBPJPY: 815
- GBPUSD: 816
- GER40: 306
- GOLD: 898
- HK50: 224
- JPN225: 210
- LINKUSD: 1130
- LTCUSD: 1130
- NAS100: 238
- NATGAS: 781
- NZDCAD: 815
- NZDCHF: 815
- NZDJPY: 815
- NZDUSD: 815
- SILVER: 777
- SOLUSD: 1130
- UK100: 306
- US30: 238
- US500: 274
- USDCAD: 815
- USDCHF: 810
- USDJPY: 948
- WTI: 777
- XRPUSD: 1130

## 6. MR candidates / resolved
- 980 candidates, 0 resolved

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