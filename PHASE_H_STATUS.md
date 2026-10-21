# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-21T07:40:36.992010

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
51

## 5. Observation count by asset
- ADAUSD: 1046
- AUDCAD: 752
- AUDCHF: 752
- AUDJPY: 752
- AUDNZD: 752
- AUDUSD: 752
- AUS200: 224
- AVAXUSD: 1046
- BCHUSD: 1046
- BNBUSD: 1046
- BRENT: 716
- BTCUSD: 1244
- CADCHF: 752
- CADJPY: 752
- CHFJPY: 752
- DOGEUSD: 1046
- DOTUSD: 1046
- ETHUSD: 1244
- EU50: 279
- EURAUD: 752
- EURCAD: 890
- EURCHF: 752
- EURGBP: 753
- EURJPY: 752
- EURUSD: 752
- FRA40: 279
- GBPAUD: 752
- GBPCAD: 752
- GBPCHF: 752
- GBPJPY: 752
- GBPUSD: 753
- GER40: 279
- GOLD: 838
- HK50: 209
- JPN225: 196
- LINKUSD: 1046
- LTCUSD: 1046
- NAS100: 217
- NATGAS: 720
- NZDCAD: 752
- NZDCHF: 752
- NZDJPY: 752
- NZDUSD: 752
- SILVER: 717
- SOLUSD: 1046
- UK100: 279
- US30: 217
- US500: 253
- USDCAD: 752
- USDCHF: 747
- USDJPY: 886
- WTI: 717
- XRPUSD: 1046

## 6. MR candidates / resolved
- 897 candidates, 0 resolved

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