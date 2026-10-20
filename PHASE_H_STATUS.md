# Phase H Status - Frozen Forward Validation

**Generated:** 2026-10-20T12:12:22.731598

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
51

## 5. Observation count by asset
- ADAUSD: 1027
- AUDCAD: 733
- AUDCHF: 733
- AUDJPY: 733
- AUDNZD: 733
- AUDUSD: 733
- AUS200: 217
- AVAXUSD: 1027
- BCHUSD: 1027
- BNBUSD: 1027
- BRENT: 698
- BTCUSD: 1225
- CADCHF: 733
- CADJPY: 733
- CHFJPY: 733
- DOGEUSD: 1027
- DOTUSD: 1027
- ETHUSD: 1225
- EU50: 275
- EURAUD: 733
- EURCAD: 871
- EURCHF: 733
- EURGBP: 734
- EURJPY: 733
- EURUSD: 733
- FRA40: 275
- GBPAUD: 733
- GBPCAD: 733
- GBPCHF: 733
- GBPJPY: 733
- GBPUSD: 734
- GER40: 275
- GOLD: 820
- HK50: 203
- JPN225: 189
- LINKUSD: 1027
- LTCUSD: 1027
- NAS100: 210
- NATGAS: 702
- NZDCAD: 733
- NZDCHF: 733
- NZDJPY: 733
- NZDUSD: 733
- SILVER: 699
- SOLUSD: 1027
- UK100: 275
- US30: 210
- US500: 246
- USDCAD: 733
- USDCHF: 728
- USDJPY: 867
- WTI: 699
- XRPUSD: 1027

## 6. MR candidates / resolved
- 870 candidates, 0 resolved

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