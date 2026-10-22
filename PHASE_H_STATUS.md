# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-22T23:39:31.141235

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
53

## 5. Observation count by asset
- ADAUSD: 1086
- AUDCAD: 792
- AUDCHF: 792
- AUDJPY: 792
- AUDNZD: 792
- AUDUSD: 792
- AUS200: 231
- AVAXUSD: 1086
- BCHUSD: 1086
- BNBUSD: 1086
- BRENT: 754
- BTCUSD: 1284
- CADCHF: 792
- CADJPY: 792
- CHFJPY: 792
- DOGEUSD: 1086
- DOTUSD: 1086
- ETHUSD: 1284
- EU50: 297
- EURAUD: 792
- EURCAD: 930
- EURCHF: 792
- EURGBP: 793
- EURJPY: 792
- EURUSD: 792
- FRA40: 297
- GBPAUD: 792
- GBPCAD: 792
- GBPCHF: 792
- GBPJPY: 792
- GBPUSD: 793
- GER40: 297
- GOLD: 876
- HK50: 217
- JPN225: 203
- LINKUSD: 1086
- LTCUSD: 1086
- NAS100: 231
- NATGAS: 758
- NZDCAD: 792
- NZDCHF: 792
- NZDJPY: 792
- NZDUSD: 792
- SILVER: 755
- SOLUSD: 1086
- UK100: 297
- US30: 231
- US500: 267
- USDCAD: 792
- USDCHF: 787
- USDJPY: 926
- WTI: 755
- XRPUSD: 1086

## 6. MR candidates / resolved
- 939 candidates, 0 resolved

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