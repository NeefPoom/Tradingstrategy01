# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-08T05:59:29.551552

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
38

## 5. Observation count by asset
- ADAUSD: 732
- AUDCAD: 536
- AUDCHF: 536
- AUDJPY: 536
- AUDNZD: 536
- AUDUSD: 536
- AUS200: 160
- AVAXUSD: 732
- BCHUSD: 732
- BNBUSD: 732
- BRENT: 507
- BTCUSD: 930
- CADCHF: 536
- CADJPY: 536
- CHFJPY: 536
- DOGEUSD: 732
- DOTUSD: 732
- ETHUSD: 930
- EU50: 198
- EURAUD: 536
- EURCAD: 674
- EURCHF: 536
- EURGBP: 536
- EURJPY: 536
- EURUSD: 536
- FRA40: 198
- GBPAUD: 536
- GBPCAD: 536
- GBPCHF: 536
- GBPJPY: 536
- GBPUSD: 536
- GER40: 198
- GOLD: 628
- HK50: 151
- JPN225: 138
- LINKUSD: 732
- LTCUSD: 732
- NAS100: 154
- NATGAS: 508
- NZDCAD: 536
- NZDCHF: 536
- NZDJPY: 536
- NZDUSD: 536
- SILVER: 508
- SOLUSD: 732
- UK100: 198
- US30: 154
- US500: 190
- USDCAD: 536
- USDCHF: 533
- USDJPY: 672
- WTI: 507
- XRPUSD: 732

## 6. MR candidates / resolved
- 574 candidates, 0 resolved

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