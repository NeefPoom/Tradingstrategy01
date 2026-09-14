# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-14T02:51:57.066865

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
14

## 5. Observation count by asset
- ADAUSD: 153
- AUDCAD: 104
- AUDCHF: 104
- AUDJPY: 104
- AUDNZD: 104
- AUDUSD: 104
- AUS200: 30
- AVAXUSD: 153
- BCHUSD: 153
- BNBUSD: 153
- BRENT: 90
- BTCUSD: 351
- CADCHF: 104
- CADJPY: 104
- CHFJPY: 104
- DOGEUSD: 153
- DOTUSD: 153
- ETHUSD: 351
- EU50: 36
- EURAUD: 104
- EURCAD: 242
- EURCHF: 104
- EURGBP: 104
- EURJPY: 104
- EURUSD: 104
- FRA40: 36
- GBPAUD: 104
- GBPCAD: 104
- GBPCHF: 104
- GBPJPY: 104
- GBPUSD: 104
- GER40: 36
- GOLD: 209
- HK50: 29
- JPN225: 30
- LINKUSD: 153
- LTCUSD: 153
- NAS100: 28
- NATGAS: 90
- NZDCAD: 104
- NZDCHF: 104
- NZDJPY: 104
- NZDUSD: 104
- SILVER: 90
- SOLUSD: 153
- UK100: 36
- US30: 28
- US500: 64
- USDCAD: 104
- USDCHF: 104
- USDJPY: 240
- WTI: 90
- XRPUSD: 153

## 6. MR candidates / resolved
- 22 candidates, 0 resolved

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