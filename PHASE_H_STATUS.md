# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-08T23:25:36.260533

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
9

## 5. Observation count by asset
- ADAUSD: 30
- AUDCAD: 30
- AUDCHF: 30
- AUDJPY: 30
- AUDNZD: 30
- AUDUSD: 30
- AUS200: 7
- AVAXUSD: 30
- BCHUSD: 30
- BNBUSD: 30
- BRENT: 18
- BTCUSD: 228
- CADCHF: 30
- CADJPY: 30
- CHFJPY: 30
- DOGEUSD: 30
- DOTUSD: 30
- ETHUSD: 228
- EU50: 9
- EURAUD: 30
- EURCAD: 168
- EURCHF: 30
- EURGBP: 30
- EURJPY: 30
- EURUSD: 30
- FRA40: 9
- GBPAUD: 30
- GBPCAD: 30
- GBPCHF: 30
- GBPJPY: 30
- GBPUSD: 30
- GER40: 9
- GOLD: 137
- HK50: 7
- JPN225: 7
- LINKUSD: 30
- LTCUSD: 30
- NAS100: 7
- NATGAS: 18
- NZDCAD: 30
- NZDCHF: 30
- NZDJPY: 30
- NZDUSD: 30
- SILVER: 18
- SOLUSD: 30
- UK100: 9
- US30: 7
- US500: 43
- USDCAD: 30
- USDCHF: 30
- USDJPY: 167
- WTI: 18
- XRPUSD: 30

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