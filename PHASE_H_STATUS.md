# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-08T19:35:04.434535

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
39

## 5. Observation count by asset
- ADAUSD: 746
- AUDCAD: 550
- AUDCHF: 550
- AUDJPY: 550
- AUDNZD: 550
- AUDUSD: 550
- AUS200: 161
- AVAXUSD: 746
- BCHUSD: 746
- BNBUSD: 746
- BRENT: 521
- BTCUSD: 944
- CADCHF: 550
- CADJPY: 550
- CHFJPY: 550
- DOGEUSD: 746
- DOTUSD: 746
- ETHUSD: 944
- EU50: 207
- EURAUD: 550
- EURCAD: 688
- EURCHF: 550
- EURGBP: 550
- EURJPY: 550
- EURUSD: 550
- FRA40: 207
- GBPAUD: 550
- GBPCAD: 550
- GBPCHF: 550
- GBPJPY: 550
- GBPUSD: 550
- GER40: 207
- GOLD: 642
- HK50: 154
- JPN225: 140
- LINKUSD: 746
- LTCUSD: 746
- NAS100: 160
- NATGAS: 522
- NZDCAD: 550
- NZDCHF: 550
- NZDJPY: 550
- NZDUSD: 550
- SILVER: 522
- SOLUSD: 746
- UK100: 207
- US30: 160
- US500: 195
- USDCAD: 550
- USDCHF: 547
- USDJPY: 686
- WTI: 522
- XRPUSD: 746

## 6. MR candidates / resolved
- 591 candidates, 0 resolved

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