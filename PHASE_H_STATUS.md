# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-15T04:39:31.522083

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
45

## 5. Observation count by asset
- ADAUSD: 899
- AUDCAD: 654
- AUDCHF: 654
- AUDJPY: 654
- AUDNZD: 654
- AUDUSD: 654
- AUS200: 194
- AVAXUSD: 899
- BCHUSD: 899
- BNBUSD: 899
- BRENT: 619
- BTCUSD: 1097
- CADCHF: 654
- CADJPY: 654
- CHFJPY: 654
- DOGEUSD: 899
- DOTUSD: 899
- ETHUSD: 1097
- EU50: 243
- EURAUD: 654
- EURCAD: 792
- EURCHF: 654
- EURGBP: 655
- EURJPY: 654
- EURUSD: 654
- FRA40: 243
- GBPAUD: 654
- GBPCAD: 654
- GBPCHF: 654
- GBPJPY: 654
- GBPUSD: 654
- GER40: 243
- GOLD: 742
- HK50: 185
- JPN225: 165
- LINKUSD: 899
- LTCUSD: 899
- NAS100: 189
- NATGAS: 623
- NZDCAD: 654
- NZDCHF: 654
- NZDJPY: 654
- NZDUSD: 654
- SILVER: 621
- SOLUSD: 899
- UK100: 243
- US30: 189
- US500: 225
- USDCAD: 654
- USDCHF: 650
- USDJPY: 789
- WTI: 620
- XRPUSD: 899

## 6. MR candidates / resolved
- 753 candidates, 0 resolved

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