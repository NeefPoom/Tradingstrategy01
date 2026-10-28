# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-28T13:38:30.175623

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
59

## 5. Observation count by asset
- ADAUSD: 1220
- AUDCAD: 876
- AUDCHF: 876
- AUDJPY: 876
- AUDNZD: 876
- AUDUSD: 876
- AUS200: 259
- AVAXUSD: 1220
- BCHUSD: 1220
- BNBUSD: 1220
- BRENT: 837
- BTCUSD: 1418
- CADCHF: 876
- CADJPY: 876
- CHFJPY: 876
- DOGEUSD: 1220
- DOTUSD: 1220
- ETHUSD: 1418
- EU50: 329
- EURAUD: 876
- EURCAD: 1014
- EURCHF: 876
- EURGBP: 877
- EURJPY: 876
- EURUSD: 876
- FRA40: 329
- GBPAUD: 876
- GBPCAD: 876
- GBPCHF: 876
- GBPJPY: 876
- GBPUSD: 877
- GER40: 329
- GOLD: 959
- HK50: 245
- JPN225: 231
- LINKUSD: 1220
- LTCUSD: 1220
- NAS100: 252
- NATGAS: 842
- NZDCAD: 876
- NZDCHF: 876
- NZDJPY: 876
- NZDUSD: 876
- SILVER: 838
- SOLUSD: 1220
- UK100: 329
- US30: 252
- US500: 288
- USDCAD: 876
- USDCHF: 871
- USDJPY: 1009
- WTI: 838
- XRPUSD: 1220

## 6. MR candidates / resolved
- 1060 candidates, 0 resolved

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