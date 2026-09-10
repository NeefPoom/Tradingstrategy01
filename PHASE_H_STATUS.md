# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-10T14:26:58.718382

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
11

## 5. Observation count by asset
- ADAUSD: 69
- AUDCAD: 66
- AUDCHF: 69
- AUDJPY: 69
- AUDNZD: 69
- AUDUSD: 69
- AUS200: 21
- AVAXUSD: 69
- BCHUSD: 69
- BNBUSD: 69
- BRENT: 56
- BTCUSD: 267
- CADCHF: 69
- CADJPY: 69
- CHFJPY: 69
- DOGEUSD: 69
- DOTUSD: 69
- ETHUSD: 267
- EU50: 25
- EURAUD: 69
- EURCAD: 207
- EURCHF: 69
- EURGBP: 69
- EURJPY: 69
- EURUSD: 69
- FRA40: 25
- GBPAUD: 69
- GBPCAD: 69
- GBPCHF: 69
- GBPJPY: 69
- GBPUSD: 65
- GER40: 25
- GOLD: 175
- HK50: 21
- JPN225: 21
- LINKUSD: 69
- LTCUSD: 69
- NAS100: 14
- NATGAS: 55
- NZDCAD: 69
- NZDCHF: 69
- NZDJPY: 69
- NZDUSD: 69
- SILVER: 53
- SOLUSD: 69
- UK100: 25
- US30: 14
- US500: 50
- USDCAD: 69
- USDCHF: 69
- USDJPY: 206
- WTI: 48
- XRPUSD: 69

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