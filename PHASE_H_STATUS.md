# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-22T20:32:56.993856

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
23

## 5. Observation count by asset
- ADAUSD: 363
- AUDCAD: 265
- AUDCHF: 265
- AUDJPY: 265
- AUDNZD: 265
- AUDUSD: 265
- AUS200: 77
- AVAXUSD: 363
- BCHUSD: 363
- BNBUSD: 363
- BRENT: 246
- BTCUSD: 561
- CADCHF: 265
- CADJPY: 265
- CHFJPY: 265
- DOGEUSD: 363
- DOTUSD: 363
- ETHUSD: 561
- EU50: 99
- EURAUD: 265
- EURCAD: 403
- EURCHF: 265
- EURGBP: 265
- EURJPY: 265
- EURUSD: 265
- FRA40: 99
- GBPAUD: 265
- GBPCAD: 265
- GBPCHF: 265
- GBPJPY: 265
- GBPUSD: 265
- GER40: 99
- GOLD: 365
- HK50: 77
- JPN225: 63
- LINKUSD: 363
- LTCUSD: 363
- NAS100: 77
- NATGAS: 247
- NZDCAD: 265
- NZDCHF: 265
- NZDJPY: 265
- NZDUSD: 265
- SILVER: 247
- SOLUSD: 363
- UK100: 99
- US30: 77
- US500: 112
- USDCAD: 265
- USDCHF: 264
- USDJPY: 401
- WTI: 246
- XRPUSD: 363

## 6. MR candidates / resolved
- 229 candidates, 0 resolved

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