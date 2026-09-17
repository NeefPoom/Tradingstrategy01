# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-17T19:19:35.444265

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
18

## 5. Observation count by asset
- ADAUSD: 242
- AUDCAD: 193
- AUDCHF: 193
- AUDJPY: 193
- AUDNZD: 193
- AUDUSD: 193
- AUS200: 56
- AVAXUSD: 242
- BCHUSD: 242
- BNBUSD: 242
- BRENT: 176
- BTCUSD: 440
- CADCHF: 193
- CADJPY: 193
- CHFJPY: 193
- DOGEUSD: 242
- DOTUSD: 242
- ETHUSD: 440
- EU50: 72
- EURAUD: 193
- EURCAD: 331
- EURCHF: 193
- EURGBP: 193
- EURJPY: 193
- EURUSD: 193
- FRA40: 72
- GBPAUD: 193
- GBPCAD: 193
- GBPCHF: 193
- GBPJPY: 193
- GBPUSD: 193
- GER40: 72
- GOLD: 295
- HK50: 56
- JPN225: 56
- LINKUSD: 242
- LTCUSD: 242
- NAS100: 54
- NATGAS: 176
- NZDCAD: 193
- NZDCHF: 193
- NZDJPY: 193
- NZDUSD: 193
- SILVER: 176
- SOLUSD: 242
- UK100: 72
- US30: 54
- US500: 90
- USDCAD: 193
- USDCHF: 193
- USDJPY: 329
- WTI: 176
- XRPUSD: 242

## 6. MR candidates / resolved
- 148 candidates, 0 resolved

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