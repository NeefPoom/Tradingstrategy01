# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-21T02:06:35.924234

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
51

## 5. Observation count by asset
- ADAUSD: 1041
- AUDCAD: 747
- AUDCHF: 747
- AUDJPY: 747
- AUDNZD: 747
- AUDUSD: 747
- AUS200: 220
- AVAXUSD: 1041
- BCHUSD: 1041
- BNBUSD: 1041
- BRENT: 711
- BTCUSD: 1238
- CADCHF: 747
- CADJPY: 747
- CHFJPY: 747
- DOGEUSD: 1041
- DOTUSD: 1041
- ETHUSD: 1239
- EU50: 279
- EURAUD: 747
- EURCAD: 885
- EURCHF: 747
- EURGBP: 748
- EURJPY: 747
- EURUSD: 747
- FRA40: 279
- GBPAUD: 747
- GBPCAD: 747
- GBPCHF: 747
- GBPJPY: 747
- GBPUSD: 748
- GER40: 279
- GOLD: 832
- HK50: 203
- JPN225: 191
- LINKUSD: 1041
- LTCUSD: 1041
- NAS100: 217
- NATGAS: 715
- NZDCAD: 747
- NZDCHF: 747
- NZDJPY: 747
- NZDUSD: 747
- SILVER: 712
- SOLUSD: 1041
- UK100: 279
- US30: 217
- US500: 253
- USDCAD: 747
- USDCHF: 742
- USDJPY: 880
- WTI: 712
- XRPUSD: 1041

## 6. MR candidates / resolved
- 890 candidates, 0 resolved

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