# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-23T07:48:21.218292

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
23

## 5. Observation count by asset
- ADAUSD: 374
- AUDCAD: 276
- AUDCHF: 276
- AUDJPY: 276
- AUDNZD: 276
- AUDUSD: 276
- AUS200: 84
- AVAXUSD: 374
- BCHUSD: 374
- BNBUSD: 374
- BRENT: 256
- BTCUSD: 572
- CADCHF: 276
- CADJPY: 276
- CHFJPY: 276
- DOGEUSD: 374
- DOTUSD: 374
- ETHUSD: 572
- EU50: 99
- EURAUD: 276
- EURCAD: 414
- EURCHF: 276
- EURGBP: 276
- EURJPY: 276
- EURUSD: 276
- FRA40: 99
- GBPAUD: 276
- GBPCAD: 276
- GBPCHF: 276
- GBPJPY: 276
- GBPUSD: 276
- GER40: 99
- GOLD: 375
- HK50: 83
- JPN225: 63
- LINKUSD: 374
- LTCUSD: 374
- NAS100: 77
- NATGAS: 257
- NZDCAD: 276
- NZDCHF: 276
- NZDJPY: 276
- NZDUSD: 276
- SILVER: 257
- SOLUSD: 374
- UK100: 99
- US30: 77
- US500: 113
- USDCAD: 276
- USDCHF: 275
- USDJPY: 412
- WTI: 256
- XRPUSD: 374

## 6. MR candidates / resolved
- 241 candidates, 0 resolved

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