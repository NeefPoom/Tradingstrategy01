# Next steps for VS Code

## Phase A — validate data
- Run `check_trades.py`.
- Download/import 1H OHLCV.
- Run `build_dataset.py`.
- Confirm every asset has price matches.

## Phase B — baseline ML
- Run `train_models.py`.
- Inspect `reports/model_metrics.csv`.
- Reject any engine model that is weak out of sample.

## Phase C — focus on what the research found
Priority:
1. MR failure-risk model.
2. Runner model.
3. TF model.
4. Market eligibility / OFF decision.

## Phase D — walk-forward
Use rolling train/test windows rather than one fixed split.

## Phase E — IBKR
Run the same feature engine on IBKR 1H bars and score the latest completed bar.

## Phase F — execution
Keep risk rules deterministic. ML decides engine quality; it should not freely invent stop/TP parameters.
