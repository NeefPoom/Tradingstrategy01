# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-18T11:12:35.791009

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
19

## 5. Observation count by asset
- ADAUSD: 258
- AUDCAD: 209
- AUDCHF: 209
- AUDJPY: 209
- AUDNZD: 209
- AUDUSD: 209
- AUS200: 63
- AVAXUSD: 258
- BCHUSD: 258
- BNBUSD: 258
- BRENT: 191
- BTCUSD: 456
- CADCHF: 209
- CADJPY: 209
- CHFJPY: 209
- DOGEUSD: 258
- DOTUSD: 258
- ETHUSD: 456
- EU50: 76
- EURAUD: 209
- EURCAD: 347
- EURCHF: 209
- EURGBP: 209
- EURJPY: 209
- EURUSD: 209
- FRA40: 76
- GBPAUD: 209
- GBPCAD: 209
- GBPCHF: 209
- GBPJPY: 209
- GBPUSD: 209
- GER40: 76
- GOLD: 310
- HK50: 63
- JPN225: 63
- LINKUSD: 258
- LTCUSD: 258
- NAS100: 56
- NATGAS: 191
- NZDCAD: 209
- NZDCHF: 209
- NZDJPY: 209
- NZDUSD: 209
- SILVER: 191
- SOLUSD: 258
- UK100: 76
- US30: 56
- US500: 92
- USDCAD: 209
- USDCHF: 209
- USDJPY: 345
- WTI: 191
- XRPUSD: 258

## 6. MR candidates / resolved
- 157 candidates, 0 resolved

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