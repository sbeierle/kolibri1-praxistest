# NIS2-Erstcheck + Meldepflicht-Triage. Reines ASCII.
# Aufruf im Ordner praxistest:  powershell -ExecutionPolicy Bypass -File .\run_nis2.ps1
# Voraussetzung: Pod laeuft, SSH-Tunnel auf localhost:8000 steht.
$ErrorActionPreference = "Continue"
$base = "http://localhost:8000/v1"
$log  = "..\nis2_log.txt"
try { $m = Invoke-RestMethod -Uri "$base/models" -TimeoutSec 15; Write-Host "Server OK: $($m.data[0].id)" }
catch { Write-Host "FEHLER: Server nicht erreichbar. Tunnel pruefen." -ForegroundColor Red; exit 1 }
function Run-Step($name, $arguments) {
    Write-Host "`n===== $name  ($(Get-Date -Format HH:mm:ss)) =====" -ForegroundColor Cyan
    "`n===== $name  $(Get-Date -Format s) =====" | Out-File -Append -Encoding utf8 $log
    & python praxistest.py @arguments 2>&1 | Tee-Object -Append -FilePath $log
}
$c = @("--base-url", $base, "--workers", "8", "--system-file", "system.txt", "--effort", "low")
Run-Step "1/7 erstcheck T0.3" (@("run") + $c + @("--suite","erstcheck","--repeats","5","--temperature","0.3","--out","..\n_erst_t03"))
Run-Step "2/7 triage T0.3"    (@("run") + $c + @("--suite","triage","--repeats","5","--temperature","0.3","--out","..\n_tri_t03"))
Run-Step "3/7 erstcheck T1.0" (@("run") + $c + @("--suite","erstcheck","--repeats","5","--temperature","1.0","--out","..\n_erst_t10"))
Run-Step "4/7 triage T1.0"    (@("run") + $c + @("--suite","triage","--repeats","5","--temperature","1.0","--out","..\n_tri_t10"))
Run-Step "5/7 luecken T0.3"   (@("run") + $c + @("--suite","luecken","--repeats","5","--temperature","0.3","--out","..\n_luecken"))
Run-Step "6/7 beleg T0.3"     (@("run") + $c + @("--suite","beleg","--repeats","5","--temperature","0.3","--out","..\n_beleg"))
Run-Step "7/7 langer Text 8k+32k" (@("run") + $c + @("--suite","longctx","--longctx","--longctx-sizes","8000,32000","--repeats","3","--temperature","0.3","--out","..\n_longctx"))
Write-Host "`nAuswertung:" -ForegroundColor Cyan
& python nis2_auswertung.py ..\n_erst_t03 ..\n_tri_t03 ..\n_erst_t10 ..\n_tri_t10 2>&1 | Tee-Object -Append -FilePath $log
Write-Host "`nFERTIG $(Get-Date -Format HH:mm:ss). Ordner ..\n_*  Log: $log" -ForegroundColor Green
