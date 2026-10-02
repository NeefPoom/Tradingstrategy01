# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-02T09:07:39.980682

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
32

## 5. Observation count by asset
- ADAUSD: 592
- AUDCAD: 445
- AUDCHF: 445
- AUDJPY: 445
- AUDNZD: 445
- AUDUSD: 445
- AUS200: 133
- AVAXUSD: 592
- BCHUSD: 592
- BNBUSD: 592
- BRENT: 419
- BTCUSD: 789
- CADCHF: 445
- CADJPY: 445
- CHFJPY: 445
- DOGEUSD: 592
- DOTUSD: 592
- ETHUSD: 789
- EU50: 164
- EURAUD: 445
- EURCAD: 582
- EURCHF: 445
- EURGBP: 445
- EURJPY: 445
- EURUSD: 444
- FRA40: 164
- GBPAUD: 445
- GBPCAD: 445
- GBPCHF: 445
- GBPJPY: 445
- GBPUSD: 444
- GER40: 164
- GOLD: 538
- HK50: 126
- JPN225: 112
- LINKUSD: 592
- LTCUSD: 592
- NAS100: 126
- NATGAS: 420
- NZDCAD: 445
- NZDCHF: 445
- NZDJPY: 445
- NZDUSD: 445
- SILVER: 420
- SOLUSD: 592
- UK100: 164
- US30: 126
- US500: 162
- USDCAD: 445
- USDCHF: 443
- USDJPY: 580
- WTI: 419
- XRPUSD: 592

## 6. MR candidates / resolved
- 452 candidates, 0 resolved

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