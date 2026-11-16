# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-16T07:28:57.612492

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
77

## 5. Observation count by asset
- ADAUSD: 1670
- AUDCAD: 1179
- AUDCHF: 1179
- AUDJPY: 1178
- AUDNZD: 1179
- AUDUSD: 1179
- AUS200: 350
- AVAXUSD: 1670
- BCHUSD: 1670
- BNBUSD: 1670
- BRENT: 1127
- BTCUSD: 1868
- CADCHF: 1181
- CADJPY: 1178
- CHFJPY: 1178
- DOGEUSD: 1670
- DOTUSD: 1670
- ETHUSD: 1868
- EU50: 441
- EURAUD: 1178
- EURCAD: 1317
- EURCHF: 1178
- EURGBP: 1179
- EURJPY: 1177
- EURUSD: 1178
- FRA40: 441
- GBPAUD: 1179
- GBPCAD: 1179
- GBPCHF: 1179
- GBPJPY: 1178
- GBPUSD: 1179
- GER40: 441
- GOLD: 1251
- HK50: 334
- JPN225: 315
- LINKUSD: 1670
- LTCUSD: 1670
- NAS100: 343
- NATGAS: 1132
- NZDCAD: 1179
- NZDCHF: 1179
- NZDJPY: 1178
- NZDUSD: 1179
- SILVER: 1129
- SOLUSD: 1670
- UK100: 441
- US30: 343
- US500: 379
- USDCAD: 1180
- USDCHF: 1174
- USDJPY: 1309
- WTI: 1130
- XRPUSD: 1670

## 6. MR candidates / resolved
- 1467 candidates, 0 resolved

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