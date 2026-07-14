#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 5 ]]; then
  echo "Usage: launch-agent.sh <claude|codex> <name> <emoji> <role> <standard|edit|auto>" >&2
  exit 2
fi

tool="$1"
name="$2"
emoji="$3"
role="$4"
mode="$5"

[[ "$tool" == "claude" || "$tool" == "codex" ]] || { echo "Unsupported tool: $tool" >&2; exit 2; }
[[ "$mode" == "standard" || "$mode" == "edit" || "$mode" == "auto" ]] || { echo "Unsupported mode: $mode" >&2; exit 2; }
[[ "$name" =~ ^[[:alnum:][:space:]_-]+$ ]] || { echo "Name may contain letters, numbers, spaces, _ or - only." >&2; exit 2; }
(( ${#role} <= 120 )) || { echo "Role must be 120 characters or fewer." >&2; exit 2; }
command -v "$tool" >/dev/null 2>&1 || { echo "'$tool' is not installed or is not on PATH. Run setup-agent-team first." >&2; exit 1; }

export AI_AGENT_NAME="$name"
export AI_AGENT_ROLE="$role"
prompt="You are $emoji $name, the workspace agent for: $role. Read the repository instructions and current status. Do not edit until the user gives you a bounded task."

echo "$emoji Starting $name with $tool ($mode mode)"

if [[ "$tool" == "claude" ]]; then
  case "$mode" in
    standard) permission_mode="default" ;;
    edit) permission_mode="acceptEdits" ;;
    auto) permission_mode="auto" ;;
  esac
  exec claude --permission-mode "$permission_mode" "$prompt"
fi

if [[ "$mode" == "standard" ]]; then
  exec codex --sandbox read-only --ask-for-approval on-request "$prompt"
fi

exec codex --sandbox workspace-write --ask-for-approval on-request "$prompt"
