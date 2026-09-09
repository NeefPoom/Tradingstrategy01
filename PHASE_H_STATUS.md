# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-09T01:32:32.031366

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
9

## 5. Observation count by asset
- ADAUSD: 32
- AUDCAD: 32
- AUDCHF: 32
- AUDJPY: 32
- AUDNZD: 31
- AUDUSD: 32
- AUS200: 8
- AVAXUSD: 32
- BCHUSD: 32
- BNBUSD: 32
- BRENT: 20
- BTCUSD: 230
- CADCHF: 32
- CADJPY: 32
- CHFJPY: 32
- DOGEUSD: 32
- DOTUSD: 32
- ETHUSD: 230
- EU50: 9
- EURAUD: 32
- EURCAD: 170
- EURCHF: 32
- EURGBP: 32
- EURJPY: 32
- EURUSD: 32
- FRA40: 9
- GBPAUD: 32
- GBPCAD: 32
- GBPCHF: 32
- GBPJPY: 32
- GBPUSD: 32
- GER40: 9
- GOLD: 139
- HK50: 7
- JPN225: 8
- LINKUSD: 32
- LTCUSD: 32
- NAS100: 7
- NATGAS: 20
- NZDCAD: 32
- NZDCHF: 32
- NZDJPY: 32
- NZDUSD: 32
- SILVER: 20
- SOLUSD: 31
- UK100: 9
- US30: 7
- US500: 43
- USDCAD: 32
- USDCHF: 32
- USDJPY: 169
- WTI: 20
- XRPUSD: 32

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