# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-08T04:58:57.754321

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
8

## 5. Observation count by asset
- ADAUSD: 10
- AUDCAD: 11
- AUDCHF: 11
- AUDJPY: 11
- AUDNZD: 11
- AUDUSD: 11
- AUS200: 4
- AVAXUSD: 11
- BCHUSD: 11
- BNBUSD: 11
- BTCUSD: 209
- CADCHF: 11
- CADJPY: 11
- CHFJPY: 11
- DOGEUSD: 11
- DOTUSD: 11
- ETHUSD: 209
- EURAUD: 10
- EURCAD: 149
- EURCHF: 11
- EURGBP: 11
- EURJPY: 11
- EURUSD: 11
- GBPAUD: 11
- GBPCAD: 9
- GBPCHF: 11
- GBPJPY: 11
- GBPUSD: 11
- GOLD: 119
- HK50: 3
- JPN225: 4
- LINKUSD: 11
- LTCUSD: 11
- NZDCAD: 11
- NZDCHF: 11
- NZDJPY: 11
- NZDUSD: 11
- SOLUSD: 11
- US500: 36
- USDCAD: 11
- USDCHF: 11
- USDJPY: 148
- XRPUSD: 11

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