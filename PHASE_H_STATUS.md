# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-05T22:13:28.683274

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
67

## 5. Observation count by asset
- ADAUSD: 1421
- AUDCAD: 1028
- AUDCHF: 1028
- AUDJPY: 1027
- AUDNZD: 1028
- AUDUSD: 1027
- AUS200: 301
- AVAXUSD: 1421
- BCHUSD: 1421
- BNBUSD: 1421
- BRENT: 983
- BTCUSD: 1618
- CADCHF: 1028
- CADJPY: 1027
- CHFJPY: 1027
- DOGEUSD: 1421
- DOTUSD: 1421
- ETHUSD: 1618
- EU50: 387
- EURAUD: 1027
- EURCAD: 1165
- EURCHF: 1027
- EURGBP: 1028
- EURJPY: 1027
- EURUSD: 1026
- FRA40: 387
- GBPAUD: 1028
- GBPCAD: 1028
- GBPCHF: 1028
- GBPJPY: 1027
- GBPUSD: 1027
- GER40: 387
- GOLD: 1104
- HK50: 287
- JPN225: 266
- LINKUSD: 1421
- LTCUSD: 1421
- NAS100: 301
- NATGAS: 988
- NZDCAD: 1028
- NZDCHF: 1028
- NZDJPY: 1027
- NZDUSD: 1028
- SILVER: 984
- SOLUSD: 1421
- UK100: 387
- US30: 301
- US500: 337
- USDCAD: 1029
- USDCHF: 1023
- USDJPY: 1158
- WTI: 984
- XRPUSD: 1421

## 6. MR candidates / resolved
- 1290 candidates, 0 resolved

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