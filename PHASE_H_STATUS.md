# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-28T23:14:26.509359

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
59

## 5. Observation count by asset
- ADAUSD: 1230
- AUDCAD: 886
- AUDCHF: 886
- AUDJPY: 886
- AUDNZD: 886
- AUDUSD: 886
- AUS200: 259
- AVAXUSD: 1230
- BCHUSD: 1230
- BNBUSD: 1230
- BRENT: 846
- BTCUSD: 1428
- CADCHF: 886
- CADJPY: 886
- CHFJPY: 886
- DOGEUSD: 1230
- DOTUSD: 1230
- ETHUSD: 1428
- EU50: 333
- EURAUD: 886
- EURCAD: 1024
- EURCHF: 886
- EURGBP: 887
- EURJPY: 886
- EURUSD: 886
- FRA40: 333
- GBPAUD: 886
- GBPCAD: 886
- GBPCHF: 886
- GBPJPY: 886
- GBPUSD: 887
- GER40: 333
- GOLD: 968
- HK50: 245
- JPN225: 231
- LINKUSD: 1230
- LTCUSD: 1230
- NAS100: 259
- NATGAS: 851
- NZDCAD: 886
- NZDCHF: 886
- NZDJPY: 886
- NZDUSD: 886
- SILVER: 847
- SOLUSD: 1230
- UK100: 333
- US30: 259
- US500: 295
- USDCAD: 886
- USDCHF: 881
- USDJPY: 1019
- WTI: 847
- XRPUSD: 1230

## 6. MR candidates / resolved
- 1084 candidates, 0 resolved

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