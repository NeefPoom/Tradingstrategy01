# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-12T19:06:39.326172

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
74

## 5. Observation count by asset
- ADAUSD: 1586
- AUDCAD: 1143
- AUDCHF: 1143
- AUDJPY: 1142
- AUDNZD: 1143
- AUDUSD: 1143
- AUS200: 336
- AVAXUSD: 1586
- BCHUSD: 1586
- BNBUSD: 1586
- BRENT: 1095
- BTCUSD: 1783
- CADCHF: 1144
- CADJPY: 1142
- CHFJPY: 1142
- DOGEUSD: 1586
- DOTUSD: 1586
- ETHUSD: 1783
- EU50: 432
- EURAUD: 1142
- EURCAD: 1281
- EURCHF: 1142
- EURGBP: 1143
- EURJPY: 1142
- EURUSD: 1142
- FRA40: 432
- GBPAUD: 1143
- GBPCAD: 1143
- GBPCHF: 1143
- GBPJPY: 1142
- GBPUSD: 1143
- GER40: 432
- GOLD: 1217
- HK50: 322
- JPN225: 301
- LINKUSD: 1586
- LTCUSD: 1586
- NAS100: 333
- NATGAS: 1100
- NZDCAD: 1143
- NZDCHF: 1143
- NZDJPY: 1142
- NZDUSD: 1143
- SILVER: 1095
- SOLUSD: 1586
- UK100: 432
- US30: 333
- US500: 369
- USDCAD: 1144
- USDCHF: 1138
- USDJPY: 1274
- WTI: 1096
- XRPUSD: 1586

## 6. MR candidates / resolved
- 1421 candidates, 0 resolved

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