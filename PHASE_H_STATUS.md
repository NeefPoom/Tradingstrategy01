# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-09T22:33:11.343489

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
10

## 5. Observation count by asset
- ADAUSD: 53
- AUDCAD: 53
- AUDCHF: 53
- AUDJPY: 53
- AUDNZD: 53
- AUDUSD: 53
- AUS200: 14
- AVAXUSD: 53
- BCHUSD: 53
- BNBUSD: 53
- BRENT: 40
- BTCUSD: 251
- CADCHF: 53
- CADJPY: 53
- CHFJPY: 53
- DOGEUSD: 53
- DOTUSD: 53
- ETHUSD: 249
- EU50: 18
- EURAUD: 53
- EURCAD: 191
- EURCHF: 53
- EURGBP: 53
- EURJPY: 53
- EURUSD: 53
- FRA40: 18
- GBPAUD: 53
- GBPCAD: 53
- GBPCHF: 53
- GBPJPY: 53
- GBPUSD: 52
- GER40: 18
- GOLD: 159
- HK50: 14
- JPN225: 14
- LINKUSD: 53
- LTCUSD: 53
- NAS100: 14
- NATGAS: 40
- NZDCAD: 53
- NZDCHF: 53
- NZDJPY: 53
- NZDUSD: 53
- SILVER: 40
- SOLUSD: 53
- UK100: 18
- US30: 14
- US500: 50
- USDCAD: 53
- USDCHF: 53
- USDJPY: 190
- WTI: 40
- XRPUSD: 53

## 6. MR candidates / resolved
- 20 candidates, 0 resolved

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