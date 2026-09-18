# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-18T21:16:30.219654

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
19

## 5. Observation count by asset
- ADAUSD: 268
- AUDCAD: 219
- AUDCHF: 219
- AUDJPY: 219
- AUDNZD: 219
- AUDUSD: 219
- AUS200: 63
- AVAXUSD: 268
- BCHUSD: 268
- BNBUSD: 268
- BRENT: 201
- BTCUSD: 466
- CADCHF: 219
- CADJPY: 219
- CHFJPY: 219
- DOGEUSD: 268
- DOTUSD: 268
- ETHUSD: 466
- EU50: 81
- EURAUD: 219
- EURCAD: 357
- EURCHF: 219
- EURGBP: 219
- EURJPY: 219
- EURUSD: 219
- FRA40: 81
- GBPAUD: 219
- GBPCAD: 219
- GBPCHF: 219
- GBPJPY: 219
- GBPUSD: 219
- GER40: 81
- GOLD: 320
- HK50: 63
- JPN225: 63
- LINKUSD: 268
- LTCUSD: 268
- NAS100: 63
- NATGAS: 201
- NZDCAD: 219
- NZDCHF: 219
- NZDJPY: 219
- NZDUSD: 219
- SILVER: 201
- SOLUSD: 268
- UK100: 81
- US30: 63
- US500: 99
- USDCAD: 219
- USDCHF: 219
- USDJPY: 355
- WTI: 201
- XRPUSD: 268

## 6. MR candidates / resolved
- 175 candidates, 0 resolved

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