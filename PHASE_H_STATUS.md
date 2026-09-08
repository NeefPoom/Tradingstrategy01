# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-08T13:53:14.393010

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
9

## 5. Observation count by asset
- ADAUSD: 20
- AUDCAD: 20
- AUDCHF: 20
- AUDJPY: 20
- AUDNZD: 20
- AUDUSD: 20
- AUS200: 7
- AVAXUSD: 20
- BCHUSD: 20
- BNBUSD: 20
- BRENT: 9
- BTCUSD: 218
- CADCHF: 20
- CADJPY: 19
- CHFJPY: 20
- DOGEUSD: 20
- DOTUSD: 20
- ETHUSD: 218
- EU50: 6
- EURAUD: 20
- EURCAD: 158
- EURCHF: 20
- EURGBP: 20
- EURJPY: 20
- EURUSD: 20
- FRA40: 6
- GBPAUD: 20
- GBPCAD: 20
- GBPCHF: 20
- GBPJPY: 19
- GBPUSD: 17
- GER40: 6
- GOLD: 128
- HK50: 7
- JPN225: 7
- LINKUSD: 20
- LTCUSD: 20
- NATGAS: 9
- NZDCAD: 20
- NZDCHF: 20
- NZDJPY: 20
- NZDUSD: 20
- SILVER: 9
- SOLUSD: 20
- UK100: 6
- US500: 36
- USDCAD: 20
- USDCHF: 20
- USDJPY: 156
- WTI: 9
- XRPUSD: 19

## 6. MR candidates / resolved
- 20 candidates, 0 resolved

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