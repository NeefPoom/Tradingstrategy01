# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-16T18:53:29.057319

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
47

## 5. Observation count by asset
- ADAUSD: 937
- AUDCAD: 692
- AUDCHF: 692
- AUDJPY: 692
- AUDNZD: 692
- AUDUSD: 692
- AUS200: 203
- AVAXUSD: 937
- BCHUSD: 937
- BNBUSD: 937
- BRENT: 658
- BTCUSD: 1135
- CADCHF: 692
- CADJPY: 692
- CHFJPY: 692
- DOGEUSD: 937
- DOTUSD: 937
- ETHUSD: 1135
- EU50: 261
- EURAUD: 692
- EURCAD: 830
- EURCHF: 692
- EURGBP: 693
- EURJPY: 692
- EURUSD: 692
- FRA40: 261
- GBPAUD: 692
- GBPCAD: 692
- GBPCHF: 692
- GBPJPY: 692
- GBPUSD: 692
- GER40: 261
- GOLD: 780
- HK50: 196
- JPN225: 175
- LINKUSD: 937
- LTCUSD: 937
- NAS100: 201
- NATGAS: 662
- NZDCAD: 692
- NZDCHF: 692
- NZDJPY: 692
- NZDUSD: 692
- SILVER: 659
- SOLUSD: 937
- UK100: 261
- US30: 201
- US500: 237
- USDCAD: 692
- USDCHF: 688
- USDJPY: 827
- WTI: 659
- XRPUSD: 937

## 6. MR candidates / resolved
- 798 candidates, 0 resolved

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