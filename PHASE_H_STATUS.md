# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-27T16:43:01.713494

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
58

## 5. Observation count by asset
- ADAUSD: 1199
- AUDCAD: 855
- AUDCHF: 855
- AUDJPY: 855
- AUDNZD: 855
- AUDUSD: 855
- AUS200: 252
- AVAXUSD: 1199
- BCHUSD: 1199
- BNBUSD: 1199
- BRENT: 817
- BTCUSD: 1397
- CADCHF: 855
- CADJPY: 855
- CHFJPY: 855
- DOGEUSD: 1199
- DOTUSD: 1199
- ETHUSD: 1397
- EU50: 323
- EURAUD: 855
- EURCAD: 993
- EURCHF: 855
- EURGBP: 856
- EURJPY: 855
- EURUSD: 855
- FRA40: 323
- GBPAUD: 855
- GBPCAD: 855
- GBPCHF: 855
- GBPJPY: 855
- GBPUSD: 856
- GER40: 323
- GOLD: 939
- HK50: 238
- JPN225: 224
- LINKUSD: 1199
- LTCUSD: 1199
- NAS100: 248
- NATGAS: 822
- NZDCAD: 855
- NZDCHF: 855
- NZDJPY: 855
- NZDUSD: 855
- SILVER: 818
- SOLUSD: 1199
- UK100: 323
- US30: 248
- US500: 284
- USDCAD: 855
- USDCHF: 850
- USDJPY: 988
- WTI: 818
- XRPUSD: 1199

## 6. MR candidates / resolved
- 1039 candidates, 0 resolved

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