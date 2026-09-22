# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-22T01:39:54.935724

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
22

## 5. Observation count by asset
- ADAUSD: 343
- AUDCAD: 246
- AUDCHF: 246
- AUDJPY: 246
- AUDNZD: 246
- AUDUSD: 246
- AUS200: 71
- AVAXUSD: 343
- BCHUSD: 343
- BNBUSD: 343
- BRENT: 227
- BTCUSD: 541
- CADCHF: 246
- CADJPY: 246
- CHFJPY: 246
- DOGEUSD: 343
- DOTUSD: 343
- ETHUSD: 541
- EU50: 90
- EURAUD: 246
- EURCAD: 384
- EURCHF: 246
- EURGBP: 246
- EURJPY: 246
- EURUSD: 246
- FRA40: 90
- GBPAUD: 246
- GBPCAD: 246
- GBPCHF: 246
- GBPJPY: 246
- GBPUSD: 246
- GER40: 90
- GOLD: 346
- HK50: 70
- JPN225: 63
- LINKUSD: 343
- LTCUSD: 343
- NAS100: 70
- NATGAS: 228
- NZDCAD: 246
- NZDCHF: 246
- NZDJPY: 246
- NZDUSD: 246
- SILVER: 228
- SOLUSD: 343
- UK100: 90
- US30: 70
- US500: 106
- USDCAD: 246
- USDCHF: 245
- USDJPY: 382
- WTI: 227
- XRPUSD: 343

## 6. MR candidates / resolved
- 204 candidates, 0 resolved

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