# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-16T00:25:38.891797

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
46

## 5. Observation count by asset
- ADAUSD: 918
- AUDCAD: 673
- AUDCHF: 673
- AUDJPY: 673
- AUDNZD: 673
- AUDUSD: 673
- AUS200: 197
- AVAXUSD: 918
- BCHUSD: 918
- BNBUSD: 918
- BRENT: 640
- BTCUSD: 1116
- CADCHF: 673
- CADJPY: 673
- CHFJPY: 673
- DOGEUSD: 918
- DOTUSD: 918
- ETHUSD: 1116
- EU50: 252
- EURAUD: 673
- EURCAD: 811
- EURCHF: 673
- EURGBP: 674
- EURJPY: 673
- EURUSD: 673
- FRA40: 252
- GBPAUD: 673
- GBPCAD: 673
- GBPCHF: 673
- GBPJPY: 673
- GBPUSD: 673
- GER40: 252
- GOLD: 762
- HK50: 189
- JPN225: 168
- LINKUSD: 918
- LTCUSD: 918
- NAS100: 196
- NATGAS: 644
- NZDCAD: 673
- NZDCHF: 673
- NZDJPY: 673
- NZDUSD: 673
- SILVER: 641
- SOLUSD: 918
- UK100: 252
- US30: 196
- US500: 232
- USDCAD: 673
- USDCHF: 669
- USDJPY: 808
- WTI: 641
- XRPUSD: 918

## 6. MR candidates / resolved
- 781 candidates, 0 resolved

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