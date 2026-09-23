# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-23T01:48:35.674182

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
23

## 5. Observation count by asset
- ADAUSD: 368
- AUDCAD: 270
- AUDCHF: 270
- AUDJPY: 270
- AUDNZD: 270
- AUDUSD: 270
- AUS200: 78
- AVAXUSD: 368
- BCHUSD: 368
- BNBUSD: 368
- BRENT: 250
- BTCUSD: 566
- CADCHF: 270
- CADJPY: 270
- CHFJPY: 270
- DOGEUSD: 368
- DOTUSD: 368
- ETHUSD: 566
- EU50: 99
- EURAUD: 270
- EURCAD: 408
- EURCHF: 270
- EURGBP: 270
- EURJPY: 270
- EURUSD: 270
- FRA40: 99
- GBPAUD: 270
- GBPCAD: 270
- GBPCHF: 270
- GBPJPY: 270
- GBPUSD: 270
- GER40: 99
- GOLD: 369
- HK50: 77
- JPN225: 63
- LINKUSD: 368
- LTCUSD: 368
- NAS100: 77
- NATGAS: 251
- NZDCAD: 270
- NZDCHF: 270
- NZDJPY: 270
- NZDUSD: 270
- SILVER: 251
- SOLUSD: 368
- UK100: 99
- US30: 77
- US500: 113
- USDCAD: 270
- USDCHF: 269
- USDJPY: 406
- WTI: 250
- XRPUSD: 368

## 6. MR candidates / resolved
- 235 candidates, 0 resolved

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