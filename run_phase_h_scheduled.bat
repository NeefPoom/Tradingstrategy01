@echo off
REM Phase H scheduled runner wrapper — launches the PowerShell runner.
REM No ML logic here; the PowerShell script is the source of truth.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "E:\hybrid_mr_tf_ml_rading\run_phase_h_scheduled.ps1"
exit /b %ERRORLEVEL%
