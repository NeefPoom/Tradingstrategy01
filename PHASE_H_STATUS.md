# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-25T11:54:14.652569

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
26

## 5. Observation count by asset
- ADAUSD: 426
- AUDCAD: 328
- AUDCHF: 328
- AUDJPY: 328
- AUDNZD: 328
- AUDUSD: 328
- AUS200: 98
- AVAXUSD: 426
- BCHUSD: 426
- BNBUSD: 426
- BRENT: 306
- BTCUSD: 624
- CADCHF: 328
- CADJPY: 328
- CHFJPY: 328
- DOGEUSD: 426
- DOTUSD: 426
- ETHUSD: 624
- EU50: 121
- EURAUD: 328
- EURCAD: 466
- EURCHF: 328
- EURGBP: 328
- EURJPY: 328
- EURUSD: 328
- FRA40: 121
- GBPAUD: 328
- GBPCAD: 328
- GBPCHF: 328
- GBPJPY: 328
- GBPUSD: 328
- GER40: 121
- GOLD: 426
- HK50: 98
- JPN225: 77
- LINKUSD: 426
- LTCUSD: 426
- NAS100: 91
- NATGAS: 307
- NZDCAD: 328
- NZDCHF: 328
- NZDJPY: 328
- NZDUSD: 328
- SILVER: 307
- SOLUSD: 426
- UK100: 121
- US30: 91
- US500: 127
- USDCAD: 328
- USDCHF: 327
- USDJPY: 464
- WTI: 306
- XRPUSD: 426

## 6. MR candidates / resolved
- 305 candidates, 0 resolved

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