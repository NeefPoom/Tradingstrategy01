# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-07T21:32:10.979477

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
8

## 5. Observation count by asset
- ADAUSD: 4
- AUDCAD: 4
- AUDCHF: 4
- AUDJPY: 4
- AUDNZD: 4
- AUDUSD: 4
- AVAXUSD: 4
- BCHUSD: 4
- BNBUSD: 4
- BTCUSD: 202
- CADCHF: 4
- CADJPY: 4
- CHFJPY: 4
- DOGEUSD: 4
- DOTUSD: 4
- ETHUSD: 202
- EURAUD: 4
- EURCAD: 142
- EURCHF: 4
- EURGBP: 4
- EURJPY: 4
- EURUSD: 4
- GBPAUD: 4
- GBPCAD: 4
- GBPCHF: 4
- GBPJPY: 4
- GBPUSD: 4
- GOLD: 119
- LINKUSD: 4
- LTCUSD: 4
- NZDCAD: 4
- NZDCHF: 4
- NZDJPY: 4
- NZDUSD: 4
- SOLUSD: 4
- US500: 36
- USDCAD: 4
- USDCHF: 4
- USDJPY: 141
- XRPUSD: 4

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