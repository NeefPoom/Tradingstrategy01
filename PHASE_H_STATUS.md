# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-10T23:10:27.885197

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
11

## 5. Observation count by asset
- ADAUSD: 78
- AUDCAD: 78
- AUDCHF: 78
- AUDJPY: 78
- AUDNZD: 78
- AUDUSD: 78
- AUS200: 21
- AVAXUSD: 78
- BCHUSD: 78
- BNBUSD: 76
- BRENT: 64
- BTCUSD: 276
- CADCHF: 78
- CADJPY: 78
- CHFJPY: 78
- DOGEUSD: 77
- DOTUSD: 78
- ETHUSD: 276
- EU50: 27
- EURAUD: 78
- EURCAD: 216
- EURCHF: 78
- EURGBP: 78
- EURJPY: 78
- EURUSD: 78
- FRA40: 27
- GBPAUD: 78
- GBPCAD: 78
- GBPCHF: 78
- GBPJPY: 78
- GBPUSD: 78
- GER40: 27
- GOLD: 183
- HK50: 21
- JPN225: 21
- LINKUSD: 78
- LTCUSD: 78
- NAS100: 21
- NATGAS: 64
- NZDCAD: 78
- NZDCHF: 78
- NZDJPY: 78
- NZDUSD: 78
- SILVER: 64
- SOLUSD: 78
- UK100: 27
- US30: 21
- US500: 57
- USDCAD: 78
- USDCHF: 78
- USDJPY: 215
- WTI: 64
- XRPUSD: 78

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