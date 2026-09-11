# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-11T05:56:46.696655

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
11

## 5. Observation count by asset
- ADAUSD: 84
- AUDCAD: 84
- AUDCHF: 84
- AUDJPY: 84
- AUDNZD: 84
- AUDUSD: 84
- AUS200: 26
- AVAXUSD: 84
- BCHUSD: 84
- BNBUSD: 84
- BRENT: 69
- BTCUSD: 282
- CADCHF: 84
- CADJPY: 84
- CHFJPY: 84
- DOGEUSD: 84
- DOTUSD: 84
- ETHUSD: 282
- EU50: 27
- EURAUD: 84
- EURCAD: 222
- EURCHF: 84
- EURGBP: 84
- EURJPY: 84
- EURUSD: 84
- FRA40: 27
- GBPAUD: 84
- GBPCAD: 84
- GBPCHF: 84
- GBPJPY: 84
- GBPUSD: 84
- GER40: 27
- GOLD: 188
- HK50: 25
- JPN225: 26
- LINKUSD: 84
- LTCUSD: 83
- NAS100: 21
- NATGAS: 69
- NZDCAD: 84
- NZDCHF: 83
- NZDJPY: 84
- NZDUSD: 84
- SILVER: 69
- SOLUSD: 84
- UK100: 27
- US30: 21
- US500: 57
- USDCAD: 84
- USDCHF: 84
- USDJPY: 221
- WTI: 69
- XRPUSD: 84

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