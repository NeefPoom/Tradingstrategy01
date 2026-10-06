# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-06T00:52:58.514889

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
36

## 5. Observation count by asset
- ADAUSD: 676
- AUDCAD: 481
- AUDCHF: 481
- AUDJPY: 481
- AUDNZD: 481
- AUDUSD: 481
- AUS200: 141
- AVAXUSD: 676
- BCHUSD: 676
- BNBUSD: 676
- BRENT: 456
- BTCUSD: 874
- CADCHF: 481
- CADJPY: 481
- CHFJPY: 481
- DOGEUSD: 676
- DOTUSD: 676
- ETHUSD: 874
- EU50: 180
- EURAUD: 481
- EURCAD: 619
- EURCHF: 481
- EURGBP: 481
- EURJPY: 481
- EURUSD: 481
- FRA40: 180
- GBPAUD: 481
- GBPCAD: 481
- GBPCHF: 481
- GBPJPY: 481
- GBPUSD: 481
- GER40: 180
- GOLD: 577
- HK50: 133
- JPN225: 119
- LINKUSD: 676
- LTCUSD: 676
- NAS100: 140
- NATGAS: 457
- NZDCAD: 481
- NZDCHF: 481
- NZDJPY: 481
- NZDUSD: 481
- SILVER: 457
- SOLUSD: 676
- UK100: 180
- US30: 140
- US500: 176
- USDCAD: 481
- USDCHF: 478
- USDJPY: 617
- WTI: 457
- XRPUSD: 676

## 6. MR candidates / resolved
- 521 candidates, 0 resolved

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