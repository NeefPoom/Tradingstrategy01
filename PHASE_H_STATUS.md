# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-18T00:49:43.645900

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
18

## 5. Observation count by asset
- ADAUSD: 246
- AUDCAD: 198
- AUDCHF: 198
- AUDJPY: 198
- AUDNZD: 198
- AUDUSD: 198
- AUS200: 56
- AVAXUSD: 246
- BCHUSD: 246
- BNBUSD: 246
- BRENT: 180
- BTCUSD: 444
- CADCHF: 198
- CADJPY: 198
- CHFJPY: 198
- DOGEUSD: 246
- DOTUSD: 246
- ETHUSD: 444
- EU50: 72
- EURAUD: 198
- EURCAD: 336
- EURCHF: 198
- EURGBP: 198
- EURJPY: 198
- EURUSD: 198
- FRA40: 72
- GBPAUD: 198
- GBPCAD: 198
- GBPCHF: 198
- GBPJPY: 198
- GBPUSD: 198
- GER40: 72
- GOLD: 299
- HK50: 56
- JPN225: 56
- LINKUSD: 246
- LTCUSD: 246
- NAS100: 56
- NATGAS: 180
- NZDCAD: 198
- NZDCHF: 198
- NZDJPY: 198
- NZDUSD: 198
- SILVER: 180
- SOLUSD: 246
- UK100: 72
- US30: 56
- US500: 92
- USDCAD: 198
- USDCHF: 198
- USDJPY: 334
- WTI: 180
- XRPUSD: 246

## 6. MR candidates / resolved
- 153 candidates, 0 resolved

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