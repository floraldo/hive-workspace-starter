param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("claude", "codex")]
    [string]$Tool,

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[\p{L}\p{N} _-]+$')]
    [string]$Name,

    [Parameter(Mandatory = $true)]
    [string]$Emoji,

    [Parameter(Mandatory = $true)]
    [ValidateLength(1, 120)]
    [string]$Role,

    [Parameter(Mandatory = $true)]
    [ValidateSet("standard", "edit", "auto")]
    [string]$Mode
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command $Tool -ErrorAction SilentlyContinue)) {
    throw "'$Tool' is not installed or is not on PATH. Run setup-agent-team first."
}

$env:AI_AGENT_NAME = $Name
$env:AI_AGENT_ROLE = $Role
$prompt = "You are $Emoji $Name, the workspace agent for: $Role. Read the repository instructions and current status. Do not edit until the user gives you a bounded task."

Write-Host "$Emoji Starting $Name with $Tool ($Mode mode)"

if ($Tool -eq "claude") {
    $permissionMode = switch ($Mode) {
        "standard" { "default" }
        "edit" { "acceptEdits" }
        "auto" { "auto" }
    }
    & claude --permission-mode $permissionMode $prompt
    exit $LASTEXITCODE
}

$codexArgs = if ($Mode -eq "standard") {
    @("--sandbox", "read-only", "--ask-for-approval", "on-request")
} else {
    @("--sandbox", "workspace-write", "--ask-for-approval", "on-request")
}

& codex @codexArgs $prompt
exit $LASTEXITCODE
