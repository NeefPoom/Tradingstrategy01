# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-29T23:02:45.641372

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
30

## 5. Observation count by asset
- ADAUSD: 533
- AUDCAD: 386
- AUDCHF: 386
- AUDJPY: 386
- AUDNZD: 386
- AUDUSD: 386
- AUS200: 112
- AVAXUSD: 534
- BCHUSD: 534
- BNBUSD: 534
- BRENT: 362
- BTCUSD: 731
- CADCHF: 386
- CADJPY: 386
- CHFJPY: 386
- DOGEUSD: 534
- DOTUSD: 534
- ETHUSD: 731
- EU50: 144
- EURAUD: 386
- EURCAD: 524
- EURCHF: 386
- EURGBP: 386
- EURJPY: 386
- EURUSD: 386
- FRA40: 144
- GBPAUD: 386
- GBPCAD: 386
- GBPCHF: 386
- GBPJPY: 386
- GBPUSD: 386
- GER40: 144
- GOLD: 482
- HK50: 112
- JPN225: 91
- LINKUSD: 534
- LTCUSD: 534
- NAS100: 112
- NATGAS: 363
- NZDCAD: 386
- NZDCHF: 386
- NZDJPY: 386
- NZDUSD: 386
- SILVER: 363
- SOLUSD: 533
- UK100: 144
- US30: 112
- US500: 148
- USDCAD: 386
- USDCHF: 384
- USDJPY: 522
- WTI: 362
- XRPUSD: 533

## 6. MR candidates / resolved
- 381 candidates, 0 resolved

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