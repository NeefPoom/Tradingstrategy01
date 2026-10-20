# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-20T20:39:47.581792

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
51

## 5. Observation count by asset
- ADAUSD: 1035
- AUDCAD: 741
- AUDCHF: 741
- AUDJPY: 741
- AUDNZD: 741
- AUDUSD: 741
- AUS200: 217
- AVAXUSD: 1035
- BCHUSD: 1035
- BNBUSD: 1035
- BRENT: 706
- BTCUSD: 1233
- CADCHF: 741
- CADJPY: 741
- CHFJPY: 741
- DOGEUSD: 1035
- DOTUSD: 1035
- ETHUSD: 1233
- EU50: 279
- EURAUD: 741
- EURCAD: 879
- EURCHF: 741
- EURGBP: 742
- EURJPY: 741
- EURUSD: 741
- FRA40: 279
- GBPAUD: 741
- GBPCAD: 741
- GBPCHF: 741
- GBPJPY: 741
- GBPUSD: 742
- GER40: 279
- GOLD: 828
- HK50: 203
- JPN225: 189
- LINKUSD: 1035
- LTCUSD: 1035
- NAS100: 217
- NATGAS: 710
- NZDCAD: 741
- NZDCHF: 741
- NZDJPY: 741
- NZDUSD: 741
- SILVER: 707
- SOLUSD: 1035
- UK100: 279
- US30: 217
- US500: 253
- USDCAD: 741
- USDCHF: 736
- USDJPY: 875
- WTI: 707
- XRPUSD: 1035

## 6. MR candidates / resolved
- 887 candidates, 0 resolved

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