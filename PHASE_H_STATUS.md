# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-20T20:48:20.940750

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
21

## 5. Observation count by asset
- ADAUSD: 315
- AUDCAD: 220
- AUDCHF: 220
- AUDJPY: 220
- AUDNZD: 220
- AUDUSD: 220
- AUS200: 63
- AVAXUSD: 315
- BCHUSD: 315
- BNBUSD: 315
- BRENT: 201
- BTCUSD: 513
- CADCHF: 220
- CADJPY: 220
- CHFJPY: 220
- DOGEUSD: 315
- DOTUSD: 315
- ETHUSD: 513
- EU50: 81
- EURAUD: 220
- EURCAD: 358
- EURCHF: 220
- EURGBP: 220
- EURJPY: 220
- EURUSD: 220
- FRA40: 81
- GBPAUD: 220
- GBPCAD: 220
- GBPCHF: 220
- GBPJPY: 220
- GBPUSD: 220
- GER40: 81
- GOLD: 320
- HK50: 63
- JPN225: 63
- LINKUSD: 315
- LTCUSD: 315
- NAS100: 63
- NATGAS: 202
- NZDCAD: 220
- NZDCHF: 220
- NZDJPY: 220
- NZDUSD: 220
- SILVER: 201
- SOLUSD: 315
- UK100: 81
- US30: 63
- US500: 99
- USDCAD: 220
- USDCHF: 219
- USDJPY: 356
- WTI: 201
- XRPUSD: 315

## 6. MR candidates / resolved
- 187 candidates, 0 resolved

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