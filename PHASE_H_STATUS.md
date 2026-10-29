# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-29T02:54:48.229626

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
59

## 5. Observation count by asset
- ADAUSD: 1233
- AUDCAD: 889
- AUDCHF: 889
- AUDJPY: 889
- AUDNZD: 889
- AUDUSD: 889
- AUS200: 262
- AVAXUSD: 1233
- BCHUSD: 1233
- BNBUSD: 1233
- BRENT: 849
- BTCUSD: 1431
- CADCHF: 889
- CADJPY: 889
- CHFJPY: 889
- DOGEUSD: 1233
- DOTUSD: 1233
- ETHUSD: 1431
- EU50: 333
- EURAUD: 889
- EURCAD: 1027
- EURCHF: 889
- EURGBP: 890
- EURJPY: 889
- EURUSD: 889
- FRA40: 333
- GBPAUD: 889
- GBPCAD: 889
- GBPCHF: 889
- GBPJPY: 889
- GBPUSD: 890
- GER40: 333
- GOLD: 971
- HK50: 246
- JPN225: 233
- LINKUSD: 1233
- LTCUSD: 1233
- NAS100: 259
- NATGAS: 854
- NZDCAD: 889
- NZDCHF: 889
- NZDJPY: 889
- NZDUSD: 889
- SILVER: 850
- SOLUSD: 1233
- UK100: 333
- US30: 259
- US500: 295
- USDCAD: 889
- USDCHF: 884
- USDJPY: 1022
- WTI: 850
- XRPUSD: 1233

## 6. MR candidates / resolved
- 1090 candidates, 0 resolved

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