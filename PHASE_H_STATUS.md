# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-19T22:28:03.803868

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
50

## 5. Observation count by asset
- ADAUSD: 1013
- AUDCAD: 719
- AUDCHF: 719
- AUDJPY: 719
- AUDNZD: 719
- AUDUSD: 719
- AUS200: 210
- AVAXUSD: 1013
- BCHUSD: 1013
- BNBUSD: 1013
- BRENT: 684
- BTCUSD: 1211
- CADCHF: 719
- CADJPY: 719
- CHFJPY: 719
- DOGEUSD: 1013
- DOTUSD: 1013
- ETHUSD: 1211
- EU50: 270
- EURAUD: 719
- EURCAD: 857
- EURCHF: 719
- EURGBP: 720
- EURJPY: 719
- EURUSD: 719
- FRA40: 270
- GBPAUD: 719
- GBPCAD: 719
- GBPCHF: 719
- GBPJPY: 719
- GBPUSD: 720
- GER40: 270
- GOLD: 806
- HK50: 196
- JPN225: 182
- LINKUSD: 1013
- LTCUSD: 1013
- NAS100: 210
- NATGAS: 688
- NZDCAD: 719
- NZDCHF: 719
- NZDJPY: 719
- NZDUSD: 719
- SILVER: 685
- SOLUSD: 1013
- UK100: 270
- US30: 210
- US500: 246
- USDCAD: 719
- USDCHF: 714
- USDJPY: 853
- WTI: 685
- XRPUSD: 1013

## 6. MR candidates / resolved
- 848 candidates, 0 resolved

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