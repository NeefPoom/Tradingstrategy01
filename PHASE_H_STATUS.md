# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-05T02:26:22.419809

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
35

## 5. Observation count by asset
- ADAUSD: 657
- AUDCAD: 461
- AUDCHF: 461
- AUDJPY: 461
- AUDNZD: 461
- AUDUSD: 461
- AUS200: 136
- AVAXUSD: 657
- BCHUSD: 657
- BNBUSD: 657
- BRENT: 435
- BTCUSD: 855
- CADCHF: 461
- CADJPY: 461
- CHFJPY: 461
- DOGEUSD: 657
- DOTUSD: 657
- ETHUSD: 855
- EU50: 171
- EURAUD: 461
- EURCAD: 599
- EURCHF: 461
- EURGBP: 461
- EURJPY: 461
- EURUSD: 461
- FRA40: 171
- GBPAUD: 461
- GBPCAD: 461
- GBPCHF: 461
- GBPJPY: 461
- GBPUSD: 461
- GER40: 171
- GOLD: 555
- HK50: 126
- JPN225: 114
- LINKUSD: 657
- LTCUSD: 657
- NAS100: 133
- NATGAS: 436
- NZDCAD: 461
- NZDCHF: 461
- NZDJPY: 461
- NZDUSD: 461
- SILVER: 436
- SOLUSD: 657
- UK100: 171
- US30: 133
- US500: 169
- USDCAD: 461
- USDCHF: 458
- USDJPY: 597
- WTI: 436
- XRPUSD: 657

## 6. MR candidates / resolved
- 494 candidates, 0 resolved

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