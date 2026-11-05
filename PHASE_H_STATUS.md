# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-05T00:27:14.277507

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
66

## 5. Observation count by asset
- ADAUSD: 1396
- AUDCAD: 1003
- AUDCHF: 1003
- AUDJPY: 1002
- AUDNZD: 1003
- AUDUSD: 1003
- AUS200: 295
- AVAXUSD: 1396
- BCHUSD: 1396
- BNBUSD: 1396
- BRENT: 961
- BTCUSD: 1594
- CADCHF: 1003
- CADJPY: 1002
- CHFJPY: 1004
- DOGEUSD: 1396
- DOTUSD: 1396
- ETHUSD: 1594
- EU50: 378
- EURAUD: 1004
- EURCAD: 1141
- EURCHF: 1004
- EURGBP: 1003
- EURJPY: 1002
- EURUSD: 1002
- FRA40: 378
- GBPAUD: 1005
- GBPCAD: 1003
- GBPCHF: 1003
- GBPJPY: 1002
- GBPUSD: 1003
- GER40: 378
- GOLD: 1083
- HK50: 280
- JPN225: 259
- LINKUSD: 1396
- LTCUSD: 1396
- NAS100: 294
- NATGAS: 966
- NZDCAD: 1003
- NZDCHF: 1003
- NZDJPY: 1002
- NZDUSD: 1003
- SILVER: 962
- SOLUSD: 1396
- UK100: 378
- US30: 294
- US500: 330
- USDCAD: 1004
- USDCHF: 998
- USDJPY: 1134
- WTI: 962
- XRPUSD: 1396

## 6. MR candidates / resolved
- 1250 candidates, 0 resolved

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