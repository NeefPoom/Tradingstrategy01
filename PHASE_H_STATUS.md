# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-18T05:56:17.355818

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
18

## 5. Observation count by asset
- ADAUSD: 252
- AUDCAD: 203
- AUDCHF: 203
- AUDJPY: 203
- AUDNZD: 203
- AUDUSD: 203
- AUS200: 61
- AVAXUSD: 252
- BCHUSD: 252
- BNBUSD: 252
- BRENT: 183
- BTCUSD: 450
- CADCHF: 203
- CADJPY: 203
- CHFJPY: 203
- DOGEUSD: 252
- DOTUSD: 252
- ETHUSD: 450
- EU50: 72
- EURAUD: 203
- EURCAD: 341
- EURCHF: 203
- EURGBP: 203
- EURJPY: 203
- EURUSD: 203
- FRA40: 72
- GBPAUD: 203
- GBPCAD: 203
- GBPCHF: 203
- GBPJPY: 203
- GBPUSD: 203
- GER40: 72
- GOLD: 302
- HK50: 60
- JPN225: 61
- LINKUSD: 252
- LTCUSD: 252
- NAS100: 56
- NATGAS: 183
- NZDCAD: 203
- NZDCHF: 203
- NZDJPY: 203
- NZDUSD: 203
- SILVER: 183
- SOLUSD: 252
- UK100: 72
- US30: 56
- US500: 92
- USDCAD: 203
- USDCHF: 203
- USDJPY: 339
- WTI: 183
- XRPUSD: 252

## 6. MR candidates / resolved
- 155 candidates, 0 resolved

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