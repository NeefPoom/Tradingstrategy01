# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-01T00:16:11.046943

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
31

## 5. Observation count by asset
- ADAUSD: 559
- AUDCAD: 412
- AUDCHF: 412
- AUDJPY: 412
- AUDNZD: 412
- AUDUSD: 412
- AUS200: 119
- AVAXUSD: 559
- BCHUSD: 559
- BNBUSD: 559
- BRENT: 387
- BTCUSD: 757
- CADCHF: 412
- CADJPY: 412
- CHFJPY: 412
- DOGEUSD: 559
- DOTUSD: 559
- ETHUSD: 757
- EU50: 153
- EURAUD: 412
- EURCAD: 550
- EURCHF: 412
- EURGBP: 412
- EURJPY: 412
- EURUSD: 412
- FRA40: 153
- GBPAUD: 412
- GBPCAD: 412
- GBPCHF: 412
- GBPJPY: 412
- GBPUSD: 412
- GER40: 153
- GOLD: 507
- HK50: 119
- JPN225: 98
- LINKUSD: 559
- LTCUSD: 559
- NAS100: 119
- NATGAS: 388
- NZDCAD: 412
- NZDCHF: 412
- NZDJPY: 412
- NZDUSD: 412
- SILVER: 388
- SOLUSD: 559
- UK100: 153
- US30: 119
- US500: 155
- USDCAD: 412
- USDCHF: 410
- USDJPY: 548
- WTI: 387
- XRPUSD: 559

## 6. MR candidates / resolved
- 414 candidates, 0 resolved

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