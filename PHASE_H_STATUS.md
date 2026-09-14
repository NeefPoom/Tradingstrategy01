# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-14T04:54:28.723449

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
14

## 5. Observation count by asset
- ADAUSD: 155
- AUDCAD: 106
- AUDCHF: 106
- AUDJPY: 106
- AUDNZD: 106
- AUDUSD: 106
- AUS200: 32
- AVAXUSD: 155
- BCHUSD: 155
- BNBUSD: 155
- BRENT: 91
- BTCUSD: 353
- CADCHF: 106
- CADJPY: 106
- CHFJPY: 106
- DOGEUSD: 155
- DOTUSD: 155
- ETHUSD: 353
- EU50: 36
- EURAUD: 106
- EURCAD: 244
- EURCHF: 106
- EURGBP: 106
- EURJPY: 106
- EURUSD: 106
- FRA40: 36
- GBPAUD: 106
- GBPCAD: 106
- GBPCHF: 106
- GBPJPY: 106
- GBPUSD: 106
- GER40: 36
- GOLD: 210
- HK50: 31
- JPN225: 32
- LINKUSD: 155
- LTCUSD: 155
- NAS100: 28
- NATGAS: 91
- NZDCAD: 106
- NZDCHF: 106
- NZDJPY: 106
- NZDUSD: 106
- SILVER: 91
- SOLUSD: 155
- UK100: 36
- US30: 28
- US500: 64
- USDCAD: 106
- USDCHF: 106
- USDJPY: 242
- WTI: 91
- XRPUSD: 155

## 6. MR candidates / resolved
- 27 candidates, 0 resolved

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