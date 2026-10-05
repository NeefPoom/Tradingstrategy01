# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-05T09:45:09.744149

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
35

## 5. Observation count by asset
- ADAUSD: 664
- AUDCAD: 468
- AUDCHF: 468
- AUDJPY: 468
- AUDNZD: 468
- AUDUSD: 468
- AUS200: 140
- AVAXUSD: 664
- BCHUSD: 664
- BNBUSD: 664
- BRENT: 442
- BTCUSD: 862
- CADCHF: 468
- CADJPY: 468
- CHFJPY: 468
- DOGEUSD: 664
- DOTUSD: 664
- ETHUSD: 862
- EU50: 173
- EURAUD: 468
- EURCAD: 606
- EURCHF: 468
- EURGBP: 468
- EURJPY: 468
- EURUSD: 468
- FRA40: 173
- GBPAUD: 468
- GBPCAD: 468
- GBPCHF: 468
- GBPJPY: 468
- GBPUSD: 468
- GER40: 173
- GOLD: 562
- HK50: 133
- JPN225: 119
- LINKUSD: 664
- LTCUSD: 664
- NAS100: 133
- NATGAS: 443
- NZDCAD: 468
- NZDCHF: 468
- NZDJPY: 468
- NZDUSD: 468
- SILVER: 443
- SOLUSD: 664
- UK100: 173
- US30: 133
- US500: 169
- USDCAD: 468
- USDCHF: 465
- USDJPY: 604
- WTI: 443
- XRPUSD: 664

## 6. MR candidates / resolved
- 500 candidates, 0 resolved

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