# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-30T15:31:14.530048

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
61

## 5. Observation count by asset
- ADAUSD: 1270
- AUDCAD: 926
- AUDCHF: 926
- AUDJPY: 926
- AUDNZD: 926
- AUDUSD: 926
- AUS200: 273
- AVAXUSD: 1270
- BCHUSD: 1270
- BNBUSD: 1270
- BRENT: 885
- BTCUSD: 1468
- CADCHF: 926
- CADJPY: 926
- CHFJPY: 926
- DOGEUSD: 1270
- DOTUSD: 1270
- ETHUSD: 1468
- EU50: 349
- EURAUD: 926
- EURCAD: 1064
- EURCHF: 926
- EURGBP: 927
- EURJPY: 926
- EURUSD: 926
- FRA40: 349
- GBPAUD: 926
- GBPCAD: 926
- GBPCHF: 926
- GBPJPY: 926
- GBPUSD: 927
- GER40: 349
- GOLD: 1007
- HK50: 259
- JPN225: 245
- LINKUSD: 1270
- LTCUSD: 1270
- NAS100: 267
- NATGAS: 890
- NZDCAD: 926
- NZDCHF: 926
- NZDJPY: 926
- NZDUSD: 926
- SILVER: 886
- SOLUSD: 1270
- UK100: 349
- US30: 267
- US500: 303
- USDCAD: 926
- USDCHF: 921
- USDJPY: 1059
- WTI: 886
- XRPUSD: 1270

## 6. MR candidates / resolved
- 1123 candidates, 0 resolved

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