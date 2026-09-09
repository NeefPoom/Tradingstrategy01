# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-09T10:27:08.325391

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
9

## 5. Observation count by asset
- ADAUSD: 41
- AUDCAD: 41
- AUDCHF: 41
- AUDJPY: 41
- AUDNZD: 41
- AUDUSD: 41
- AUS200: 14
- AVAXUSD: 41
- BCHUSD: 41
- BNBUSD: 41
- BRENT: 29
- BTCUSD: 239
- CADCHF: 41
- CADJPY: 41
- CHFJPY: 41
- DOGEUSD: 41
- DOTUSD: 41
- ETHUSD: 239
- EU50: 12
- EURAUD: 41
- EURCAD: 179
- EURCHF: 41
- EURGBP: 41
- EURJPY: 41
- EURUSD: 41
- FRA40: 12
- GBPAUD: 41
- GBPCAD: 41
- GBPCHF: 41
- GBPJPY: 41
- GBPUSD: 41
- GER40: 12
- GOLD: 148
- HK50: 14
- JPN225: 14
- LINKUSD: 41
- LTCUSD: 41
- NAS100: 7
- NATGAS: 29
- NZDCAD: 41
- NZDCHF: 41
- NZDJPY: 41
- NZDUSD: 41
- SILVER: 29
- SOLUSD: 41
- UK100: 12
- US30: 7
- US500: 43
- USDCAD: 41
- USDCHF: 41
- USDJPY: 178
- WTI: 29
- XRPUSD: 41

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