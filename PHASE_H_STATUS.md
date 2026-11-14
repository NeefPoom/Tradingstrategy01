# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-14T02:25:41.767195

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
75

## 5. Observation count by asset
- ADAUSD: 1617
- AUDCAD: 1172
- AUDCHF: 1172
- AUDJPY: 1171
- AUDNZD: 1172
- AUDUSD: 1172
- AUS200: 343
- AVAXUSD: 1617
- BCHUSD: 1617
- BNBUSD: 1617
- BRENT: 1121
- BTCUSD: 1815
- CADCHF: 1174
- CADJPY: 1171
- CHFJPY: 1171
- DOGEUSD: 1617
- DOTUSD: 1617
- ETHUSD: 1815
- EU50: 441
- EURAUD: 1171
- EURCAD: 1310
- EURCHF: 1171
- EURGBP: 1172
- EURJPY: 1170
- EURUSD: 1171
- FRA40: 441
- GBPAUD: 1172
- GBPCAD: 1172
- GBPCHF: 1172
- GBPJPY: 1171
- GBPUSD: 1172
- GER40: 441
- GOLD: 1244
- HK50: 329
- JPN225: 308
- LINKUSD: 1617
- LTCUSD: 1617
- NAS100: 343
- NATGAS: 1126
- NZDCAD: 1172
- NZDCHF: 1172
- NZDJPY: 1171
- NZDUSD: 1172
- SILVER: 1122
- SOLUSD: 1617
- UK100: 441
- US30: 343
- US500: 379
- USDCAD: 1173
- USDCHF: 1167
- USDJPY: 1302
- WTI: 1124
- XRPUSD: 1617

## 6. MR candidates / resolved
- 1448 candidates, 0 resolved

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