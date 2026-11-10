# evals.md — real tasks the brain must handle
Run with brain-evals after any change to AGENTS.md, folders, brain.py, skills or model.
One case per `## <id> <question or task>`, then:
- `Expected:` what a good result looks like (judged).
- `Must contain:` / `Must not contain:` optional exact strings, checked mechanically ("; " separated).
Add a case each time the brain gets something wrong that matters (for example a superseded price).

## context-1 What does my business do and who works there?
Expected: answers like a teammate from context/ notes, citing them, without a deep search.

## connections-1 Give me a Monday catch-up.
Expected: priorities, items needing an answer, people needing attention, from hot.md and the connectors in config.md.

## capabilities-1 Run my most repeated weekly task from a one-line request.
Expected: a real output without many clarifying questions or reinventing the process. Replace this line with the actual task once a skill exists for it.

## cadence-1 Did the last scheduled daily run work?
Expected: log.md has a daily line from the last 24 h and hot.md was rewritten since.
