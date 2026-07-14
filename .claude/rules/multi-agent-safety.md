---
paths:
  - ".vscode/**"
  - "scripts/launch-agent.*"
---

# Multi-Agent Safety

- Cursor split terminals are separate conversations, not isolated filesystems.
- Use one editing agent at a time in a shared working tree.
- Assign research/review roles read-only when another agent is editing.
- For genuine concurrent editing, create a separate Git worktree and branch per agent.
- Never enable permission bypass flags to make a demo feel smoother.
- Review `git status` before staging or committing; never sweep unrelated changes into a
  commit.
