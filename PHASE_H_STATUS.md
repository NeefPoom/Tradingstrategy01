# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-15T07:44:39.939043

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
15

## 5. Observation count by asset
- ADAUSD: 182
- AUDCAD: 133
- AUDCHF: 133
- AUDJPY: 133
- AUDNZD: 133
- AUDUSD: 133
- AUS200: 42
- AVAXUSD: 182
- BCHUSD: 182
- BNBUSD: 182
- BRENT: 117
- BTCUSD: 380
- CADCHF: 133
- CADJPY: 133
- CHFJPY: 133
- DOGEUSD: 182
- DOTUSD: 182
- ETHUSD: 380
- EU50: 45
- EURAUD: 133
- EURCAD: 271
- EURCHF: 133
- EURGBP: 133
- EURJPY: 133
- EURUSD: 133
- FRA40: 45
- GBPAUD: 133
- GBPCAD: 133
- GBPCHF: 133
- GBPJPY: 133
- GBPUSD: 133
- GER40: 45
- GOLD: 236
- HK50: 41
- JPN225: 42
- LINKUSD: 182
- LTCUSD: 182
- NAS100: 35
- NATGAS: 117
- NZDCAD: 133
- NZDCHF: 133
- NZDJPY: 133
- NZDUSD: 133
- SILVER: 117
- SOLUSD: 182
- UK100: 45
- US30: 35
- US500: 71
- USDCAD: 133
- USDCHF: 133
- USDJPY: 269
- WTI: 117
- XRPUSD: 182

## 6. MR candidates / resolved
- 70 candidates, 0 resolved

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