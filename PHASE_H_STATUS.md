# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-09T13:19:39.351753

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
40

## 5. Observation count by asset
- ADAUSD: 764
- AUDCAD: 568
- AUDCHF: 568
- AUDJPY: 568
- AUDNZD: 568
- AUDUSD: 568
- AUS200: 168
- AVAXUSD: 764
- BCHUSD: 764
- BNBUSD: 764
- BRENT: 538
- BTCUSD: 962
- CADCHF: 568
- CADJPY: 568
- CHFJPY: 568
- DOGEUSD: 764
- DOTUSD: 764
- ETHUSD: 962
- EU50: 213
- EURAUD: 568
- EURCAD: 706
- EURCHF: 568
- EURGBP: 568
- EURJPY: 568
- EURUSD: 568
- FRA40: 213
- GBPAUD: 568
- GBPCAD: 568
- GBPCHF: 568
- GBPJPY: 568
- GBPUSD: 568
- GER40: 213
- GOLD: 659
- HK50: 161
- JPN225: 147
- LINKUSD: 764
- LTCUSD: 764
- NAS100: 161
- NATGAS: 540
- NZDCAD: 568
- NZDCHF: 568
- NZDJPY: 568
- NZDUSD: 568
- SILVER: 539
- SOLUSD: 764
- UK100: 213
- US30: 161
- US500: 197
- USDCAD: 568
- USDCHF: 565
- USDJPY: 704
- WTI: 539
- XRPUSD: 764

## 6. MR candidates / resolved
- 630 candidates, 0 resolved

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