# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-02T20:48:03.575638

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
33

## 5. Observation count by asset
- ADAUSD: 603
- AUDCAD: 456
- AUDCHF: 456
- AUDJPY: 456
- AUDNZD: 456
- AUDUSD: 456
- AUS200: 133
- AVAXUSD: 603
- BCHUSD: 603
- BNBUSD: 603
- BRENT: 430
- BTCUSD: 801
- CADCHF: 456
- CADJPY: 456
- CHFJPY: 456
- DOGEUSD: 603
- DOTUSD: 603
- ETHUSD: 801
- EU50: 171
- EURAUD: 456
- EURCAD: 594
- EURCHF: 456
- EURGBP: 456
- EURJPY: 456
- EURUSD: 456
- FRA40: 171
- GBPAUD: 456
- GBPCAD: 456
- GBPCHF: 456
- GBPJPY: 456
- GBPUSD: 456
- GER40: 171
- GOLD: 550
- HK50: 126
- JPN225: 112
- LINKUSD: 603
- LTCUSD: 603
- NAS100: 133
- NATGAS: 431
- NZDCAD: 456
- NZDCHF: 456
- NZDJPY: 456
- NZDUSD: 456
- SILVER: 431
- SOLUSD: 603
- UK100: 171
- US30: 133
- US500: 169
- USDCAD: 456
- USDCHF: 454
- USDJPY: 592
- WTI: 430
- XRPUSD: 603

## 6. MR candidates / resolved
- 478 candidates, 0 resolved

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