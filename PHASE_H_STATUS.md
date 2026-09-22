# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-22T17:21:50.058827

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
23

## 5. Observation count by asset
- ADAUSD: 360
- AUDCAD: 262
- AUDCHF: 262
- AUDJPY: 262
- AUDNZD: 262
- AUDUSD: 262
- AUS200: 77
- AVAXUSD: 360
- BCHUSD: 360
- BNBUSD: 360
- BRENT: 243
- BTCUSD: 558
- CADCHF: 262
- CADJPY: 262
- CHFJPY: 262
- DOGEUSD: 360
- DOTUSD: 360
- ETHUSD: 558
- EU50: 99
- EURAUD: 262
- EURCAD: 400
- EURCHF: 262
- EURGBP: 262
- EURJPY: 262
- EURUSD: 262
- FRA40: 99
- GBPAUD: 262
- GBPCAD: 262
- GBPCHF: 262
- GBPJPY: 262
- GBPUSD: 262
- GER40: 99
- GOLD: 362
- HK50: 77
- JPN225: 63
- LINKUSD: 360
- LTCUSD: 360
- NAS100: 73
- NATGAS: 244
- NZDCAD: 262
- NZDCHF: 262
- NZDJPY: 262
- NZDUSD: 262
- SILVER: 244
- SOLUSD: 360
- UK100: 99
- US30: 73
- US500: 109
- USDCAD: 262
- USDCHF: 261
- USDJPY: 398
- WTI: 243
- XRPUSD: 360

## 6. MR candidates / resolved
- 228 candidates, 0 resolved

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