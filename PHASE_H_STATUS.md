# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-09T19:47:03.306418

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
10

## 5. Observation count by asset
- ADAUSD: 50
- AUDCAD: 50
- AUDCHF: 50
- AUDJPY: 50
- AUDNZD: 50
- AUDUSD: 47
- AUS200: 14
- AVAXUSD: 50
- BCHUSD: 50
- BNBUSD: 50
- BRENT: 38
- BTCUSD: 248
- CADCHF: 50
- CADJPY: 50
- CHFJPY: 50
- DOGEUSD: 48
- DOTUSD: 50
- ETHUSD: 248
- EU50: 18
- EURAUD: 50
- EURCAD: 188
- EURCHF: 50
- EURGBP: 50
- EURJPY: 50
- EURUSD: 50
- FRA40: 18
- GBPAUD: 50
- GBPCAD: 50
- GBPCHF: 50
- GBPJPY: 50
- GBPUSD: 50
- GER40: 18
- GOLD: 157
- HK50: 14
- JPN225: 14
- LINKUSD: 50
- LTCUSD: 50
- NAS100: 13
- NATGAS: 38
- NZDCAD: 50
- NZDCHF: 50
- NZDJPY: 50
- NZDUSD: 50
- SILVER: 38
- SOLUSD: 50
- UK100: 18
- US30: 13
- US500: 49
- USDCAD: 50
- USDCHF: 50
- USDJPY: 187
- WTI: 38
- XRPUSD: 50

## 6. MR candidates / resolved
- 20 candidates, 0 resolved

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