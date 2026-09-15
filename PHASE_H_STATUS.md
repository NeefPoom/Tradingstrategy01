# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-15T21:20:30.818198

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
16

## 5. Observation count by asset
- ADAUSD: 196
- AUDCAD: 147
- AUDCHF: 147
- AUDJPY: 147
- AUDNZD: 147
- AUDUSD: 147
- AUS200: 42
- AVAXUSD: 196
- BCHUSD: 196
- BNBUSD: 196
- BRENT: 132
- BTCUSD: 394
- CADCHF: 147
- CADJPY: 147
- CHFJPY: 147
- DOGEUSD: 196
- DOTUSD: 196
- ETHUSD: 394
- EU50: 54
- EURAUD: 147
- EURCAD: 285
- EURCHF: 147
- EURGBP: 147
- EURJPY: 147
- EURUSD: 147
- FRA40: 54
- GBPAUD: 147
- GBPCAD: 147
- GBPCHF: 147
- GBPJPY: 147
- GBPUSD: 147
- GER40: 54
- GOLD: 251
- HK50: 42
- JPN225: 42
- LINKUSD: 196
- LTCUSD: 196
- NAS100: 42
- NATGAS: 132
- NZDCAD: 147
- NZDCHF: 147
- NZDJPY: 147
- NZDUSD: 147
- SILVER: 132
- SOLUSD: 196
- UK100: 54
- US30: 42
- US500: 78
- USDCAD: 147
- USDCHF: 147
- USDJPY: 283
- WTI: 132
- XRPUSD: 196

## 6. MR candidates / resolved
- 87 candidates, 0 resolved

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