# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-09T06:11:24.307030

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
39

## 5. Observation count by asset
- ADAUSD: 757
- AUDCAD: 561
- AUDCHF: 561
- AUDJPY: 561
- AUDNZD: 561
- AUDUSD: 561
- AUS200: 168
- AVAXUSD: 757
- BCHUSD: 757
- BNBUSD: 757
- BRENT: 531
- BTCUSD: 955
- CADCHF: 561
- CADJPY: 561
- CHFJPY: 561
- DOGEUSD: 757
- DOTUSD: 757
- ETHUSD: 955
- EU50: 207
- EURAUD: 561
- EURCAD: 699
- EURCHF: 561
- EURGBP: 561
- EURJPY: 561
- EURUSD: 561
- FRA40: 207
- GBPAUD: 561
- GBPCAD: 561
- GBPCHF: 561
- GBPJPY: 561
- GBPUSD: 561
- GER40: 207
- GOLD: 652
- HK50: 158
- JPN225: 146
- LINKUSD: 757
- LTCUSD: 757
- NAS100: 161
- NATGAS: 533
- NZDCAD: 561
- NZDCHF: 561
- NZDJPY: 561
- NZDUSD: 561
- SILVER: 532
- SOLUSD: 757
- UK100: 207
- US30: 161
- US500: 197
- USDCAD: 561
- USDCHF: 558
- USDJPY: 697
- WTI: 532
- XRPUSD: 757

## 6. MR candidates / resolved
- 620 candidates, 0 resolved

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