# Phase H Status - Frozen Forward Validation

**Generated:** 2026-09-10T05:16:34.789827

## 1. Phase H start date
2026-08-30

## 2. Frozen model version
H1.0

## 3. Frozen MR_FAIL threshold
0.45 (locked)

## 4. Days observed
10

## 5. Observation count by asset
- ADAUSD: 60
- AUDCAD: 60
- AUDCHF: 60
- AUDJPY: 60
- AUDNZD: 60
- AUDUSD: 60
- AUS200: 19
- AVAXUSD: 60
- BCHUSD: 60
- BNBUSD: 60
- BRENT: 45
- BTCUSD: 258
- CADCHF: 60
- CADJPY: 60
- CHFJPY: 60
- DOGEUSD: 60
- DOTUSD: 60
- ETHUSD: 258
- EU50: 18
- EURAUD: 60
- EURCAD: 198
- EURCHF: 60
- EURGBP: 59
- EURJPY: 60
- EURUSD: 56
- FRA40: 18
- GBPAUD: 60
- GBPCAD: 60
- GBPCHF: 60
- GBPJPY: 60
- GBPUSD: 60
- GER40: 18
- GOLD: 164
- HK50: 17
- JPN225: 15
- LINKUSD: 60
- LTCUSD: 60
- NAS100: 14
- NATGAS: 45
- NZDCAD: 60
- NZDCHF: 60
- NZDJPY: 60
- NZDUSD: 59
- SILVER: 45
- SOLUSD: 60
- UK100: 18
- US30: 14
- US500: 50
- USDCAD: 60
- USDCHF: 60
- USDJPY: 197
- WTI: 45
- XRPUSD: 60

## 6. MR candidates / resolved
- 20 candidates, 0 resolved

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