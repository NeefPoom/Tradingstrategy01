# Phase H Local Scheduler

The Phase H scheduler runs the frozen forward-validation loop locally through Windows Task Scheduler.

It runs:

```powershell
E:\hybrid_mr_tf_ml_rading\.venv\Scripts\python.exe E:\hybrid_mr_tf_ml_rading\scripts\run_phase_h.py
```

from:

```text
E:\hybrid_mr_tf_ml_rading
```

## Task

- Task name: `Hybrid MR-TF Phase H`
- Schedule: every hour at minute `05`
- Example run times: `00:05`, `01:05`, `02:05`, ... `23:05`
- Reason for `HH:05`: gives the hourly candle a short buffer after close before Yahoo data is requested.

The task does not depend on VS Code and does not require manual virtual-environment activation.

## Logs and Health

- Scheduler log: `logs\phase_h_scheduler.log`
- Overlap lock: `logs\phase_h_scheduler.lock`
- Health file: `reports\phase_h_scheduler_health.json`

The scheduler log rotates when it exceeds 20 MB. Archived logs are named `phase_h_scheduler_YYYYMMDD_HHMMSS.log`; the newest 10 archives are kept. Only old archived scheduler logs are deleted.

## Install

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\install_phase_h_scheduler.ps1
```

The install script is idempotent. If the task already exists, it updates the task instead of creating a duplicate.

## Check

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\check_phase_h_scheduler.ps1
```

## Uninstall

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\uninstall_phase_h_scheduler.ps1
```

Uninstall removes only the Windows task named `Hybrid MR-TF Phase H`. It does not delete logs, models, observations, reports, or project files.

## Manual Run

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File run_phase_h_scheduled.ps1
```

## Runtime Behavior

If the PC is asleep, Task Scheduler can wake it when Windows power settings allow wake timers. If the PC is powered off, it cannot run tasks. If a scheduled run is missed, Windows should run it as soon as possible after the computer resumes.

If Internet or Yahoo Finance fails, the run is logged and `reports\phase_h_scheduler_health.json` records failure details. If one asset fails, Phase H continues according to the existing orchestrator behavior and records warnings.

If a previous Phase H run is still active, the next runner invocation skips with:

```text
SKIP: previous Phase H run still active
```

Phase H itself also uses append-only/deterministic observation IDs, so repeated runs should skip duplicate completed bars rather than duplicating observations.

## Safety

The scheduler is research/forward-observation only. It must not:

- place trades
- connect to a broker
- use IBKR
- click TradingView
- send orders
- retrain models
- optimize parameters
- change the MR_FAIL threshold
- enable TF
- open Runner standalone trades

Expected frozen settings:

- Model version: `H1.0`
- MR_FAIL threshold: `0.45 locked`
- `automatic_retraining: false`
- `tf_enabled: false`
- `broker_enabled: false`
- `standalone_entry: false`
- US500 remains `RESEARCH_ONLY`
