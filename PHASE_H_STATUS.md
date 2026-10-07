# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-07T19:40:21.231803

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
38

## 5. Observation count by asset
- ADAUSD: 722
- AUDCAD: 526
- AUDCHF: 526
- AUDJPY: 526
- AUDNZD: 526
- AUDUSD: 526
- AUS200: 154
- AVAXUSD: 722
- BCHUSD: 722
- BNBUSD: 722
- BRENT: 498
- BTCUSD: 920
- CADCHF: 526
- CADJPY: 526
- CHFJPY: 526
- DOGEUSD: 722
- DOTUSD: 722
- ETHUSD: 920
- EU50: 198
- EURAUD: 526
- EURCAD: 664
- EURCHF: 526
- EURGBP: 526
- EURJPY: 526
- EURUSD: 526
- FRA40: 198
- GBPAUD: 526
- GBPCAD: 526
- GBPCHF: 526
- GBPJPY: 526
- GBPUSD: 526
- GER40: 198
- GOLD: 619
- HK50: 147
- JPN225: 133
- LINKUSD: 722
- LTCUSD: 722
- NAS100: 153
- NATGAS: 499
- NZDCAD: 526
- NZDCHF: 526
- NZDJPY: 526
- NZDUSD: 526
- SILVER: 499
- SOLUSD: 722
- UK100: 198
- US30: 153
- US500: 189
- USDCAD: 526
- USDCHF: 523
- USDJPY: 662
- WTI: 499
- XRPUSD: 722

## 6. MR candidates / resolved
- 561 candidates, 0 resolved

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