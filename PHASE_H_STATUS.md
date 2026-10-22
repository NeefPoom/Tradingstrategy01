# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-22T06:16:18.179508

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
52

## 5. Observation count by asset
- ADAUSD: 1069
- AUDCAD: 775
- AUDCHF: 775
- AUDJPY: 775
- AUDNZD: 775
- AUDUSD: 775
- AUS200: 231
- AVAXUSD: 1069
- BCHUSD: 1069
- BNBUSD: 1069
- BRENT: 737
- BTCUSD: 1267
- CADCHF: 775
- CADJPY: 775
- CHFJPY: 775
- DOGEUSD: 1069
- DOTUSD: 1069
- ETHUSD: 1267
- EU50: 288
- EURAUD: 775
- EURCAD: 913
- EURCHF: 775
- EURGBP: 776
- EURJPY: 775
- EURUSD: 775
- FRA40: 288
- GBPAUD: 775
- GBPCAD: 775
- GBPCHF: 775
- GBPJPY: 775
- GBPUSD: 776
- GER40: 288
- GOLD: 859
- HK50: 214
- JPN225: 202
- LINKUSD: 1069
- LTCUSD: 1069
- NAS100: 224
- NATGAS: 741
- NZDCAD: 775
- NZDCHF: 775
- NZDJPY: 775
- NZDUSD: 775
- SILVER: 738
- SOLUSD: 1069
- UK100: 288
- US30: 224
- US500: 260
- USDCAD: 775
- USDCHF: 770
- USDJPY: 909
- WTI: 738
- XRPUSD: 1069

## 6. MR candidates / resolved
- 934 candidates, 0 resolved

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