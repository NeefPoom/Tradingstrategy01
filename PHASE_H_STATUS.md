# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-17T10:29:37.243645

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
17

## 5. Observation count by asset
- ADAUSD: 233
- AUDCAD: 184
- AUDCHF: 184
- AUDJPY: 184
- AUDNZD: 184
- AUDUSD: 184
- AUS200: 56
- AVAXUSD: 233
- BCHUSD: 233
- BNBUSD: 233
- BRENT: 167
- BTCUSD: 431
- CADCHF: 184
- CADJPY: 184
- CHFJPY: 184
- DOGEUSD: 233
- DOTUSD: 233
- ETHUSD: 431
- EU50: 66
- EURAUD: 184
- EURCAD: 322
- EURCHF: 184
- EURGBP: 184
- EURJPY: 184
- EURUSD: 184
- FRA40: 66
- GBPAUD: 184
- GBPCAD: 184
- GBPCHF: 184
- GBPJPY: 184
- GBPUSD: 184
- GER40: 66
- GOLD: 286
- HK50: 56
- JPN225: 56
- LINKUSD: 233
- LTCUSD: 233
- NAS100: 49
- NATGAS: 167
- NZDCAD: 184
- NZDCHF: 184
- NZDJPY: 184
- NZDUSD: 184
- SILVER: 167
- SOLUSD: 233
- UK100: 66
- US30: 49
- US500: 85
- USDCAD: 184
- USDCHF: 184
- USDJPY: 320
- WTI: 167
- XRPUSD: 233

## 6. MR candidates / resolved
- 138 candidates, 0 resolved

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