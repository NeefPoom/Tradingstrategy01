# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-17T18:54:02.425245

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
79

## 5. Observation count by asset
- ADAUSD: 1705
- AUDCAD: 1214
- AUDCHF: 1214
- AUDJPY: 1213
- AUDNZD: 1214
- AUDUSD: 1214
- AUS200: 357
- AVAXUSD: 1705
- BCHUSD: 1705
- BNBUSD: 1705
- BRENT: 1163
- BTCUSD: 1903
- CADCHF: 1216
- CADJPY: 1213
- CHFJPY: 1213
- DOGEUSD: 1705
- DOTUSD: 1705
- ETHUSD: 1903
- EU50: 459
- EURAUD: 1213
- EURCAD: 1352
- EURCHF: 1213
- EURGBP: 1214
- EURJPY: 1212
- EURUSD: 1213
- FRA40: 459
- GBPAUD: 1214
- GBPCAD: 1214
- GBPCHF: 1214
- GBPJPY: 1213
- GBPUSD: 1214
- GER40: 459
- GOLD: 1286
- HK50: 343
- JPN225: 322
- LINKUSD: 1705
- LTCUSD: 1705
- NAS100: 354
- NATGAS: 1168
- NZDCAD: 1214
- NZDCHF: 1214
- NZDJPY: 1213
- NZDUSD: 1214
- SILVER: 1164
- SOLUSD: 1705
- UK100: 459
- US30: 354
- US500: 390
- USDCAD: 1215
- USDCHF: 1209
- USDJPY: 1344
- WTI: 1166
- XRPUSD: 1705

## 6. MR candidates / resolved
- 1497 candidates, 0 resolved

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