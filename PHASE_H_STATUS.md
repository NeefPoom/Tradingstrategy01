# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-15T01:57:01.277805

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
15

## 5. Observation count by asset
- ADAUSD: 176
- AUDCAD: 127
- AUDCHF: 127
- AUDJPY: 127
- AUDNZD: 127
- AUDUSD: 127
- AUS200: 36
- AVAXUSD: 176
- BCHUSD: 176
- BNBUSD: 176
- BRENT: 112
- BTCUSD: 374
- CADCHF: 127
- CADJPY: 127
- CHFJPY: 127
- DOGEUSD: 176
- DOTUSD: 176
- ETHUSD: 374
- EU50: 45
- EURAUD: 127
- EURCAD: 265
- EURCHF: 127
- EURGBP: 127
- EURJPY: 127
- EURUSD: 127
- FRA40: 45
- GBPAUD: 127
- GBPCAD: 127
- GBPCHF: 127
- GBPJPY: 127
- GBPUSD: 127
- GER40: 45
- GOLD: 231
- HK50: 35
- JPN225: 36
- LINKUSD: 176
- LTCUSD: 176
- NAS100: 35
- NATGAS: 112
- NZDCAD: 127
- NZDCHF: 127
- NZDJPY: 127
- NZDUSD: 127
- SILVER: 112
- SOLUSD: 176
- UK100: 45
- US30: 35
- US500: 71
- USDCAD: 127
- USDCHF: 127
- USDJPY: 263
- WTI: 112
- XRPUSD: 176

## 6. MR candidates / resolved
- 61 candidates, 0 resolved

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