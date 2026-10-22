# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-22T11:51:24.642020

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
53

## 5. Observation count by asset
- ADAUSD: 1074
- AUDCAD: 780
- AUDCHF: 780
- AUDJPY: 780
- AUDNZD: 780
- AUDUSD: 780
- AUS200: 231
- AVAXUSD: 1074
- BCHUSD: 1074
- BNBUSD: 1074
- BRENT: 743
- BTCUSD: 1272
- CADCHF: 780
- CADJPY: 780
- CHFJPY: 780
- DOGEUSD: 1074
- DOTUSD: 1074
- ETHUSD: 1272
- EU50: 292
- EURAUD: 780
- EURCAD: 918
- EURCHF: 780
- EURGBP: 781
- EURJPY: 780
- EURUSD: 780
- FRA40: 292
- GBPAUD: 780
- GBPCAD: 780
- GBPCHF: 780
- GBPJPY: 780
- GBPUSD: 781
- GER40: 292
- GOLD: 865
- HK50: 217
- JPN225: 203
- LINKUSD: 1074
- LTCUSD: 1074
- NAS100: 224
- NATGAS: 747
- NZDCAD: 780
- NZDCHF: 780
- NZDJPY: 780
- NZDUSD: 780
- SILVER: 744
- SOLUSD: 1074
- UK100: 292
- US30: 224
- US500: 260
- USDCAD: 780
- USDCHF: 775
- USDJPY: 914
- WTI: 744
- XRPUSD: 1074

## 6. MR candidates / resolved
- 937 candidates, 0 resolved

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