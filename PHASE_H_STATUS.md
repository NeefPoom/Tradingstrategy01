# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-15T13:32:37.940784

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
16

## 5. Observation count by asset
- ADAUSD: 188
- AUDCAD: 139
- AUDCHF: 139
- AUDJPY: 139
- AUDNZD: 139
- AUDUSD: 139
- AUS200: 42
- AVAXUSD: 188
- BCHUSD: 188
- BNBUSD: 188
- BRENT: 124
- BTCUSD: 386
- CADCHF: 139
- CADJPY: 139
- CHFJPY: 139
- DOGEUSD: 188
- DOTUSD: 188
- ETHUSD: 386
- EU50: 51
- EURAUD: 139
- EURCAD: 277
- EURCHF: 139
- EURGBP: 139
- EURJPY: 139
- EURUSD: 139
- FRA40: 51
- GBPAUD: 139
- GBPCAD: 139
- GBPCHF: 139
- GBPJPY: 139
- GBPUSD: 139
- GER40: 51
- GOLD: 243
- HK50: 42
- JPN225: 42
- LINKUSD: 188
- LTCUSD: 188
- NAS100: 35
- NATGAS: 124
- NZDCAD: 139
- NZDCHF: 139
- NZDJPY: 139
- NZDUSD: 139
- SILVER: 124
- SOLUSD: 188
- UK100: 51
- US30: 35
- US500: 71
- USDCAD: 139
- USDCHF: 139
- USDJPY: 275
- WTI: 124
- XRPUSD: 188

## 6. MR candidates / resolved
- 79 candidates, 0 resolved

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