# Agent Team Reference

Last checked against official documentation on 2026-07-14. Re-check the linked pages
before changing installers, CLI flags, or permission modes.

## Bootstrap boundary

The first agent CLI must be installed manually because an uninstalled tool cannot run its
own setup skill. Install CLIs at user level, never inside this repository. After one tool
is running, `setup-agent-team` may verify it, offer the second tool, and rewrite only the
bounded task fields.

## Official installation

Claude Code:

- Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`
- macOS/Linux/WSL: `curl -fsSL https://claude.ai/install.sh | bash`
- Verify: `claude --version` and `claude doctor`
- Source: <https://code.claude.com/docs/en/installation>

Codex:

- Windows PowerShell: `irm https://chatgpt.com/codex/install.ps1 | iex`
- macOS/Linux: `curl -fsSL https://chatgpt.com/codex/install.sh | sh`
- Verify: `codex --version`
- Source: <https://developers.openai.com/codex/cli>

Show the exact command and obtain confirmation before running a downloaded installer.
Authentication is a separate interactive step: launch `claude` or `codex` and let the user
complete the provider's sign-in flow. Never request or store tokens in this repository.

## Team questions

Ask in one compact round:

1. Use Claude Code, Codex, or a mixture?
2. How many terminals, from one to four? Three is the useful default.
3. For each: emoji, short name, role, and tool.
4. Permission posture: review, guided edit, or official auto where supported?
5. Should the task file be changed now? Show the proposed roster first.

Suggested roster:

| Agent | Default role | Default posture |
|---|---|---|
| `🌊 Flow` | primary builder and coordinator | guided edit |
| `🔭 Scout` | research, sources, and orientation | review |
| `🛠 Forge` | implementation and refinement | guided edit |

Keep names to letters, numbers, spaces, `_`, or `-`; keep roles to one short sentence. Do
not embed shell commands, paths, secrets, or provider flags in names or roles.

## Permission mapping

| Requested posture | Claude Code | Codex |
|---|---|---|
| review | `--permission-mode default` | `--sandbox read-only --ask-for-approval on-request` |
| guided edit | `--permission-mode acceptEdits` | `--sandbox workspace-write --ask-for-approval on-request` |
| auto | `--permission-mode auto` only when the account/client supports it | same safe workspace-write/on-request preset |

Claude Code auto mode is a research preview and is not available to every plan, model, or
provider. If eligibility is unknown, use guided edit. Never substitute
`--dangerously-skip-permissions`. Never use Codex `--yolo` or danger-full-access for the
workshop.

## Cursor task contract

`.vscode/tasks.json` contains one task per agent and one compound task. The individual
tasks share `presentation.group: "ai-agent-team"`; VS Code-compatible editors display them
as split terminals. The compound task uses parallel dependencies.

Customization may change only:

- task label;
- `-Tool`/tool argument: `claude` or `codex`;
- name, emoji, role, and mode arguments;
- compound dependency labels.

Preserve the shell commands, script paths, task type, presentation group, and instance
limit. Parse the JSON after edits and run one single-agent task before the whole team.

## Concurrency boundary

Split terminals share the same repository and Git index. Default to one writer: Flow edits,
Scout researches, Forge reviews or waits. For simultaneous edits, create a separate Git
worktree and branch per agent; do not pretend terminal panes provide filesystem isolation.

Official references:

- Claude permission modes: <https://code.claude.com/docs/en/permission-modes>
- Codex sandbox and approvals: <https://developers.openai.com/codex/security>
- VS Code tasks and split terminal groups: <https://code.visualstudio.com/docs/debugtest/tasks>
