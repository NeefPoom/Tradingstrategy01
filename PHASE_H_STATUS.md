# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-29T18:58:31.549864

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
30

## 5. Observation count by asset
- ADAUSD: 529
- AUDCAD: 382
- AUDCHF: 382
- AUDJPY: 382
- AUDNZD: 382
- AUDUSD: 382
- AUS200: 112
- AVAXUSD: 529
- BCHUSD: 529
- BNBUSD: 529
- BRENT: 359
- BTCUSD: 727
- CADCHF: 382
- CADJPY: 382
- CHFJPY: 382
- DOGEUSD: 529
- DOTUSD: 529
- ETHUSD: 727
- EU50: 144
- EURAUD: 382
- EURCAD: 520
- EURCHF: 382
- EURGBP: 382
- EURJPY: 382
- EURUSD: 382
- FRA40: 144
- GBPAUD: 382
- GBPCAD: 382
- GBPCHF: 382
- GBPJPY: 382
- GBPUSD: 382
- GER40: 144
- GOLD: 479
- HK50: 112
- JPN225: 91
- LINKUSD: 529
- LTCUSD: 529
- NAS100: 110
- NATGAS: 360
- NZDCAD: 382
- NZDCHF: 382
- NZDJPY: 382
- NZDUSD: 382
- SILVER: 360
- SOLUSD: 529
- UK100: 144
- US30: 110
- US500: 146
- USDCAD: 382
- USDCHF: 380
- USDJPY: 518
- WTI: 359
- XRPUSD: 529

## 6. MR candidates / resolved
- 378 candidates, 0 resolved

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