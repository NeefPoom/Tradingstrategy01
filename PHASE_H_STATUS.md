# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-10T09:49:20.911449

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
40

## 5. Observation count by asset
- ADAUSD: 784
- AUDCAD: 577
- AUDCHF: 577
- AUDJPY: 577
- AUDNZD: 577
- AUDUSD: 577
- AUS200: 168
- AVAXUSD: 784
- BCHUSD: 784
- BNBUSD: 784
- BRENT: 546
- BTCUSD: 982
- CADCHF: 577
- CADJPY: 577
- CHFJPY: 577
- DOGEUSD: 784
- DOTUSD: 784
- ETHUSD: 982
- EU50: 216
- EURAUD: 577
- EURCAD: 715
- EURCHF: 577
- EURGBP: 578
- EURJPY: 577
- EURUSD: 577
- FRA40: 216
- GBPAUD: 577
- GBPCAD: 577
- GBPCHF: 577
- GBPJPY: 577
- GBPUSD: 577
- GER40: 216
- GOLD: 667
- HK50: 161
- JPN225: 147
- LINKUSD: 784
- LTCUSD: 784
- NAS100: 168
- NATGAS: 549
- NZDCAD: 577
- NZDCHF: 577
- NZDJPY: 577
- NZDUSD: 577
- SILVER: 547
- SOLUSD: 784
- UK100: 216
- US30: 168
- US500: 204
- USDCAD: 577
- USDCHF: 573
- USDJPY: 712
- WTI: 547
- XRPUSD: 784

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