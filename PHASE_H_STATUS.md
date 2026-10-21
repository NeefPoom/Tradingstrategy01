# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-21T18:26:23.304792

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
52

## 5. Observation count by asset
- ADAUSD: 1057
- AUDCAD: 763
- AUDCHF: 763
- AUDJPY: 763
- AUDNZD: 763
- AUDUSD: 763
- AUS200: 224
- AVAXUSD: 1057
- BCHUSD: 1057
- BNBUSD: 1057
- BRENT: 727
- BTCUSD: 1255
- CADCHF: 763
- CADJPY: 763
- CHFJPY: 763
- DOGEUSD: 1057
- DOTUSD: 1057
- ETHUSD: 1255
- EU50: 288
- EURAUD: 763
- EURCAD: 901
- EURCHF: 763
- EURGBP: 764
- EURJPY: 763
- EURUSD: 763
- FRA40: 288
- GBPAUD: 763
- GBPCAD: 763
- GBPCHF: 763
- GBPJPY: 763
- GBPUSD: 764
- GER40: 288
- GOLD: 849
- HK50: 210
- JPN225: 196
- LINKUSD: 1057
- LTCUSD: 1057
- NAS100: 221
- NATGAS: 731
- NZDCAD: 763
- NZDCHF: 763
- NZDJPY: 763
- NZDUSD: 763
- SILVER: 728
- SOLUSD: 1057
- UK100: 288
- US30: 221
- US500: 257
- USDCAD: 763
- USDCHF: 758
- USDJPY: 897
- WTI: 728
- XRPUSD: 1057

## 6. MR candidates / resolved
- 904 candidates, 0 resolved

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