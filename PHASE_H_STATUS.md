# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-23T07:35:23.842788

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
53

## 5. Observation count by asset
- ADAUSD: 1094
- AUDCAD: 800
- AUDCHF: 800
- AUDJPY: 800
- AUDNZD: 800
- AUDUSD: 800
- AUS200: 238
- AVAXUSD: 1094
- BCHUSD: 1094
- BNBUSD: 1094
- BRENT: 762
- BTCUSD: 1292
- CADCHF: 800
- CADJPY: 800
- CHFJPY: 800
- DOGEUSD: 1094
- DOTUSD: 1094
- ETHUSD: 1292
- EU50: 297
- EURAUD: 800
- EURCAD: 938
- EURCHF: 800
- EURGBP: 801
- EURJPY: 800
- EURUSD: 800
- FRA40: 297
- GBPAUD: 800
- GBPCAD: 800
- GBPCHF: 800
- GBPJPY: 800
- GBPUSD: 801
- GER40: 297
- GOLD: 884
- HK50: 223
- JPN225: 210
- LINKUSD: 1094
- LTCUSD: 1094
- NAS100: 231
- NATGAS: 766
- NZDCAD: 800
- NZDCHF: 800
- NZDJPY: 800
- NZDUSD: 800
- SILVER: 763
- SOLUSD: 1094
- UK100: 297
- US30: 231
- US500: 267
- USDCAD: 800
- USDCHF: 795
- USDJPY: 934
- WTI: 763
- XRPUSD: 1094

## 6. MR candidates / resolved
- 952 candidates, 0 resolved

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