# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-01T14:01:55.032202

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
32

## 5. Observation count by asset
- ADAUSD: 572
- AUDCAD: 425
- AUDCHF: 425
- AUDJPY: 425
- AUDNZD: 425
- AUDUSD: 425
- AUS200: 126
- AVAXUSD: 572
- BCHUSD: 572
- BNBUSD: 572
- BRENT: 400
- BTCUSD: 770
- CADCHF: 425
- CADJPY: 425
- CHFJPY: 425
- DOGEUSD: 572
- DOTUSD: 572
- ETHUSD: 770
- EU50: 159
- EURAUD: 425
- EURCAD: 563
- EURCHF: 425
- EURGBP: 425
- EURJPY: 425
- EURUSD: 425
- FRA40: 159
- GBPAUD: 425
- GBPCAD: 425
- GBPCHF: 425
- GBPJPY: 425
- GBPUSD: 425
- GER40: 159
- GOLD: 520
- HK50: 119
- JPN225: 105
- LINKUSD: 572
- LTCUSD: 572
- NAS100: 119
- NATGAS: 401
- NZDCAD: 425
- NZDCHF: 425
- NZDJPY: 425
- NZDUSD: 425
- SILVER: 401
- SOLUSD: 572
- UK100: 159
- US30: 119
- US500: 155
- USDCAD: 425
- USDCHF: 423
- USDJPY: 561
- WTI: 400
- XRPUSD: 572

## 6. MR candidates / resolved
- 429 candidates, 0 resolved

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