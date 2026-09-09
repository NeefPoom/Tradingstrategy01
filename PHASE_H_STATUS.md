# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-09T12:22:23.810571

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
10

## 5. Observation count by asset
- ADAUSD: 43
- AUDCAD: 43
- AUDCHF: 43
- AUDJPY: 43
- AUDNZD: 43
- AUDUSD: 43
- AUS200: 14
- AVAXUSD: 43
- BCHUSD: 43
- BNBUSD: 43
- BRENT: 31
- BTCUSD: 241
- CADCHF: 43
- CADJPY: 43
- CHFJPY: 43
- DOGEUSD: 43
- DOTUSD: 43
- ETHUSD: 241
- EU50: 14
- EURAUD: 43
- EURCAD: 180
- EURCHF: 43
- EURGBP: 43
- EURJPY: 43
- EURUSD: 43
- FRA40: 14
- GBPAUD: 43
- GBPCAD: 43
- GBPCHF: 43
- GBPJPY: 43
- GBPUSD: 42
- GER40: 14
- GOLD: 149
- HK50: 14
- JPN225: 14
- LINKUSD: 43
- LTCUSD: 43
- NAS100: 7
- NATGAS: 31
- NZDCAD: 43
- NZDCHF: 43
- NZDJPY: 43
- NZDUSD: 43
- SILVER: 31
- SOLUSD: 43
- UK100: 14
- US30: 7
- US500: 43
- USDCAD: 43
- USDCHF: 43
- USDJPY: 180
- WTI: 31
- XRPUSD: 43

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