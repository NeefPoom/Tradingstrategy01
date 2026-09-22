# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-22T23:19:29.012266

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
23

## 5. Observation count by asset
- ADAUSD: 366
- AUDCAD: 268
- AUDCHF: 268
- AUDJPY: 268
- AUDNZD: 268
- AUDUSD: 268
- AUS200: 77
- AVAXUSD: 366
- BCHUSD: 366
- BNBUSD: 366
- BRENT: 248
- BTCUSD: 564
- CADCHF: 268
- CADJPY: 268
- CHFJPY: 268
- DOGEUSD: 366
- DOTUSD: 366
- ETHUSD: 564
- EU50: 99
- EURAUD: 268
- EURCAD: 406
- EURCHF: 268
- EURGBP: 268
- EURJPY: 268
- EURUSD: 268
- FRA40: 99
- GBPAUD: 268
- GBPCAD: 268
- GBPCHF: 268
- GBPJPY: 268
- GBPUSD: 268
- GER40: 99
- GOLD: 367
- HK50: 77
- JPN225: 63
- LINKUSD: 366
- LTCUSD: 366
- NAS100: 77
- NATGAS: 249
- NZDCAD: 268
- NZDCHF: 268
- NZDJPY: 268
- NZDUSD: 268
- SILVER: 249
- SOLUSD: 366
- UK100: 99
- US30: 77
- US500: 113
- USDCAD: 268
- USDCHF: 267
- USDJPY: 404
- WTI: 248
- XRPUSD: 366

## 6. MR candidates / resolved
- 231 candidates, 0 resolved

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