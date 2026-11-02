# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-02T01:52:18.582012

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
63

## 5. Observation count by asset
- ADAUSD: 1327
- AUDCAD: 935
- AUDCHF: 935
- AUDJPY: 934
- AUDNZD: 935
- AUDUSD: 935
- AUS200: 275
- AVAXUSD: 1327
- BCHUSD: 1327
- BNBUSD: 1327
- BRENT: 893
- BTCUSD: 1525
- CADCHF: 935
- CADJPY: 934
- CHFJPY: 934
- DOGEUSD: 1327
- DOTUSD: 1327
- ETHUSD: 1525
- EU50: 351
- EURAUD: 934
- EURCAD: 1073
- EURCHF: 934
- EURGBP: 935
- EURJPY: 934
- EURUSD: 934
- FRA40: 351
- GBPAUD: 935
- GBPCAD: 935
- GBPCHF: 935
- GBPJPY: 934
- GBPUSD: 935
- GER40: 351
- GOLD: 1015
- HK50: 259
- JPN225: 246
- LINKUSD: 1327
- LTCUSD: 1327
- NAS100: 273
- NATGAS: 898
- NZDCAD: 935
- NZDCHF: 935
- NZDJPY: 934
- NZDUSD: 935
- SILVER: 894
- SOLUSD: 1327
- UK100: 351
- US30: 273
- US500: 309
- USDCAD: 936
- USDCHF: 930
- USDJPY: 1066
- WTI: 894
- XRPUSD: 1327

## 6. MR candidates / resolved
- 1159 candidates, 0 resolved

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