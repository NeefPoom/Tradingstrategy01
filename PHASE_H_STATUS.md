# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-21T01:39:23.203779

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
21

## 5. Observation count by asset
- ADAUSD: 320
- AUDCAD: 222
- AUDCHF: 222
- AUDJPY: 222
- AUDNZD: 222
- AUDUSD: 222
- AUS200: 64
- AVAXUSD: 320
- BCHUSD: 320
- BNBUSD: 320
- BRENT: 204
- BTCUSD: 518
- CADCHF: 222
- CADJPY: 222
- CHFJPY: 222
- DOGEUSD: 320
- DOTUSD: 320
- ETHUSD: 518
- EU50: 81
- EURAUD: 222
- EURCAD: 360
- EURCHF: 222
- EURGBP: 222
- EURJPY: 222
- EURUSD: 222
- FRA40: 81
- GBPAUD: 222
- GBPCAD: 222
- GBPCHF: 222
- GBPJPY: 222
- GBPUSD: 222
- GER40: 81
- GOLD: 323
- HK50: 63
- JPN225: 63
- LINKUSD: 320
- LTCUSD: 320
- NAS100: 63
- NATGAS: 205
- NZDCAD: 222
- NZDCHF: 222
- NZDJPY: 222
- NZDUSD: 222
- SILVER: 204
- SOLUSD: 320
- UK100: 81
- US30: 63
- US500: 99
- USDCAD: 222
- USDCHF: 221
- USDJPY: 358
- WTI: 204
- XRPUSD: 320

## 6. MR candidates / resolved
- 189 candidates, 0 resolved

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