# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-16T09:47:47.955941

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
46

## 5. Observation count by asset
- ADAUSD: 928
- AUDCAD: 683
- AUDCHF: 683
- AUDJPY: 683
- AUDNZD: 683
- AUDUSD: 683
- AUS200: 203
- AVAXUSD: 928
- BCHUSD: 928
- BNBUSD: 928
- BRENT: 649
- BTCUSD: 1126
- CADCHF: 683
- CADJPY: 683
- CHFJPY: 683
- DOGEUSD: 928
- DOTUSD: 928
- ETHUSD: 1126
- EU50: 254
- EURAUD: 683
- EURCAD: 821
- EURCHF: 683
- EURGBP: 684
- EURJPY: 683
- EURUSD: 683
- FRA40: 254
- GBPAUD: 683
- GBPCAD: 683
- GBPCHF: 683
- GBPJPY: 683
- GBPUSD: 683
- GER40: 254
- GOLD: 771
- HK50: 196
- JPN225: 175
- LINKUSD: 928
- LTCUSD: 928
- NAS100: 196
- NATGAS: 653
- NZDCAD: 683
- NZDCHF: 683
- NZDJPY: 683
- NZDUSD: 683
- SILVER: 650
- SOLUSD: 928
- UK100: 254
- US30: 196
- US500: 232
- USDCAD: 683
- USDCHF: 679
- USDJPY: 818
- WTI: 650
- XRPUSD: 928

## 6. MR candidates / resolved
- 791 candidates, 0 resolved

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