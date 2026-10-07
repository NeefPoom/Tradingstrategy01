# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-07T23:53:46.058596

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
38

## 5. Observation count by asset
- ADAUSD: 726
- AUDCAD: 530
- AUDCHF: 530
- AUDJPY: 530
- AUDNZD: 530
- AUDUSD: 530
- AUS200: 154
- AVAXUSD: 726
- BCHUSD: 726
- BNBUSD: 726
- BRENT: 501
- BTCUSD: 924
- CADCHF: 530
- CADJPY: 530
- CHFJPY: 530
- DOGEUSD: 726
- DOTUSD: 726
- ETHUSD: 924
- EU50: 198
- EURAUD: 530
- EURCAD: 668
- EURCHF: 530
- EURGBP: 530
- EURJPY: 530
- EURUSD: 530
- FRA40: 198
- GBPAUD: 530
- GBPCAD: 530
- GBPCHF: 530
- GBPJPY: 530
- GBPUSD: 530
- GER40: 198
- GOLD: 622
- HK50: 147
- JPN225: 133
- LINKUSD: 726
- LTCUSD: 726
- NAS100: 154
- NATGAS: 502
- NZDCAD: 530
- NZDCHF: 530
- NZDJPY: 530
- NZDUSD: 530
- SILVER: 502
- SOLUSD: 726
- UK100: 198
- US30: 154
- US500: 190
- USDCAD: 530
- USDCHF: 527
- USDJPY: 666
- WTI: 502
- XRPUSD: 726

## 6. MR candidates / resolved
- 563 candidates, 0 resolved

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