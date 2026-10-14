# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-14T01:58:07.123098

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
44

## 5. Observation count by asset
- ADAUSD: 872
- AUDCAD: 627
- AUDCHF: 627
- AUDJPY: 627
- AUDNZD: 627
- AUDUSD: 627
- AUS200: 184
- AVAXUSD: 872
- BCHUSD: 872
- BNBUSD: 872
- BRENT: 595
- BTCUSD: 1070
- CADCHF: 627
- CADJPY: 627
- CHFJPY: 627
- DOGEUSD: 872
- DOTUSD: 872
- ETHUSD: 1070
- EU50: 234
- EURAUD: 627
- EURCAD: 765
- EURCHF: 627
- EURGBP: 628
- EURJPY: 627
- EURUSD: 627
- FRA40: 234
- GBPAUD: 627
- GBPCAD: 627
- GBPCHF: 627
- GBPJPY: 627
- GBPUSD: 627
- GER40: 234
- GOLD: 717
- HK50: 175
- JPN225: 155
- LINKUSD: 872
- LTCUSD: 872
- NAS100: 182
- NATGAS: 599
- NZDCAD: 627
- NZDCHF: 627
- NZDJPY: 627
- NZDUSD: 627
- SILVER: 596
- SOLUSD: 872
- UK100: 234
- US30: 182
- US500: 218
- USDCAD: 627
- USDCHF: 623
- USDJPY: 762
- WTI: 596
- XRPUSD: 872

## 6. MR candidates / resolved
- 713 candidates, 0 resolved

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