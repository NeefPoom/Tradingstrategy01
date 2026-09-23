# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-23T18:04:33.622771

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
24

## 5. Observation count by asset
- ADAUSD: 385
- AUDCAD: 287
- AUDCHF: 287
- AUDJPY: 287
- AUDNZD: 287
- AUDUSD: 286
- AUS200: 84
- AVAXUSD: 385
- BCHUSD: 385
- BNBUSD: 385
- BRENT: 267
- BTCUSD: 582
- CADCHF: 287
- CADJPY: 287
- CHFJPY: 287
- DOGEUSD: 385
- DOTUSD: 385
- ETHUSD: 582
- EU50: 108
- EURAUD: 287
- EURCAD: 424
- EURCHF: 287
- EURGBP: 287
- EURJPY: 286
- EURUSD: 286
- FRA40: 108
- GBPAUD: 287
- GBPCAD: 287
- GBPCHF: 287
- GBPJPY: 287
- GBPUSD: 286
- GER40: 108
- GOLD: 385
- HK50: 84
- JPN225: 63
- LINKUSD: 385
- LTCUSD: 385
- NAS100: 81
- NATGAS: 268
- NZDCAD: 287
- NZDCHF: 287
- NZDJPY: 287
- NZDUSD: 286
- SILVER: 268
- SOLUSD: 385
- UK100: 108
- US30: 81
- US500: 117
- USDCAD: 286
- USDCHF: 285
- USDJPY: 422
- WTI: 267
- XRPUSD: 385

## 6. MR candidates / resolved
- 256 candidates, 0 resolved

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