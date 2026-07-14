# Scripts

Use this folder for throwaway experiments, one-off migrations, and small helpers while a
workflow is still being learned.

At the top of a script, state its purpose, inputs, outputs, side effects, safe run command,
and likely deletion date. If the same logic serves multiple workflows or needs tests and a
stable contract, promote it to `packages/`.

The two `launch-agent` scripts are deliberate workspace infrastructure used by Cursor
tasks, not business logic.
