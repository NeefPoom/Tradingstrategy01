# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-18T18:25:43.873611

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
19

## 5. Observation count by asset
- ADAUSD: 265
- AUDCAD: 216
- AUDCHF: 216
- AUDJPY: 216
- AUDNZD: 216
- AUDUSD: 216
- AUS200: 63
- AVAXUSD: 265
- BCHUSD: 265
- BNBUSD: 265
- BRENT: 198
- BTCUSD: 463
- CADCHF: 216
- CADJPY: 216
- CHFJPY: 216
- DOGEUSD: 265
- DOTUSD: 265
- ETHUSD: 463
- EU50: 81
- EURAUD: 216
- EURCAD: 354
- EURCHF: 216
- EURGBP: 216
- EURJPY: 216
- EURUSD: 216
- FRA40: 81
- GBPAUD: 216
- GBPCAD: 216
- GBPCHF: 216
- GBPJPY: 216
- GBPUSD: 216
- GER40: 81
- GOLD: 317
- HK50: 63
- JPN225: 63
- LINKUSD: 265
- LTCUSD: 265
- NAS100: 60
- NATGAS: 198
- NZDCAD: 216
- NZDCHF: 216
- NZDJPY: 216
- NZDUSD: 216
- SILVER: 198
- SOLUSD: 265
- UK100: 81
- US30: 60
- US500: 96
- USDCAD: 216
- USDCHF: 216
- USDJPY: 352
- WTI: 198
- XRPUSD: 265

## 6. MR candidates / resolved
- 169 candidates, 0 resolved

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