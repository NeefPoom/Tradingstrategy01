# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-21T22:04:46.544579

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
52

## 5. Observation count by asset
- ADAUSD: 1061
- AUDCAD: 767
- AUDCHF: 767
- AUDJPY: 766
- AUDNZD: 767
- AUDUSD: 766
- AUS200: 224
- AVAXUSD: 1061
- BCHUSD: 1061
- BNBUSD: 1061
- BRENT: 730
- BTCUSD: 1258
- CADCHF: 767
- CADJPY: 766
- CHFJPY: 766
- DOGEUSD: 1061
- DOTUSD: 1061
- ETHUSD: 1258
- EU50: 288
- EURAUD: 767
- EURCAD: 904
- EURCHF: 767
- EURGBP: 768
- EURJPY: 766
- EURUSD: 766
- FRA40: 288
- GBPAUD: 767
- GBPCAD: 767
- GBPCHF: 767
- GBPJPY: 766
- GBPUSD: 767
- GER40: 288
- GOLD: 852
- HK50: 210
- JPN225: 196
- LINKUSD: 1061
- LTCUSD: 1061
- NAS100: 224
- NATGAS: 734
- NZDCAD: 767
- NZDCHF: 767
- NZDJPY: 767
- NZDUSD: 766
- SILVER: 731
- SOLUSD: 1061
- UK100: 288
- US30: 224
- US500: 260
- USDCAD: 766
- USDCHF: 761
- USDJPY: 900
- WTI: 731
- XRPUSD: 1061

## 6. MR candidates / resolved
- 906 candidates, 0 resolved

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