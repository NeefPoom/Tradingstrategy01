# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-19T05:25:32.284437

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
49

## 5. Observation count by asset
- ADAUSD: 996
- AUDCAD: 702
- AUDCHF: 702
- AUDJPY: 702
- AUDNZD: 702
- AUDUSD: 702
- AUS200: 209
- AVAXUSD: 996
- BCHUSD: 996
- BNBUSD: 996
- BRENT: 666
- BTCUSD: 1194
- CADCHF: 702
- CADJPY: 702
- CHFJPY: 702
- DOGEUSD: 996
- DOTUSD: 996
- ETHUSD: 1194
- EU50: 261
- EURAUD: 702
- EURCAD: 840
- EURCHF: 702
- EURGBP: 703
- EURJPY: 702
- EURUSD: 702
- FRA40: 261
- GBPAUD: 702
- GBPCAD: 702
- GBPCHF: 702
- GBPJPY: 702
- GBPUSD: 703
- GER40: 261
- GOLD: 790
- HK50: 196
- JPN225: 180
- LINKUSD: 996
- LTCUSD: 996
- NAS100: 203
- NATGAS: 670
- NZDCAD: 702
- NZDCHF: 702
- NZDJPY: 702
- NZDUSD: 702
- SILVER: 669
- SOLUSD: 996
- UK100: 261
- US30: 203
- US500: 239
- USDCAD: 702
- USDCHF: 697
- USDJPY: 836
- WTI: 667
- XRPUSD: 996

## 6. MR candidates / resolved
- 835 candidates, 0 resolved

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