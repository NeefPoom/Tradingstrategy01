# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-10T19:56:12.112449

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
72

## 5. Observation count by asset
- ADAUSD: 1538
- AUDCAD: 1096
- AUDCHF: 1096
- AUDJPY: 1095
- AUDNZD: 1096
- AUDUSD: 1096
- AUS200: 322
- AVAXUSD: 1538
- BCHUSD: 1538
- BNBUSD: 1538
- BRENT: 1049
- BTCUSD: 1736
- CADCHF: 1097
- CADJPY: 1095
- CHFJPY: 1095
- DOGEUSD: 1538
- DOTUSD: 1538
- ETHUSD: 1736
- EU50: 414
- EURAUD: 1095
- EURCAD: 1234
- EURCHF: 1095
- EURGBP: 1096
- EURJPY: 1095
- EURUSD: 1095
- FRA40: 414
- GBPAUD: 1096
- GBPCAD: 1096
- GBPCHF: 1096
- GBPJPY: 1095
- GBPUSD: 1096
- GER40: 414
- GOLD: 1172
- HK50: 308
- JPN225: 287
- LINKUSD: 1538
- LTCUSD: 1538
- NAS100: 320
- NATGAS: 1054
- NZDCAD: 1096
- NZDCHF: 1096
- NZDJPY: 1095
- NZDUSD: 1096
- SILVER: 1050
- SOLUSD: 1538
- UK100: 414
- US30: 320
- US500: 356
- USDCAD: 1097
- USDCHF: 1091
- USDJPY: 1227
- WTI: 1050
- XRPUSD: 1538

## 6. MR candidates / resolved
- 1377 candidates, 0 resolved

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