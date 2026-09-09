# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-09T06:42:45.037470

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
9

## 5. Observation count by asset
- ADAUSD: 34
- AUDCAD: 37
- AUDCHF: 37
- AUDJPY: 37
- AUDNZD: 37
- AUDUSD: 37
- AUS200: 13
- AVAXUSD: 37
- BCHUSD: 36
- BNBUSD: 37
- BRENT: 25
- BTCUSD: 235
- CADCHF: 34
- CADJPY: 37
- CHFJPY: 37
- DOGEUSD: 37
- DOTUSD: 37
- ETHUSD: 235
- EU50: 9
- EURAUD: 37
- EURCAD: 175
- EURCHF: 37
- EURGBP: 37
- EURJPY: 37
- EURUSD: 37
- FRA40: 9
- GBPAUD: 37
- GBPCAD: 37
- GBPCHF: 37
- GBPJPY: 37
- GBPUSD: 37
- GER40: 9
- GOLD: 144
- HK50: 12
- JPN225: 13
- LINKUSD: 37
- LTCUSD: 37
- NAS100: 7
- NATGAS: 25
- NZDCAD: 35
- NZDCHF: 37
- NZDJPY: 37
- NZDUSD: 37
- SILVER: 25
- SOLUSD: 37
- UK100: 9
- US30: 7
- US500: 43
- USDCAD: 37
- USDCHF: 37
- USDJPY: 174
- WTI: 25
- XRPUSD: 37

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