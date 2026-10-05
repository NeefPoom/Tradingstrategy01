# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-05T19:02:40.836917

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
36

## 5. Observation count by asset
- ADAUSD: 673
- AUDCAD: 477
- AUDCHF: 477
- AUDJPY: 477
- AUDNZD: 477
- AUDUSD: 477
- AUS200: 140
- AVAXUSD: 674
- BCHUSD: 673
- BNBUSD: 673
- BRENT: 451
- BTCUSD: 871
- CADCHF: 477
- CADJPY: 477
- CHFJPY: 477
- DOGEUSD: 673
- DOTUSD: 673
- ETHUSD: 871
- EU50: 180
- EURAUD: 477
- EURCAD: 615
- EURCHF: 477
- EURGBP: 477
- EURJPY: 477
- EURUSD: 477
- FRA40: 180
- GBPAUD: 477
- GBPCAD: 477
- GBPCHF: 477
- GBPJPY: 477
- GBPUSD: 477
- GER40: 180
- GOLD: 571
- HK50: 133
- JPN225: 119
- LINKUSD: 673
- LTCUSD: 673
- NAS100: 138
- NATGAS: 452
- NZDCAD: 477
- NZDCHF: 477
- NZDJPY: 477
- NZDUSD: 477
- SILVER: 452
- SOLUSD: 673
- UK100: 180
- US30: 138
- US500: 174
- USDCAD: 477
- USDCHF: 474
- USDJPY: 613
- WTI: 452
- XRPUSD: 673

## 6. MR candidates / resolved
- 514 candidates, 0 resolved

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