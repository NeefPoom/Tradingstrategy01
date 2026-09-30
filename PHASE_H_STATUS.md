# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-30T20:22:26.937861

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
31

## 5. Observation count by asset
- ADAUSD: 555
- AUDCAD: 408
- AUDCHF: 408
- AUDJPY: 408
- AUDNZD: 408
- AUDUSD: 408
- AUS200: 119
- AVAXUSD: 555
- BCHUSD: 555
- BNBUSD: 555
- BRENT: 384
- BTCUSD: 753
- CADCHF: 408
- CADJPY: 408
- CHFJPY: 408
- DOGEUSD: 555
- DOTUSD: 555
- ETHUSD: 753
- EU50: 153
- EURAUD: 408
- EURCAD: 546
- EURCHF: 408
- EURGBP: 408
- EURJPY: 408
- EURUSD: 408
- FRA40: 153
- GBPAUD: 408
- GBPCAD: 408
- GBPCHF: 408
- GBPJPY: 408
- GBPUSD: 408
- GER40: 153
- GOLD: 504
- HK50: 119
- JPN225: 98
- LINKUSD: 555
- LTCUSD: 555
- NAS100: 118
- NATGAS: 385
- NZDCAD: 408
- NZDCHF: 408
- NZDJPY: 408
- NZDUSD: 408
- SILVER: 385
- SOLUSD: 555
- UK100: 153
- US30: 118
- US500: 154
- USDCAD: 408
- USDCHF: 406
- USDJPY: 544
- WTI: 384
- XRPUSD: 555

## 6. MR candidates / resolved
- 411 candidates, 0 resolved

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