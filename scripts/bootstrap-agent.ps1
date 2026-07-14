[CmdletBinding()]
param(
    [ValidateSet("claude", "codex", "both")]
    [string]$Tool
)

$ErrorActionPreference = "Stop"

function Confirm-Install {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name,
        [Parameter(Mandatory = $true)]
        [string]$Url
    )

    Write-Host ""
    Write-Host "Installer: $Name"
    Write-Host "Official source: $Url"
    $answer = Read-Host "Download this installer to a temporary file and run it? [y/N]"
    return $answer -match '^(?i:y|yes)$'
}

function Install-AgentCli {
    param(
        [Parameter(Mandatory = $true)]
        [ValidateSet("claude", "codex")]
        [string]$Name,
        [Parameter(Mandatory = $true)]
        [string]$Url
    )

    if (Get-Command $Name -ErrorAction SilentlyContinue) {
        Write-Host "$Name is already installed:"
        & $Name --version
        return
    }

    if (-not (Confirm-Install -Name $Name -Url $Url)) {
        Write-Host "Skipped $Name."
        return
    }

    $tempFile = Join-Path ([IO.Path]::GetTempPath()) ("hive-{0}-installer-{1}.ps1" -f $Name, [guid]::NewGuid().ToString("N"))
    try {
        Invoke-WebRequest -UseBasicParsing -Uri $Url -OutFile $tempFile
        $firstLines = (Get-Content -LiteralPath $tempFile -TotalCount 5) -join "`n"
        if ($firstLines -match '(?i)<!doctype|<html') {
            throw "The installer URL returned HTML instead of a PowerShell script."
        }
        & $tempFile
        if ($LASTEXITCODE -and $LASTEXITCODE -ne 0) {
            throw "$Name installer exited with code $LASTEXITCODE."
        }
    }
    finally {
        Remove-Item -LiteralPath $tempFile -Force -ErrorAction SilentlyContinue
    }

    if (Get-Command $Name -ErrorAction SilentlyContinue) {
        Write-Host "$Name installation verified:"
        & $Name --version
    }
    else {
        Write-Host "$Name was installed, but this terminal cannot see it yet. Open a new terminal and run '$Name --version'."
    }
}

if (-not $Tool) {
    Write-Host "Choose the terminal agent to install:"
    Write-Host "  1. Claude Code"
    Write-Host "  2. Codex"
    Write-Host "  3. Both"
    $choice = Read-Host "Selection [1-3]"
    $Tool = switch ($choice) {
        "1" { "claude" }
        "2" { "codex" }
        "3" { "both" }
        default { throw "Choose 1, 2, or 3." }
    }
}

if ($Tool -in @("claude", "both")) {
    Install-AgentCli -Name "claude" -Url "https://claude.ai/install.ps1"
}
if ($Tool -in @("codex", "both")) {
    Install-AgentCli -Name "codex" -Url "https://chatgpt.com/codex/install.ps1"
}

Write-Host ""
Write-Host "Bootstrap finished. Authentication remains interactive and is never stored in this repository."
Write-Host "Open a new terminal, run 'claude' or 'codex', complete sign-in, then invoke setup-workspace."
