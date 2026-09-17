# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-17T22:29:10.439387

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
18

## 5. Observation count by asset
- ADAUSD: 245
- AUDCAD: 196
- AUDCHF: 196
- AUDJPY: 196
- AUDNZD: 196
- AUDUSD: 196
- AUS200: 56
- AVAXUSD: 245
- BCHUSD: 245
- BNBUSD: 245
- BRENT: 178
- BTCUSD: 443
- CADCHF: 196
- CADJPY: 196
- CHFJPY: 196
- DOGEUSD: 245
- DOTUSD: 245
- ETHUSD: 443
- EU50: 72
- EURAUD: 196
- EURCAD: 334
- EURCHF: 196
- EURGBP: 196
- EURJPY: 196
- EURUSD: 196
- FRA40: 72
- GBPAUD: 196
- GBPCAD: 196
- GBPCHF: 196
- GBPJPY: 196
- GBPUSD: 196
- GER40: 72
- GOLD: 297
- HK50: 56
- JPN225: 56
- LINKUSD: 245
- LTCUSD: 245
- NAS100: 56
- NATGAS: 178
- NZDCAD: 196
- NZDCHF: 196
- NZDJPY: 196
- NZDUSD: 196
- SILVER: 178
- SOLUSD: 245
- UK100: 72
- US30: 56
- US500: 92
- USDCAD: 196
- USDCHF: 196
- USDJPY: 332
- WTI: 178
- XRPUSD: 245

## 6. MR candidates / resolved
- 152 candidates, 0 resolved

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