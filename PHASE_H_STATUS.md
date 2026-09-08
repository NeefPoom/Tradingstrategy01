# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-08T21:09:22.398889

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
9

## 5. Observation count by asset
- ADAUSD: 28
- AUDCAD: 28
- AUDCHF: 28
- AUDJPY: 28
- AUDNZD: 28
- AUDUSD: 28
- AUS200: 7
- AVAXUSD: 28
- BCHUSD: 28
- BNBUSD: 28
- BRENT: 17
- BTCUSD: 226
- CADCHF: 28
- CADJPY: 28
- CHFJPY: 28
- DOGEUSD: 28
- DOTUSD: 28
- ETHUSD: 226
- EU50: 9
- EURAUD: 28
- EURCAD: 166
- EURCHF: 25
- EURGBP: 28
- EURJPY: 28
- EURUSD: 28
- FRA40: 9
- GBPAUD: 28
- GBPCAD: 28
- GBPCHF: 25
- GBPJPY: 28
- GBPUSD: 28
- GER40: 9
- GOLD: 136
- HK50: 7
- JPN225: 7
- LINKUSD: 28
- LTCUSD: 28
- NAS100: 7
- NATGAS: 17
- NZDCAD: 28
- NZDCHF: 28
- NZDJPY: 28
- NZDUSD: 28
- SILVER: 17
- SOLUSD: 28
- UK100: 9
- US30: 7
- US500: 42
- USDCAD: 28
- USDCHF: 26
- USDJPY: 165
- WTI: 17
- XRPUSD: 28

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