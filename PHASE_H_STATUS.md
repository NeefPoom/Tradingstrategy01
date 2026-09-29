# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-29T00:26:10.422856

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
29

## 5. Observation count by asset
- ADAUSD: 508
- AUDCAD: 362
- AUDCHF: 362
- AUDJPY: 362
- AUDNZD: 362
- AUDUSD: 362
- AUS200: 105
- AVAXUSD: 508
- BCHUSD: 508
- BNBUSD: 508
- BRENT: 341
- BTCUSD: 706
- CADCHF: 362
- CADJPY: 362
- CHFJPY: 362
- DOGEUSD: 508
- DOTUSD: 508
- ETHUSD: 706
- EU50: 135
- EURAUD: 362
- EURCAD: 500
- EURCHF: 362
- EURGBP: 362
- EURJPY: 362
- EURUSD: 362
- FRA40: 135
- GBPAUD: 362
- GBPCAD: 362
- GBPCHF: 362
- GBPJPY: 362
- GBPUSD: 362
- GER40: 135
- GOLD: 461
- HK50: 105
- JPN225: 84
- LINKUSD: 508
- LTCUSD: 508
- NAS100: 105
- NATGAS: 342
- NZDCAD: 362
- NZDCHF: 362
- NZDJPY: 362
- NZDUSD: 362
- SILVER: 342
- SOLUSD: 508
- UK100: 135
- US30: 105
- US500: 141
- USDCAD: 362
- USDCHF: 360
- USDJPY: 498
- WTI: 341
- XRPUSD: 508

## 6. MR candidates / resolved
- 349 candidates, 0 resolved

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