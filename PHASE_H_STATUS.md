# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-16T22:10:03.755148

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
17

## 5. Observation count by asset
- ADAUSD: 221
- AUDCAD: 172
- AUDCHF: 172
- AUDJPY: 172
- AUDNZD: 172
- AUDUSD: 172
- AUS200: 49
- AVAXUSD: 221
- BCHUSD: 221
- BNBUSD: 221
- BRENT: 155
- BTCUSD: 419
- CADCHF: 172
- CADJPY: 172
- CHFJPY: 172
- DOGEUSD: 221
- DOTUSD: 221
- ETHUSD: 419
- EU50: 63
- EURAUD: 172
- EURCAD: 310
- EURCHF: 172
- EURGBP: 172
- EURJPY: 172
- EURUSD: 172
- FRA40: 63
- GBPAUD: 172
- GBPCAD: 172
- GBPCHF: 172
- GBPJPY: 172
- GBPUSD: 172
- GER40: 63
- GOLD: 274
- HK50: 49
- JPN225: 49
- LINKUSD: 221
- LTCUSD: 221
- NAS100: 49
- NATGAS: 155
- NZDCAD: 172
- NZDCHF: 172
- NZDJPY: 172
- NZDUSD: 172
- SILVER: 155
- SOLUSD: 221
- UK100: 63
- US30: 49
- US500: 85
- USDCAD: 172
- USDCHF: 172
- USDJPY: 308
- WTI: 155
- XRPUSD: 221

## 6. MR candidates / resolved
- 131 candidates, 0 resolved

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