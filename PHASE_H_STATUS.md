# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-13T07:34:34.294741

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
74

## 5. Observation count by asset
- ADAUSD: 1598
- AUDCAD: 1156
- AUDCHF: 1156
- AUDJPY: 1155
- AUDNZD: 1156
- AUDUSD: 1156
- AUS200: 343
- AVAXUSD: 1598
- BCHUSD: 1598
- BNBUSD: 1598
- BRENT: 1105
- BTCUSD: 1796
- CADCHF: 1157
- CADJPY: 1155
- CHFJPY: 1155
- DOGEUSD: 1598
- DOTUSD: 1598
- ETHUSD: 1796
- EU50: 432
- EURAUD: 1155
- EURCAD: 1294
- EURCHF: 1155
- EURGBP: 1156
- EURJPY: 1155
- EURUSD: 1155
- FRA40: 432
- GBPAUD: 1156
- GBPCAD: 1156
- GBPCHF: 1156
- GBPJPY: 1155
- GBPUSD: 1156
- GER40: 432
- GOLD: 1228
- HK50: 327
- JPN225: 308
- LINKUSD: 1598
- LTCUSD: 1598
- NAS100: 336
- NATGAS: 1110
- NZDCAD: 1156
- NZDCHF: 1156
- NZDJPY: 1155
- NZDUSD: 1156
- SILVER: 1106
- SOLUSD: 1598
- UK100: 432
- US30: 336
- US500: 372
- USDCAD: 1157
- USDCHF: 1151
- USDJPY: 1287
- WTI: 1107
- XRPUSD: 1598

## 6. MR candidates / resolved
- 1427 candidates, 0 resolved

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