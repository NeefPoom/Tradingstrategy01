# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-18T01:28:56.307851

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
79

## 5. Observation count by asset
- ADAUSD: 1712
- AUDCAD: 1221
- AUDCHF: 1221
- AUDJPY: 1220
- AUDNZD: 1221
- AUDUSD: 1221
- AUS200: 359
- AVAXUSD: 1712
- BCHUSD: 1712
- BNBUSD: 1712
- BRENT: 1169
- BTCUSD: 1910
- CADCHF: 1223
- CADJPY: 1220
- CHFJPY: 1220
- DOGEUSD: 1712
- DOTUSD: 1712
- ETHUSD: 1910
- EU50: 459
- EURAUD: 1220
- EURCAD: 1359
- EURCHF: 1220
- EURGBP: 1221
- EURJPY: 1219
- EURUSD: 1220
- FRA40: 459
- GBPAUD: 1221
- GBPCAD: 1221
- GBPCHF: 1221
- GBPJPY: 1220
- GBPUSD: 1221
- GER40: 459
- GOLD: 1292
- HK50: 343
- JPN225: 323
- LINKUSD: 1712
- LTCUSD: 1712
- NAS100: 357
- NATGAS: 1174
- NZDCAD: 1221
- NZDCHF: 1221
- NZDJPY: 1220
- NZDUSD: 1221
- SILVER: 1170
- SOLUSD: 1712
- UK100: 459
- US30: 357
- US500: 393
- USDCAD: 1222
- USDCHF: 1216
- USDJPY: 1351
- WTI: 1172
- XRPUSD: 1712

## 6. MR candidates / resolved
- 1504 candidates, 0 resolved

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