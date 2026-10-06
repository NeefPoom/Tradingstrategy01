# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-06T19:57:22.471720

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
37

## 5. Observation count by asset
- ADAUSD: 698
- AUDCAD: 502
- AUDCHF: 502
- AUDJPY: 502
- AUDNZD: 502
- AUDUSD: 502
- AUS200: 147
- AVAXUSD: 698
- BCHUSD: 698
- BNBUSD: 698
- BRENT: 475
- BTCUSD: 896
- CADCHF: 502
- CADJPY: 502
- CHFJPY: 502
- DOGEUSD: 698
- DOTUSD: 698
- ETHUSD: 896
- EU50: 189
- EURAUD: 502
- EURCAD: 640
- EURCHF: 502
- EURGBP: 502
- EURJPY: 502
- EURUSD: 502
- FRA40: 189
- GBPAUD: 502
- GBPCAD: 502
- GBPCHF: 502
- GBPJPY: 502
- GBPUSD: 502
- GER40: 189
- GOLD: 596
- HK50: 140
- JPN225: 126
- LINKUSD: 698
- LTCUSD: 698
- NAS100: 146
- NATGAS: 476
- NZDCAD: 502
- NZDCHF: 502
- NZDJPY: 502
- NZDUSD: 502
- SILVER: 476
- SOLUSD: 698
- UK100: 189
- US30: 146
- US500: 182
- USDCAD: 502
- USDCHF: 499
- USDJPY: 638
- WTI: 476
- XRPUSD: 698

## 6. MR candidates / resolved
- 539 candidates, 0 resolved

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