# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-18T09:26:24.667416

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
79

## 5. Observation count by asset
- ADAUSD: 1720
- AUDCAD: 1229
- AUDCHF: 1229
- AUDJPY: 1228
- AUDNZD: 1229
- AUDUSD: 1229
- AUS200: 364
- AVAXUSD: 1720
- BCHUSD: 1720
- BNBUSD: 1720
- BRENT: 1177
- BTCUSD: 1918
- CADCHF: 1231
- CADJPY: 1228
- CHFJPY: 1228
- DOGEUSD: 1720
- DOTUSD: 1720
- ETHUSD: 1918
- EU50: 460
- EURAUD: 1228
- EURCAD: 1367
- EURCHF: 1228
- EURGBP: 1229
- EURJPY: 1227
- EURUSD: 1228
- FRA40: 460
- GBPAUD: 1229
- GBPCAD: 1229
- GBPCHF: 1229
- GBPJPY: 1228
- GBPUSD: 1229
- GER40: 460
- GOLD: 1300
- HK50: 350
- JPN225: 329
- LINKUSD: 1720
- LTCUSD: 1720
- NAS100: 357
- NATGAS: 1182
- NZDCAD: 1229
- NZDCHF: 1229
- NZDJPY: 1228
- NZDUSD: 1229
- SILVER: 1178
- SOLUSD: 1720
- UK100: 460
- US30: 357
- US500: 393
- USDCAD: 1230
- USDCHF: 1224
- USDJPY: 1359
- WTI: 1180
- XRPUSD: 1720

## 6. MR candidates / resolved
- 1508 candidates, 0 resolved

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