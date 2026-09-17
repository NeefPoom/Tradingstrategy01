# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-17T15:21:53.646461

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
18

## 5. Observation count by asset
- ADAUSD: 238
- AUDCAD: 189
- AUDCHF: 189
- AUDJPY: 189
- AUDNZD: 189
- AUDUSD: 189
- AUS200: 56
- AVAXUSD: 238
- BCHUSD: 238
- BNBUSD: 238
- BRENT: 172
- BTCUSD: 436
- CADCHF: 189
- CADJPY: 189
- CHFJPY: 189
- DOGEUSD: 238
- DOTUSD: 238
- ETHUSD: 436
- EU50: 71
- EURAUD: 189
- EURCAD: 327
- EURCHF: 189
- EURGBP: 189
- EURJPY: 189
- EURUSD: 189
- FRA40: 71
- GBPAUD: 189
- GBPCAD: 189
- GBPCHF: 189
- GBPJPY: 189
- GBPUSD: 189
- GER40: 71
- GOLD: 291
- HK50: 56
- JPN225: 56
- LINKUSD: 238
- LTCUSD: 238
- NAS100: 50
- NATGAS: 172
- NZDCAD: 189
- NZDCHF: 189
- NZDJPY: 189
- NZDUSD: 189
- SILVER: 172
- SOLUSD: 238
- UK100: 71
- US30: 50
- US500: 86
- USDCAD: 189
- USDCHF: 189
- USDJPY: 325
- WTI: 172
- XRPUSD: 238

## 6. MR candidates / resolved
- 145 candidates, 0 resolved

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