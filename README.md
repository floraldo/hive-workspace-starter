# Hive Workspace Starter

A beginner-friendly, document-first AI workspace for Claude Code or Codex in Cursor.

The same five-folder lifecycle appears at the workspace root and inside every project:

```text
00-context/   what the work is and what matters
01-input/     source material and incoming items
02-output/    drafts and deliverables
03-status/    current state, tasks, decisions, and next action
04-knowledge/ reviewed learning worth remembering
```

`projects/` is an unnumbered container. Each project repeats the five folders. `apps/`,
`packages/`, and `scripts/` support work that becomes more repeatable over time.

## Start in five minutes

1. On GitHub, choose **Use this template** and create your own repository.
2. Clone your repository and open its folder in Cursor.
3. Install one terminal agent if needed:
   - Claude Code: follow <https://code.claude.com/docs/en/installation>
   - Codex: follow <https://developers.openai.com/codex/cli>
4. Start `claude` or `codex` in Cursor's terminal.
5. Run `/setup-workspace` in Claude Code or `$setup-workspace` in Codex.
6. Run `/setup-agent-team` or `$setup-agent-team` to personalize the split-terminal team.

An AI tool cannot install itself before it exists. The first CLI installation is therefore
the only manual bootstrap; the setup skill can verify it, install an optional second CLI
with approval, and configure the workspace.

## Included

- project-local Claude Code skills in `.claude/skills/`;
- matching Codex skills in `.agents/skills/`;
- durable rules and references instead of one oversized prompt;
- three safe Cursor tasks: `🌊 Flow`, `🔭 Scout`, and `🛠 Forge`;
- a fictional `projects/kinsai-workshop/` example with no client or personal data;
- empty, documented `apps/` and `packages/` areas plus a `scripts/` experimentation area.

## Safety defaults

- Reading personal documents outside this repository requires specific, current consent.
- Credentials and common key files are denied and gitignored.
- External writes, publishing, authentication, and destructive actions require approval.
- Agent launchers never use Claude's bypass-permissions mode or Codex's `--yolo` mode.
- Parallel agents share one working tree, so only one should edit at a time unless the user
  deliberately creates separate Git worktrees.

Read [.claude/reference/workspace-system.md](.claude/reference/workspace-system.md) for the
folder contract and [.claude/reference/agent-team.md](.claude/reference/agent-team.md) for
the launcher model.

## License

MIT. See [LICENSE](LICENSE).
