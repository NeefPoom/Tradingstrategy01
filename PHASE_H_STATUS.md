# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-25T00:50:32.880917

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
25

## 5. Observation count by asset
- ADAUSD: 414
- AUDCAD: 317
- AUDCHF: 317
- AUDJPY: 317
- AUDNZD: 317
- AUDUSD: 317
- AUS200: 91
- AVAXUSD: 414
- BCHUSD: 414
- BNBUSD: 414
- BRENT: 295
- BTCUSD: 612
- CADCHF: 317
- CADJPY: 317
- CHFJPY: 317
- DOGEUSD: 414
- DOTUSD: 414
- ETHUSD: 612
- EU50: 117
- EURAUD: 317
- EURCAD: 455
- EURCHF: 317
- EURGBP: 317
- EURJPY: 317
- EURUSD: 317
- FRA40: 117
- GBPAUD: 317
- GBPCAD: 317
- GBPCHF: 317
- GBPJPY: 317
- GBPUSD: 317
- GER40: 117
- GOLD: 415
- HK50: 91
- JPN225: 70
- LINKUSD: 414
- LTCUSD: 414
- NAS100: 91
- NATGAS: 296
- NZDCAD: 317
- NZDCHF: 317
- NZDJPY: 317
- NZDUSD: 317
- SILVER: 296
- SOLUSD: 414
- UK100: 117
- US30: 91
- US500: 127
- USDCAD: 317
- USDCHF: 316
- USDJPY: 453
- WTI: 295
- XRPUSD: 414

## 6. MR candidates / resolved
- 293 candidates, 0 resolved

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