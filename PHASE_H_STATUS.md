# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-20T17:02:02.266126

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
51

## 5. Observation count by asset
- ADAUSD: 1031
- AUDCAD: 737
- AUDCHF: 737
- AUDJPY: 737
- AUDNZD: 737
- AUDUSD: 737
- AUS200: 217
- AVAXUSD: 1032
- BCHUSD: 1032
- BNBUSD: 1032
- BRENT: 702
- BTCUSD: 1229
- CADCHF: 737
- CADJPY: 737
- CHFJPY: 737
- DOGEUSD: 1031
- DOTUSD: 1032
- ETHUSD: 1229
- EU50: 279
- EURAUD: 737
- EURCAD: 875
- EURCHF: 737
- EURGBP: 738
- EURJPY: 737
- EURUSD: 737
- FRA40: 279
- GBPAUD: 737
- GBPCAD: 737
- GBPCHF: 737
- GBPJPY: 737
- GBPUSD: 738
- GER40: 279
- GOLD: 824
- HK50: 203
- JPN225: 189
- LINKUSD: 1032
- LTCUSD: 1032
- NAS100: 213
- NATGAS: 706
- NZDCAD: 737
- NZDCHF: 737
- NZDJPY: 737
- NZDUSD: 737
- SILVER: 703
- SOLUSD: 1031
- UK100: 279
- US30: 213
- US500: 249
- USDCAD: 737
- USDCHF: 732
- USDJPY: 871
- WTI: 703
- XRPUSD: 1031

## 6. MR candidates / resolved
- 885 candidates, 0 resolved

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