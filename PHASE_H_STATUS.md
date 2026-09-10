# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-10T20:52:12.727383

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
11

## 5. Observation count by asset
- ADAUSD: 75
- AUDCAD: 75
- AUDCHF: 75
- AUDJPY: 75
- AUDNZD: 75
- AUDUSD: 75
- AUS200: 21
- AVAXUSD: 75
- BCHUSD: 75
- BNBUSD: 75
- BRENT: 62
- BTCUSD: 273
- CADCHF: 75
- CADJPY: 75
- CHFJPY: 75
- DOGEUSD: 75
- DOTUSD: 75
- ETHUSD: 273
- EU50: 27
- EURAUD: 75
- EURCAD: 213
- EURCHF: 75
- EURGBP: 75
- EURJPY: 75
- EURUSD: 75
- FRA40: 27
- GBPAUD: 75
- GBPCAD: 75
- GBPCHF: 75
- GBPJPY: 75
- GBPUSD: 75
- GER40: 27
- GOLD: 181
- HK50: 21
- JPN225: 21
- LINKUSD: 75
- LTCUSD: 75
- NAS100: 21
- NATGAS: 62
- NZDCAD: 75
- NZDCHF: 75
- NZDJPY: 75
- NZDUSD: 75
- SILVER: 62
- SOLUSD: 75
- UK100: 27
- US30: 21
- US500: 57
- USDCAD: 75
- USDCHF: 75
- USDJPY: 212
- WTI: 62
- XRPUSD: 75

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