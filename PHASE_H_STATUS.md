# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-16T17:50:37.234363

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
78

## 5. Observation count by asset
- ADAUSD: 1680
- AUDCAD: 1189
- AUDCHF: 1189
- AUDJPY: 1188
- AUDNZD: 1189
- AUDUSD: 1189
- AUS200: 350
- AVAXUSD: 1680
- BCHUSD: 1680
- BNBUSD: 1680
- BRENT: 1139
- BTCUSD: 1878
- CADCHF: 1191
- CADJPY: 1188
- CHFJPY: 1188
- DOGEUSD: 1680
- DOTUSD: 1680
- ETHUSD: 1878
- EU50: 450
- EURAUD: 1188
- EURCAD: 1327
- EURCHF: 1188
- EURGBP: 1189
- EURJPY: 1187
- EURUSD: 1188
- FRA40: 450
- GBPAUD: 1189
- GBPCAD: 1189
- GBPCHF: 1189
- GBPJPY: 1188
- GBPUSD: 1189
- GER40: 450
- GOLD: 1262
- HK50: 336
- JPN225: 315
- LINKUSD: 1680
- LTCUSD: 1680
- NAS100: 346
- NATGAS: 1144
- NZDCAD: 1189
- NZDCHF: 1189
- NZDJPY: 1188
- NZDUSD: 1189
- SILVER: 1140
- SOLUSD: 1680
- UK100: 450
- US30: 346
- US500: 381
- USDCAD: 1190
- USDCHF: 1184
- USDJPY: 1319
- WTI: 1142
- XRPUSD: 1680

## 6. MR candidates / resolved
- 1476 candidates, 0 resolved

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