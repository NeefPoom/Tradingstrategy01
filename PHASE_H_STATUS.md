# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-16T04:47:05.091291

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
16

## 5. Observation count by asset
- ADAUSD: 203
- AUDCAD: 154
- AUDCHF: 154
- AUDJPY: 154
- AUDNZD: 154
- AUDUSD: 154
- AUS200: 46
- AVAXUSD: 203
- BCHUSD: 203
- BNBUSD: 203
- BRENT: 138
- BTCUSD: 401
- CADCHF: 154
- CADJPY: 154
- CHFJPY: 154
- DOGEUSD: 203
- DOTUSD: 203
- ETHUSD: 401
- EU50: 54
- EURAUD: 154
- EURCAD: 292
- EURCHF: 154
- EURGBP: 154
- EURJPY: 154
- EURUSD: 154
- FRA40: 54
- GBPAUD: 154
- GBPCAD: 154
- GBPCHF: 154
- GBPJPY: 154
- GBPUSD: 154
- GER40: 54
- GOLD: 257
- HK50: 45
- JPN225: 46
- LINKUSD: 203
- LTCUSD: 203
- NAS100: 42
- NATGAS: 138
- NZDCAD: 154
- NZDCHF: 154
- NZDJPY: 154
- NZDUSD: 154
- SILVER: 138
- SOLUSD: 203
- UK100: 54
- US30: 42
- US500: 78
- USDCAD: 154
- USDCHF: 154
- USDJPY: 290
- WTI: 138
- XRPUSD: 203

## 6. MR candidates / resolved
- 93 candidates, 0 resolved

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