# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-21T07:14:17.785754

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
21

## 5. Observation count by asset
- ADAUSD: 326
- AUDCAD: 228
- AUDCHF: 228
- AUDJPY: 228
- AUDNZD: 228
- AUDUSD: 228
- AUS200: 70
- AVAXUSD: 326
- BCHUSD: 326
- BNBUSD: 326
- BRENT: 210
- BTCUSD: 524
- CADCHF: 228
- CADJPY: 228
- CHFJPY: 228
- DOGEUSD: 326
- DOTUSD: 326
- ETHUSD: 524
- EU50: 81
- EURAUD: 228
- EURCAD: 366
- EURCHF: 228
- EURGBP: 228
- EURJPY: 228
- EURUSD: 228
- FRA40: 81
- GBPAUD: 228
- GBPCAD: 228
- GBPCHF: 228
- GBPJPY: 228
- GBPUSD: 228
- GER40: 81
- GOLD: 329
- HK50: 68
- JPN225: 63
- LINKUSD: 326
- LTCUSD: 326
- NAS100: 63
- NATGAS: 211
- NZDCAD: 228
- NZDCHF: 228
- NZDJPY: 228
- NZDUSD: 228
- SILVER: 210
- SOLUSD: 326
- UK100: 81
- US30: 63
- US500: 99
- USDCAD: 228
- USDCHF: 227
- USDJPY: 364
- WTI: 210
- XRPUSD: 326

## 6. MR candidates / resolved
- 193 candidates, 0 resolved

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