# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-14T00:09:29.473843

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
14

## 5. Observation count by asset
- ADAUSD: 149
- AUDCAD: 102
- AUDCHF: 102
- AUDJPY: 102
- AUDNZD: 102
- AUDUSD: 102
- AUS200: 28
- AVAXUSD: 149
- BCHUSD: 149
- BNBUSD: 149
- BRENT: 88
- BTCUSD: 347
- CADCHF: 102
- CADJPY: 102
- CHFJPY: 102
- DOGEUSD: 149
- DOTUSD: 149
- ETHUSD: 347
- EU50: 36
- EURAUD: 102
- EURCAD: 240
- EURCHF: 102
- EURGBP: 102
- EURJPY: 102
- EURUSD: 102
- FRA40: 36
- GBPAUD: 102
- GBPCAD: 102
- GBPCHF: 102
- GBPJPY: 102
- GBPUSD: 102
- GER40: 36
- GOLD: 207
- HK50: 28
- JPN225: 28
- LINKUSD: 149
- LTCUSD: 149
- NAS100: 28
- NATGAS: 88
- NZDCAD: 102
- NZDCHF: 102
- NZDJPY: 102
- NZDUSD: 102
- SILVER: 88
- SOLUSD: 149
- UK100: 36
- US30: 28
- US500: 64
- USDCAD: 102
- USDCHF: 102
- USDJPY: 238
- WTI: 88
- XRPUSD: 149

## 6. MR candidates / resolved
- 22 candidates, 0 resolved

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