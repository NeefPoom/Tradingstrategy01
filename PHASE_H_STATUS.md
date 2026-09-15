# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-15T23:43:59.719114

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
16

## 5. Observation count by asset
- ADAUSD: 198
- AUDCAD: 149
- AUDCHF: 149
- AUDJPY: 149
- AUDNZD: 149
- AUDUSD: 149
- AUS200: 42
- AVAXUSD: 198
- BCHUSD: 198
- BNBUSD: 198
- BRENT: 133
- BTCUSD: 396
- CADCHF: 149
- CADJPY: 149
- CHFJPY: 149
- DOGEUSD: 198
- DOTUSD: 198
- ETHUSD: 396
- EU50: 54
- EURAUD: 149
- EURCAD: 287
- EURCHF: 149
- EURGBP: 149
- EURJPY: 149
- EURUSD: 149
- FRA40: 54
- GBPAUD: 149
- GBPCAD: 149
- GBPCHF: 149
- GBPJPY: 149
- GBPUSD: 149
- GER40: 54
- GOLD: 252
- HK50: 42
- JPN225: 42
- LINKUSD: 198
- LTCUSD: 198
- NAS100: 42
- NATGAS: 133
- NZDCAD: 149
- NZDCHF: 149
- NZDJPY: 149
- NZDUSD: 149
- SILVER: 133
- SOLUSD: 198
- UK100: 54
- US30: 42
- US500: 78
- USDCAD: 149
- USDCHF: 149
- USDJPY: 285
- WTI: 133
- XRPUSD: 198

## 6. MR candidates / resolved
- 91 candidates, 0 resolved

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