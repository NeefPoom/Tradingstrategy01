# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-13T11:10:43.255860

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
44

## 5. Observation count by asset
- ADAUSD: 858
- AUDCAD: 613
- AUDCHF: 613
- AUDJPY: 613
- AUDNZD: 613
- AUDUSD: 613
- AUS200: 182
- AVAXUSD: 858
- BCHUSD: 858
- BNBUSD: 858
- BRENT: 582
- BTCUSD: 1056
- CADCHF: 613
- CADJPY: 613
- CHFJPY: 613
- DOGEUSD: 858
- DOTUSD: 858
- ETHUSD: 1056
- EU50: 229
- EURAUD: 613
- EURCAD: 751
- EURCHF: 613
- EURGBP: 614
- EURJPY: 613
- EURUSD: 613
- FRA40: 229
- GBPAUD: 613
- GBPCAD: 613
- GBPCHF: 613
- GBPJPY: 613
- GBPUSD: 613
- GER40: 229
- GOLD: 703
- HK50: 175
- JPN225: 154
- LINKUSD: 858
- LTCUSD: 858
- NAS100: 175
- NATGAS: 585
- NZDCAD: 613
- NZDCHF: 613
- NZDJPY: 613
- NZDUSD: 613
- SILVER: 583
- SOLUSD: 858
- UK100: 229
- US30: 175
- US500: 211
- USDCAD: 613
- USDCHF: 609
- USDJPY: 748
- WTI: 583
- XRPUSD: 858

## 6. MR candidates / resolved
- 696 candidates, 0 resolved

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