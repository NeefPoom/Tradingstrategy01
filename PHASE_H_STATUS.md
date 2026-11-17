# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-17T09:27:09.058493

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
78

## 5. Observation count by asset
- ADAUSD: 1696
- AUDCAD: 1205
- AUDCHF: 1205
- AUDJPY: 1204
- AUDNZD: 1205
- AUDUSD: 1205
- AUS200: 357
- AVAXUSD: 1696
- BCHUSD: 1696
- BNBUSD: 1696
- BRENT: 1154
- BTCUSD: 1894
- CADCHF: 1207
- CADJPY: 1204
- CHFJPY: 1204
- DOGEUSD: 1696
- DOTUSD: 1696
- ETHUSD: 1894
- EU50: 451
- EURAUD: 1204
- EURCAD: 1343
- EURCHF: 1204
- EURGBP: 1205
- EURJPY: 1203
- EURUSD: 1204
- FRA40: 451
- GBPAUD: 1205
- GBPCAD: 1205
- GBPCHF: 1205
- GBPJPY: 1204
- GBPUSD: 1205
- GER40: 451
- GOLD: 1277
- HK50: 343
- JPN225: 322
- LINKUSD: 1696
- LTCUSD: 1696
- NAS100: 350
- NATGAS: 1159
- NZDCAD: 1205
- NZDCHF: 1205
- NZDJPY: 1204
- NZDUSD: 1205
- SILVER: 1155
- SOLUSD: 1696
- UK100: 451
- US30: 350
- US500: 386
- USDCAD: 1206
- USDCHF: 1200
- USDJPY: 1335
- WTI: 1157
- XRPUSD: 1696

## 6. MR candidates / resolved
- 1484 candidates, 0 resolved

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