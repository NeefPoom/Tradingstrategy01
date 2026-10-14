# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-14T13:13:13.768304

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
45

## 5. Observation count by asset
- ADAUSD: 884
- AUDCAD: 639
- AUDCHF: 639
- AUDJPY: 639
- AUDNZD: 639
- AUDUSD: 639
- AUS200: 189
- AVAXUSD: 884
- BCHUSD: 884
- BNBUSD: 884
- BRENT: 607
- BTCUSD: 1082
- CADCHF: 639
- CADJPY: 639
- CHFJPY: 639
- DOGEUSD: 884
- DOTUSD: 884
- ETHUSD: 1082
- EU50: 240
- EURAUD: 639
- EURCAD: 777
- EURCHF: 639
- EURGBP: 640
- EURJPY: 639
- EURUSD: 639
- FRA40: 240
- GBPAUD: 639
- GBPCAD: 639
- GBPCHF: 639
- GBPJPY: 639
- GBPUSD: 639
- GER40: 240
- GOLD: 729
- HK50: 182
- JPN225: 161
- LINKUSD: 884
- LTCUSD: 884
- NAS100: 182
- NATGAS: 611
- NZDCAD: 639
- NZDCHF: 639
- NZDJPY: 639
- NZDUSD: 639
- SILVER: 608
- SOLUSD: 884
- UK100: 240
- US30: 182
- US500: 218
- USDCAD: 639
- USDCHF: 635
- USDJPY: 774
- WTI: 608
- XRPUSD: 884

## 6. MR candidates / resolved
- 727 candidates, 0 resolved

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