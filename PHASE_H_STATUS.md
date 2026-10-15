# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-15T18:42:32.818224

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
46

## 5. Observation count by asset
- ADAUSD: 913
- AUDCAD: 668
- AUDCHF: 668
- AUDJPY: 668
- AUDNZD: 668
- AUDUSD: 668
- AUS200: 196
- AVAXUSD: 913
- BCHUSD: 913
- BNBUSD: 913
- BRENT: 635
- BTCUSD: 1111
- CADCHF: 668
- CADJPY: 668
- CHFJPY: 668
- DOGEUSD: 913
- DOTUSD: 913
- ETHUSD: 1111
- EU50: 252
- EURAUD: 668
- EURCAD: 806
- EURCHF: 668
- EURGBP: 669
- EURJPY: 668
- EURUSD: 668
- FRA40: 252
- GBPAUD: 668
- GBPCAD: 668
- GBPCHF: 668
- GBPJPY: 668
- GBPUSD: 668
- GER40: 252
- GOLD: 757
- HK50: 189
- JPN225: 168
- LINKUSD: 913
- LTCUSD: 913
- NAS100: 194
- NATGAS: 639
- NZDCAD: 668
- NZDCHF: 668
- NZDJPY: 668
- NZDUSD: 668
- SILVER: 636
- SOLUSD: 913
- UK100: 252
- US30: 194
- US500: 230
- USDCAD: 668
- USDCHF: 664
- USDJPY: 803
- WTI: 636
- XRPUSD: 913

## 6. MR candidates / resolved
- 774 candidates, 0 resolved

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