# =============================================================================
# Phase H Scheduler — uninstall
# Removes ONLY the scheduled task "Hybrid MR-TF Phase H".
# Never deletes: logs, models, observations, reports, or project files.
# =============================================================================
$TaskName = "Hybrid MR-TF Phase H"
$task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($task) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Output "Scheduled task '$TaskName' removed."
} else {
    Write-Output "Task '$TaskName' not found — nothing to remove."
}
Write-Output "Preserved: logs, models, data/forward observations, reports, project files."
