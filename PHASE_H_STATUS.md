# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-29T10:02:28.408030

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
59

## 5. Observation count by asset
- ADAUSD: 1240
- AUDCAD: 896
- AUDCHF: 896
- AUDJPY: 896
- AUDNZD: 896
- AUDUSD: 896
- AUS200: 266
- AVAXUSD: 1241
- BCHUSD: 1240
- BNBUSD: 1241
- BRENT: 856
- BTCUSD: 1438
- CADCHF: 896
- CADJPY: 896
- CHFJPY: 896
- DOGEUSD: 1240
- DOTUSD: 1241
- ETHUSD: 1438
- EU50: 334
- EURAUD: 896
- EURCAD: 1034
- EURCHF: 896
- EURGBP: 897
- EURJPY: 896
- EURUSD: 896
- FRA40: 334
- GBPAUD: 896
- GBPCAD: 896
- GBPCHF: 896
- GBPJPY: 896
- GBPUSD: 897
- GER40: 334
- GOLD: 978
- HK50: 252
- JPN225: 238
- LINKUSD: 1241
- LTCUSD: 1240
- NAS100: 259
- NATGAS: 861
- NZDCAD: 896
- NZDCHF: 896
- NZDJPY: 896
- NZDUSD: 896
- SILVER: 857
- SOLUSD: 1240
- UK100: 334
- US30: 259
- US500: 295
- USDCAD: 896
- USDCHF: 891
- USDJPY: 1029
- WTI: 857
- XRPUSD: 1240

## 6. MR candidates / resolved
- 1098 candidates, 0 resolved

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