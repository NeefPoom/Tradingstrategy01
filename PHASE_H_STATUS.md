# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-13T18:18:43.657303

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
44

## 5. Observation count by asset
- ADAUSD: 865
- AUDCAD: 620
- AUDCHF: 620
- AUDJPY: 620
- AUDNZD: 620
- AUDUSD: 620
- AUS200: 182
- AVAXUSD: 865
- BCHUSD: 865
- BNBUSD: 865
- BRENT: 589
- BTCUSD: 1063
- CADCHF: 620
- CADJPY: 620
- CHFJPY: 620
- DOGEUSD: 865
- DOTUSD: 865
- ETHUSD: 1063
- EU50: 234
- EURAUD: 620
- EURCAD: 758
- EURCHF: 620
- EURGBP: 621
- EURJPY: 620
- EURUSD: 620
- FRA40: 234
- GBPAUD: 620
- GBPCAD: 620
- GBPCHF: 620
- GBPJPY: 620
- GBPUSD: 620
- GER40: 234
- GOLD: 710
- HK50: 175
- JPN225: 154
- LINKUSD: 865
- LTCUSD: 865
- NAS100: 179
- NATGAS: 592
- NZDCAD: 620
- NZDCHF: 620
- NZDJPY: 620
- NZDUSD: 620
- SILVER: 590
- SOLUSD: 865
- UK100: 234
- US30: 179
- US500: 215
- USDCAD: 620
- USDCHF: 616
- USDJPY: 755
- WTI: 590
- XRPUSD: 865

## 6. MR candidates / resolved
- 709 candidates, 0 resolved

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