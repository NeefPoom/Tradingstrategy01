# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-14T23:29:11.339777

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
15

## 5. Observation count by asset
- ADAUSD: 174
- AUDCAD: 125
- AUDCHF: 125
- AUDJPY: 125
- AUDNZD: 125
- AUDUSD: 125
- AUS200: 35
- AVAXUSD: 174
- BCHUSD: 174
- BNBUSD: 174
- BRENT: 110
- BTCUSD: 372
- CADCHF: 125
- CADJPY: 125
- CHFJPY: 125
- DOGEUSD: 174
- DOTUSD: 174
- ETHUSD: 372
- EU50: 45
- EURAUD: 125
- EURCAD: 263
- EURCHF: 125
- EURGBP: 125
- EURJPY: 125
- EURUSD: 125
- FRA40: 45
- GBPAUD: 125
- GBPCAD: 125
- GBPCHF: 125
- GBPJPY: 125
- GBPUSD: 125
- GER40: 45
- GOLD: 229
- HK50: 35
- JPN225: 35
- LINKUSD: 174
- LTCUSD: 174
- NAS100: 35
- NATGAS: 110
- NZDCAD: 125
- NZDCHF: 125
- NZDJPY: 125
- NZDUSD: 125
- SILVER: 110
- SOLUSD: 174
- UK100: 45
- US30: 35
- US500: 71
- USDCAD: 125
- USDCHF: 125
- USDJPY: 261
- WTI: 110
- XRPUSD: 174

## 6. MR candidates / resolved
- 58 candidates, 0 resolved

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