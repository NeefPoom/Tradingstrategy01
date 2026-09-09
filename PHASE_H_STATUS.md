# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-09T16:56:06.827295

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
10

## 5. Observation count by asset
- ADAUSD: 47
- AUDCAD: 46
- AUDCHF: 47
- AUDJPY: 47
- AUDNZD: 47
- AUDUSD: 44
- AUS200: 14
- AVAXUSD: 47
- BCHUSD: 47
- BNBUSD: 46
- BRENT: 35
- BTCUSD: 245
- CADCHF: 47
- CADJPY: 47
- CHFJPY: 47
- DOGEUSD: 47
- DOTUSD: 47
- ETHUSD: 245
- EU50: 18
- EURAUD: 47
- EURCAD: 185
- EURCHF: 44
- EURGBP: 47
- EURJPY: 47
- EURUSD: 47
- FRA40: 18
- GBPAUD: 47
- GBPCAD: 45
- GBPCHF: 47
- GBPJPY: 46
- GBPUSD: 47
- GER40: 18
- GOLD: 154
- HK50: 14
- JPN225: 14
- LINKUSD: 47
- LTCUSD: 47
- NAS100: 8
- NATGAS: 35
- NZDCAD: 47
- NZDCHF: 47
- NZDJPY: 46
- NZDUSD: 47
- SILVER: 35
- SOLUSD: 47
- UK100: 18
- US30: 10
- US500: 46
- USDCAD: 47
- USDCHF: 47
- USDJPY: 184
- WTI: 35
- XRPUSD: 47

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