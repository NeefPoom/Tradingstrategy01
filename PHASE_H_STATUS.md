# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-21T19:27:36.983291

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
22

## 5. Observation count by asset
- ADAUSD: 338
- AUDCAD: 240
- AUDCHF: 240
- AUDJPY: 240
- AUDNZD: 240
- AUDUSD: 240
- AUS200: 70
- AVAXUSD: 338
- BCHUSD: 338
- BNBUSD: 338
- BRENT: 222
- BTCUSD: 536
- CADCHF: 240
- CADJPY: 240
- CHFJPY: 240
- DOGEUSD: 338
- DOTUSD: 338
- ETHUSD: 536
- EU50: 90
- EURAUD: 240
- EURCAD: 378
- EURCHF: 240
- EURGBP: 240
- EURJPY: 240
- EURUSD: 240
- FRA40: 90
- GBPAUD: 240
- GBPCAD: 240
- GBPCHF: 240
- GBPJPY: 240
- GBPUSD: 240
- GER40: 90
- GOLD: 341
- HK50: 70
- JPN225: 63
- LINKUSD: 338
- LTCUSD: 338
- NAS100: 68
- NATGAS: 223
- NZDCAD: 240
- NZDCHF: 240
- NZDJPY: 240
- NZDUSD: 240
- SILVER: 222
- SOLUSD: 338
- UK100: 90
- US30: 68
- US500: 104
- USDCAD: 240
- USDCHF: 239
- USDJPY: 376
- WTI: 222
- XRPUSD: 338

## 6. MR candidates / resolved
- 201 candidates, 0 resolved

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