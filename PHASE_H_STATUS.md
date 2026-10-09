# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-09T19:09:07.228916

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
40

## 5. Observation count by asset
- ADAUSD: 770
- AUDCAD: 574
- AUDCHF: 574
- AUDJPY: 574
- AUDNZD: 574
- AUDUSD: 574
- AUS200: 168
- AVAXUSD: 770
- BCHUSD: 770
- BNBUSD: 770
- BRENT: 544
- BTCUSD: 967
- CADCHF: 574
- CADJPY: 574
- CHFJPY: 574
- DOGEUSD: 770
- DOTUSD: 770
- ETHUSD: 967
- EU50: 216
- EURAUD: 574
- EURCAD: 712
- EURCHF: 574
- EURGBP: 574
- EURJPY: 574
- EURUSD: 574
- FRA40: 216
- GBPAUD: 574
- GBPCAD: 574
- GBPCHF: 574
- GBPJPY: 574
- GBPUSD: 574
- GER40: 216
- GOLD: 664
- HK50: 161
- JPN225: 147
- LINKUSD: 770
- LTCUSD: 770
- NAS100: 166
- NATGAS: 546
- NZDCAD: 574
- NZDCHF: 574
- NZDJPY: 574
- NZDUSD: 574
- SILVER: 545
- SOLUSD: 770
- UK100: 216
- US30: 166
- US500: 202
- USDCAD: 574
- USDCHF: 571
- USDJPY: 709
- WTI: 545
- XRPUSD: 770

## 6. MR candidates / resolved
- 635 candidates, 0 resolved

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