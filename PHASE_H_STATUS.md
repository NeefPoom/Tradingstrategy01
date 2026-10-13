# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-13T03:15:41.839994

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
43

## 5. Observation count by asset
- ADAUSD: 850
- AUDCAD: 605
- AUDCHF: 605
- AUDJPY: 605
- AUDNZD: 605
- AUDUSD: 605
- AUS200: 179
- AVAXUSD: 850
- BCHUSD: 850
- BNBUSD: 850
- BRENT: 574
- BTCUSD: 1048
- CADCHF: 605
- CADJPY: 605
- CHFJPY: 605
- DOGEUSD: 850
- DOTUSD: 850
- ETHUSD: 1048
- EU50: 225
- EURAUD: 605
- EURCAD: 743
- EURCHF: 605
- EURGBP: 606
- EURJPY: 605
- EURUSD: 605
- FRA40: 225
- GBPAUD: 605
- GBPCAD: 605
- GBPCHF: 605
- GBPJPY: 605
- GBPUSD: 605
- GER40: 225
- GOLD: 695
- HK50: 169
- JPN225: 150
- LINKUSD: 850
- LTCUSD: 850
- NAS100: 175
- NATGAS: 577
- NZDCAD: 605
- NZDCHF: 605
- NZDJPY: 605
- NZDUSD: 605
- SILVER: 575
- SOLUSD: 850
- UK100: 225
- US30: 175
- US500: 211
- USDCAD: 605
- USDCHF: 601
- USDJPY: 740
- WTI: 575
- XRPUSD: 850

## 6. MR candidates / resolved
- 683 candidates, 0 resolved

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