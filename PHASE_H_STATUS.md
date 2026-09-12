# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-12T16:19:33.034664

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
13

## 5. Observation count by asset
- ADAUSD: 119
- AUDCAD: 101
- AUDCHF: 101
- AUDJPY: 101
- AUDNZD: 101
- AUDUSD: 101
- AUS200: 28
- AVAXUSD: 119
- BCHUSD: 119
- BNBUSD: 119
- BRENT: 86
- BTCUSD: 317
- CADCHF: 101
- CADJPY: 101
- CHFJPY: 101
- DOGEUSD: 119
- DOTUSD: 119
- ETHUSD: 317
- EU50: 36
- EURAUD: 101
- EURCAD: 239
- EURCHF: 101
- EURGBP: 101
- EURJPY: 101
- EURUSD: 101
- FRA40: 36
- GBPAUD: 101
- GBPCAD: 101
- GBPCHF: 101
- GBPJPY: 101
- GBPUSD: 101
- GER40: 36
- GOLD: 205
- HK50: 28
- JPN225: 28
- LINKUSD: 119
- LTCUSD: 119
- NAS100: 28
- NATGAS: 86
- NZDCAD: 101
- NZDCHF: 101
- NZDJPY: 101
- NZDUSD: 101
- SILVER: 86
- SOLUSD: 119
- UK100: 36
- US30: 28
- US500: 64
- USDCAD: 101
- USDCHF: 101
- USDJPY: 237
- WTI: 86
- XRPUSD: 119

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