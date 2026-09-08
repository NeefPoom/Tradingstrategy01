# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-08T09:37:45.325600

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
8

## 5. Observation count by asset
- ADAUSD: 16
- AUDCAD: 16
- AUDCHF: 16
- AUDJPY: 16
- AUDNZD: 16
- AUDUSD: 16
- AUS200: 7
- AVAXUSD: 16
- BCHUSD: 16
- BNBUSD: 15
- BRENT: 5
- BTCUSD: 214
- CADCHF: 16
- CADJPY: 16
- CHFJPY: 16
- DOGEUSD: 16
- DOTUSD: 14
- ETHUSD: 214
- EU50: 2
- EURAUD: 16
- EURCAD: 154
- EURCHF: 16
- EURGBP: 16
- EURJPY: 16
- EURUSD: 15
- FRA40: 2
- GBPAUD: 16
- GBPCAD: 16
- GBPCHF: 16
- GBPJPY: 16
- GBPUSD: 16
- GER40: 2
- GOLD: 124
- HK50: 7
- JPN225: 7
- LINKUSD: 16
- LTCUSD: 16
- NATGAS: 5
- NZDCAD: 16
- NZDCHF: 16
- NZDJPY: 16
- NZDUSD: 16
- SILVER: 5
- SOLUSD: 16
- UK100: 2
- US500: 36
- USDCAD: 16
- USDCHF: 14
- USDJPY: 153
- WTI: 5
- XRPUSD: 16

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