# Phase H Local Research Dashboard — Design & Implementation Specification

**Project:** Hybrid MR-TF ML  
**Purpose:** Read-only local dashboard for Phase H forward validation  
**Data source:** Existing Phase H files generated from Yahoo Finance workflow  
**Execution mode:** Local only, manual refresh only

## 1. Core requirement

Build a local dashboard for monitoring Phase H progress and results.

The dashboard must **NOT auto-refresh** when `scripts/run_phase_h.py` runs.

Required behavior:

```text
Phase H scheduler
    ↓
updates research files
    ↓
dashboard stays unchanged
    ↓
user opens dashboard or clicks Refresh Data
    ↓
dashboard reloads latest files
```

No polling, no filesystem watcher, no timed Streamlit rerun, and no dashboard-triggered Phase H run.

Show:

- Dashboard Data Loaded At
- Latest Phase H Observation
- Latest Scheduler Run

Use a visible **Refresh Data** button.

Recommended implementation:

```python
if st.sidebar.button("Refresh Data"):
    st.cache_data.clear()
    st.rerun()
```

Use `@st.cache_data` for file loading.

---

## 2. Technology

Use:

- Python 3.12
- Streamlit
- pandas
- numpy
- Plotly
- pathlib
- json
- pyarrow/parquet support

Recommended structure:

```text
dashboard/
    app.py
    data_loader.py
    metrics.py
    charts.py
    components.py

tests/
    test_dashboard.py

run_phase_h_dashboard.bat
PHASE_H_DASHBOARD.md
```

Launch manually:

```powershell
streamlit run dashboard/app.py
```

or:

```powershell
run_phase_h_dashboard.bat
```

Do not start the dashboard from `scripts/run_phase_h.py`.

---

## 3. Dashboard purpose

The dashboard should answer:

1. Is Phase H healthy?
2. Is the model still frozen?
3. How much forward data has accumulated?
4. Is the sample large enough to interpret?
5. Is MR_FAIL still useful?
6. Does the 0.45 gate reduce MR losses?
7. How many losers were avoided?
8. How many winners were blocked?
9. Is Runner still positive?
10. Which Runner exit method looks better?
11. Which assets are healthy, weak, or research-only?
12. What is the latest state for each asset?
13. Are Yahoo data and scheduler healthy?

This is a **research dashboard**, not a trading terminal.

---

## 4. Safety constraints

The dashboard must be read-only.

Do NOT add controls for:

- model retraining
- threshold tuning
- ER/NW parameter changes
- broker execution
- BUY / SELL / CLOSE
- position mutation
- TF activation
- Runner standalone entry
- asset-policy editing

Display these as frozen/read-only:

```text
Model Version: H1.0
MR_FAIL Threshold: 0.45 LOCKED
TF: OFF
Broker Execution: OFF
Yahoo Finance: ACTIVE
US500: RESEARCH_ONLY
```

The dashboard must never invoke:

```text
scripts/train_models.py
scripts/walk_forward.py
scripts/run_phase_h.py
```

automatically.

---

## 5. Data sources

Read existing Phase H outputs when available:

```text
PHASE_H_STATUS.md

reports/phase_h_baseline.json
reports/phase_h_scheduler_health.json
reports/price_quality.csv
reports/latest_scores.csv
reports/trade_plan_latest.csv

reports/forward_mr_gate.csv
reports/forward_mr_gate_summary.md

reports/forward_runner_comparison.csv
reports/forward_runner_summary.md

reports/mr_fail_forward_calibration.csv

data/forward/phase_h_observations.parquet
data/forward/phase_h_observations.csv

data/forward/mr_candidates.parquet
data/forward/mr_candidates.csv

data/forward/runner_events.parquet
data/forward/runner_events.csv

data/state/current_positions.json
models/registry.json
```

Not every file will exist early in Phase H.

The dashboard must not crash when data is unavailable.

Use messages such as:

```text
INSUFFICIENT DATA
NOT YET AVAILABLE
WAITING FOR RESOLVED EVENTS
```

Prefer Parquet, fallback to CSV.

Create helper:

```python
load_parquet_or_csv(...)
```

---

## 6. Navigation

Use sidebar navigation:

```text
1. Overview
2. MR_FAIL Monitor
3. MR Gate Analysis
4. Runner Research
5. Assets
6. Latest Market State
7. Data & Scheduler Health
8. Forward Observations
```

---

# PAGE 1 — OVERVIEW

## 7. Header

Show:

```text
PHASE H — FROZEN FORWARD VALIDATION
RESEARCH / FORWARD VALIDATION ONLY
NO BROKER EXECUTION
```

Below:

```text
Model Version: H1.0
MR_FAIL Threshold: 0.45 LOCKED
TF: OFF
Data Source: Yahoo Finance
```

Read values from config/baseline files where possible.

---

## 8. Top status cards

Show:

### Phase H Decision

Possible values:

```text
INSUFFICIENT_FORWARD_DATA
CONTINUE_FORWARD_VALIDATION
MODEL_WARNING
CANDIDATE_FOR_PAPER_TRADING
```

### Model Freeze

```text
PASS
WARNING
FAIL
```

### Scheduler

```text
HEALTHY
WARNING
FAILED
UNKNOWN
```

### Yahoo Data

```text
PASS
WARNING
STALE
FAILED
```

### Days Observed

Example:

```text
12 / 28 minimum
12 / 56 preferred
```

---

## 9. Progress section

Show progress bars for:

### Days

```text
Days observed / 28 minimum
Days observed / 56 preferred
```

### MR Candidates

```text
MR Candidates / 30 first checkpoint
MR Candidates / 60 preferred
```

### Resolved MR

```text
Resolved
Waiting
```

### Runner Events

```text
Runner Events / 20 first checkpoint
Runner Events / 40 preferred
```

Do not declare success from elapsed days alone.

---

## 10. Sample confidence labels

Use consistent sample labels.

General:

```text
0–9      VERY LOW SAMPLE
10–19    LOW SAMPLE
20–49    EARLY EVIDENCE
50–99    USABLE SAMPLE
100+     STRONGER SAMPLE
```

Runner:

```text
n < 20      LOW_SAMPLE
20–49       EARLY
n >= 50     USABLE_SAMPLE
```

---

## 11. Overview research snapshot

Create:

| Research Area | Status | Key Metric | Interpretation |
|---|---|---:|---|
| MR_FAIL | Waiting/Green/Yellow/Red | ROC-AUC | Risk gate |
| MR Gate | Waiting/Positive/Weak | PF delta | Gate value |
| Runner Osc Cross | Waiting/Positive/Negative | PF | Exit research |
| Runner Hybrid | Waiting/Positive/Negative | PF | Exit research |
| US500 | Research Only | — | Holdout issue |
| TF | OFF | historical n=41 | Rejected |

---

# PAGE 2 — MR_FAIL MONITOR

## 12. Main metrics

Show forward:

```text
ROC-AUC
PR-AUC
Brier Score
ECE
Resolved MR Candidates
```

Also show Phase G baseline:

```text
ROC-AUC ≈ 0.743
Brier ≈ 0.212
ECE ≈ 0.098
```

Keep historical and forward clearly separated.

---

## 13. MR_FAIL status logic

Suggested labels:

### GREEN

```text
ROC-AUC >= 0.65
and no severe calibration degradation
```

### YELLOW

```text
ROC-AUC 0.55–0.65
or material calibration deterioration
```

### RED

```text
ROC-AUC <= 0.55
or ranking becomes unreliable
```

### INSUFFICIENT

When too few resolved MR candidates exist.

Never calculate meaningful AUC from tiny samples.

---

## 14. ROC-AUC progress chart

If enough resolved events exist, plot expanding or rolling ROC-AUC.

X-axis:

```text
Date or resolved candidate count
```

Y-axis:

```text
ROC-AUC
```

Reference lines:

```text
0.50 = random
0.65 = preferred Phase H level
0.743 = Phase G baseline
```

Require an adequate sample before plotting.

---

## 15. Calibration chart

Plot:

```text
Predicted p_mr_fail
vs
Actual failure rate
```

Add ideal `y=x` diagonal.

Calibration table:

| Probability Bin | N | Mean Predicted | Actual Fail Rate | Error |
|---|---:|---:|---:|---:|

Highlight low-sample bins.

---

## 16. p_mr_fail distribution

Show distributions for:

- all MR candidates
- accepted
- blocked

Add vertical threshold line:

```text
0.45 LOCKED
```

Do not make it editable.

---

# PAGE 3 — MR GATE ANALYSIS

## 17. Gated vs ungated comparison

| Metric | Unfiltered MR | MR_FAIL Gated | Difference |
|---|---:|---:|---:|
| Candidates | | | |
| Win Rate | | | |
| Avg Return | | | |
| Median Return | | | |
| Profit Factor | | | |
| Max Drawdown | | | |
| Worst Trade | | | |
| Avg MAE | | | |
| Tail Loss | | | |

---

## 18. Gate economic impact

Display:

```text
Blocked Losers
Blocked Winners
Avoided Loss
Missed Profit
```

Calculate informationally:

```text
Gate Economic Benefit =
Avoided Loss - Missed Profit
```

Status:

```text
POSITIVE
NEGATIVE
INSUFFICIENT SAMPLE
```

Do not auto-optimize threshold from this.

---

## 19. Candidate outcome matrix

| Gate Decision | Actual Winner | Actual Loser |
|---|---:|---:|
| Accepted | | |
| Blocked | | |

Show:

```text
True Block Rate
False Block Rate
Accepted Win Rate
Blocked Win Rate
```

Definitions:

- True Block = bad hypothetical MR correctly blocked.
- False Block = profitable hypothetical MR blocked.

---

## 20. MR cumulative performance

Plot forward research curves:

```text
Unfiltered MR
MR_FAIL <= 0.45
```

Label:

```text
Forward Research Simulation — Not Broker P&L
```

---

# PAGE 4 — RUNNER RESEARCH

## 21. Permanent Runner explanation

Show:

```text
Runner is not a standalone entry engine.

Runner begins only after a successful MR trade reaches
the Runner transition point.
```

---

## 22. Compare Runner policies

Compare:

```text
OSC_CROSS
HYBRID
```

For each show:

```text
Events
Resolved
Win Rate
Average Return
Median Return
Profit Factor
Max Drawdown
Avg Duration
P90 Winner
P95 Winner
Worst Trade
```

---

## 23. Runner comparison table

| Metric | Osc Cross | Hybrid | Current Leader |
|---|---:|---:|---|
| Events | | | |
| Win Rate | | | |
| Avg Return | | | |
| PF | | | |
| Max DD | | | |
| P95 Winner | | | |
| Avg Duration | | | |

The "leader" is informational only.

Do not automatically change Runner policy.

---

## 24. Runner cumulative performance

Plot:

```text
OSC_CROSS
HYBRID
```

for the same forward Runner events.

Label:

```text
Parallel Forward Research
```

---

## 25. Runner by asset class

Use:

```text
METALS
FX
INDEX
CRYPTO
```

Table:

| Asset Class | Exit | N | PF | Avg Return | Max DD | Confidence |
|---|---|---:|---:|---:|---:|---|

Do not optimize per-symbol parameters.

---

## 26. Runner by asset

Optional drill-down:

```text
GOLD
USDJPY
EURCAD
US500
BTCUSD
ETHUSD
```

Always show sample count and confidence label.

---

# PAGE 5 — ASSETS

## 27. Asset cards/table

For each:

```text
GOLD
USDJPY
US500
BTCUSD
ETHUSD
EURCAD
```

Show:

```text
Asset Class
Data Status
Latest Completed Bar
Current Position State
MR Candidates
Resolved MR
MR_FAIL AUC if meaningful
Eligible MR Avg Return
Runner Events
Runner Avg Return
Research Status
```

---

## 28. Asset research status

Use:

```text
HEALTHY
WATCH
WEAK
RESEARCH_ONLY
INSUFFICIENT_DATA
```

US500 must show:

```text
RESEARCH_ONLY
```

unless changed explicitly outside the dashboard.

---

## 29. Asset detail

Allow asset selection.

Show latest feature state:

```text
ER10
ER20
ER40
ATR
NATR
Vol Ratio
Cross Count
Osc
Signal
Osc - Signal
Osc Slope
```

ML evidence:

```text
p_mr_win
p_mr_fail
pred_mr_return_pct
p_runner_win
pred_runner_return_pct
```

Policy:

```text
MR setup
MR gate
Asset policy
Current position
Recommended action
```

Also show recent MR candidates and Runner events.

---

# PAGE 6 — LATEST MARKET STATE

## 30. Current-state table

Columns:

```text
Asset
Latest Completed Bar
Data Status
Position State
MR Setup
p_mr_win
p_mr_fail
MR Gate
MR Eligible
Runner Active
p_runner_win
Pred Runner Return
Action
Reason
```

Example actions:

```text
NO_ACTION
WATCH_MR
MR_ELIGIBLE
MR_BLOCK
HOLD_MR
MR_TP1_TRANSITION
HOLD_RUNNER
EXIT_RUNNER
RESEARCH_ONLY
STALE_DATA
```

Never show:

```text
TF_ENTRY
RUNNER_ENTRY
```

---

## 31. Position lifecycle

For non-FLAT positions show:

```text
State
Entry Time
Entry Price
Direction
TP1 Reached
Runner Started At
Runner Exit Research Status
```

No trading buttons.

---

# PAGE 7 — DATA & SCHEDULER HEALTH

## 32. Scheduler health

Read:

```text
reports/phase_h_scheduler_health.json
```

Show:

```text
Last Start
Last Finish
Exit Code
Status
Duration
Last Successful Run
Next Scheduled Run if available
```

---

## 33. Model freeze health

Show:

```text
Model Version
Expected Hash
Current Hash
Freeze Status
MR_FAIL Threshold
Automatic Retraining
TF Enabled
```

Expected:

```text
H1.0
PASS
0.45 LOCKED
automatic_retraining = false
TF = OFF
```

If violation:

```text
PHASE H MODEL FREEZE VIOLATION
```

with red status.

---

## 34. Yahoo data quality

Read:

```text
reports/price_quality.csv
```

Show:

| Asset | Rows | Latest Timestamp | Duplicates | Bad OHLC | Max Gap | Status |
|---|---:|---|---:|---:|---:|---|

Colors:

```text
PASS = green
WARNING = amber
FAIL = red
```

Expected weekends/session gaps should not be treated as corruption automatically.

---

## 35. Observation freshness

Show last Phase H observation per asset and age.

Flag:

```text
STALE
```

where appropriate.

---

# PAGE 8 — FORWARD OBSERVATIONS

## 36. Observation browser

Filters:

```text
Asset
Date Range
Position State
Decision
MR Eligible
Blocked
Resolved/Unresolved
```

Display selected columns.

Optional read-only CSV download is allowed.

---

## 37. MR candidate browser

Show:

```text
Candidate ID
Asset
Timestamp
Direction
Entry Price
p_mr_win
p_mr_fail
Pred Return
Decision
Reason
Resolved
Actual Outcome
Hypothetical Return
```

Allow sorting.

---

## 38. Runner event browser

Show:

```text
Runner ID
Asset
Direction
Start
Start Price
p_runner_win
Pred Return
Osc Exit Return
Hybrid Exit Return
MAE
MFE
Duration
Resolved
```

---

# MANUAL REFRESH SYSTEM

## 39. Sidebar refresh

Sidebar must contain:

```text
[ Refresh Data ]
```

Behavior:

- clear Streamlit cache
- reload files
- update dashboard load timestamp
- rerender

No timer.

No auto-refresh.

---

## 40. Sidebar status

Show:

```text
Dashboard Loaded:
<timestamp>

Latest Phase H Observation:
<timestamp>

Scheduler Latest Run:
<timestamp>
```

---

## 41. Optional stale-dashboard indicator

On user interaction only, it is acceptable to compare file modification times.

Example:

```text
Newer Phase H files exist.
Press Refresh Data to load them.
```

Do not poll in the background.

---

# RESEARCH INTERPRETATION

## 42. Milestone timeline

Overview should show:

```text
1–2 weeks
Pipeline sanity observation

~30 MR candidates
First meaningful MR_FAIL review

~20 Runner events
First Runner review

~4 weeks
Early Phase H checkpoint

~60 MR candidates / ~40 Runner events
Stronger GO / MODIFY / STOP decision

6–8 weeks
Preferred first serious conclusion window
```

These are targets, not guarantees.

---

## 43. Decision explanation

Show current Phase H decision plus reason.

Example:

```text
INSUFFICIENT_FORWARD_DATA

Why:
- resolved MR candidates: 14
- first checkpoint target: 30
- Runner events: 6
- first checkpoint target: 20
- model freeze intact
```

Do not invent independent decision logic if `PHASE_H_STATUS.md` already defines it.

---

## 44. Historical vs forward comparison

Display separately:

| Metric | Phase G Historical | Phase H Forward |
|---|---:|---:|
| MR_FAIL AUC | 0.743 | |
| Brier | 0.212 | |
| ECE | 0.098 | |
| MR Threshold | 0.45 | 0.45 |
| Runner conclusion | Positive OOS | |

Never merge Phase A–G observations into Phase H sample counts.

---

# VISUAL DESIGN

## 45. Style

Use:

```python
st.set_page_config(
    page_title="Hybrid MR-TF — Phase H",
    layout="wide"
)
```

Style:

- clean
- quantitative
- research-focused
- dark or neutral professional theme
- compact
- responsive wide layout

Status colors only:

```text
GREEN = healthy/pass/positive
AMBER = warning/early evidence
RED = failure/model warning/stale critical
GRAY = insufficient/research-only/unavailable
```

Do not use colors to exaggerate one profitable observation.

---

## 46. Useful charts

Prioritize:

1. Observations accumulated over time
2. MR candidates accumulated over time
3. p_mr_fail distribution
4. MR calibration curve
5. Expanding MR_FAIL ROC-AUC
6. Gated vs ungated MR cumulative return
7. Runner Osc Cross vs Hybrid cumulative return
8. MR candidates by asset
9. Runner events by asset
10. Latest p_mr_fail by asset
11. Latest p_mr_win by asset
12. Latest predicted return by asset

Avoid decorative charts.

---

## 47. Latest p_mr_fail chart

A compact bar chart can show current p_mr_fail by asset.

Add horizontal line:

```text
0.45
```

Add note:

```text
Low p_mr_fail alone is NOT an entry signal.
Original MR setup must also exist.
```

---

## 48. Explain model evidence vs setup

Permanent info section:

```text
A favorable ML score does not create an MR setup.

MR requires:
1. original oscillator MR setup,
2. MR_FAIL gate,
3. model evidence,
4. asset policy.

Runner requires:
an existing successful MR lifecycle.
```

---

# PERFORMANCE & ERROR HANDLING

## 49. Caching

Use:

```python
@st.cache_data
```

for file loads.

Manual Refresh clears cache.

Navigation should not reload large datasets unnecessarily.

---

## 50. Missing-data handling

One missing report must not crash the dashboard.

Examples:

```text
Runner report unavailable:
No resolved Runner events yet.
```

If Parquet missing but CSV exists, use CSV.

If both are missing, show an empty-state message.

Do not render broken NaN charts.

---

## 51. Logging

Create:

```text
logs/dashboard.log
```

Log only useful events:

```text
dashboard start
manual refresh
missing file warning
parse error
```

Do not log every rerender.

---

## 52. Local-only operation

Bind to localhost:

```powershell
streamlit run dashboard/app.py --server.address 127.0.0.1
```

Do not expose externally.

Do not deploy to cloud.

---

# HELPER FILES

## 53. Dashboard BAT

Create:

```text
run_phase_h_dashboard.bat
```

It should launch Streamlit with:

```text
.venv\Scripts\python.exe
```

Do not run Phase H automatically before dashboard launch.

Dashboard and scheduler remain independent.

---

# TESTS

## 54. Required tests

Create:

```text
tests/test_dashboard.py
```

At minimum test:

1. dashboard loader works with missing Runner file
2. works with zero MR candidates
3. works with zero Runner events
4. threshold is read-only 0.45
5. US500 displays RESEARCH_ONLY
6. TF displays OFF
7. no Runner entry action exists
8. no broker action exists
9. Parquet→CSV fallback works
10. Refresh Data does not modify research files
11. no dashboard function invokes model training
12. no dashboard function invokes `run_phase_h.py` automatically

Run:

```powershell
pytest -q
```

---

# DOCUMENTATION

## 55. Required files

Create:

```text
dashboard/
    app.py
    data_loader.py
    metrics.py
    charts.py
    components.py

tests/
    test_dashboard.py

run_phase_h_dashboard.bat

PHASE_H_DASHBOARD.md
```

Update README:

```text
## Phase H Dashboard
```

Explain:

```text
streamlit run dashboard/app.py
```

and:

```text
The dashboard does not auto-refresh.
Press Refresh Data to load newly collected Phase H data.
```

---

# IMPLEMENTATION VERIFICATION

## 56. Mandatory manual refresh test

After implementation:

1. Run:

```powershell
pytest -q
```

2. Launch:

```powershell
streamlit run dashboard/app.py
```

3. Confirm the dashboard works even when Phase H currently has:

```text
1 observation per asset
0 MR candidates
0 Runner events
```

4. Leave dashboard open.

5. Run separately:

```powershell
python scripts/run_phase_h.py
```

Expected:

```text
Phase H files update on disk.
Dashboard display remains unchanged.
```

6. Click:

```text
Refresh Data
```

Expected:

```text
Dashboard now shows the new data.
```

This test is mandatory.

7. Confirm dashboard did NOT:

- modify models
- retrain
- change threshold
- change current_positions.json
- place trades
- enable TF
- create Runner entry
- invoke broker

---

# FINAL AI / CODEX RESPONSE

After implementation report:

## Files Created
List all dashboard files.

## Files Modified
List existing files changed.

## Tests
Report pytest results.

## Launch
Give exact launch command.

## Refresh
Explicitly confirm:

```text
AUTO REFRESH: DISABLED
MANUAL REFRESH: ENABLED
```

## Current Dashboard State
Show:

```text
Phase H decision
Days observed
Observation rows
MR candidates
Runner events
Model freeze
Scheduler health
```

## Safety
Confirm:

```text
Model retraining from dashboard: DISABLED
Threshold editing: DISABLED
Broker execution: DISABLED
TF: OFF
Runner standalone entry: IMPOSSIBLE
US500: RESEARCH_ONLY
```

If successful end with:

```text
PHASE H LOCAL DASHBOARD: READY
```

Otherwise:

```text
PHASE H LOCAL DASHBOARD: NOT READY — <reason>
```

---

# Final Architecture

```text
WINDOWS TASK SCHEDULER
        |
        v
Phase H Data Collection
        |
    Yahoo Finance
        |
        v
Append-Only Research Files
        |
        |  NO AUTO DASHBOARD PUSH
        v
Local Streamlit Dashboard
        |
User presses Refresh Data
        |
        v
Read Current Files
        |
        v
Research Monitoring / Review
```

The scheduler collects evidence.

The dashboard visualizes evidence.

The dashboard does not control or modify the experiment.

Implement this as a local, read-only, manually refreshed Phase H research dashboard.
