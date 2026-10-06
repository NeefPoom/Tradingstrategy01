# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-06T07:42:46.406168

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
36

## 5. Observation count by asset
- ADAUSD: 686
- AUDCAD: 490
- AUDCHF: 490
- AUDJPY: 490
- AUDNZD: 490
- AUDUSD: 490
- AUS200: 147
- AVAXUSD: 686
- BCHUSD: 686
- BNBUSD: 686
- BRENT: 463
- BTCUSD: 884
- CADCHF: 490
- CADJPY: 490
- CHFJPY: 490
- DOGEUSD: 686
- DOTUSD: 686
- ETHUSD: 884
- EU50: 180
- EURAUD: 490
- EURCAD: 628
- EURCHF: 490
- EURGBP: 490
- EURJPY: 490
- EURUSD: 490
- FRA40: 180
- GBPAUD: 490
- GBPCAD: 490
- GBPCHF: 490
- GBPJPY: 490
- GBPUSD: 490
- GER40: 180
- GOLD: 584
- HK50: 139
- JPN225: 126
- LINKUSD: 686
- LTCUSD: 686
- NAS100: 140
- NATGAS: 464
- NZDCAD: 490
- NZDCHF: 490
- NZDJPY: 490
- NZDUSD: 490
- SILVER: 464
- SOLUSD: 686
- UK100: 180
- US30: 140
- US500: 176
- USDCAD: 490
- USDCHF: 487
- USDJPY: 626
- WTI: 464
- XRPUSD: 686

## 6. MR candidates / resolved
- 528 candidates, 0 resolved

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