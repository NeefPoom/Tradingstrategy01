# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-17T05:23:39.385503

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
17

## 5. Observation count by asset
- ADAUSD: 228
- AUDCAD: 179
- AUDCHF: 179
- AUDJPY: 179
- AUDNZD: 179
- AUDUSD: 179
- AUS200: 54
- AVAXUSD: 228
- BCHUSD: 228
- BNBUSD: 228
- BRENT: 162
- BTCUSD: 426
- CADCHF: 179
- CADJPY: 179
- CHFJPY: 179
- DOGEUSD: 228
- DOTUSD: 228
- ETHUSD: 426
- EU50: 63
- EURAUD: 179
- EURCAD: 317
- EURCHF: 179
- EURGBP: 179
- EURJPY: 179
- EURUSD: 179
- FRA40: 63
- GBPAUD: 179
- GBPCAD: 179
- GBPCHF: 179
- GBPJPY: 179
- GBPUSD: 179
- GER40: 63
- GOLD: 281
- HK50: 52
- JPN225: 54
- LINKUSD: 228
- LTCUSD: 228
- NAS100: 49
- NATGAS: 162
- NZDCAD: 179
- NZDCHF: 179
- NZDJPY: 179
- NZDUSD: 179
- SILVER: 162
- SOLUSD: 228
- UK100: 63
- US30: 49
- US500: 85
- USDCAD: 179
- USDCHF: 179
- USDJPY: 315
- WTI: 162
- XRPUSD: 228

## 6. MR candidates / resolved
- 132 candidates, 0 resolved

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