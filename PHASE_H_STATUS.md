# Phase H Status - Frozen Forward Validation

**Generated:** 2026-11-04T11:48:32.083303

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
66

## 5. Observation count by asset
- ADAUSD: 1386
- AUDCAD: 993
- AUDCHF: 993
- AUDJPY: 992
- AUDNZD: 993
- AUDUSD: 993
- AUS200: 294
- AVAXUSD: 1386
- BCHUSD: 1386
- BNBUSD: 1386
- BRENT: 949
- BTCUSD: 1584
- CADCHF: 993
- CADJPY: 992
- CHFJPY: 992
- DOGEUSD: 1386
- DOTUSD: 1386
- ETHUSD: 1584
- EU50: 372
- EURAUD: 992
- EURCAD: 1131
- EURCHF: 992
- EURGBP: 993
- EURJPY: 992
- EURUSD: 992
- FRA40: 372
- GBPAUD: 993
- GBPCAD: 993
- GBPCHF: 993
- GBPJPY: 992
- GBPUSD: 993
- GER40: 372
- GOLD: 1071
- HK50: 280
- JPN225: 259
- LINKUSD: 1386
- LTCUSD: 1386
- NAS100: 287
- NATGAS: 954
- NZDCAD: 993
- NZDCHF: 993
- NZDJPY: 992
- NZDUSD: 993
- SILVER: 950
- SOLUSD: 1386
- UK100: 372
- US30: 287
- US500: 323
- USDCAD: 994
- USDCHF: 988
- USDJPY: 1124
- WTI: 950
- XRPUSD: 1386

## 6. MR candidates / resolved
- 1240 candidates, 0 resolved

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