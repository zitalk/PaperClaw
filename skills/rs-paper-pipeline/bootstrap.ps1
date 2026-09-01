[CmdletBinding()]
param(
    [switch]$SkipInstall
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$VenvDir = Join-Path $ProjectRoot ".venv"
$VenvPython = Join-Path $VenvDir "Scripts\python.exe"
$EnvFile = Join-Path $ProjectRoot ".env"

Write-Host "[1/5] Project root: $ProjectRoot"

if (-not (Test-Path -LiteralPath $VenvPython)) {
    Write-Host "[2/5] Creating virtual environment: $VenvDir"
    & python -m venv $VenvDir
} else {
    Write-Host "[2/5] Virtual environment already exists: $VenvDir"
}

if (-not $SkipInstall) {
    Write-Host "[3/5] Installing Python dependencies"
    & $VenvPython -m pip install --upgrade pip
    if ($LASTEXITCODE -ne 0) { throw "Failed to upgrade pip." }
    & $VenvPython -m pip install -r (Join-Path $ProjectRoot "requirements.txt")
    if ($LASTEXITCODE -ne 0) { throw "Failed to install Python dependencies." }
} else {
    Write-Host "[3/5] Dependency installation skipped"
}

if (-not (Test-Path -LiteralPath $EnvFile)) {
    Write-Host "[4/5] Creating .env from .env.example"
    Copy-Item -LiteralPath (Join-Path $ProjectRoot ".env.example") -Destination $EnvFile
    Write-Host "      Fill in GITHUB_TOKEN, LLM_API_KEY, and RS_GITHUB_REPO before a full run."
} else {
    Write-Host "[4/5] .env already exists"
}

foreach ($RelativePath in @("memory", "logs", "papers\figures", "tmp")) {
    $Directory = Join-Path $ProjectRoot $RelativePath
    if (-not (Test-Path -LiteralPath $Directory)) {
        New-Item -ItemType Directory -Path $Directory | Out-Null
    }
}

Write-Host "[5/5] Running environment doctor"
Push-Location $ProjectRoot
try {
    & $VenvPython "scripts\cli.py" doctor
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "Doctor found missing configuration. This is expected until .env contains your credentials."
    }
} finally {
    Pop-Location
}

Write-Host ""
Write-Host "Bootstrap complete."
Write-Host "Activate with: .\.venv\Scripts\Activate.ps1"

