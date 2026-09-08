# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-08T00:22:55.974060

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
8

## 5. Observation count by asset
- ADAUSD: 5
- AUDCAD: 6
- AUDCHF: 5
- AUDJPY: 6
- AUDNZD: 6
- AUDUSD: 6
- AVAXUSD: 5
- BCHUSD: 5
- BNBUSD: 5
- BTCUSD: 203
- CADCHF: 6
- CADJPY: 6
- CHFJPY: 6
- DOGEUSD: 5
- DOTUSD: 5
- ETHUSD: 203
- EURAUD: 6
- EURCAD: 144
- EURCHF: 6
- EURGBP: 6
- EURJPY: 6
- EURUSD: 6
- GBPAUD: 6
- GBPCAD: 6
- GBPCHF: 6
- GBPJPY: 6
- GBPUSD: 6
- GOLD: 119
- LINKUSD: 5
- LTCUSD: 5
- NZDCAD: 6
- NZDCHF: 6
- NZDJPY: 6
- NZDUSD: 6
- SOLUSD: 5
- US500: 36
- USDCAD: 6
- USDCHF: 6
- USDJPY: 143
- XRPUSD: 5

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