# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-21T14:12:20.365353

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
22

## 5. Observation count by asset
- ADAUSD: 333
- AUDCAD: 235
- AUDCHF: 235
- AUDJPY: 235
- AUDNZD: 235
- AUDUSD: 235
- AUS200: 70
- AVAXUSD: 333
- BCHUSD: 333
- BNBUSD: 333
- BRENT: 217
- BTCUSD: 531
- CADCHF: 235
- CADJPY: 235
- CHFJPY: 235
- DOGEUSD: 333
- DOTUSD: 333
- ETHUSD: 531
- EU50: 88
- EURAUD: 235
- EURCAD: 373
- EURCHF: 235
- EURGBP: 235
- EURJPY: 235
- EURUSD: 235
- FRA40: 88
- GBPAUD: 235
- GBPCAD: 235
- GBPCHF: 235
- GBPJPY: 235
- GBPUSD: 235
- GER40: 88
- GOLD: 336
- HK50: 70
- JPN225: 63
- LINKUSD: 333
- LTCUSD: 333
- NAS100: 63
- NATGAS: 218
- NZDCAD: 235
- NZDCHF: 235
- NZDJPY: 235
- NZDUSD: 235
- SILVER: 217
- SOLUSD: 333
- UK100: 88
- US30: 63
- US500: 99
- USDCAD: 235
- USDCHF: 234
- USDJPY: 371
- WTI: 217
- XRPUSD: 333

## 6. MR candidates / resolved
- 198 candidates, 0 resolved

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