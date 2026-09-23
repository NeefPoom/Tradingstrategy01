# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-23T13:42:47.167026

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
24

## 5. Observation count by asset
- ADAUSD: 380
- AUDCAD: 282
- AUDCHF: 282
- AUDJPY: 282
- AUDNZD: 282
- AUDUSD: 282
- AUS200: 84
- AVAXUSD: 380
- BCHUSD: 380
- BNBUSD: 380
- BRENT: 262
- BTCUSD: 578
- CADCHF: 282
- CADJPY: 282
- CHFJPY: 282
- DOGEUSD: 380
- DOTUSD: 380
- ETHUSD: 578
- EU50: 105
- EURAUD: 282
- EURCAD: 420
- EURCHF: 282
- EURGBP: 282
- EURJPY: 282
- EURUSD: 282
- FRA40: 105
- GBPAUD: 282
- GBPCAD: 282
- GBPCHF: 282
- GBPJPY: 282
- GBPUSD: 282
- GER40: 105
- GOLD: 381
- HK50: 84
- JPN225: 63
- LINKUSD: 380
- LTCUSD: 380
- NAS100: 77
- NATGAS: 263
- NZDCAD: 282
- NZDCHF: 282
- NZDJPY: 282
- NZDUSD: 282
- SILVER: 263
- SOLUSD: 380
- UK100: 105
- US30: 77
- US500: 113
- USDCAD: 282
- USDCHF: 281
- USDJPY: 418
- WTI: 262
- XRPUSD: 380

## 6. MR candidates / resolved
- 254 candidates, 0 resolved

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