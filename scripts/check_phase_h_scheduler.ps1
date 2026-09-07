# Phase H Scheduler status check.

$ErrorActionPreference = "Continue"

$TaskName = "Hybrid MR-TF Phase H"
$ProjectRoot = "E:\hybrid_mr_tf_ml_rading"
$LogFile = Join-Path $ProjectRoot "logs\phase_h_scheduler.log"
$HealthPath = Join-Path $ProjectRoot "reports\phase_h_scheduler_health.json"

$task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if (-not $task) {
    Write-Output "Task '$TaskName' is NOT installed."
    if (Test-Path -LiteralPath $LogFile) {
        Write-Output ""
        Write-Output "--- last 50 lines of logs\phase_h_scheduler.log ---"
        Get-Content -LiteralPath $LogFile -Tail 50
    }
    exit 1
}

$info = Get-ScheduledTaskInfo -TaskName $TaskName

Write-Output "=============================================================="
Write-Output "PHASE H SCHEDULER STATUS"
Write-Output "=============================================================="
Write-Output ("Task name:        {0}" -f $task.TaskName)
Write-Output ("Task state:       {0}" -f $task.State)
Write-Output ("Enabled:          {0}" -f ($task.State -ne "Disabled"))
Write-Output ("Last run time:    {0}" -f $info.LastRunTime)
Write-Output ("Last result:      {0}" -f $info.LastTaskResult)
Write-Output ("Next run time:    {0}" -f $info.NextRunTime)

$events = @(Get-WinEvent -FilterHashtable @{ LogName = "Microsoft-Windows-TaskScheduler/Operational" } -MaxEvents 300 -ErrorAction SilentlyContinue |
    Where-Object { $_.Message -like "*$TaskName*" })
$successes = @($events | Where-Object { $_.Id -in 102, 201 })
$failures = @($events | Where-Object { $_.Id -in 101, 103, 203 })
Write-Output ("Number of recent successful runs: {0}" -f $successes.Count)
if ($failures.Count -gt 0) {
    Write-Output "Recent failures:"
    $failures | Select-Object -First 5 | ForEach-Object {
        Write-Output ("  [{0}] Event {1}: {2}" -f $_.TimeCreated, $_.Id, $_.Message)
    }
} else {
    Write-Output "Recent failures: none found in recent Task Scheduler events"
}

Write-Output ""
Write-Output "Latest scheduler health:"
if (Test-Path -LiteralPath $HealthPath) {
    Get-Content -LiteralPath $HealthPath -Raw
} else {
    Write-Output "  (no scheduler health JSON yet)"
}

Write-Output ""
Write-Output "Latest Phase H scheduler log timestamp:"
if (Test-Path -LiteralPath $LogFile) {
    $last = Get-Content -LiteralPath $LogFile -Tail 1
    Write-Output ("  {0}" -f $last)
    Write-Output ""
    Write-Output "--- last 50 lines of logs\phase_h_scheduler.log ---"
    Get-Content -LiteralPath $LogFile -Tail 50
} else {
    Write-Output "  (no scheduler log yet)"
}
