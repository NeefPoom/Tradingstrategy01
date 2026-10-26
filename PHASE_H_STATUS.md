# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-26T20:55:27.107023

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
57

## 5. Observation count by asset
- ADAUSD: 1179
- AUDCAD: 835
- AUDCHF: 835
- AUDJPY: 835
- AUDNZD: 835
- AUDUSD: 835
- AUS200: 245
- AVAXUSD: 1179
- BCHUSD: 1179
- BNBUSD: 1179
- BRENT: 798
- BTCUSD: 1377
- CADCHF: 835
- CADJPY: 835
- CHFJPY: 835
- DOGEUSD: 1179
- DOTUSD: 1179
- ETHUSD: 1377
- EU50: 315
- EURAUD: 835
- EURCAD: 973
- EURCHF: 835
- EURGBP: 836
- EURJPY: 835
- EURUSD: 835
- FRA40: 315
- GBPAUD: 835
- GBPCAD: 835
- GBPCHF: 835
- GBPJPY: 835
- GBPUSD: 836
- GER40: 315
- GOLD: 920
- HK50: 231
- JPN225: 217
- LINKUSD: 1179
- LTCUSD: 1179
- NAS100: 245
- NATGAS: 803
- NZDCAD: 835
- NZDCHF: 835
- NZDJPY: 835
- NZDUSD: 835
- SILVER: 799
- SOLUSD: 1179
- UK100: 315
- US30: 245
- US500: 281
- USDCAD: 835
- USDCHF: 830
- USDJPY: 968
- WTI: 799
- XRPUSD: 1179

## 6. MR candidates / resolved
- 1020 candidates, 0 resolved

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