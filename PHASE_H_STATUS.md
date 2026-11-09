# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-09T21:04:12.913651

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
71

## 5. Observation count by asset
- ADAUSD: 1515
- AUDCAD: 1073
- AUDCHF: 1073
- AUDJPY: 1072
- AUDNZD: 1073
- AUDUSD: 1073
- AUS200: 315
- AVAXUSD: 1516
- BCHUSD: 1516
- BNBUSD: 1516
- BRENT: 1027
- BTCUSD: 1713
- CADCHF: 1074
- CADJPY: 1072
- CHFJPY: 1072
- DOGEUSD: 1515
- DOTUSD: 1516
- ETHUSD: 1713
- EU50: 405
- EURAUD: 1072
- EURCAD: 1211
- EURCHF: 1072
- EURGBP: 1073
- EURJPY: 1072
- EURUSD: 1072
- FRA40: 405
- GBPAUD: 1073
- GBPCAD: 1073
- GBPCHF: 1073
- GBPJPY: 1072
- GBPUSD: 1073
- GER40: 405
- GOLD: 1149
- HK50: 301
- JPN225: 280
- LINKUSD: 1516
- LTCUSD: 1515
- NAS100: 314
- NATGAS: 1032
- NZDCAD: 1073
- NZDCHF: 1073
- NZDJPY: 1072
- NZDUSD: 1073
- SILVER: 1028
- SOLUSD: 1515
- UK100: 405
- US30: 314
- US500: 350
- USDCAD: 1074
- USDCHF: 1068
- USDJPY: 1204
- WTI: 1028
- XRPUSD: 1515

## 6. MR candidates / resolved
- 1351 candidates, 0 resolved

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