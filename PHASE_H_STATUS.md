# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-27T00:27:59.716420

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
57

## 5. Observation count by asset
- ADAUSD: 1182
- AUDCAD: 837
- AUDCHF: 837
- AUDJPY: 837
- AUDNZD: 837
- AUDUSD: 837
- AUS200: 246
- AVAXUSD: 1182
- BCHUSD: 1182
- BNBUSD: 1182
- BRENT: 801
- BTCUSD: 1380
- CADCHF: 837
- CADJPY: 837
- CHFJPY: 837
- DOGEUSD: 1182
- DOTUSD: 1182
- ETHUSD: 1380
- EU50: 315
- EURAUD: 837
- EURCAD: 975
- EURCHF: 837
- EURGBP: 838
- EURJPY: 837
- EURUSD: 837
- FRA40: 315
- GBPAUD: 837
- GBPCAD: 837
- GBPCHF: 837
- GBPJPY: 837
- GBPUSD: 838
- GER40: 315
- GOLD: 923
- HK50: 231
- JPN225: 217
- LINKUSD: 1182
- LTCUSD: 1182
- NAS100: 245
- NATGAS: 806
- NZDCAD: 837
- NZDCHF: 837
- NZDJPY: 837
- NZDUSD: 837
- SILVER: 802
- SOLUSD: 1182
- UK100: 315
- US30: 245
- US500: 281
- USDCAD: 837
- USDCHF: 832
- USDJPY: 970
- WTI: 802
- XRPUSD: 1182

## 6. MR candidates / resolved
- 1022 candidates, 0 resolved

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