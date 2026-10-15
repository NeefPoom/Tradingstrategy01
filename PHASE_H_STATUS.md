# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-15T09:33:37.181977

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
45

## 5. Observation count by asset
- ADAUSD: 904
- AUDCAD: 659
- AUDCHF: 659
- AUDJPY: 659
- AUDNZD: 659
- AUDUSD: 659
- AUS200: 196
- AVAXUSD: 904
- BCHUSD: 904
- BNBUSD: 904
- BRENT: 626
- BTCUSD: 1102
- CADCHF: 659
- CADJPY: 659
- CHFJPY: 659
- DOGEUSD: 904
- DOTUSD: 904
- ETHUSD: 1102
- EU50: 245
- EURAUD: 659
- EURCAD: 797
- EURCHF: 659
- EURGBP: 660
- EURJPY: 659
- EURUSD: 659
- FRA40: 245
- GBPAUD: 659
- GBPCAD: 659
- GBPCHF: 659
- GBPJPY: 659
- GBPUSD: 659
- GER40: 245
- GOLD: 748
- HK50: 189
- JPN225: 168
- LINKUSD: 904
- LTCUSD: 904
- NAS100: 189
- NATGAS: 630
- NZDCAD: 659
- NZDCHF: 659
- NZDJPY: 659
- NZDUSD: 659
- SILVER: 627
- SOLUSD: 904
- UK100: 245
- US30: 189
- US500: 225
- USDCAD: 659
- USDCHF: 655
- USDJPY: 794
- WTI: 627
- XRPUSD: 904

## 6. MR candidates / resolved
- 761 candidates, 0 resolved

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