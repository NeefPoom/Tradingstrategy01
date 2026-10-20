# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-20T01:19:58.140964

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
50

## 5. Observation count by asset
- ADAUSD: 1016
- AUDCAD: 722
- AUDCHF: 722
- AUDJPY: 722
- AUDNZD: 722
- AUDUSD: 722
- AUS200: 212
- AVAXUSD: 1016
- BCHUSD: 1016
- BNBUSD: 1016
- BRENT: 687
- BTCUSD: 1214
- CADCHF: 722
- CADJPY: 722
- CHFJPY: 722
- DOGEUSD: 1016
- DOTUSD: 1016
- ETHUSD: 1214
- EU50: 270
- EURAUD: 722
- EURCAD: 860
- EURCHF: 722
- EURGBP: 723
- EURJPY: 722
- EURUSD: 722
- FRA40: 270
- GBPAUD: 722
- GBPCAD: 722
- GBPCHF: 722
- GBPJPY: 722
- GBPUSD: 723
- GER40: 270
- GOLD: 809
- HK50: 196
- JPN225: 183
- LINKUSD: 1016
- LTCUSD: 1016
- NAS100: 210
- NATGAS: 691
- NZDCAD: 722
- NZDCHF: 722
- NZDJPY: 722
- NZDUSD: 722
- SILVER: 688
- SOLUSD: 1016
- UK100: 270
- US30: 210
- US500: 246
- USDCAD: 722
- USDCHF: 717
- USDJPY: 856
- WTI: 688
- XRPUSD: 1016

## 6. MR candidates / resolved
- 850 candidates, 0 resolved

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