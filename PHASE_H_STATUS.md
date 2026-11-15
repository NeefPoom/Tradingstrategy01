# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-15T15:42:02.022033

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
77

## 5. Observation count by asset
- ADAUSD: 1654
- AUDCAD: 1172
- AUDCHF: 1172
- AUDJPY: 1171
- AUDNZD: 1172
- AUDUSD: 1172
- AUS200: 343
- AVAXUSD: 1654
- BCHUSD: 1654
- BNBUSD: 1654
- BRENT: 1121
- BTCUSD: 1852
- CADCHF: 1174
- CADJPY: 1171
- CHFJPY: 1171
- DOGEUSD: 1654
- DOTUSD: 1654
- ETHUSD: 1852
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
- LINKUSD: 1654
- LTCUSD: 1654
- NAS100: 343
- NATGAS: 1126
- NZDCAD: 1172
- NZDCHF: 1172
- NZDJPY: 1171
- NZDUSD: 1172
- SILVER: 1122
- SOLUSD: 1654
- UK100: 441
- US30: 343
- US500: 379
- USDCAD: 1173
- USDCHF: 1167
- USDJPY: 1302
- WTI: 1124
- XRPUSD: 1654

## 6. MR candidates / resolved
- 1461 candidates, 0 resolved

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