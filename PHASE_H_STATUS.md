# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-01T06:37:20.529331

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
31

## 5. Observation count by asset
- ADAUSD: 565
- AUDCAD: 418
- AUDCHF: 418
- AUDJPY: 418
- AUDNZD: 418
- AUDUSD: 418
- AUS200: 125
- AVAXUSD: 565
- BCHUSD: 565
- BNBUSD: 565
- BRENT: 393
- BTCUSD: 763
- CADCHF: 418
- CADJPY: 418
- CHFJPY: 418
- DOGEUSD: 565
- DOTUSD: 565
- ETHUSD: 763
- EU50: 153
- EURAUD: 418
- EURCAD: 556
- EURCHF: 418
- EURGBP: 418
- EURJPY: 418
- EURUSD: 418
- FRA40: 153
- GBPAUD: 418
- GBPCAD: 418
- GBPCHF: 418
- GBPJPY: 418
- GBPUSD: 418
- GER40: 153
- GOLD: 513
- HK50: 119
- JPN225: 104
- LINKUSD: 565
- LTCUSD: 565
- NAS100: 119
- NATGAS: 394
- NZDCAD: 418
- NZDCHF: 418
- NZDJPY: 418
- NZDUSD: 418
- SILVER: 394
- SOLUSD: 565
- UK100: 153
- US30: 119
- US500: 155
- USDCAD: 418
- USDCHF: 416
- USDJPY: 554
- WTI: 393
- XRPUSD: 565

## 6. MR candidates / resolved
- 422 candidates, 0 resolved

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