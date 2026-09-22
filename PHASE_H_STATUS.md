# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-22T06:52:23.578540

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
22

## 5. Observation count by asset
- ADAUSD: 349
- AUDCAD: 251
- AUDCHF: 251
- AUDJPY: 251
- AUDNZD: 251
- AUDUSD: 251
- AUS200: 76
- AVAXUSD: 349
- BCHUSD: 349
- BNBUSD: 349
- BRENT: 230
- BTCUSD: 547
- CADCHF: 251
- CADJPY: 251
- CHFJPY: 251
- DOGEUSD: 349
- DOTUSD: 349
- ETHUSD: 547
- EU50: 90
- EURAUD: 251
- EURCAD: 389
- EURCHF: 251
- EURGBP: 251
- EURJPY: 251
- EURUSD: 251
- FRA40: 90
- GBPAUD: 251
- GBPCAD: 251
- GBPCHF: 251
- GBPJPY: 251
- GBPUSD: 251
- GER40: 90
- GOLD: 349
- HK50: 75
- JPN225: 63
- LINKUSD: 349
- LTCUSD: 349
- NAS100: 70
- NATGAS: 231
- NZDCAD: 251
- NZDCHF: 251
- NZDJPY: 251
- NZDUSD: 251
- SILVER: 231
- SOLUSD: 349
- UK100: 90
- US30: 70
- US500: 106
- USDCAD: 251
- USDCHF: 250
- USDJPY: 387
- WTI: 230
- XRPUSD: 349

## 6. MR candidates / resolved
- 210 candidates, 0 resolved

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