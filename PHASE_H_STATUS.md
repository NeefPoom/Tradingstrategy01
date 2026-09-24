# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-24T10:01:29.354911

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
24

## 5. Observation count by asset
- ADAUSD: 400
- AUDCAD: 302
- AUDCHF: 302
- AUDJPY: 302
- AUDNZD: 302
- AUDUSD: 302
- AUS200: 91
- AVAXUSD: 400
- BCHUSD: 400
- BNBUSD: 400
- BRENT: 281
- BTCUSD: 598
- CADCHF: 302
- CADJPY: 302
- CHFJPY: 302
- DOGEUSD: 400
- DOTUSD: 400
- ETHUSD: 598
- EU50: 110
- EURAUD: 302
- EURCAD: 440
- EURCHF: 302
- EURGBP: 302
- EURJPY: 302
- EURUSD: 302
- FRA40: 110
- GBPAUD: 302
- GBPCAD: 302
- GBPCHF: 302
- GBPJPY: 302
- GBPUSD: 302
- GER40: 110
- GOLD: 401
- HK50: 91
- JPN225: 70
- LINKUSD: 400
- LTCUSD: 400
- NAS100: 84
- NATGAS: 282
- NZDCAD: 302
- NZDCHF: 302
- NZDJPY: 302
- NZDUSD: 302
- SILVER: 282
- SOLUSD: 400
- UK100: 110
- US30: 84
- US500: 120
- USDCAD: 302
- USDCHF: 301
- USDJPY: 438
- WTI: 281
- XRPUSD: 400

## 6. MR candidates / resolved
- 270 candidates, 0 resolved

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