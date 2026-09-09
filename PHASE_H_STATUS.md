# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-09T08:58:16.618125

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
9

## 5. Observation count by asset
- ADAUSD: 39
- AUDCAD: 39
- AUDCHF: 39
- AUDJPY: 39
- AUDNZD: 39
- AUDUSD: 39
- AUS200: 14
- AVAXUSD: 39
- BCHUSD: 39
- BNBUSD: 39
- BRENT: 27
- BTCUSD: 237
- CADCHF: 39
- CADJPY: 39
- CHFJPY: 39
- DOGEUSD: 39
- DOTUSD: 39
- ETHUSD: 237
- EU50: 10
- EURAUD: 39
- EURCAD: 177
- EURCHF: 39
- EURGBP: 39
- EURJPY: 39
- EURUSD: 39
- FRA40: 10
- GBPAUD: 39
- GBPCAD: 39
- GBPCHF: 39
- GBPJPY: 39
- GBPUSD: 39
- GER40: 10
- GOLD: 146
- HK50: 14
- JPN225: 14
- LINKUSD: 39
- LTCUSD: 39
- NAS100: 7
- NATGAS: 27
- NZDCAD: 39
- NZDCHF: 39
- NZDJPY: 39
- NZDUSD: 39
- SILVER: 26
- SOLUSD: 39
- UK100: 10
- US30: 7
- US500: 43
- USDCAD: 39
- USDCHF: 39
- USDJPY: 176
- WTI: 27
- XRPUSD: 39

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