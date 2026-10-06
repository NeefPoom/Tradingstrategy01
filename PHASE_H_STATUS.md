# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-06T14:34:07.777431

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
37

## 5. Observation count by asset
- ADAUSD: 693
- AUDCAD: 497
- AUDCHF: 497
- AUDJPY: 497
- AUDNZD: 497
- AUDUSD: 497
- AUS200: 147
- AVAXUSD: 693
- BCHUSD: 693
- BNBUSD: 693
- BRENT: 470
- BTCUSD: 891
- CADCHF: 497
- CADJPY: 497
- CHFJPY: 497
- DOGEUSD: 693
- DOTUSD: 693
- ETHUSD: 891
- EU50: 187
- EURAUD: 497
- EURCAD: 635
- EURCHF: 497
- EURGBP: 497
- EURJPY: 497
- EURUSD: 497
- FRA40: 187
- GBPAUD: 497
- GBPCAD: 497
- GBPCHF: 497
- GBPJPY: 497
- GBPUSD: 497
- GER40: 187
- GOLD: 591
- HK50: 140
- JPN225: 126
- LINKUSD: 693
- LTCUSD: 693
- NAS100: 141
- NATGAS: 471
- NZDCAD: 497
- NZDCHF: 497
- NZDJPY: 497
- NZDUSD: 497
- SILVER: 471
- SOLUSD: 693
- UK100: 187
- US30: 141
- US500: 176
- USDCAD: 497
- USDCHF: 494
- USDJPY: 633
- WTI: 471
- XRPUSD: 693

## 6. MR candidates / resolved
- 534 candidates, 0 resolved

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