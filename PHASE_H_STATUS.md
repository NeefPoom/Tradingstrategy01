# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-23T01:59:56.402005

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
53

## 5. Observation count by asset
- ADAUSD: 1088
- AUDCAD: 794
- AUDCHF: 794
- AUDJPY: 794
- AUDNZD: 794
- AUDUSD: 794
- AUS200: 233
- AVAXUSD: 1088
- BCHUSD: 1088
- BNBUSD: 1088
- BRENT: 756
- BTCUSD: 1286
- CADCHF: 794
- CADJPY: 794
- CHFJPY: 794
- DOGEUSD: 1088
- DOTUSD: 1088
- ETHUSD: 1286
- EU50: 297
- EURAUD: 794
- EURCAD: 932
- EURCHF: 794
- EURGBP: 795
- EURJPY: 794
- EURUSD: 794
- FRA40: 297
- GBPAUD: 794
- GBPCAD: 794
- GBPCHF: 794
- GBPJPY: 794
- GBPUSD: 795
- GER40: 297
- GOLD: 878
- HK50: 217
- JPN225: 204
- LINKUSD: 1088
- LTCUSD: 1088
- NAS100: 231
- NATGAS: 760
- NZDCAD: 794
- NZDCHF: 794
- NZDJPY: 794
- NZDUSD: 794
- SILVER: 757
- SOLUSD: 1088
- UK100: 297
- US30: 231
- US500: 267
- USDCAD: 794
- USDCHF: 789
- USDJPY: 928
- WTI: 757
- XRPUSD: 1088

## 6. MR candidates / resolved
- 939 candidates, 0 resolved

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