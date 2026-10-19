# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-19T11:21:12.003422

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
50

## 5. Observation count by asset
- ADAUSD: 1002
- AUDCAD: 708
- AUDCHF: 708
- AUDJPY: 708
- AUDNZD: 708
- AUDUSD: 708
- AUS200: 210
- AVAXUSD: 1002
- BCHUSD: 1002
- BNBUSD: 1002
- BRENT: 674
- BTCUSD: 1200
- CADCHF: 708
- CADJPY: 708
- CHFJPY: 708
- DOGEUSD: 1002
- DOTUSD: 1002
- ETHUSD: 1200
- EU50: 265
- EURAUD: 708
- EURCAD: 846
- EURCHF: 708
- EURGBP: 709
- EURJPY: 708
- EURUSD: 708
- FRA40: 265
- GBPAUD: 708
- GBPCAD: 708
- GBPCHF: 708
- GBPJPY: 708
- GBPUSD: 709
- GER40: 265
- GOLD: 796
- HK50: 196
- JPN225: 182
- LINKUSD: 1002
- LTCUSD: 1002
- NAS100: 203
- NATGAS: 678
- NZDCAD: 708
- NZDCHF: 708
- NZDJPY: 708
- NZDUSD: 708
- SILVER: 675
- SOLUSD: 1002
- UK100: 265
- US30: 203
- US500: 239
- USDCAD: 708
- USDCHF: 703
- USDJPY: 842
- WTI: 675
- XRPUSD: 1002

## 6. MR candidates / resolved
- 838 candidates, 0 resolved

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