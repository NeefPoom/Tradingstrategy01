# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-13T23:14:44.993212

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
44

## 5. Observation count by asset
- ADAUSD: 870
- AUDCAD: 625
- AUDCHF: 625
- AUDJPY: 625
- AUDNZD: 625
- AUDUSD: 625
- AUS200: 182
- AVAXUSD: 870
- BCHUSD: 870
- BNBUSD: 870
- BRENT: 593
- BTCUSD: 1068
- CADCHF: 625
- CADJPY: 625
- CHFJPY: 625
- DOGEUSD: 870
- DOTUSD: 870
- ETHUSD: 1068
- EU50: 234
- EURAUD: 625
- EURCAD: 763
- EURCHF: 625
- EURGBP: 626
- EURJPY: 625
- EURUSD: 625
- FRA40: 234
- GBPAUD: 625
- GBPCAD: 625
- GBPCHF: 625
- GBPJPY: 625
- GBPUSD: 625
- GER40: 234
- GOLD: 715
- HK50: 175
- JPN225: 154
- LINKUSD: 870
- LTCUSD: 870
- NAS100: 182
- NATGAS: 597
- NZDCAD: 625
- NZDCHF: 625
- NZDJPY: 625
- NZDUSD: 625
- SILVER: 594
- SOLUSD: 870
- UK100: 234
- US30: 182
- US500: 218
- USDCAD: 625
- USDCHF: 621
- USDJPY: 760
- WTI: 594
- XRPUSD: 870

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