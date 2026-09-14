$logPath = "$env:TEMP\lemonade-server.log"
$configPath = "$env:USERPROFILE\.config\lemonade\config.json"

Write-Host "=== Lemonade Server Locations & Content ===" -ForegroundColor Cyan

# 1. Config File
Write-Host "`n[+] Config Location: $configPath" -ForegroundColor Green
if (Test-Path $configPath) {
    Write-Host "--- Config Content ---" -ForegroundColor DarkGray
    Get-Content $configPath -Raw | ConvertFrom-Json | ConvertTo-Json -Depth 10
} else {
    Write-Host "Config file not found." -ForegroundColor Yellow
}

# 2. Log File
Write-Host "`n[+] Log Location: $logPath" -ForegroundColor Green
if (Test-Path $logPath) {
    Write-Host "--- Log Content (Last 50 lines) ---" -ForegroundColor DarkGray
    Get-Content $logPath -Tail 50
} else {
    Write-Host "Log file not found." -ForegroundColor Yellow
}