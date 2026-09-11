# Install/update the Windows Scheduled Task for Phase H.

$ErrorActionPreference = "Stop"

$TaskName = "Hybrid MR-TF Phase H"
$ProjectRoot = "E:\hybrid_mr_tf_ml_rading"
$RunnerPs1 = Join-Path $ProjectRoot "run_phase_h_scheduled.ps1"
$PythonExe = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
$RunnerPy = Join-Path $ProjectRoot "scripts\run_phase_h.py"
$ConfigPath = Join-Path $ProjectRoot "config.yaml"

function Get-NextMinuteFive {
    $now = Get-Date
    $candidate = Get-Date -Year $now.Year -Month $now.Month -Day $now.Day -Hour $now.Hour -Minute 5 -Second 0
    if ($candidate -le $now) {
        $candidate = $candidate.AddHours(1)
    }
    return $candidate
}

function Assert-Contains([string]$Text, [string]$Pattern, [string]$Description) {
    if ($Text -notmatch $Pattern) {
        throw "SAFETY CHECK FAILED: $Description"
    }
}

if (-not (Test-Path -LiteralPath $ProjectRoot)) { throw "Project root not found: $ProjectRoot" }
if (-not (Test-Path -LiteralPath $RunnerPs1)) { throw "Runner script not found: $RunnerPs1" }
if (-not (Test-Path -LiteralPath $PythonExe)) { throw "Python interpreter not found: $PythonExe" }
if (-not (Test-Path -LiteralPath $RunnerPy)) { throw "Phase H runner not found: $RunnerPy" }

$rawConfig = Get-Content -LiteralPath $ConfigPath -Raw
Assert-Contains $rawConfig "threshold:\s*0\.45" "MR_FAIL threshold must be 0.45"
Assert-Contains $rawConfig "threshold_locked:\s*true" "MR_FAIL threshold must be locked"
Assert-Contains $rawConfig "automatic_retraining:\s*false" "automatic_retraining must be false"
Assert-Contains $rawConfig "tf_enabled:\s*false" "TF must be disabled"
Assert-Contains $rawConfig "standalone_entry:\s*false" "Runner standalone entry must be disabled"
Assert-Contains $rawConfig "broker_enabled:\s*false" "broker execution must be disabled"

$orchestrator = Get-Content -LiteralPath $RunnerPy -Raw
foreach ($bad in @("train_models.py", "walk_forward.py", "threshold_research.py", "calibration_research.py", "runner_exit_research.py", "asset_holdout.py", "download_ibkr.py")) {
    if ($orchestrator -match [regex]::Escape($bad)) {
        throw "STOP: scripts\run_phase_h.py references prohibited script $bad"
    }
}

$startAt = Get-NextMinuteFive
$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$RunnerPs1`"" `
    -WorkingDirectory $ProjectRoot
$trigger = New-ScheduledTaskTrigger `
    -Once `
    -At $startAt `
    -RepetitionInterval (New-TimeSpan -Hours 1) `
    -RepetitionDuration (New-TimeSpan -Days 3650)
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -WakeToRun `
    -MultipleInstances IgnoreNew `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 55) `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 10) `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited

$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Set-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal | Out-Null
    Write-Output "Scheduled task '$TaskName' updated."
} else {
    Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force | Out-Null
    Write-Output "Scheduled task '$TaskName' created."
}

$task = Get-ScheduledTask -TaskName $TaskName -ErrorAction Stop
$info = Get-ScheduledTaskInfo -TaskName $TaskName
Write-Output "Safety check: model freeze intact; scheduled runner does not call training/optimization scripts."
Write-Output "Task name: $($task.TaskName)"
Write-Output "Task state: $($task.State)"
Write-Output "Schedule: every 1 hour starting $($startAt.ToString('yyyy-MM-dd HH:mm:ss'))"
Write-Output "Next run: $($info.NextRunTime)"
