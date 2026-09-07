# Phase H Scheduled Runner - Windows Task Scheduler entry point.
# Runs the frozen Phase H forward-validation loop once per invocation.
# Uses the project venv Python directly. No activation, no VS Code, no IBKR.

$ErrorActionPreference = "Continue"

$ProjectRoot = "E:\hybrid_mr_tf_ml_rading"
$PythonExe = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
$RunnerPy = Join-Path $ProjectRoot "scripts\run_phase_h.py"
$LogDir = Join-Path $ProjectRoot "logs"
$LogFile = Join-Path $LogDir "phase_h_scheduler.log"
$LockPath = Join-Path $LogDir "phase_h_scheduler.lock"
$LockOwnerPath = Join-Path $LockPath "owner.json"
$MutexName = "Local\HybridMrTfPhaseH"
$Mutex = $null
$MutexHeld = $false
$HealthPath = Join-Path $ProjectRoot "reports\phase_h_scheduler_health.json"
$StatusMd = Join-Path $ProjectRoot "PHASE_H_STATUS.md"
$ConfigPath = Join-Path $ProjectRoot "config.yaml"
$RegistryPath = Join-Path $ProjectRoot "models\registry.json"

function Ensure-Directory([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
}

function Write-Log([string]$Message) {
    $ts = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    Add-Content -LiteralPath $LogFile -Value "[$ts] $Message" -Encoding UTF8
}

function Rotate-Log {
    if (-not (Test-Path -LiteralPath $LogFile)) { return }
    if ((Get-Item -LiteralPath $LogFile).Length -le 20MB) { return }

    $archive = Join-Path $LogDir ("phase_h_scheduler_{0}.log" -f (Get-Date -Format "yyyyMMdd_HHmmss"))
    Move-Item -LiteralPath $LogFile -Destination $archive -Force
    $archives = Get-ChildItem -LiteralPath $LogDir -Filter "phase_h_scheduler_*.log" |
        Sort-Object LastWriteTime -Descending
    if ($archives.Count -gt 10) {
        $archives | Select-Object -Skip 10 | ForEach-Object {
            Remove-Item -LiteralPath $_.FullName -Force
        }
    }
}

function Get-PhaseHDecision {
    if (-not (Test-Path -LiteralPath $StatusMd)) { return "UNKNOWN" }
    $match = Select-String -LiteralPath $StatusMd -Pattern "\*\*([A-Z_]+)\*\*" | Select-Object -Last 1
    if ($match) { return $match.Matches[0].Groups[1].Value }
    return "UNKNOWN"
}

function Get-ModelFreezeStatus {
    $status = "PASS"
    $issues = @()
    if (Test-Path -LiteralPath $ConfigPath) {
        $raw = Get-Content -LiteralPath $ConfigPath -Raw
        foreach ($check in @(
            @{ Pattern = "threshold:\s*0\.45"; Name = "MR_FAIL threshold 0.45" },
            @{ Pattern = "threshold_locked:\s*true"; Name = "MR_FAIL threshold locked" },
            @{ Pattern = "automatic_retraining:\s*false"; Name = "automatic_retraining false" },
            @{ Pattern = "tf_enabled:\s*false"; Name = "TF disabled" },
            @{ Pattern = "standalone_entry:\s*false"; Name = "Runner standalone entry disabled" },
            @{ Pattern = "broker_enabled:\s*false"; Name = "broker disabled" }
        )) {
            if ($raw -notmatch $check.Pattern) {
                $status = "FAIL"
                $issues += $check.Name
            }
        }
    } else {
        $status = "UNKNOWN"
        $issues += "config.yaml missing"
    }
    if (Test-Path -LiteralPath $RegistryPath) {
        try {
            $registry = Get-Content -LiteralPath $RegistryPath -Raw | ConvertFrom-Json
            if ($registry.phase_h_baseline.version -ne "H1.0") {
                $status = "FAIL"
                $issues += "model version is not H1.0"
            }
            if ([double]$registry.phase_h_baseline.mr_fail_threshold -ne 0.45) {
                $status = "FAIL"
                $issues += "registry threshold is not 0.45"
            }
        } catch {
            $status = "UNKNOWN"
            $issues += "registry parse error"
        }
    }
    return @{ Status = $status; Issues = $issues }
}

function Write-Health(
    [datetime]$StartTs,
    [datetime]$FinishTs,
    [int]$ExitCode,
    [string]$Status,
    [string]$ErrorSummary
) {
    $freeze = Get-ModelFreezeStatus
    $health = [ordered]@{
        last_start = $StartTs.ToString("o")
        last_finish = $FinishTs.ToString("o")
        exit_code = $ExitCode
        status = $Status
        duration_seconds = [math]::Round(($FinishTs - $StartTs).TotalSeconds, 1)
        model_freeze = $freeze.Status
        model_freeze_issues = @($freeze.Issues)
        phase_h_status = Get-PhaseHDecision
    }
    if ($ErrorSummary) {
        $health.error_summary = $ErrorSummary
    }
    $health | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $HealthPath -Encoding UTF8
}

function Try-Acquire-Lock {
    $script:Mutex = New-Object System.Threading.Mutex($false, $MutexName)
    $script:MutexHeld = $script:Mutex.WaitOne(0)
    if (-not $script:MutexHeld) {
        Write-Log "SKIP: previous Phase H run still active (mutex=$MutexName)"
        Write-Output "SKIP: previous Phase H run still active"
        return $false
    }

    if ((Test-Path -LiteralPath $LockPath) -and -not (Get-Item -LiteralPath $LockPath).PSIsContainer) {
        Remove-Item -LiteralPath $LockPath -Force -ErrorAction SilentlyContinue
        Write-Log "Removed legacy stale lock file."
    }

    Remove-Item -LiteralPath $LockPath -Recurse -Force -ErrorAction SilentlyContinue
    try {
        New-Item -ItemType Directory -Path $LockPath -ErrorAction Stop | Out-Null
        @{ pid = $PID; started = (Get-Date).ToString("o"); script = $PSCommandPath } |
            ConvertTo-Json | Set-Content -LiteralPath $LockOwnerPath -Encoding UTF8
    } catch {
        Write-Log "WARNING: could not write lock metadata: $($_.Exception.Message)"
    }
    return $true
}

Ensure-Directory $LogDir
Ensure-Directory (Split-Path -Parent $HealthPath)
Rotate-Log

Set-Location -LiteralPath $ProjectRoot
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
$startTs = Get-Date

if (-not (Try-Acquire-Lock)) {
    $finishTs = Get-Date
    Write-Health -StartTs $startTs -FinishTs $finishTs -ExitCode 0 -Status "SKIPPED_ACTIVE" -ErrorSummary "Previous Phase H scheduled run still active."
    exit 0
}

$exitCode = 0
$status = "SUCCESS"
$errorSummary = ""

try {
    Write-Log "============================================================="
    Write-Log "PHASE H SCHEDULED RUN - start $($startTs.ToString('yyyy-MM-dd HH:mm:ss'))"

    if (-not (Test-Path -LiteralPath $PythonExe)) {
        throw "Python interpreter not found: $PythonExe"
    }
    if (-not (Test-Path -LiteralPath $RunnerPy)) {
        throw "Phase H runner not found: $RunnerPy"
    }

    $freeze = Get-ModelFreezeStatus
    if ($freeze.Status -eq "FAIL") {
        throw "Model freeze safety check failed: $([string]::Join('; ', @($freeze.Issues)))"
    }

    $output = & $PythonExe $RunnerPy 2>&1
    $exitCode = if ($null -eq $LASTEXITCODE) { 0 } else { [int]$LASTEXITCODE }
    $output | ForEach-Object { Add-Content -LiteralPath $LogFile -Value "$_" -Encoding UTF8 }

    if ($exitCode -ne 0) {
        $status = "FAILED"
        $errs = @($output | Where-Object { "$_" -match "ERROR|Traceback|FAILED|FATAL" } | Select-Object -Last 5)
        $errorSummary = [string]::Join(" | ", @($errs))
    }
} catch {
    $exitCode = 1
    $status = "FAILED"
    $errorSummary = $_.Exception.Message
    Write-Log "FATAL: $errorSummary"
} finally {
    $finishTs = Get-Date
    Write-Log "completion: $($finishTs.ToString('yyyy-MM-dd HH:mm:ss')) exit_code=$exitCode status=$status duration=$([math]::Round(($finishTs - $startTs).TotalSeconds, 1))s"
    Write-Health -StartTs $startTs -FinishTs $finishTs -ExitCode $exitCode -Status $status -ErrorSummary $errorSummary
    Remove-Item -LiteralPath $LockPath -Recurse -Force -ErrorAction SilentlyContinue
    if ($MutexHeld -and $null -ne $Mutex) {
        $Mutex.ReleaseMutex() | Out-Null
        $Mutex.Dispose()
    }
}

Write-Output "=============================================================="
Write-Output "PHASE H SCHEDULED RUN COMPLETE - exit $exitCode ($status)"
Write-Output "=============================================================="
exit $exitCode
