# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-16T18:56:37.965801

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
17

## 5. Observation count by asset
- ADAUSD: 217
- AUDCAD: 168
- AUDCHF: 168
- AUDJPY: 168
- AUDNZD: 168
- AUDUSD: 168
- AUS200: 49
- AVAXUSD: 217
- BCHUSD: 217
- BNBUSD: 217
- BRENT: 152
- BTCUSD: 415
- CADCHF: 168
- CADJPY: 168
- CHFJPY: 168
- DOGEUSD: 217
- DOTUSD: 217
- ETHUSD: 415
- EU50: 63
- EURAUD: 168
- EURCAD: 306
- EURCHF: 168
- EURGBP: 168
- EURJPY: 168
- EURUSD: 168
- FRA40: 63
- GBPAUD: 168
- GBPCAD: 168
- GBPCHF: 168
- GBPJPY: 168
- GBPUSD: 168
- GER40: 63
- GOLD: 271
- HK50: 49
- JPN225: 49
- LINKUSD: 217
- LTCUSD: 217
- NAS100: 47
- NATGAS: 152
- NZDCAD: 168
- NZDCHF: 168
- NZDJPY: 168
- NZDUSD: 168
- SILVER: 152
- SOLUSD: 217
- UK100: 63
- US30: 47
- US500: 83
- USDCAD: 168
- USDCHF: 168
- USDJPY: 304
- WTI: 152
- XRPUSD: 217

## 6. MR candidates / resolved
- 122 candidates, 0 resolved

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