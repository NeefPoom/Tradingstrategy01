# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-12T11:17:32.254803

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
74

## 5. Observation count by asset
- ADAUSD: 1578
- AUDCAD: 1136
- AUDCHF: 1136
- AUDJPY: 1135
- AUDNZD: 1136
- AUDUSD: 1135
- AUS200: 336
- AVAXUSD: 1578
- BCHUSD: 1578
- BNBUSD: 1578
- BRENT: 1087
- BTCUSD: 1775
- CADCHF: 1137
- CADJPY: 1135
- CHFJPY: 1135
- DOGEUSD: 1578
- DOTUSD: 1578
- ETHUSD: 1775
- EU50: 426
- EURAUD: 1135
- EURCAD: 1273
- EURCHF: 1135
- EURGBP: 1136
- EURJPY: 1135
- EURUSD: 1134
- FRA40: 426
- GBPAUD: 1136
- GBPCAD: 1136
- GBPCHF: 1136
- GBPJPY: 1135
- GBPUSD: 1135
- GER40: 426
- GOLD: 1209
- HK50: 322
- JPN225: 301
- LINKUSD: 1578
- LTCUSD: 1578
- NAS100: 329
- NATGAS: 1092
- NZDCAD: 1136
- NZDCHF: 1136
- NZDJPY: 1135
- NZDUSD: 1136
- SILVER: 1088
- SOLUSD: 1578
- UK100: 426
- US30: 329
- US500: 365
- USDCAD: 1137
- USDCHF: 1131
- USDJPY: 1266
- WTI: 1088
- XRPUSD: 1578

## 6. MR candidates / resolved
- 1417 candidates, 0 resolved

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