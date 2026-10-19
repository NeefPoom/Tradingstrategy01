# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-19T17:53:14.148754

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
50

## 5. Observation count by asset
- ADAUSD: 1008
- AUDCAD: 714
- AUDCHF: 714
- AUDJPY: 714
- AUDNZD: 714
- AUDUSD: 714
- AUS200: 210
- AVAXUSD: 1008
- BCHUSD: 1008
- BNBUSD: 1008
- BRENT: 680
- BTCUSD: 1206
- CADCHF: 714
- CADJPY: 714
- CHFJPY: 714
- DOGEUSD: 1008
- DOTUSD: 1008
- ETHUSD: 1206
- EU50: 270
- EURAUD: 714
- EURCAD: 852
- EURCHF: 714
- EURGBP: 715
- EURJPY: 714
- EURUSD: 714
- FRA40: 270
- GBPAUD: 714
- GBPCAD: 714
- GBPCHF: 714
- GBPJPY: 714
- GBPUSD: 715
- GER40: 270
- GOLD: 802
- HK50: 196
- JPN225: 182
- LINKUSD: 1008
- LTCUSD: 1008
- NAS100: 207
- NATGAS: 684
- NZDCAD: 714
- NZDCHF: 714
- NZDJPY: 714
- NZDUSD: 714
- SILVER: 681
- SOLUSD: 1008
- UK100: 270
- US30: 207
- US500: 243
- USDCAD: 714
- USDCHF: 709
- USDJPY: 848
- WTI: 681
- XRPUSD: 1008

## 6. MR candidates / resolved
- 843 candidates, 0 resolved

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