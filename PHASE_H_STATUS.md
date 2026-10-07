# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-07T13:25:22.871055

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
38

## 5. Observation count by asset
- ADAUSD: 716
- AUDCAD: 520
- AUDCHF: 520
- AUDJPY: 520
- AUDNZD: 520
- AUDUSD: 520
- AUS200: 154
- AVAXUSD: 716
- BCHUSD: 716
- BNBUSD: 716
- BRENT: 492
- BTCUSD: 914
- CADCHF: 520
- CADJPY: 520
- CHFJPY: 520
- DOGEUSD: 716
- DOTUSD: 716
- ETHUSD: 914
- EU50: 195
- EURAUD: 520
- EURCAD: 658
- EURCHF: 520
- EURGBP: 520
- EURJPY: 520
- EURUSD: 520
- FRA40: 195
- GBPAUD: 520
- GBPCAD: 520
- GBPCHF: 520
- GBPJPY: 520
- GBPUSD: 520
- GER40: 195
- GOLD: 613
- HK50: 147
- JPN225: 133
- LINKUSD: 716
- LTCUSD: 716
- NAS100: 147
- NATGAS: 493
- NZDCAD: 520
- NZDCHF: 520
- NZDJPY: 520
- NZDUSD: 520
- SILVER: 493
- SOLUSD: 716
- UK100: 195
- US30: 147
- US500: 183
- USDCAD: 520
- USDCHF: 517
- USDJPY: 656
- WTI: 493
- XRPUSD: 716

## 6. MR candidates / resolved
- 559 candidates, 0 resolved

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