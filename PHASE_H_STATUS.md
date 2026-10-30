# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-30T08:48:51.999307

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
60

## 5. Observation count by asset
- ADAUSD: 1263
- AUDCAD: 919
- AUDCHF: 919
- AUDJPY: 919
- AUDNZD: 919
- AUDUSD: 919
- AUS200: 273
- AVAXUSD: 1263
- BCHUSD: 1263
- BNBUSD: 1263
- BRENT: 878
- BTCUSD: 1461
- CADCHF: 919
- CADJPY: 919
- CHFJPY: 919
- DOGEUSD: 1263
- DOTUSD: 1263
- ETHUSD: 1461
- EU50: 342
- EURAUD: 919
- EURCAD: 1057
- EURCHF: 919
- EURGBP: 920
- EURJPY: 919
- EURUSD: 919
- FRA40: 342
- GBPAUD: 919
- GBPCAD: 919
- GBPCHF: 919
- GBPJPY: 919
- GBPUSD: 920
- GER40: 342
- GOLD: 1000
- HK50: 259
- JPN225: 245
- LINKUSD: 1263
- LTCUSD: 1263
- NAS100: 266
- NATGAS: 883
- NZDCAD: 919
- NZDCHF: 919
- NZDJPY: 919
- NZDUSD: 919
- SILVER: 879
- SOLUSD: 1263
- UK100: 342
- US30: 266
- US500: 302
- USDCAD: 919
- USDCHF: 914
- USDJPY: 1052
- WTI: 879
- XRPUSD: 1263

## 6. MR candidates / resolved
- 1114 candidates, 0 resolved

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