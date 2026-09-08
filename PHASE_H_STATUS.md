# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-08T15:35:31.082249

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
9

## 5. Observation count by asset
- ADAUSD: 22
- AUDCAD: 22
- AUDCHF: 22
- AUDJPY: 21
- AUDNZD: 22
- AUDUSD: 22
- AUS200: 7
- AVAXUSD: 22
- BCHUSD: 22
- BNBUSD: 22
- BRENT: 11
- BTCUSD: 220
- CADCHF: 22
- CADJPY: 22
- CHFJPY: 22
- DOGEUSD: 22
- DOTUSD: 22
- ETHUSD: 220
- EU50: 8
- EURAUD: 22
- EURCAD: 160
- EURCHF: 22
- EURGBP: 22
- EURJPY: 22
- EURUSD: 22
- FRA40: 8
- GBPAUD: 22
- GBPCAD: 22
- GBPCHF: 22
- GBPJPY: 22
- GBPUSD: 22
- GER40: 8
- GOLD: 130
- HK50: 7
- JPN225: 7
- LINKUSD: 22
- LTCUSD: 22
- NAS100: 2
- NATGAS: 11
- NZDCAD: 22
- NZDCHF: 22
- NZDJPY: 22
- NZDUSD: 22
- SILVER: 11
- SOLUSD: 22
- UK100: 8
- US30: 2
- US500: 38
- USDCAD: 22
- USDCHF: 22
- USDJPY: 159
- WTI: 11
- XRPUSD: 22

## 6. MR candidates / resolved
- 20 candidates, 0 resolved

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