# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-10T17:54:41.025132

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
11

## 5. Observation count by asset
- ADAUSD: 72
- AUDCAD: 72
- AUDCHF: 72
- AUDJPY: 72
- AUDNZD: 72
- AUDUSD: 72
- AUS200: 21
- AVAXUSD: 72
- BCHUSD: 72
- BNBUSD: 72
- BRENT: 59
- BTCUSD: 270
- CADCHF: 72
- CADJPY: 72
- CHFJPY: 72
- DOGEUSD: 72
- DOTUSD: 72
- ETHUSD: 270
- EU50: 27
- EURAUD: 72
- EURCAD: 210
- EURCHF: 72
- EURGBP: 72
- EURJPY: 72
- EURUSD: 72
- FRA40: 27
- GBPAUD: 72
- GBPCAD: 70
- GBPCHF: 72
- GBPJPY: 72
- GBPUSD: 72
- GER40: 27
- GOLD: 178
- HK50: 21
- JPN225: 21
- LINKUSD: 72
- LTCUSD: 72
- NAS100: 18
- NATGAS: 59
- NZDCAD: 72
- NZDCHF: 72
- NZDJPY: 72
- NZDUSD: 72
- SILVER: 59
- SOLUSD: 72
- UK100: 27
- US30: 18
- US500: 54
- USDCAD: 72
- USDCHF: 72
- USDJPY: 209
- WTI: 59
- XRPUSD: 72

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