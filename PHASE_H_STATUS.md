# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-03T00:28:07.601849

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
33

## 5. Observation count by asset
- ADAUSD: 606
- AUDCAD: 458
- AUDCHF: 458
- AUDJPY: 458
- AUDNZD: 458
- AUDUSD: 458
- AUS200: 133
- AVAXUSD: 606
- BCHUSD: 606
- BNBUSD: 606
- BRENT: 431
- BTCUSD: 804
- CADCHF: 458
- CADJPY: 458
- CHFJPY: 458
- DOGEUSD: 606
- DOTUSD: 606
- ETHUSD: 804
- EU50: 171
- EURAUD: 458
- EURCAD: 596
- EURCHF: 458
- EURGBP: 458
- EURJPY: 458
- EURUSD: 458
- FRA40: 171
- GBPAUD: 458
- GBPCAD: 458
- GBPCHF: 458
- GBPJPY: 458
- GBPUSD: 458
- GER40: 171
- GOLD: 551
- HK50: 126
- JPN225: 112
- LINKUSD: 606
- LTCUSD: 606
- NAS100: 133
- NATGAS: 432
- NZDCAD: 458
- NZDCHF: 458
- NZDJPY: 458
- NZDUSD: 458
- SILVER: 432
- SOLUSD: 606
- UK100: 171
- US30: 133
- US500: 169
- USDCAD: 458
- USDCHF: 455
- USDJPY: 594
- WTI: 431
- XRPUSD: 606

## 6. MR candidates / resolved
- 480 candidates, 0 resolved

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