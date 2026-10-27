# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-27T11:01:48.606584

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
57

## 5. Observation count by asset
- ADAUSD: 1193
- AUDCAD: 849
- AUDCHF: 849
- AUDJPY: 849
- AUDNZD: 849
- AUDUSD: 849
- AUS200: 252
- AVAXUSD: 1194
- BCHUSD: 1194
- BNBUSD: 1194
- BRENT: 811
- BTCUSD: 1391
- CADCHF: 849
- CADJPY: 849
- CHFJPY: 849
- DOGEUSD: 1193
- DOTUSD: 1194
- ETHUSD: 1391
- EU50: 317
- EURAUD: 849
- EURCAD: 987
- EURCHF: 849
- EURGBP: 850
- EURJPY: 849
- EURUSD: 849
- FRA40: 317
- GBPAUD: 849
- GBPCAD: 849
- GBPCHF: 849
- GBPJPY: 849
- GBPUSD: 850
- GER40: 317
- GOLD: 933
- HK50: 238
- JPN225: 224
- LINKUSD: 1194
- LTCUSD: 1194
- NAS100: 245
- NATGAS: 816
- NZDCAD: 849
- NZDCHF: 849
- NZDJPY: 849
- NZDUSD: 849
- SILVER: 812
- SOLUSD: 1193
- UK100: 317
- US30: 245
- US500: 281
- USDCAD: 849
- USDCHF: 844
- USDJPY: 982
- WTI: 812
- XRPUSD: 1193

## 6. MR candidates / resolved
- 1031 candidates, 0 resolved

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