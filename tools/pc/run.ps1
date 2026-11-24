# ail-train on the Windows PC (RTX 3070, 8 GB). Paste from the repository root in PowerShell:
#
#   powershell -ExecutionPolicy Bypass -File tools\pc\run.ps1 setup        # first time: WSL2, Ubuntu, CUDA Python, ail
#   powershell -ExecutionPolicy Bypass -File tools\pc\run.ps1 preflight    # measure VRAM and speed of both models
#   powershell -ExecutionPolicy Bypass -File tools\pc\run.ps1 build        # build data/build with the PC's ail and tokenizer
#   powershell -ExecutionPolicy Bypass -File tools\pc\run.ps1 train small  # LoRA on the autocomplete model
#   powershell -ExecutionPolicy Bypass -File tools\pc\run.ps1 train big    # QLoRA on the whole-program model
#   powershell -ExecutionPolicy Bypass -File tools\pc\run.ps1 eval small   # quick eval of the newest run (or: eval small base)
#   powershell -ExecutionPolicy Bypass -File tools\pc\run.ps1 evalloop big # eval + up to 3 ail check correction rounds
#   powershell -ExecutionPolicy Bypass -File tools\pc\run.ps1 export small # merged weights + GGUF for the Mac
#
# Everything runs inside WSL2 Ubuntu (tools/pc/run.sh); this file only sets WSL up, copies this checkout into the
# Linux file system (~/ail-train-work/ail-train, much faster than /mnt/c) and keeps Windows awake while a job runs.
# Environment for run.sh (MAX_STEPS, LR, RANK, ...) passes through with the WSLENV rule below: set $env:AILT_ARGS to
# "NAME=value NAME=value". Reads config.local at the repository root (copied with the checkout).
param([Parameter(Position = 0)][string]$Task = "help", [Parameter(Position = 1)][string]$What = "", [Parameter(Position = 2)][string]$Extra = "")
$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$distro = "Ubuntu-24.04"

function Die($m) { Write-Host "run.ps1: $m" -ForegroundColor Red; exit 2 }

if ($Task -eq "help") { Get-Content $PSCommandPath | Select-Object -First 15; exit 0 }
if (-not (Get-Command nvidia-smi -ErrorAction SilentlyContinue)) { Die "no nvidia-smi: install the current NVIDIA Game Ready or Studio driver first" }

# 1. WSL2 and the Ubuntu distribution (first run only; needs an administrator prompt and maybe a reboot).
$have = $false
try { $have = ((wsl.exe -l -q 2>$null) -replace "`0", "" | Where-Object { $_.Trim() -eq $distro }).Count -gt 0 } catch { }
if (-not $have) {
    Write-Host "Installing WSL2 and $distro (Windows asks for administrator approval)."
    Start-Process wsl.exe -ArgumentList "--install -d $distro --no-launch" -Verb RunAs -Wait
    Write-Host "If Windows asked for a reboot, reboot and run this command again."
    Write-Host "Otherwise open '$distro' from the Start menu once to choose a Linux user name and password, then run this again."
    exit 0
}

# 2. Give WSL enough memory to merge the big model (bf16 weights on the CPU), once, if there is no .wslconfig.
$wslcfg = Join-Path $env:USERPROFILE ".wslconfig"
if (-not (Test-Path $wslcfg)) {
    $gb = [math]::Floor((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB)
    $mem = [math]::Max(8, [math]::Floor($gb * 0.75))
    "[wsl2]`nmemory=${mem}GB`nswap=16GB`n" | Set-Content -Encoding ascii $wslcfg
    Write-Host "Wrote $wslcfg (memory ${mem}GB of ${gb}GB, swap 16GB); restarting WSL."
    wsl.exe --shutdown
}

# 3. Root setup inside Ubuntu (no sudo password needed this way).
if ($Task -eq "setup") {
    wsl.exe -d $distro -u root -- bash -c "apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3-venv python3-dev build-essential cmake git curl rsync >/dev/null && echo apt ok"
    if ($LASTEXITCODE -ne 0) { Die "apt setup failed" }
}

# 4. Copy this checkout (with .git, for the commit stamp) into the Linux file system.
$wroot = (wsl.exe -d $distro -- wslpath -a ($root -replace "\\", "/")).Trim()
wsl.exe -d $distro -- bash -c "mkdir -p ~/ail-train-work && rsync -a --delete --exclude data/build/ --exclude runs/ '$wroot/' ~/ail-train-work/ail-train/"
if ($LASTEXITCODE -ne 0) { Die "could not copy the checkout into WSL" }

# 5. Keep Windows awake while the job runs (like caffeinate on the Mac).
Add-Type -Namespace AilTrain -Name Power -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint f);'
[void][AilTrain.Power]::SetThreadExecutionState([uint32]"0x80000001")   # ES_CONTINUOUS | ES_SYSTEM_REQUIRED
try {
    $envs = if ($env:AILT_ARGS) { $env:AILT_ARGS } else { "" }
    wsl.exe -d $distro -- bash -lc "cd ~/ail-train-work/ail-train && env $envs bash tools/pc/run.sh '$Task' '$What' '$Extra'"
    $rc = $LASTEXITCODE
} finally {
    [void][AilTrain.Power]::SetThreadExecutionState([uint32]"0x80000000")
}
# Bring the built data and run summaries back next to the Windows checkout, so they can be read from Windows too.
wsl.exe -d $distro -- bash -c "mkdir -p '$wroot/data/build' && rsync -a ~/ail-train-work/ail-train/data/build/ '$wroot/data/build/' 2>/dev/null; true"
exit $rc
