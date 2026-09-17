# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-17T00:30:44.364797

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
17

## 5. Observation count by asset
- ADAUSD: 222
- AUDCAD: 174
- AUDCHF: 174
- AUDJPY: 174
- AUDNZD: 174
- AUDUSD: 174
- AUS200: 49
- AVAXUSD: 222
- BCHUSD: 222
- BNBUSD: 222
- BRENT: 157
- BTCUSD: 420
- CADCHF: 174
- CADJPY: 174
- CHFJPY: 174
- DOGEUSD: 222
- DOTUSD: 222
- ETHUSD: 420
- EU50: 63
- EURAUD: 174
- EURCAD: 312
- EURCHF: 174
- EURGBP: 174
- EURJPY: 174
- EURUSD: 174
- FRA40: 63
- GBPAUD: 174
- GBPCAD: 174
- GBPCHF: 174
- GBPJPY: 174
- GBPUSD: 174
- GER40: 63
- GOLD: 276
- HK50: 49
- JPN225: 49
- LINKUSD: 222
- LTCUSD: 222
- NAS100: 49
- NATGAS: 157
- NZDCAD: 174
- NZDCHF: 174
- NZDJPY: 174
- NZDUSD: 174
- SILVER: 157
- SOLUSD: 222
- UK100: 63
- US30: 49
- US500: 85
- USDCAD: 174
- USDCHF: 174
- USDJPY: 310
- WTI: 157
- XRPUSD: 222

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