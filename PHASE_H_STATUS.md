# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-20T23:14:39.494233

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
21

## 5. Observation count by asset
- ADAUSD: 318
- AUDCAD: 220
- AUDCHF: 220
- AUDJPY: 220
- AUDNZD: 220
- AUDUSD: 220
- AUS200: 63
- AVAXUSD: 318
- BCHUSD: 318
- BNBUSD: 318
- BRENT: 202
- BTCUSD: 516
- CADCHF: 220
- CADJPY: 220
- CHFJPY: 220
- DOGEUSD: 318
- DOTUSD: 318
- ETHUSD: 516
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
- GOLD: 321
- HK50: 63
- JPN225: 63
- LINKUSD: 318
- LTCUSD: 318
- NAS100: 63
- NATGAS: 203
- NZDCAD: 220
- NZDCHF: 220
- NZDJPY: 220
- NZDUSD: 220
- SILVER: 202
- SOLUSD: 318
- UK100: 81
- US30: 63
- US500: 99
- USDCAD: 220
- USDCHF: 219
- USDJPY: 356
- WTI: 202
- XRPUSD: 318

## 6. MR candidates / resolved
- 188 candidates, 0 resolved

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