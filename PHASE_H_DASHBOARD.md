# Phase H Local Dashboard

This is a local, read-only Streamlit dashboard for Phase H forward validation.

Launch from the project root:

```powershell
streamlit run dashboard/app.py --server.address 127.0.0.1
```

or:

```powershell
run_phase_h_dashboard.bat
```

The dashboard does not auto-refresh. Press **Refresh Data** to clear the Streamlit cache and load newly collected Phase H files.

Safety:

- Model retraining from the dashboard is disabled.
- MR_FAIL threshold editing is disabled; the dashboard displays `0.45 LOCKED`.
- Broker execution is disabled.
- TF is displayed as `OFF`.
- Runner standalone entry is not available.
- US500 is displayed as `RESEARCH_ONLY`.

The dashboard reads Phase H files from `reports/`, `data/forward/`, `data/state/`, and `models/registry.json`. Missing files show empty-state messages instead of crashing.
