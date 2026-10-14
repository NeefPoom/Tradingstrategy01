# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-14T21:43:44.099594

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
45

## 5. Observation count by asset
- ADAUSD: 892
- AUDCAD: 647
- AUDCHF: 647
- AUDJPY: 647
- AUDNZD: 647
- AUDUSD: 647
- AUS200: 189
- AVAXUSD: 892
- BCHUSD: 892
- BNBUSD: 892
- BRENT: 615
- BTCUSD: 1090
- CADCHF: 647
- CADJPY: 647
- CHFJPY: 647
- DOGEUSD: 892
- DOTUSD: 892
- ETHUSD: 1090
- EU50: 243
- EURAUD: 647
- EURCAD: 785
- EURCHF: 647
- EURGBP: 648
- EURJPY: 647
- EURUSD: 647
- FRA40: 243
- GBPAUD: 647
- GBPCAD: 647
- GBPCHF: 647
- GBPJPY: 647
- GBPUSD: 647
- GER40: 243
- GOLD: 737
- HK50: 182
- JPN225: 161
- LINKUSD: 892
- LTCUSD: 892
- NAS100: 189
- NATGAS: 619
- NZDCAD: 647
- NZDCHF: 647
- NZDJPY: 647
- NZDUSD: 647
- SILVER: 616
- SOLUSD: 892
- UK100: 243
- US30: 189
- US500: 225
- USDCAD: 647
- USDCHF: 643
- USDJPY: 782
- WTI: 616
- XRPUSD: 892

## 6. MR candidates / resolved
- 743 candidates, 0 resolved

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