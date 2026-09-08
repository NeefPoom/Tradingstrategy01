# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-08T05:24:24.360226

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
8

## 5. Observation count by asset
- ADAUSD: 12
- AUDCAD: 12
- AUDCHF: 12
- AUDJPY: 12
- AUDNZD: 12
- AUDUSD: 12
- AUS200: 5
- AVAXUSD: 12
- BCHUSD: 12
- BNBUSD: 12
- BRENT: 1
- BTCUSD: 210
- CADCHF: 12
- CADJPY: 12
- CHFJPY: 12
- DOGEUSD: 12
- DOTUSD: 12
- ETHUSD: 210
- EURAUD: 12
- EURCAD: 150
- EURCHF: 12
- EURGBP: 12
- EURJPY: 12
- EURUSD: 12
- GBPAUD: 12
- GBPCAD: 12
- GBPCHF: 12
- GBPJPY: 12
- GBPUSD: 12
- GOLD: 120
- HK50: 3
- JPN225: 5
- LINKUSD: 12
- LTCUSD: 12
- NATGAS: 1
- NZDCAD: 12
- NZDCHF: 12
- NZDJPY: 12
- NZDUSD: 12
- SILVER: 1
- SOLUSD: 12
- US500: 36
- USDCAD: 12
- USDCHF: 12
- USDJPY: 149
- WTI: 1
- XRPUSD: 12

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