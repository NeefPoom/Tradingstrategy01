# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-10T00:36:40.688485

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
10

## 5. Observation count by asset
- ADAUSD: 55
- AUDCAD: 55
- AUDCHF: 55
- AUDJPY: 55
- AUDNZD: 55
- AUDUSD: 55
- AUS200: 14
- AVAXUSD: 55
- BCHUSD: 55
- BNBUSD: 55
- BRENT: 42
- BTCUSD: 253
- CADCHF: 55
- CADJPY: 55
- CHFJPY: 55
- DOGEUSD: 55
- DOTUSD: 55
- ETHUSD: 253
- EU50: 18
- EURAUD: 55
- EURCAD: 193
- EURCHF: 55
- EURGBP: 55
- EURJPY: 55
- EURUSD: 55
- FRA40: 18
- GBPAUD: 55
- GBPCAD: 55
- GBPCHF: 55
- GBPJPY: 55
- GBPUSD: 55
- GER40: 18
- GOLD: 161
- HK50: 14
- JPN225: 14
- LINKUSD: 55
- LTCUSD: 55
- NAS100: 14
- NATGAS: 42
- NZDCAD: 55
- NZDCHF: 55
- NZDJPY: 55
- NZDUSD: 55
- SILVER: 42
- SOLUSD: 55
- UK100: 18
- US30: 14
- US500: 50
- USDCAD: 55
- USDCHF: 55
- USDJPY: 192
- WTI: 42
- XRPUSD: 55

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