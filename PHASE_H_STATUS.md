# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-28T06:28:21.367517

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
58

## 5. Observation count by asset
- ADAUSD: 1213
- AUDCAD: 869
- AUDCHF: 869
- AUDJPY: 869
- AUDNZD: 869
- AUDUSD: 869
- AUS200: 259
- AVAXUSD: 1213
- BCHUSD: 1213
- BNBUSD: 1213
- BRENT: 830
- BTCUSD: 1411
- CADCHF: 869
- CADJPY: 869
- CHFJPY: 869
- DOGEUSD: 1213
- DOTUSD: 1213
- ETHUSD: 1411
- EU50: 324
- EURAUD: 869
- EURCAD: 1007
- EURCHF: 869
- EURGBP: 870
- EURJPY: 869
- EURUSD: 869
- FRA40: 324
- GBPAUD: 869
- GBPCAD: 869
- GBPCHF: 869
- GBPJPY: 869
- GBPUSD: 870
- GER40: 324
- GOLD: 952
- HK50: 242
- JPN225: 230
- LINKUSD: 1213
- LTCUSD: 1213
- NAS100: 252
- NATGAS: 835
- NZDCAD: 869
- NZDCHF: 869
- NZDJPY: 869
- NZDUSD: 869
- SILVER: 831
- SOLUSD: 1213
- UK100: 324
- US30: 252
- US500: 288
- USDCAD: 869
- USDCHF: 864
- USDJPY: 1002
- WTI: 831
- XRPUSD: 1213

## 6. MR candidates / resolved
- 1053 candidates, 0 resolved

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