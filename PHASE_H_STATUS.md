# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-12T15:29:18.169022

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
43

## 5. Observation count by asset
- ADAUSD: 838
- AUDCAD: 593
- AUDCHF: 593
- AUDJPY: 593
- AUDNZD: 593
- AUDUSD: 593
- AUS200: 175
- AVAXUSD: 838
- BCHUSD: 838
- BNBUSD: 838
- BRENT: 563
- BTCUSD: 1036
- CADCHF: 593
- CADJPY: 593
- CHFJPY: 593
- DOGEUSD: 838
- DOTUSD: 838
- ETHUSD: 1036
- EU50: 224
- EURAUD: 593
- EURCAD: 731
- EURCHF: 593
- EURGBP: 594
- EURJPY: 593
- EURUSD: 593
- FRA40: 224
- GBPAUD: 593
- GBPCAD: 593
- GBPCHF: 593
- GBPJPY: 593
- GBPUSD: 593
- GER40: 224
- GOLD: 684
- HK50: 168
- JPN225: 147
- LINKUSD: 838
- LTCUSD: 838
- NAS100: 169
- NATGAS: 566
- NZDCAD: 593
- NZDCHF: 593
- NZDJPY: 593
- NZDUSD: 593
- SILVER: 564
- SOLUSD: 838
- UK100: 224
- US30: 169
- US500: 205
- USDCAD: 593
- USDCHF: 589
- USDJPY: 728
- WTI: 564
- XRPUSD: 838

## 6. MR candidates / resolved
- 670 candidates, 0 resolved

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