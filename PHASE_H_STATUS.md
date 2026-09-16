# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-16T09:58:08.792847

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
16

## 5. Observation count by asset
- ADAUSD: 208
- AUDCAD: 159
- AUDCHF: 159
- AUDJPY: 159
- AUDNZD: 159
- AUDUSD: 159
- AUS200: 49
- AVAXUSD: 208
- BCHUSD: 208
- BNBUSD: 208
- BRENT: 143
- BTCUSD: 406
- CADCHF: 159
- CADJPY: 159
- CHFJPY: 159
- DOGEUSD: 208
- DOTUSD: 208
- ETHUSD: 406
- EU50: 56
- EURAUD: 159
- EURCAD: 297
- EURCHF: 159
- EURGBP: 159
- EURJPY: 159
- EURUSD: 159
- FRA40: 56
- GBPAUD: 159
- GBPCAD: 159
- GBPCHF: 159
- GBPJPY: 159
- GBPUSD: 159
- GER40: 56
- GOLD: 262
- HK50: 49
- JPN225: 49
- LINKUSD: 208
- LTCUSD: 208
- NAS100: 42
- NATGAS: 143
- NZDCAD: 159
- NZDCHF: 159
- NZDJPY: 159
- NZDUSD: 159
- SILVER: 143
- SOLUSD: 208
- UK100: 56
- US30: 42
- US500: 78
- USDCAD: 159
- USDCHF: 159
- USDJPY: 295
- WTI: 143
- XRPUSD: 208

## 6. MR candidates / resolved
- 103 candidates, 0 resolved

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