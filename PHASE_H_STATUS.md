# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-24T15:05:33.098373

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
25

## 5. Observation count by asset
- ADAUSD: 406
- AUDCAD: 308
- AUDCHF: 308
- AUDJPY: 308
- AUDNZD: 308
- AUDUSD: 307
- AUS200: 91
- AVAXUSD: 406
- BCHUSD: 406
- BNBUSD: 406
- BRENT: 287
- BTCUSD: 603
- CADCHF: 308
- CADJPY: 308
- CHFJPY: 308
- DOGEUSD: 406
- DOTUSD: 406
- ETHUSD: 603
- EU50: 116
- EURAUD: 308
- EURCAD: 445
- EURCHF: 308
- EURGBP: 308
- EURJPY: 308
- EURUSD: 307
- FRA40: 116
- GBPAUD: 308
- GBPCAD: 308
- GBPCHF: 308
- GBPJPY: 308
- GBPUSD: 307
- GER40: 116
- GOLD: 406
- HK50: 91
- JPN225: 70
- LINKUSD: 406
- LTCUSD: 406
- NAS100: 85
- NATGAS: 288
- NZDCAD: 308
- NZDCHF: 308
- NZDJPY: 308
- NZDUSD: 307
- SILVER: 288
- SOLUSD: 406
- UK100: 116
- US30: 85
- US500: 121
- USDCAD: 307
- USDCHF: 307
- USDJPY: 443
- WTI: 287
- XRPUSD: 406

## 6. MR candidates / resolved
- 283 candidates, 0 resolved

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