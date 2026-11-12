# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-12T03:06:50.323983

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
73

## 5. Observation count by asset
- ADAUSD: 1570
- AUDCAD: 1127
- AUDCHF: 1127
- AUDJPY: 1126
- AUDNZD: 1127
- AUDUSD: 1127
- AUS200: 333
- AVAXUSD: 1570
- BCHUSD: 1570
- BNBUSD: 1570
- BRENT: 1079
- BTCUSD: 1767
- CADCHF: 1129
- CADJPY: 1126
- CHFJPY: 1126
- DOGEUSD: 1570
- DOTUSD: 1570
- ETHUSD: 1767
- EU50: 423
- EURAUD: 1126
- EURCAD: 1265
- EURCHF: 1126
- EURGBP: 1127
- EURJPY: 1126
- EURUSD: 1126
- FRA40: 423
- GBPAUD: 1127
- GBPCAD: 1127
- GBPCHF: 1127
- GBPJPY: 1126
- GBPUSD: 1127
- GER40: 423
- GOLD: 1201
- HK50: 316
- JPN225: 297
- LINKUSD: 1570
- LTCUSD: 1570
- NAS100: 329
- NATGAS: 1084
- NZDCAD: 1128
- NZDCHF: 1128
- NZDJPY: 1127
- NZDUSD: 1127
- SILVER: 1080
- SOLUSD: 1570
- UK100: 423
- US30: 329
- US500: 365
- USDCAD: 1128
- USDCHF: 1122
- USDJPY: 1258
- WTI: 1080
- XRPUSD: 1570

## 6. MR candidates / resolved
- 1405 candidates, 0 resolved

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