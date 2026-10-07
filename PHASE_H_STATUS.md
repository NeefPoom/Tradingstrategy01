# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-07T05:55:44.641174

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
37

## 5. Observation count by asset
- ADAUSD: 708
- AUDCAD: 512
- AUDCHF: 512
- AUDJPY: 512
- AUDNZD: 512
- AUDUSD: 512
- AUS200: 153
- AVAXUSD: 708
- BCHUSD: 708
- BNBUSD: 708
- BRENT: 483
- BTCUSD: 906
- CADCHF: 512
- CADJPY: 512
- CHFJPY: 512
- DOGEUSD: 708
- DOTUSD: 708
- ETHUSD: 906
- EU50: 189
- EURAUD: 512
- EURCAD: 650
- EURCHF: 512
- EURGBP: 512
- EURJPY: 512
- EURUSD: 512
- FRA40: 189
- GBPAUD: 512
- GBPCAD: 512
- GBPCHF: 512
- GBPJPY: 512
- GBPUSD: 512
- GER40: 189
- GOLD: 604
- HK50: 144
- JPN225: 131
- LINKUSD: 708
- LTCUSD: 708
- NAS100: 147
- NATGAS: 484
- NZDCAD: 512
- NZDCHF: 512
- NZDJPY: 512
- NZDUSD: 512
- SILVER: 484
- SOLUSD: 708
- UK100: 189
- US30: 147
- US500: 183
- USDCAD: 512
- USDCHF: 509
- USDJPY: 648
- WTI: 484
- XRPUSD: 708

## 6. MR candidates / resolved
- 545 candidates, 0 resolved

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