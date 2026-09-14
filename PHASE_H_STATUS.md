# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-14T10:39:09.657420

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
14

## 5. Observation count by asset
- ADAUSD: 161
- AUDCAD: 112
- AUDCHF: 112
- AUDJPY: 112
- AUDNZD: 112
- AUDUSD: 112
- AUS200: 35
- AVAXUSD: 161
- BCHUSD: 161
- BNBUSD: 161
- BRENT: 98
- BTCUSD: 359
- CADCHF: 112
- CADJPY: 112
- CHFJPY: 112
- DOGEUSD: 161
- DOTUSD: 161
- ETHUSD: 359
- EU50: 39
- EURAUD: 112
- EURCAD: 250
- EURCHF: 112
- EURGBP: 112
- EURJPY: 112
- EURUSD: 112
- FRA40: 39
- GBPAUD: 112
- GBPCAD: 112
- GBPCHF: 112
- GBPJPY: 112
- GBPUSD: 112
- GER40: 39
- GOLD: 217
- HK50: 35
- JPN225: 35
- LINKUSD: 161
- LTCUSD: 161
- NAS100: 28
- NATGAS: 98
- NZDCAD: 112
- NZDCHF: 112
- NZDJPY: 112
- NZDUSD: 112
- SILVER: 98
- SOLUSD: 161
- UK100: 39
- US30: 28
- US500: 64
- USDCAD: 112
- USDCHF: 112
- USDJPY: 248
- WTI: 98
- XRPUSD: 161

## 6. MR candidates / resolved
- 41 candidates, 0 resolved

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