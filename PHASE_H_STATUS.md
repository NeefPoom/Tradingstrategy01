# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-15T14:29:34.652688

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
46

## 5. Observation count by asset
- ADAUSD: 909
- AUDCAD: 664
- AUDCHF: 664
- AUDJPY: 664
- AUDNZD: 664
- AUDUSD: 664
- AUS200: 196
- AVAXUSD: 909
- BCHUSD: 909
- BNBUSD: 909
- BRENT: 631
- BTCUSD: 1107
- CADCHF: 664
- CADJPY: 664
- CHFJPY: 664
- DOGEUSD: 909
- DOTUSD: 909
- ETHUSD: 1107
- EU50: 250
- EURAUD: 664
- EURCAD: 802
- EURCHF: 664
- EURGBP: 665
- EURJPY: 664
- EURUSD: 664
- FRA40: 250
- GBPAUD: 664
- GBPCAD: 664
- GBPCHF: 664
- GBPJPY: 664
- GBPUSD: 664
- GER40: 250
- GOLD: 753
- HK50: 189
- JPN225: 168
- LINKUSD: 909
- LTCUSD: 909
- NAS100: 189
- NATGAS: 635
- NZDCAD: 664
- NZDCHF: 664
- NZDJPY: 664
- NZDUSD: 664
- SILVER: 632
- SOLUSD: 909
- UK100: 250
- US30: 189
- US500: 225
- USDCAD: 664
- USDCHF: 660
- USDJPY: 799
- WTI: 632
- XRPUSD: 909

## 6. MR candidates / resolved
- 762 candidates, 0 resolved

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