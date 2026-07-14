# Hive Workspace Starter

A beginner-friendly, document-first AI workspace for Claude Code or Codex in Cursor.

**Giving or taking the Claude Code workshop? Start with [START-HERE.md](START-HERE.md).** It is
the short, numbered Cursor path from a fresh clone to a first Flow agent.

## Before you start

- Install [Cursor](https://www.cursor.com/downloads).
- Install [Git](https://git-scm.com/downloads) or GitHub Desktop. Git for Windows is
  recommended for native Windows Claude Code.
- Have access to an eligible Claude Code or Codex account. A GitHub account is needed only
  when you want your own remote repository.

## Get your copy

### Recommended: create your own repository

Choose [Use this template](https://github.com/floraldo/hive-workspace-starter/generate),
then clone the repository GitHub creates for you. Its `origin` will already be yours.

### Clone a local workshop copy

Anyone can clone the public starter without a GitHub seat or write access:

```bash
git clone https://github.com/floraldo/hive-workspace-starter.git my-ai-workspace
cd my-ai-workspace
```

A direct clone is fully editable on your computer, but its `origin` still points to the
public starter and normally cannot be pushed by participants. Keep it local, or run
`setup-workspace` and ask it to connect the copy to a repository you own.

## Use Claude Code in Cursor

When Cursor opens this workspace, it recommends Anthropic's **Claude Code** extension. Install
it and sign in for the easiest visual experience: plans and edits appear in Cursor rather than
only in a terminal. The workspace sets new graphical Claude conversations to **plan** mode and
keeps bypass permissions unavailable.

The extension is recommended, not silently installed. The terminal agent team below needs the
separate CLI install because the extension's private CLI is not added to your terminal `PATH`.
See [Anthropic's Cursor/VS Code guide](https://code.claude.com/docs/en/ide-integrations) for
extension installation and troubleshooting.

## Install the first terminal agent

An uninstalled AI agent cannot run its own setup skill, so installation is the one manual
bootstrap. The included script shows the official source, downloads to a temporary file, and
asks again before executing it.

For the Claude workshop, use **Terminal → Run Task → 1. Install — Claude Code**. It
preselects Claude Code while retaining the confirmation gate. Choose
**Optional — Install Codex or Both** only when you want the broader tool choice.

Windows PowerShell:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\bootstrap-agent.ps1 -Tool claude
```

macOS, Linux, or WSL:

```bash
bash scripts/bootstrap-agent.sh claude
```

The CLI installs at user level, never inside this repository. Authentication remains in the
provider's own interactive flow and no token is written here. After installation, close that
terminal, open a new one, and run:

```text
claude --version
```

If the version check fails or something looks wrong, run `claude doctor`.

Then start **2. Start 🌊 Flow (Claude)** from Cursor's task picker. That task opens the normal
browser sign-in when needed and starts the workspace session. In Flow, invoke the exact command
`/setup-workspace`.

If you chose Codex instead, run `codex --version`, then `codex`, and invoke
`$setup-workspace`. Next run `/setup-agent-team` in Claude Code or `$setup-agent-team` in
Codex to tailor the team after the first agent is working.

## Folder system

The same lifecycle appears at root and inside every project:

```text
00-context/   what the work is and what matters
01-input/     source material and incoming items
02-output/    drafts and deliverables
03-status/    current state, tasks, decisions, and next action
04-knowledge/ reviewed learning worth remembering

projects/
  <project>/
    00-context/
    01-input/
    02-output/
    03-status/
    04-knowledge/
```

`projects/` is an unnumbered container. `apps/`, `packages/`, and `scripts/` support work
that becomes more repeatable over time.

## What is in `.claude/`

| Area | Purpose |
|---|---|
| `.claude/CLAUDE.md` | Small, always-loaded workspace map and behavior contract |
| `.claude/settings.json` | Schema-backed secret-file read denies and disabled dynamic skill shell execution |
| `.claude/rules/` | Lifecycle, safety, source-integrity, promotion, and multi-agent rules |
| `.claude/reference/` | Detailed folder, interview/privacy, GitHub, and agent-team contracts loaded on demand |
| `.claude/skills/` | Six explicit workflows listed below |

The equivalent Codex entry points live in `.agents/skills/` and route to the same canonical
skill bodies, so the two tools cannot silently develop different procedures.

| Skill | What it does |
|---|---|
| `setup-workspace` | Interviews the owner, personalizes bounded context/status fields, applies the personal-document consent gate, creates a first project, and optionally connects GitHub |
| `setup-agent-team` | Verifies/installs CLIs and configures one to four Cursor terminal agents |
| `session-open` | Reads context and status, then offers a focused next outcome without editing |
| `new-project` | Copies the exact five-folder project template and fills its brief/status |
| `capture` | Routes a new item to the correct lifecycle folder with provenance |
| `session-close` | Leaves clean status, decisions, knowledge, and one next action |

All Claude skills are user-invoked. They do not grant themselves pre-approved tools.

## Cursor agent team

The starter includes three safe defaults. Run them manually from **Terminal → Run Task**;
opening a folder never starts an installer or an agent automatically.

- `🌊 Flow` — primary builder and coordinator;
- `🔭 Scout` — research and orientation;
- `🛠 Forge` — bounded review and refinement.

Start with **2. Start 🌊 Flow (Claude)**. When you are ready for the demonstration, choose
**Optional — 🤖 Start 3-Agent Demo** to open all three in a shared split-terminal group. The
panes share one working tree and Git index, so Flow is the only default writer; Scout and Forge
are review agents. Use separate Git worktrees for deliberate concurrent editing.

Claude tasks use official `default`, `acceptEdits`, or eligible `auto` permission modes.
Codex tasks use read-only or the documented workspace-write/on-request Auto preset. No task
uses bypass-permissions, `--yolo`, danger-full-access, or approval-never flags.

## Apps, packages, scripts, and connectors

- Start with a manual checklist or conversation.
- Put a one-off repeatable experiment in `scripts/`.
- Promote logic to `packages/` after reuse by at least two workflows or when it needs
  tests, schemas, versioning, or a stable contract.
- Put a stable human-facing entry point in `apps/`.
- Treat Drive, Gmail, Calendar, Notion, Slack, and CRMs as scoped connectors first.

Empty `apps/` and `packages/` folders are a correct beginner state.

## Safety and validation

- Outside-repository document access needs exact, current, read-only consent first.
- Common secret paths are gitignored and denied to Claude's built-in file-reading tools.
  This is not an operating-system security boundary; arbitrary shell access still requires
  care and approval.
- External writes, authentication, publishing, and destructive changes require approval.
- `scripts/validate-starter.py` deterministically checks the lifecycle, settings, skill
  parity, Cursor task contract, bootstrap URLs, and placeholder scope.
- GitHub Actions runs the same validator plus Bash and PowerShell syntax checks.

Optional local check when Python is installed:

```bash
python scripts/validate-starter.py
```

The fictional `projects/kinsai-workshop/` example contains no client or personal data.

Read [.claude/reference/workspace-system.md](.claude/reference/workspace-system.md) for the
folder contract and [.claude/reference/agent-team.md](.claude/reference/agent-team.md) for
the launcher contract.

## License

MIT. See [LICENSE](LICENSE).
