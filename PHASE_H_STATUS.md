# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-28T19:17:56.694145

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
59

## 5. Observation count by asset
- ADAUSD: 1226
- AUDCAD: 882
- AUDCHF: 882
- AUDJPY: 882
- AUDNZD: 882
- AUDUSD: 882
- AUS200: 259
- AVAXUSD: 1226
- BCHUSD: 1226
- BNBUSD: 1226
- BRENT: 843
- BTCUSD: 1424
- CADCHF: 882
- CADJPY: 882
- CHFJPY: 882
- DOGEUSD: 1226
- DOTUSD: 1226
- ETHUSD: 1424
- EU50: 333
- EURAUD: 882
- EURCAD: 1020
- EURCHF: 882
- EURGBP: 883
- EURJPY: 882
- EURUSD: 882
- FRA40: 333
- GBPAUD: 882
- GBPCAD: 882
- GBPCHF: 882
- GBPJPY: 882
- GBPUSD: 883
- GER40: 333
- GOLD: 965
- HK50: 245
- JPN225: 231
- LINKUSD: 1226
- LTCUSD: 1226
- NAS100: 257
- NATGAS: 848
- NZDCAD: 882
- NZDCHF: 882
- NZDJPY: 882
- NZDUSD: 882
- SILVER: 844
- SOLUSD: 1226
- UK100: 333
- US30: 257
- US500: 293
- USDCAD: 882
- USDCHF: 877
- USDJPY: 1015
- WTI: 844
- XRPUSD: 1226

## 6. MR candidates / resolved
- 1077 candidates, 0 resolved

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