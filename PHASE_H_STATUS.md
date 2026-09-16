# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-16T14:58:41.668652

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
17

## 5. Observation count by asset
- ADAUSD: 213
- AUDCAD: 164
- AUDCHF: 164
- AUDJPY: 164
- AUDNZD: 164
- AUDUSD: 164
- AUS200: 49
- AVAXUSD: 213
- BCHUSD: 213
- BNBUSD: 213
- BRENT: 148
- BTCUSD: 411
- CADCHF: 164
- CADJPY: 164
- CHFJPY: 164
- DOGEUSD: 213
- DOTUSD: 213
- ETHUSD: 411
- EU50: 61
- EURAUD: 164
- EURCAD: 302
- EURCHF: 164
- EURGBP: 164
- EURJPY: 164
- EURUSD: 164
- FRA40: 61
- GBPAUD: 164
- GBPCAD: 164
- GBPCHF: 164
- GBPJPY: 164
- GBPUSD: 164
- GER40: 61
- GOLD: 267
- HK50: 49
- JPN225: 49
- LINKUSD: 213
- LTCUSD: 213
- NAS100: 43
- NATGAS: 148
- NZDCAD: 164
- NZDCHF: 164
- NZDJPY: 164
- NZDUSD: 164
- SILVER: 148
- SOLUSD: 213
- UK100: 61
- US30: 43
- US500: 79
- USDCAD: 164
- USDCHF: 164
- USDJPY: 300
- WTI: 148
- XRPUSD: 213

## 6. MR candidates / resolved
- 116 candidates, 0 resolved

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