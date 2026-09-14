# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-14T20:34:49.294760

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
15

## 5. Observation count by asset
- ADAUSD: 171
- AUDCAD: 122
- AUDCHF: 122
- AUDJPY: 122
- AUDNZD: 122
- AUDUSD: 122
- AUS200: 35
- AVAXUSD: 171
- BCHUSD: 171
- BNBUSD: 171
- BRENT: 108
- BTCUSD: 369
- CADCHF: 122
- CADJPY: 122
- CHFJPY: 122
- DOGEUSD: 171
- DOTUSD: 171
- ETHUSD: 369
- EU50: 45
- EURAUD: 122
- EURCAD: 260
- EURCHF: 122
- EURGBP: 122
- EURJPY: 122
- EURUSD: 122
- FRA40: 45
- GBPAUD: 122
- GBPCAD: 122
- GBPCHF: 122
- GBPJPY: 122
- GBPUSD: 122
- GER40: 45
- GOLD: 227
- HK50: 35
- JPN225: 35
- LINKUSD: 171
- LTCUSD: 171
- NAS100: 35
- NATGAS: 108
- NZDCAD: 122
- NZDCHF: 122
- NZDJPY: 122
- NZDUSD: 122
- SILVER: 108
- SOLUSD: 171
- UK100: 45
- US30: 35
- US500: 71
- USDCAD: 122
- USDCHF: 122
- USDJPY: 258
- WTI: 108
- XRPUSD: 171

## 6. MR candidates / resolved
- 54 candidates, 0 resolved

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