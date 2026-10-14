# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-14T07:36:23.018719

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
44

## 5. Observation count by asset
- ADAUSD: 878
- AUDCAD: 633
- AUDCHF: 633
- AUDJPY: 633
- AUDNZD: 633
- AUDUSD: 633
- AUS200: 189
- AVAXUSD: 878
- BCHUSD: 878
- BNBUSD: 878
- BRENT: 601
- BTCUSD: 1076
- CADCHF: 633
- CADJPY: 633
- CHFJPY: 633
- DOGEUSD: 878
- DOTUSD: 878
- ETHUSD: 1076
- EU50: 234
- EURAUD: 633
- EURCAD: 771
- EURCHF: 633
- EURGBP: 634
- EURJPY: 633
- EURUSD: 633
- FRA40: 234
- GBPAUD: 633
- GBPCAD: 633
- GBPCHF: 633
- GBPJPY: 633
- GBPUSD: 633
- GER40: 234
- GOLD: 723
- HK50: 181
- JPN225: 161
- LINKUSD: 878
- LTCUSD: 878
- NAS100: 182
- NATGAS: 605
- NZDCAD: 633
- NZDCHF: 633
- NZDJPY: 633
- NZDUSD: 633
- SILVER: 602
- SOLUSD: 878
- UK100: 234
- US30: 182
- US500: 218
- USDCAD: 633
- USDCHF: 629
- USDJPY: 768
- WTI: 602
- XRPUSD: 878

## 6. MR candidates / resolved
- 718 candidates, 0 resolved

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