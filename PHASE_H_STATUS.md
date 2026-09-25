# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-25T06:14:40.874196

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
25

## 5. Observation count by asset
- ADAUSD: 421
- AUDCAD: 323
- AUDCHF: 323
- AUDJPY: 323
- AUDNZD: 323
- AUDUSD: 323
- AUS200: 97
- AVAXUSD: 421
- BCHUSD: 421
- BNBUSD: 421
- BRENT: 299
- BTCUSD: 619
- CADCHF: 323
- CADJPY: 323
- CHFJPY: 323
- DOGEUSD: 421
- DOTUSD: 421
- ETHUSD: 619
- EU50: 117
- EURAUD: 323
- EURCAD: 461
- EURCHF: 323
- EURGBP: 323
- EURJPY: 323
- EURUSD: 323
- FRA40: 117
- GBPAUD: 323
- GBPCAD: 323
- GBPCHF: 323
- GBPJPY: 323
- GBPUSD: 323
- GER40: 117
- GOLD: 419
- HK50: 95
- JPN225: 76
- LINKUSD: 421
- LTCUSD: 421
- NAS100: 91
- NATGAS: 300
- NZDCAD: 323
- NZDCHF: 323
- NZDJPY: 323
- NZDUSD: 323
- SILVER: 300
- SOLUSD: 421
- UK100: 117
- US30: 91
- US500: 127
- USDCAD: 323
- USDCHF: 322
- USDJPY: 459
- WTI: 299
- XRPUSD: 421

## 6. MR candidates / resolved
- 301 candidates, 0 resolved

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