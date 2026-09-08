# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-08T17:57:04.622315

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
9

## 5. Observation count by asset
- ADAUSD: 24
- AUDCAD: 24
- AUDCHF: 24
- AUDJPY: 24
- AUDNZD: 24
- AUDUSD: 24
- AUS200: 7
- AVAXUSD: 24
- BCHUSD: 24
- BNBUSD: 24
- BRENT: 13
- BTCUSD: 222
- CADCHF: 24
- CADJPY: 24
- CHFJPY: 24
- DOGEUSD: 24
- DOTUSD: 24
- ETHUSD: 222
- EU50: 9
- EURAUD: 24
- EURCAD: 162
- EURCHF: 24
- EURGBP: 24
- EURJPY: 24
- EURUSD: 24
- FRA40: 9
- GBPAUD: 24
- GBPCAD: 24
- GBPCHF: 24
- GBPJPY: 24
- GBPUSD: 24
- GER40: 9
- GOLD: 132
- HK50: 7
- JPN225: 7
- LINKUSD: 24
- LTCUSD: 24
- NAS100: 4
- NATGAS: 13
- NZDCAD: 24
- NZDCHF: 24
- NZDJPY: 24
- NZDUSD: 24
- SILVER: 13
- SOLUSD: 24
- UK100: 9
- US30: 4
- US500: 40
- USDCAD: 24
- USDCHF: 24
- USDJPY: 161
- WTI: 13
- XRPUSD: 24

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