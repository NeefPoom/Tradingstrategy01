# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-12T05:58:09.923650

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
42

## 5. Observation count by asset
- ADAUSD: 828
- AUDCAD: 583
- AUDCHF: 583
- AUDJPY: 583
- AUDNZD: 583
- AUDUSD: 583
- AUS200: 174
- AVAXUSD: 828
- BCHUSD: 828
- BNBUSD: 828
- BRENT: 553
- BTCUSD: 1026
- CADCHF: 583
- CADJPY: 583
- CHFJPY: 583
- DOGEUSD: 828
- DOTUSD: 828
- ETHUSD: 1026
- EU50: 216
- EURAUD: 583
- EURCAD: 721
- EURCHF: 583
- EURGBP: 584
- EURJPY: 583
- EURUSD: 583
- FRA40: 216
- GBPAUD: 583
- GBPCAD: 583
- GBPCHF: 583
- GBPJPY: 583
- GBPUSD: 583
- GER40: 216
- GOLD: 674
- HK50: 165
- JPN225: 147
- LINKUSD: 828
- LTCUSD: 828
- NAS100: 168
- NATGAS: 556
- NZDCAD: 583
- NZDCHF: 583
- NZDJPY: 583
- NZDUSD: 583
- SILVER: 554
- SOLUSD: 828
- UK100: 216
- US30: 168
- US500: 204
- USDCAD: 583
- USDCHF: 579
- USDJPY: 718
- WTI: 554
- XRPUSD: 828

## 6. MR candidates / resolved
- 646 candidates, 0 resolved

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