#!/usr/bin/env bash
set -euo pipefail

tool="${1:-}"

choose_tool() {
  printf '%s\n' \
    "Choose the terminal agent to install:" \
    "  1. Claude Code" \
    "  2. Codex" \
    "  3. Both"
  read -r -p "Selection [1-3]: " choice
  case "$choice" in
    1) tool="claude" ;;
    2) tool="codex" ;;
    3) tool="both" ;;
    *) echo "Choose 1, 2, or 3." >&2; exit 2 ;;
  esac
}

confirm_install() {
  local name="$1"
  local url="$2"
  printf '\nInstaller: %s\nOfficial source: %s\n' "$name" "$url"
  read -r -p "Download this installer to a temporary file and run it? [y/N]: " answer
  [[ "$answer" =~ ^[Yy]([Ee][Ss])?$ ]]
}

install_agent_cli() {
  local name="$1"
  local url="$2"
  local shell_name="$3"

  if command -v "$name" >/dev/null 2>&1; then
    echo "$name is already installed:"
    "$name" --version
    return
  fi

  if ! confirm_install "$name" "$url"; then
    echo "Skipped $name."
    return
  fi

  command -v curl >/dev/null 2>&1 || {
    echo "curl is required. Use the official installation page instead." >&2
    exit 1
  }

  local temp_file
  temp_file="$(mktemp "${TMPDIR:-/tmp}/hive-${name}-installer.XXXXXX")"
  trap "rm -f '$temp_file'" EXIT
  curl --fail --location --silent --show-error --proto '=https' --tlsv1.2 "$url" --output "$temp_file"
  if head -n 5 "$temp_file" | grep -Eiq '<!doctype|<html'; then
    echo "The installer URL returned HTML instead of a shell script." >&2
    return 1
  fi
  "$shell_name" "$temp_file"
  rm -f "$temp_file"
  trap - EXIT

  if command -v "$name" >/dev/null 2>&1; then
    echo "$name installation verified:"
    "$name" --version
  else
    echo "$name was installed, but this shell cannot see it yet. Open a new terminal and run '$name --version'."
  fi
}

case "$tool" in
  "") choose_tool ;;
  claude|codex|both) ;;
  *) echo "Usage: bootstrap-agent.sh [claude|codex|both]" >&2; exit 2 ;;
esac

if [[ "$tool" == "claude" || "$tool" == "both" ]]; then
  install_agent_cli "claude" "https://claude.ai/install.sh" "bash"
fi
if [[ "$tool" == "codex" || "$tool" == "both" ]]; then
  install_agent_cli "codex" "https://chatgpt.com/codex/install.sh" "sh"
fi

printf '\n%s\n' \
  "Bootstrap finished. Authentication remains interactive and is never stored in this repository." \
  "Open a new terminal, run 'claude' or 'codex', complete sign-in, then invoke setup-workspace."
