# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-13T00:18:23.639038

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
74

## 5. Observation count by asset
- ADAUSD: 1589
- AUDCAD: 1147
- AUDCHF: 1147
- AUDJPY: 1146
- AUDNZD: 1147
- AUDUSD: 1147
- AUS200: 337
- AVAXUSD: 1589
- BCHUSD: 1589
- BNBUSD: 1589
- BRENT: 1099
- BTCUSD: 1787
- CADCHF: 1148
- CADJPY: 1146
- CHFJPY: 1146
- DOGEUSD: 1589
- DOTUSD: 1589
- ETHUSD: 1787
- EU50: 432
- EURAUD: 1146
- EURCAD: 1285
- EURCHF: 1146
- EURGBP: 1147
- EURJPY: 1146
- EURUSD: 1146
- FRA40: 432
- GBPAUD: 1147
- GBPCAD: 1147
- GBPCHF: 1147
- GBPJPY: 1146
- GBPUSD: 1147
- GER40: 432
- GOLD: 1222
- HK50: 322
- JPN225: 301
- LINKUSD: 1589
- LTCUSD: 1589
- NAS100: 336
- NATGAS: 1104
- NZDCAD: 1147
- NZDCHF: 1147
- NZDJPY: 1146
- NZDUSD: 1147
- SILVER: 1100
- SOLUSD: 1589
- UK100: 432
- US30: 336
- US500: 372
- USDCAD: 1148
- USDCHF: 1142
- USDJPY: 1278
- WTI: 1101
- XRPUSD: 1589

## 6. MR candidates / resolved
- 1422 candidates, 0 resolved

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