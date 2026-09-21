# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-21T22:53:27.642046

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
22

## 5. Observation count by asset
- ADAUSD: 341
- AUDCAD: 243
- AUDCHF: 243
- AUDJPY: 243
- AUDNZD: 243
- AUDUSD: 243
- AUS200: 70
- AVAXUSD: 341
- BCHUSD: 341
- BNBUSD: 341
- BRENT: 224
- BTCUSD: 539
- CADCHF: 243
- CADJPY: 243
- CHFJPY: 243
- DOGEUSD: 341
- DOTUSD: 341
- ETHUSD: 539
- EU50: 90
- EURAUD: 243
- EURCAD: 381
- EURCHF: 243
- EURGBP: 243
- EURJPY: 243
- EURUSD: 243
- FRA40: 90
- GBPAUD: 243
- GBPCAD: 243
- GBPCHF: 243
- GBPJPY: 243
- GBPUSD: 243
- GER40: 90
- GOLD: 343
- HK50: 70
- JPN225: 63
- LINKUSD: 341
- LTCUSD: 341
- NAS100: 70
- NATGAS: 225
- NZDCAD: 243
- NZDCHF: 243
- NZDJPY: 243
- NZDUSD: 243
- SILVER: 225
- SOLUSD: 341
- UK100: 90
- US30: 70
- US500: 106
- USDCAD: 243
- USDCHF: 242
- USDJPY: 379
- WTI: 224
- XRPUSD: 341

## 6. MR candidates / resolved
- 202 candidates, 0 resolved

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