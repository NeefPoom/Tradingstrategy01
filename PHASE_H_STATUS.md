# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-14T16:37:07.741038

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
15

## 5. Observation count by asset
- ADAUSD: 167
- AUDCAD: 118
- AUDCHF: 118
- AUDJPY: 118
- AUDNZD: 118
- AUDUSD: 118
- AUS200: 35
- AVAXUSD: 167
- BCHUSD: 167
- BNBUSD: 167
- BRENT: 104
- BTCUSD: 365
- CADCHF: 118
- CADJPY: 118
- CHFJPY: 118
- DOGEUSD: 167
- DOTUSD: 167
- ETHUSD: 365
- EU50: 45
- EURAUD: 118
- EURCAD: 256
- EURCHF: 118
- EURGBP: 118
- EURJPY: 118
- EURUSD: 118
- FRA40: 45
- GBPAUD: 118
- GBPCAD: 118
- GBPCHF: 118
- GBPJPY: 118
- GBPUSD: 118
- GER40: 45
- GOLD: 223
- HK50: 35
- JPN225: 35
- LINKUSD: 167
- LTCUSD: 167
- NAS100: 31
- NATGAS: 104
- NZDCAD: 118
- NZDCHF: 118
- NZDJPY: 118
- NZDUSD: 118
- SILVER: 104
- SOLUSD: 167
- UK100: 45
- US30: 31
- US500: 67
- USDCAD: 118
- USDCHF: 118
- USDJPY: 254
- WTI: 104
- XRPUSD: 167

## 6. MR candidates / resolved
- 49 candidates, 0 resolved

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