# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-24T19:23:00.142102

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
86

## 5. Observation count by asset
- ADAUSD: 1874
- AUDCAD: 1334
- AUDCHF: 1334
- AUDJPY: 1332
- AUDNZD: 1334
- AUDUSD: 1333
- AUS200: 392
- AVAXUSD: 1874
- BCHUSD: 1874
- BNBUSD: 1874
- BRENT: 1279
- BTCUSD: 2071
- CADCHF: 1337
- CADJPY: 1333
- CHFJPY: 1333
- DOGEUSD: 1874
- DOTUSD: 1874
- ETHUSD: 2071
- EU50: 504
- EURAUD: 1333
- EURCAD: 1471
- EURCHF: 1333
- EURGBP: 1334
- EURJPY: 1331
- EURUSD: 1332
- FRA40: 504
- GBPAUD: 1334
- GBPCAD: 1334
- GBPCHF: 1334
- GBPJPY: 1332
- GBPUSD: 1333
- GER40: 504
- GOLD: 1403
- HK50: 378
- JPN225: 350
- LINKUSD: 1874
- LTCUSD: 1874
- NAS100: 389
- NATGAS: 1284
- NZDCAD: 1334
- NZDCHF: 1334
- NZDJPY: 1333
- NZDUSD: 1333
- SILVER: 1281
- SOLUSD: 1874
- UK100: 504
- US30: 389
- US500: 425
- USDCAD: 1334
- USDCHF: 1328
- USDJPY: 1462
- WTI: 1283
- XRPUSD: 1874

## 6. MR candidates / resolved
- 1649 candidates, 0 resolved

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