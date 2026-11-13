# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-13T22:14:42.787715

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
75

## 5. Observation count by asset
- ADAUSD: 1613
- AUDCAD: 1171
- AUDCHF: 1171
- AUDJPY: 1170
- AUDNZD: 1171
- AUDUSD: 1170
- AUS200: 343
- AVAXUSD: 1613
- BCHUSD: 1613
- BNBUSD: 1613
- BRENT: 1121
- BTCUSD: 1810
- CADCHF: 1172
- CADJPY: 1170
- CHFJPY: 1170
- DOGEUSD: 1613
- DOTUSD: 1613
- ETHUSD: 1810
- EU50: 441
- EURAUD: 1170
- EURCAD: 1308
- EURCHF: 1170
- EURGBP: 1171
- EURJPY: 1170
- EURUSD: 1169
- FRA40: 441
- GBPAUD: 1171
- GBPCAD: 1171
- GBPCHF: 1171
- GBPJPY: 1170
- GBPUSD: 1170
- GER40: 441
- GOLD: 1243
- HK50: 329
- JPN225: 308
- LINKUSD: 1613
- LTCUSD: 1613
- NAS100: 343
- NATGAS: 1126
- NZDCAD: 1171
- NZDCHF: 1171
- NZDJPY: 1170
- NZDUSD: 1170
- SILVER: 1122
- SOLUSD: 1613
- UK100: 441
- US30: 343
- US500: 379
- USDCAD: 1172
- USDCHF: 1166
- USDJPY: 1301
- WTI: 1123
- XRPUSD: 1613

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