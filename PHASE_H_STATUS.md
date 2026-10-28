# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-28T00:35:09.906691

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
58

## 5. Observation count by asset
- ADAUSD: 1207
- AUDCAD: 862
- AUDCHF: 862
- AUDJPY: 862
- AUDNZD: 862
- AUDUSD: 862
- AUS200: 253
- AVAXUSD: 1207
- BCHUSD: 1207
- BNBUSD: 1207
- BRENT: 824
- BTCUSD: 1405
- CADCHF: 862
- CADJPY: 862
- CHFJPY: 862
- DOGEUSD: 1207
- DOTUSD: 1207
- ETHUSD: 1405
- EU50: 324
- EURAUD: 862
- EURCAD: 1000
- EURCHF: 862
- EURGBP: 863
- EURJPY: 862
- EURUSD: 862
- FRA40: 324
- GBPAUD: 862
- GBPCAD: 862
- GBPCHF: 862
- GBPJPY: 862
- GBPUSD: 863
- GER40: 324
- GOLD: 946
- HK50: 238
- JPN225: 224
- LINKUSD: 1207
- LTCUSD: 1207
- NAS100: 252
- NATGAS: 829
- NZDCAD: 862
- NZDCHF: 862
- NZDJPY: 862
- NZDUSD: 862
- SILVER: 825
- SOLUSD: 1207
- UK100: 324
- US30: 252
- US500: 288
- USDCAD: 862
- USDCHF: 857
- USDJPY: 995
- WTI: 825
- XRPUSD: 1207

## 6. MR candidates / resolved
- 1048 candidates, 0 resolved

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