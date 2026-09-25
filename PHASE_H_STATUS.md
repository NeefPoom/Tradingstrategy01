# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-25T20:30:19.506477

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
26

## 5. Observation count by asset
- ADAUSD: 435
- AUDCAD: 337
- AUDCHF: 337
- AUDJPY: 337
- AUDNZD: 337
- AUDUSD: 337
- AUS200: 98
- AVAXUSD: 435
- BCHUSD: 435
- BNBUSD: 435
- BRENT: 315
- BTCUSD: 633
- CADCHF: 337
- CADJPY: 337
- CHFJPY: 337
- DOGEUSD: 435
- DOTUSD: 435
- ETHUSD: 633
- EU50: 126
- EURAUD: 337
- EURCAD: 475
- EURCHF: 337
- EURGBP: 337
- EURJPY: 337
- EURUSD: 337
- FRA40: 126
- GBPAUD: 337
- GBPCAD: 337
- GBPCHF: 337
- GBPJPY: 337
- GBPUSD: 337
- GER40: 126
- GOLD: 435
- HK50: 98
- JPN225: 77
- LINKUSD: 435
- LTCUSD: 435
- NAS100: 97
- NATGAS: 316
- NZDCAD: 337
- NZDCHF: 337
- NZDJPY: 337
- NZDUSD: 337
- SILVER: 316
- SOLUSD: 435
- UK100: 126
- US30: 97
- US500: 133
- USDCAD: 337
- USDCHF: 336
- USDJPY: 473
- WTI: 315
- XRPUSD: 435

## 6. MR candidates / resolved
- 309 candidates, 0 resolved

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