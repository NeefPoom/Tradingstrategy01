# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-27T21:07:00.785728

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
58

## 5. Observation count by asset
- ADAUSD: 1204
- AUDCAD: 860
- AUDCHF: 860
- AUDJPY: 859
- AUDNZD: 860
- AUDUSD: 859
- AUS200: 252
- AVAXUSD: 1204
- BCHUSD: 1204
- BNBUSD: 1204
- BRENT: 822
- BTCUSD: 1401
- CADCHF: 860
- CADJPY: 859
- CHFJPY: 859
- DOGEUSD: 1204
- DOTUSD: 1204
- ETHUSD: 1401
- EU50: 324
- EURAUD: 859
- EURCAD: 997
- EURCHF: 859
- EURGBP: 860
- EURJPY: 859
- EURUSD: 859
- FRA40: 324
- GBPAUD: 860
- GBPCAD: 860
- GBPCHF: 860
- GBPJPY: 859
- GBPUSD: 860
- GER40: 324
- GOLD: 943
- HK50: 238
- JPN225: 224
- LINKUSD: 1204
- LTCUSD: 1204
- NAS100: 252
- NATGAS: 827
- NZDCAD: 860
- NZDCHF: 860
- NZDJPY: 860
- NZDUSD: 859
- SILVER: 823
- SOLUSD: 1204
- UK100: 324
- US30: 252
- US500: 288
- USDCAD: 859
- USDCHF: 854
- USDJPY: 992
- WTI: 823
- XRPUSD: 1204

## 6. MR candidates / resolved
- 1047 candidates, 0 resolved

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