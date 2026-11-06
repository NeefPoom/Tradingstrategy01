# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-06T22:28:47.818233

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
68

## 5. Observation count by asset
- ADAUSD: 1445
- AUDCAD: 1052
- AUDCHF: 1052
- AUDJPY: 1051
- AUDNZD: 1052
- AUDUSD: 1052
- AUS200: 308
- AVAXUSD: 1445
- BCHUSD: 1445
- BNBUSD: 1445
- BRENT: 1006
- BTCUSD: 1643
- CADCHF: 1052
- CADJPY: 1051
- CHFJPY: 1051
- DOGEUSD: 1445
- DOTUSD: 1445
- ETHUSD: 1643
- EU50: 396
- EURAUD: 1051
- EURCAD: 1190
- EURCHF: 1051
- EURGBP: 1052
- EURJPY: 1051
- EURUSD: 1051
- FRA40: 396
- GBPAUD: 1052
- GBPCAD: 1052
- GBPCHF: 1052
- GBPJPY: 1051
- GBPUSD: 1052
- GER40: 396
- GOLD: 1128
- HK50: 294
- JPN225: 273
- LINKUSD: 1445
- LTCUSD: 1445
- NAS100: 308
- NATGAS: 1011
- NZDCAD: 1052
- NZDCHF: 1052
- NZDJPY: 1051
- NZDUSD: 1052
- SILVER: 1007
- SOLUSD: 1445
- UK100: 396
- US30: 308
- US500: 344
- USDCAD: 1053
- USDCHF: 1047
- USDJPY: 1183
- WTI: 1007
- XRPUSD: 1445

## 6. MR candidates / resolved
- 1319 candidates, 0 resolved

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