# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-15T00:12:08.571267

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
45

## 5. Observation count by asset
- ADAUSD: 893
- AUDCAD: 650
- AUDCHF: 650
- AUDJPY: 650
- AUDNZD: 650
- AUDUSD: 650
- AUS200: 190
- AVAXUSD: 893
- BCHUSD: 893
- BNBUSD: 893
- BRENT: 617
- BTCUSD: 1091
- CADCHF: 650
- CADJPY: 650
- CHFJPY: 650
- DOGEUSD: 893
- DOTUSD: 893
- ETHUSD: 1091
- EU50: 243
- EURAUD: 650
- EURCAD: 788
- EURCHF: 650
- EURGBP: 651
- EURJPY: 650
- EURUSD: 650
- FRA40: 243
- GBPAUD: 650
- GBPCAD: 650
- GBPCHF: 650
- GBPJPY: 650
- GBPUSD: 650
- GER40: 243
- GOLD: 739
- HK50: 182
- JPN225: 161
- LINKUSD: 893
- LTCUSD: 893
- NAS100: 189
- NATGAS: 621
- NZDCAD: 650
- NZDCHF: 650
- NZDJPY: 650
- NZDUSD: 650
- SILVER: 618
- SOLUSD: 893
- UK100: 243
- US30: 189
- US500: 225
- USDCAD: 650
- USDCHF: 646
- USDJPY: 785
- WTI: 618
- XRPUSD: 893

## 6. MR candidates / resolved
- 746 candidates, 0 resolved

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