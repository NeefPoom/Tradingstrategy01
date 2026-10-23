# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-23T12:59:42.909620

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
54

## 5. Observation count by asset
- ADAUSD: 1099
- AUDCAD: 805
- AUDCHF: 805
- AUDJPY: 805
- AUDNZD: 805
- AUDUSD: 805
- AUS200: 238
- AVAXUSD: 1099
- BCHUSD: 1099
- BNBUSD: 1099
- BRENT: 767
- BTCUSD: 1297
- CADCHF: 805
- CADJPY: 805
- CHFJPY: 805
- DOGEUSD: 1099
- DOTUSD: 1099
- ETHUSD: 1297
- EU50: 302
- EURAUD: 805
- EURCAD: 943
- EURCHF: 805
- EURGBP: 806
- EURJPY: 805
- EURUSD: 805
- FRA40: 302
- GBPAUD: 805
- GBPCAD: 805
- GBPCHF: 805
- GBPJPY: 805
- GBPUSD: 806
- GER40: 302
- GOLD: 889
- HK50: 224
- JPN225: 210
- LINKUSD: 1099
- LTCUSD: 1099
- NAS100: 231
- NATGAS: 771
- NZDCAD: 805
- NZDCHF: 805
- NZDJPY: 805
- NZDUSD: 805
- SILVER: 768
- SOLUSD: 1099
- UK100: 302
- US30: 231
- US500: 267
- USDCAD: 805
- USDCHF: 800
- USDJPY: 939
- WTI: 768
- XRPUSD: 1099

## 6. MR candidates / resolved
- 971 candidates, 0 resolved

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