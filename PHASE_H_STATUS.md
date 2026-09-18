# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-18T15:01:45.382771

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
19

## 5. Observation count by asset
- ADAUSD: 262
- AUDCAD: 212
- AUDCHF: 212
- AUDJPY: 212
- AUDNZD: 212
- AUDUSD: 212
- AUS200: 63
- AVAXUSD: 262
- BCHUSD: 262
- BNBUSD: 262
- BRENT: 194
- BTCUSD: 459
- CADCHF: 212
- CADJPY: 212
- CHFJPY: 212
- DOGEUSD: 262
- DOTUSD: 262
- ETHUSD: 459
- EU50: 79
- EURAUD: 212
- EURCAD: 350
- EURCHF: 212
- EURGBP: 212
- EURJPY: 212
- EURUSD: 212
- FRA40: 79
- GBPAUD: 212
- GBPCAD: 212
- GBPCHF: 212
- GBPJPY: 212
- GBPUSD: 212
- GER40: 79
- GOLD: 313
- HK50: 63
- JPN225: 63
- LINKUSD: 262
- LTCUSD: 262
- NAS100: 57
- NATGAS: 194
- NZDCAD: 212
- NZDCHF: 212
- NZDJPY: 212
- NZDUSD: 212
- SILVER: 194
- SOLUSD: 261
- UK100: 79
- US30: 57
- US500: 93
- USDCAD: 212
- USDCHF: 212
- USDJPY: 348
- WTI: 194
- XRPUSD: 261

## 6. MR candidates / resolved
- 160 candidates, 0 resolved

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