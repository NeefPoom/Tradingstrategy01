# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-26T07:56:39.844686

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
56

## 5. Observation count by asset
- ADAUSD: 1166
- AUDCAD: 822
- AUDCHF: 822
- AUDJPY: 822
- AUDNZD: 822
- AUDUSD: 822
- AUS200: 245
- AVAXUSD: 1166
- BCHUSD: 1166
- BNBUSD: 1166
- BRENT: 785
- BTCUSD: 1364
- CADCHF: 822
- CADJPY: 822
- CHFJPY: 822
- DOGEUSD: 1166
- DOTUSD: 1166
- ETHUSD: 1364
- EU50: 306
- EURAUD: 822
- EURCAD: 960
- EURCHF: 822
- EURGBP: 823
- EURJPY: 822
- EURUSD: 822
- FRA40: 306
- GBPAUD: 822
- GBPCAD: 822
- GBPCHF: 822
- GBPJPY: 822
- GBPUSD: 823
- GER40: 306
- GOLD: 907
- HK50: 230
- JPN225: 217
- LINKUSD: 1166
- LTCUSD: 1166
- NAS100: 238
- NATGAS: 790
- NZDCAD: 822
- NZDCHF: 822
- NZDJPY: 822
- NZDUSD: 822
- SILVER: 786
- SOLUSD: 1166
- UK100: 306
- US30: 238
- US500: 274
- USDCAD: 822
- USDCHF: 817
- USDJPY: 955
- WTI: 786
- XRPUSD: 1166

## 6. MR candidates / resolved
- 1006 candidates, 0 resolved

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