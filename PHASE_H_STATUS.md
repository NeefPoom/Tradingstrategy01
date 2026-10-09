# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-09T00:03:15.434844

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
39

## 5. Observation count by asset
- ADAUSD: 751
- AUDCAD: 554
- AUDCHF: 554
- AUDJPY: 554
- AUDNZD: 554
- AUDUSD: 554
- AUS200: 161
- AVAXUSD: 751
- BCHUSD: 751
- BNBUSD: 751
- BRENT: 524
- BTCUSD: 948
- CADCHF: 554
- CADJPY: 554
- CHFJPY: 554
- DOGEUSD: 751
- DOTUSD: 751
- ETHUSD: 948
- EU50: 207
- EURAUD: 554
- EURCAD: 692
- EURCHF: 554
- EURGBP: 554
- EURJPY: 554
- EURUSD: 554
- FRA40: 207
- GBPAUD: 554
- GBPCAD: 554
- GBPCHF: 554
- GBPJPY: 554
- GBPUSD: 554
- GER40: 207
- GOLD: 645
- HK50: 154
- JPN225: 140
- LINKUSD: 751
- LTCUSD: 751
- NAS100: 161
- NATGAS: 526
- NZDCAD: 554
- NZDCHF: 554
- NZDJPY: 554
- NZDUSD: 554
- SILVER: 525
- SOLUSD: 750
- UK100: 207
- US30: 161
- US500: 197
- USDCAD: 554
- USDCHF: 551
- USDJPY: 690
- WTI: 525
- XRPUSD: 751

## 6. MR candidates / resolved
- 599 candidates, 0 resolved

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