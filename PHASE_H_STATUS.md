# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-25T03:17:08.019053

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
86

## 5. Observation count by asset
- ADAUSD: 1882
- AUDCAD: 1342
- AUDCHF: 1342
- AUDJPY: 1341
- AUDNZD: 1342
- AUDUSD: 1342
- AUS200: 396
- AVAXUSD: 1882
- BCHUSD: 1882
- BNBUSD: 1882
- BRENT: 1286
- BTCUSD: 2080
- CADCHF: 1345
- CADJPY: 1341
- CHFJPY: 1341
- DOGEUSD: 1882
- DOTUSD: 1882
- ETHUSD: 2080
- EU50: 504
- EURAUD: 1341
- EURCAD: 1480
- EURCHF: 1341
- EURGBP: 1342
- EURJPY: 1340
- EURUSD: 1341
- FRA40: 504
- GBPAUD: 1342
- GBPCAD: 1342
- GBPCHF: 1342
- GBPJPY: 1341
- GBPUSD: 1342
- GER40: 504
- GOLD: 1411
- HK50: 379
- JPN225: 353
- LINKUSD: 1882
- LTCUSD: 1882
- NAS100: 392
- NATGAS: 1291
- NZDCAD: 1342
- NZDCHF: 1342
- NZDJPY: 1341
- NZDUSD: 1342
- SILVER: 1288
- SOLUSD: 1882
- UK100: 504
- US30: 392
- US500: 428
- USDCAD: 1343
- USDCHF: 1337
- USDJPY: 1471
- WTI: 1290
- XRPUSD: 1882

## 6. MR candidates / resolved
- 1650 candidates, 0 resolved

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