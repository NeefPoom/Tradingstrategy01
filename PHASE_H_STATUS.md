# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-15T17:50:33.543639

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
16

## 5. Observation count by asset
- ADAUSD: 192
- AUDCAD: 143
- AUDCHF: 143
- AUDJPY: 143
- AUDNZD: 143
- AUDUSD: 143
- AUS200: 42
- AVAXUSD: 192
- BCHUSD: 192
- BNBUSD: 192
- BRENT: 128
- BTCUSD: 390
- CADCHF: 143
- CADJPY: 143
- CHFJPY: 143
- DOGEUSD: 192
- DOTUSD: 192
- ETHUSD: 390
- EU50: 54
- EURAUD: 143
- EURCAD: 281
- EURCHF: 143
- EURGBP: 143
- EURJPY: 143
- EURUSD: 143
- FRA40: 54
- GBPAUD: 143
- GBPCAD: 143
- GBPCHF: 143
- GBPJPY: 143
- GBPUSD: 143
- GER40: 54
- GOLD: 247
- HK50: 42
- JPN225: 42
- LINKUSD: 192
- LTCUSD: 192
- NAS100: 39
- NATGAS: 128
- NZDCAD: 143
- NZDCHF: 143
- NZDJPY: 143
- NZDUSD: 143
- SILVER: 128
- SOLUSD: 192
- UK100: 54
- US30: 39
- US500: 75
- USDCAD: 143
- USDCHF: 143
- USDJPY: 279
- WTI: 128
- XRPUSD: 192

## 6. MR candidates / resolved
- 84 candidates, 0 resolved

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