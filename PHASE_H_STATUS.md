# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-06T23:51:38.219744

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
37

## 5. Observation count by asset
- ADAUSD: 702
- AUDCAD: 506
- AUDCHF: 506
- AUDJPY: 506
- AUDNZD: 506
- AUDUSD: 506
- AUS200: 147
- AVAXUSD: 702
- BCHUSD: 702
- BNBUSD: 702
- BRENT: 478
- BTCUSD: 900
- CADCHF: 506
- CADJPY: 506
- CHFJPY: 506
- DOGEUSD: 702
- DOTUSD: 702
- ETHUSD: 900
- EU50: 189
- EURAUD: 506
- EURCAD: 644
- EURCHF: 506
- EURGBP: 506
- EURJPY: 506
- EURUSD: 506
- FRA40: 189
- GBPAUD: 506
- GBPCAD: 506
- GBPCHF: 506
- GBPJPY: 506
- GBPUSD: 506
- GER40: 189
- GOLD: 599
- HK50: 140
- JPN225: 126
- LINKUSD: 702
- LTCUSD: 702
- NAS100: 147
- NATGAS: 479
- NZDCAD: 506
- NZDCHF: 506
- NZDJPY: 506
- NZDUSD: 506
- SILVER: 479
- SOLUSD: 702
- UK100: 189
- US30: 147
- US500: 183
- USDCAD: 506
- USDCHF: 503
- USDJPY: 642
- WTI: 479
- XRPUSD: 702

## 6. MR candidates / resolved
- 542 candidates, 0 resolved

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