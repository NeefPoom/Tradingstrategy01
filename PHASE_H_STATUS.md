# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-02T15:49:57.181484

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
33

## 5. Observation count by asset
- ADAUSD: 598
- AUDCAD: 451
- AUDCHF: 451
- AUDJPY: 451
- AUDNZD: 451
- AUDUSD: 451
- AUS200: 133
- AVAXUSD: 598
- BCHUSD: 598
- BNBUSD: 598
- BRENT: 425
- BTCUSD: 796
- CADCHF: 451
- CADJPY: 451
- CHFJPY: 451
- DOGEUSD: 598
- DOTUSD: 598
- ETHUSD: 796
- EU50: 170
- EURAUD: 451
- EURCAD: 589
- EURCHF: 451
- EURGBP: 451
- EURJPY: 451
- EURUSD: 451
- FRA40: 170
- GBPAUD: 451
- GBPCAD: 451
- GBPCHF: 451
- GBPJPY: 451
- GBPUSD: 451
- GER40: 170
- GOLD: 545
- HK50: 126
- JPN225: 112
- LINKUSD: 598
- LTCUSD: 598
- NAS100: 128
- NATGAS: 426
- NZDCAD: 451
- NZDCHF: 451
- NZDJPY: 451
- NZDUSD: 451
- SILVER: 426
- SOLUSD: 598
- UK100: 170
- US30: 128
- US500: 164
- USDCAD: 451
- USDCHF: 449
- USDJPY: 587
- WTI: 425
- XRPUSD: 598

## 6. MR candidates / resolved
- 465 candidates, 0 resolved

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