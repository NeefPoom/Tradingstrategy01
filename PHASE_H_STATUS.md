# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-22T17:17:42.416340

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
53

## 5. Observation count by asset
- ADAUSD: 1080
- AUDCAD: 786
- AUDCHF: 786
- AUDJPY: 786
- AUDNZD: 786
- AUDUSD: 786
- AUS200: 231
- AVAXUSD: 1080
- BCHUSD: 1080
- BNBUSD: 1080
- BRENT: 749
- BTCUSD: 1278
- CADCHF: 786
- CADJPY: 786
- CHFJPY: 786
- DOGEUSD: 1080
- DOTUSD: 1080
- ETHUSD: 1278
- EU50: 297
- EURAUD: 786
- EURCAD: 924
- EURCHF: 786
- EURGBP: 787
- EURJPY: 786
- EURUSD: 786
- FRA40: 297
- GBPAUD: 786
- GBPCAD: 786
- GBPCHF: 786
- GBPJPY: 786
- GBPUSD: 787
- GER40: 297
- GOLD: 871
- HK50: 217
- JPN225: 203
- LINKUSD: 1080
- LTCUSD: 1080
- NAS100: 227
- NATGAS: 753
- NZDCAD: 786
- NZDCHF: 786
- NZDJPY: 786
- NZDUSD: 786
- SILVER: 750
- SOLUSD: 1080
- UK100: 297
- US30: 227
- US500: 263
- USDCAD: 786
- USDCHF: 781
- USDJPY: 920
- WTI: 750
- XRPUSD: 1080

## 6. MR candidates / resolved
- 939 candidates, 0 resolved

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