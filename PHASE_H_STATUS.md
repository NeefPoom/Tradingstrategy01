# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-26T15:17:05.251518

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
57

## 5. Observation count by asset
- ADAUSD: 1174
- AUDCAD: 830
- AUDCHF: 830
- AUDJPY: 830
- AUDNZD: 830
- AUDUSD: 830
- AUS200: 245
- AVAXUSD: 1174
- BCHUSD: 1174
- BNBUSD: 1174
- BRENT: 793
- BTCUSD: 1372
- CADCHF: 830
- CADJPY: 830
- CHFJPY: 830
- DOGEUSD: 1174
- DOTUSD: 1174
- ETHUSD: 1372
- EU50: 313
- EURAUD: 830
- EURCAD: 968
- EURCHF: 830
- EURGBP: 831
- EURJPY: 830
- EURUSD: 830
- FRA40: 313
- GBPAUD: 830
- GBPCAD: 830
- GBPCHF: 830
- GBPJPY: 830
- GBPUSD: 831
- GER40: 313
- GOLD: 915
- HK50: 231
- JPN225: 217
- LINKUSD: 1174
- LTCUSD: 1174
- NAS100: 239
- NATGAS: 798
- NZDCAD: 830
- NZDCHF: 830
- NZDJPY: 830
- NZDUSD: 830
- SILVER: 794
- SOLUSD: 1174
- UK100: 313
- US30: 239
- US500: 275
- USDCAD: 830
- USDCHF: 825
- USDJPY: 963
- WTI: 794
- XRPUSD: 1174

## 6. MR candidates / resolved
- 1016 candidates, 0 resolved

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