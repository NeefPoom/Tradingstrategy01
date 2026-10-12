# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-12T22:44:45.099919

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
43

## 5. Observation count by asset
- ADAUSD: 845
- AUDCAD: 600
- AUDCHF: 600
- AUDJPY: 600
- AUDNZD: 600
- AUDUSD: 600
- AUS200: 175
- AVAXUSD: 845
- BCHUSD: 845
- BNBUSD: 845
- BRENT: 569
- BTCUSD: 1043
- CADCHF: 600
- CADJPY: 600
- CHFJPY: 600
- DOGEUSD: 845
- DOTUSD: 845
- ETHUSD: 1043
- EU50: 225
- EURAUD: 600
- EURCAD: 738
- EURCHF: 600
- EURGBP: 601
- EURJPY: 600
- EURUSD: 600
- FRA40: 225
- GBPAUD: 600
- GBPCAD: 600
- GBPCHF: 600
- GBPJPY: 600
- GBPUSD: 600
- GER40: 225
- GOLD: 690
- HK50: 168
- JPN225: 147
- LINKUSD: 845
- LTCUSD: 845
- NAS100: 175
- NATGAS: 572
- NZDCAD: 600
- NZDCHF: 600
- NZDJPY: 600
- NZDUSD: 600
- SILVER: 570
- SOLUSD: 845
- UK100: 225
- US30: 175
- US500: 211
- USDCAD: 600
- USDCHF: 596
- USDJPY: 735
- WTI: 570
- XRPUSD: 845

## 6. MR candidates / resolved
- 678 candidates, 0 resolved

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