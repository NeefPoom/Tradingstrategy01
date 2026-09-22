# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-22T12:40:48.926927

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
23

## 5. Observation count by asset
- ADAUSD: 355
- AUDCAD: 257
- AUDCHF: 257
- AUDJPY: 257
- AUDNZD: 257
- AUDUSD: 257
- AUS200: 77
- AVAXUSD: 355
- BCHUSD: 355
- BNBUSD: 355
- BRENT: 238
- BTCUSD: 553
- CADCHF: 257
- CADJPY: 257
- CHFJPY: 257
- DOGEUSD: 355
- DOTUSD: 355
- ETHUSD: 553
- EU50: 95
- EURAUD: 257
- EURCAD: 395
- EURCHF: 257
- EURGBP: 257
- EURJPY: 257
- EURUSD: 257
- FRA40: 95
- GBPAUD: 257
- GBPCAD: 257
- GBPCHF: 257
- GBPJPY: 257
- GBPUSD: 257
- GER40: 95
- GOLD: 357
- HK50: 77
- JPN225: 63
- LINKUSD: 355
- LTCUSD: 355
- NAS100: 70
- NATGAS: 239
- NZDCAD: 257
- NZDCHF: 257
- NZDJPY: 257
- NZDUSD: 257
- SILVER: 239
- SOLUSD: 355
- UK100: 95
- US30: 70
- US500: 106
- USDCAD: 257
- USDCHF: 256
- USDJPY: 393
- WTI: 238
- XRPUSD: 355

## 6. MR candidates / resolved
- 224 candidates, 0 resolved

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