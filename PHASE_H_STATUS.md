# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-22T00:44:24.920483

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
- AUDCAD: 769
- AUDCHF: 769
- AUDJPY: 769
- AUDNZD: 769
- AUDUSD: 769
- AUS200: 225
- AVAXUSD: 1061
- BCHUSD: 1061
- BNBUSD: 1061
- BRENT: 732
- BTCUSD: 1259
- CADCHF: 769
- CADJPY: 769
- CHFJPY: 769
- DOGEUSD: 1061
- DOTUSD: 1061
- ETHUSD: 1259
- EU50: 288
- EURAUD: 769
- EURCAD: 907
- EURCHF: 769
- EURGBP: 770
- EURJPY: 769
- EURUSD: 769
- FRA40: 288
- GBPAUD: 769
- GBPCAD: 769
- GBPCHF: 769
- GBPJPY: 769
- GBPUSD: 770
- GER40: 288
- GOLD: 854
- HK50: 210
- JPN225: 196
- LINKUSD: 1061
- LTCUSD: 1061
- NAS100: 224
- NATGAS: 736
- NZDCAD: 769
- NZDCHF: 769
- NZDJPY: 769
- NZDUSD: 769
- SILVER: 733
- SOLUSD: 1061
- UK100: 288
- US30: 224
- US500: 260
- USDCAD: 769
- USDCHF: 764
- USDJPY: 903
- WTI: 733
- XRPUSD: 1061

## 6. MR candidates / resolved
- 909 candidates, 0 resolved

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