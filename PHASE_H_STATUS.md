# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-08T13:32:13.909825

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
39

## 5. Observation count by asset
- ADAUSD: 740
- AUDCAD: 544
- AUDCHF: 544
- AUDJPY: 544
- AUDNZD: 544
- AUDUSD: 544
- AUS200: 161
- AVAXUSD: 740
- BCHUSD: 740
- BNBUSD: 740
- BRENT: 515
- BTCUSD: 938
- CADCHF: 544
- CADJPY: 544
- CHFJPY: 544
- DOGEUSD: 740
- DOTUSD: 740
- ETHUSD: 938
- EU50: 204
- EURAUD: 544
- EURCAD: 682
- EURCHF: 544
- EURGBP: 544
- EURJPY: 544
- EURUSD: 544
- FRA40: 204
- GBPAUD: 544
- GBPCAD: 544
- GBPCHF: 544
- GBPJPY: 544
- GBPUSD: 544
- GER40: 204
- GOLD: 636
- HK50: 154
- JPN225: 140
- LINKUSD: 740
- LTCUSD: 740
- NAS100: 154
- NATGAS: 516
- NZDCAD: 544
- NZDCHF: 544
- NZDJPY: 544
- NZDUSD: 544
- SILVER: 516
- SOLUSD: 740
- UK100: 204
- US30: 154
- US500: 190
- USDCAD: 544
- USDCHF: 541
- USDJPY: 680
- WTI: 516
- XRPUSD: 740

## 6. MR candidates / resolved
- 578 candidates, 0 resolved

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