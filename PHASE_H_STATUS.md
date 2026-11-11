# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-11T00:43:30.831867

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
72

## 5. Observation count by asset
- ADAUSD: 1543
- AUDCAD: 1101
- AUDCHF: 1101
- AUDJPY: 1100
- AUDNZD: 1101
- AUDUSD: 1101
- AUS200: 323
- AVAXUSD: 1543
- BCHUSD: 1543
- BNBUSD: 1543
- BRENT: 1053
- BTCUSD: 1741
- CADCHF: 1102
- CADJPY: 1100
- CHFJPY: 1100
- DOGEUSD: 1543
- DOTUSD: 1543
- ETHUSD: 1741
- EU50: 414
- EURAUD: 1100
- EURCAD: 1239
- EURCHF: 1100
- EURGBP: 1101
- EURJPY: 1100
- EURUSD: 1100
- FRA40: 414
- GBPAUD: 1101
- GBPCAD: 1101
- GBPCHF: 1101
- GBPJPY: 1100
- GBPUSD: 1101
- GER40: 414
- GOLD: 1176
- HK50: 308
- JPN225: 287
- LINKUSD: 1543
- LTCUSD: 1543
- NAS100: 322
- NATGAS: 1058
- NZDCAD: 1101
- NZDCHF: 1101
- NZDJPY: 1100
- NZDUSD: 1101
- SILVER: 1054
- SOLUSD: 1543
- UK100: 414
- US30: 322
- US500: 358
- USDCAD: 1102
- USDCHF: 1096
- USDJPY: 1232
- WTI: 1054
- XRPUSD: 1543

## 6. MR candidates / resolved
- 1382 candidates, 0 resolved

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