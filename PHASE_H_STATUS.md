# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-14T18:09:11.526385

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
45

## 5. Observation count by asset
- ADAUSD: 889
- AUDCAD: 644
- AUDCHF: 644
- AUDJPY: 644
- AUDNZD: 644
- AUDUSD: 644
- AUS200: 189
- AVAXUSD: 889
- BCHUSD: 889
- BNBUSD: 889
- BRENT: 612
- BTCUSD: 1087
- CADCHF: 644
- CADJPY: 644
- CHFJPY: 644
- DOGEUSD: 889
- DOTUSD: 889
- ETHUSD: 1087
- EU50: 243
- EURAUD: 644
- EURCAD: 782
- EURCHF: 644
- EURGBP: 645
- EURJPY: 644
- EURUSD: 644
- FRA40: 243
- GBPAUD: 644
- GBPCAD: 644
- GBPCHF: 644
- GBPJPY: 644
- GBPUSD: 644
- GER40: 243
- GOLD: 733
- HK50: 182
- JPN225: 161
- LINKUSD: 889
- LTCUSD: 889
- NAS100: 186
- NATGAS: 616
- NZDCAD: 644
- NZDCHF: 644
- NZDJPY: 644
- NZDUSD: 644
- SILVER: 613
- SOLUSD: 889
- UK100: 243
- US30: 186
- US500: 222
- USDCAD: 644
- USDCHF: 640
- USDJPY: 778
- WTI: 613
- XRPUSD: 889

## 6. MR candidates / resolved
- 740 candidates, 0 resolved

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