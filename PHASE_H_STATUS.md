# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-17T01:22:41.312517

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
78

## 5. Observation count by asset
- ADAUSD: 1688
- AUDCAD: 1197
- AUDCHF: 1197
- AUDJPY: 1196
- AUDNZD: 1197
- AUDUSD: 1197
- AUS200: 352
- AVAXUSD: 1688
- BCHUSD: 1688
- BNBUSD: 1688
- BRENT: 1146
- BTCUSD: 1886
- CADCHF: 1199
- CADJPY: 1196
- CHFJPY: 1196
- DOGEUSD: 1688
- DOTUSD: 1688
- ETHUSD: 1886
- EU50: 450
- EURAUD: 1196
- EURCAD: 1335
- EURCHF: 1196
- EURGBP: 1197
- EURJPY: 1195
- EURUSD: 1196
- FRA40: 450
- GBPAUD: 1197
- GBPCAD: 1197
- GBPCHF: 1197
- GBPJPY: 1196
- GBPUSD: 1197
- GER40: 450
- GOLD: 1269
- HK50: 336
- JPN225: 316
- LINKUSD: 1688
- LTCUSD: 1688
- NAS100: 350
- NATGAS: 1151
- NZDCAD: 1197
- NZDCHF: 1197
- NZDJPY: 1196
- NZDUSD: 1197
- SILVER: 1147
- SOLUSD: 1688
- UK100: 450
- US30: 350
- US500: 386
- USDCAD: 1198
- USDCHF: 1192
- USDJPY: 1327
- WTI: 1149
- XRPUSD: 1688

## 6. MR candidates / resolved
- 1477 candidates, 0 resolved

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