# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-16T14:53:00.317506

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
47

## 5. Observation count by asset
- ADAUSD: 933
- AUDCAD: 688
- AUDCHF: 688
- AUDJPY: 688
- AUDNZD: 688
- AUDUSD: 688
- AUS200: 203
- AVAXUSD: 933
- BCHUSD: 933
- BNBUSD: 933
- BRENT: 654
- BTCUSD: 1131
- CADCHF: 688
- CADJPY: 688
- CHFJPY: 688
- DOGEUSD: 933
- DOTUSD: 933
- ETHUSD: 1131
- EU50: 259
- EURAUD: 688
- EURCAD: 826
- EURCHF: 688
- EURGBP: 689
- EURJPY: 688
- EURUSD: 688
- FRA40: 259
- GBPAUD: 688
- GBPCAD: 688
- GBPCHF: 688
- GBPJPY: 688
- GBPUSD: 688
- GER40: 259
- GOLD: 776
- HK50: 196
- JPN225: 175
- LINKUSD: 933
- LTCUSD: 933
- NAS100: 197
- NATGAS: 658
- NZDCAD: 688
- NZDCHF: 688
- NZDJPY: 688
- NZDUSD: 688
- SILVER: 655
- SOLUSD: 933
- UK100: 259
- US30: 197
- US500: 233
- USDCAD: 688
- USDCHF: 684
- USDJPY: 823
- WTI: 655
- XRPUSD: 933

## 6. MR candidates / resolved
- 796 candidates, 0 resolved

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