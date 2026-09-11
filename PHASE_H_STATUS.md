# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-11T11:16:02.319896

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
12

## 5. Observation count by asset
- ADAUSD: 85
- AUDCAD: 87
- AUDCHF: 87
- AUDJPY: 90
- AUDNZD: 90
- AUDUSD: 87
- AUS200: 28
- AVAXUSD: 90
- BCHUSD: 90
- BNBUSD: 90
- BRENT: 73
- BTCUSD: 285
- CADCHF: 90
- CADJPY: 90
- CHFJPY: 90
- DOGEUSD: 90
- DOTUSD: 90
- ETHUSD: 288
- EU50: 31
- EURAUD: 86
- EURCAD: 228
- EURCHF: 87
- EURGBP: 88
- EURJPY: 90
- EURUSD: 90
- FRA40: 31
- GBPAUD: 85
- GBPCAD: 90
- GBPCHF: 90
- GBPJPY: 90
- GBPUSD: 90
- GER40: 31
- GOLD: 195
- HK50: 28
- JPN225: 28
- LINKUSD: 90
- LTCUSD: 90
- NAS100: 21
- NATGAS: 76
- NZDCAD: 90
- NZDCHF: 90
- NZDJPY: 90
- NZDUSD: 85
- SILVER: 76
- SOLUSD: 85
- UK100: 31
- US30: 21
- US500: 57
- USDCAD: 90
- USDCHF: 90
- USDJPY: 227
- WTI: 73
- XRPUSD: 88

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