# Runde 2b: Wiederholung mit sauberem System-Prompt (aus system.txt, UTF-8). Skript ist bewusst reines ASCII.
# Aufruf im Ordner praxistest:  powershell -ExecutionPolicy Bypass -File .\run_all2.ps1
$ErrorActionPreference = "Continue"
$base = "http://localhost:8000/v1"
$log  = "..\runde2b_log.txt"
try { $m = Invoke-RestMethod -Uri "$base/models" -TimeoutSec 15; Write-Host "Server OK: $($m.data[0].id)" }
catch { Write-Host "FEHLER: Server nicht erreichbar. Tunnel pruefen." -ForegroundColor Red; exit 1 }

# Kontrolle: Prompt kommt sauber an?
python -c "import sys; t=open('system.txt',encoding='utf-8-sig').read(); print('Prompt-Kontrolle:', t[:90].encode('utf-8').decode('utf-8'))"

function Run-Step($name, $arguments) {
    Write-Host "`n===== $name  ($(Get-Date -Format HH:mm:ss)) =====" -ForegroundColor Cyan
    "`n===== $name  $(Get-Date -Format s) =====" | Out-File -Append -Encoding utf8 $log
    & python praxistest.py @arguments 2>&1 | Tee-Object -Append -FilePath $log
}
$c = @("--base-url", $base, "--workers", "8", "--system-file", "system.txt")

Run-Step "1/7 abstain, low"       (@("run") + $c + @("--effort","low","--suite","abstain","--repeats","10","--out","..\r2_abstain"))
Run-Step "2/7 rag, low"           (@("run") + $c + @("--effort","low","--suite","rag","--repeats","10","--out","..\r2_rag"))
Run-Step "3/7 praxis, low"        (@("run") + $c + @("--effort","low","--suite","praxis","--repeats","10","--out","..\r2_praxis"))
Run-Step "4/7 inject, low"        (@("run") + $c + @("--effort","low","--suite","inject","--repeats","10","--out","..\r2_inject"))
Run-Step "5/7 nis2+kanzlei T0.3 low"    (@("run") + $c + @("--effort","low","--suite","nis2,kanzlei","--repeats","10","--temperature","0.3","--out","..\r2_t03"))
Run-Step "6/7 nis2+kanzlei T1.0 low"    (@("run") + $c + @("--effort","low","--suite","nis2,kanzlei","--repeats","10","--temperature","1.0","--out","..\r2_t10"))
Run-Step "7/7 nis2+kanzlei T0.3 medium" (@("run") + $c + @("--effort","medium","--suite","nis2,kanzlei","--repeats","10","--temperature","0.3","--out","..\r2_t03_medium"))
Write-Host "`nFERTIG $(Get-Date -Format HH:mm:ss). Ordner ..\r2_*  Log: $log" -ForegroundColor Green
