# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-18T09:07:54.004436

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
48

## 5. Observation count by asset
- ADAUSD: 976
- AUDCAD: 696
- AUDCHF: 696
- AUDJPY: 696
- AUDNZD: 696
- AUDUSD: 696
- AUS200: 203
- AVAXUSD: 976
- BCHUSD: 976
- BNBUSD: 976
- BRENT: 661
- BTCUSD: 1174
- CADCHF: 696
- CADJPY: 696
- CHFJPY: 696
- DOGEUSD: 976
- DOTUSD: 976
- ETHUSD: 1174
- EU50: 261
- EURAUD: 696
- EURCAD: 834
- EURCHF: 696
- EURGBP: 697
- EURJPY: 696
- EURUSD: 696
- FRA40: 261
- GBPAUD: 696
- GBPCAD: 696
- GBPCHF: 696
- GBPJPY: 696
- GBPUSD: 697
- GER40: 261
- GOLD: 783
- HK50: 196
- JPN225: 175
- LINKUSD: 976
- LTCUSD: 976
- NAS100: 203
- NATGAS: 665
- NZDCAD: 696
- NZDCHF: 696
- NZDJPY: 696
- NZDUSD: 696
- SILVER: 662
- SOLUSD: 976
- UK100: 261
- US30: 203
- US500: 239
- USDCAD: 696
- USDCHF: 691
- USDJPY: 830
- WTI: 662
- XRPUSD: 976

## 6. MR candidates / resolved
- 816 candidates, 0 resolved

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