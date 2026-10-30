# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-30T02:02:14.673486

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
60

## 5. Observation count by asset
- ADAUSD: 1255
- AUDCAD: 911
- AUDCHF: 911
- AUDJPY: 911
- AUDNZD: 911
- AUDUSD: 911
- AUS200: 268
- AVAXUSD: 1256
- BCHUSD: 1255
- BNBUSD: 1256
- BRENT: 871
- BTCUSD: 1453
- CADCHF: 911
- CADJPY: 911
- CHFJPY: 911
- DOGEUSD: 1255
- DOTUSD: 1255
- ETHUSD: 1453
- EU50: 342
- EURAUD: 911
- EURCAD: 1049
- EURCHF: 911
- EURGBP: 912
- EURJPY: 911
- EURUSD: 911
- FRA40: 342
- GBPAUD: 911
- GBPCAD: 911
- GBPCHF: 911
- GBPJPY: 911
- GBPUSD: 912
- GER40: 342
- GOLD: 993
- HK50: 252
- JPN225: 239
- LINKUSD: 1255
- LTCUSD: 1255
- NAS100: 266
- NATGAS: 876
- NZDCAD: 911
- NZDCHF: 911
- NZDJPY: 911
- NZDUSD: 911
- SILVER: 872
- SOLUSD: 1255
- UK100: 342
- US30: 266
- US500: 302
- USDCAD: 911
- USDCHF: 906
- USDJPY: 1044
- WTI: 872
- XRPUSD: 1255

## 6. MR candidates / resolved
- 1113 candidates, 0 resolved

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