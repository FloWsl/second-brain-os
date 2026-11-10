---
name: brain-evals
description: Run the second brain's eval cases (evals.md) on a disposable copy of the brain and report pass/fail per case with the cause. Use after any change to AGENTS.md, the folder structure, brain.py, a brain-* skill or the model, or when the user asks to test or check the brain.
---

# brain-evals

Shared rules: `../_shared/contracts.md`. Evals measure real tasks; they never change the real brain. [guide §5.2 step 7; Cole: the four-C audits re-run after every big change]

## 1. Prepare a disposable copy
1. Read `evals.md` at the brain root. No cases → say so, suggest the four-C cases from the template and stop.
2. Copy the brain to a temporary folder (`cp -r <root> <tmp>/brain`, without `.git`). All cases run there with `BRAIN_AUTOMATED=1`, so cases that write (capture, daily, lint) cannot touch the real brain.
3. Note the run context: date, model, git commit of the brain if any, and what changed since the last run (from log.md and git log).

## 2. Run each case in a fresh context
For each `## <id> <task>`, launch one sub-agent with no memory of this session, working directory `<tmp>/brain`, prompt: "You work in this second brain. Read AGENTS.md and hot.md first. Task: <task>". It uses the brain-* skills like a normal session. Collect its final answer and the list of files it changed (`diff -r` against a pristine copy, or git status in the copy).
Run independent cases in parallel; reset the copy between cases that write.

## 3. Judge
- **Mechanical first**: every `Must contain:` string present, every `Must not contain:` string absent (case-insensitive). Any miss = fail, no judgment needed.
- **Then judged**: compare the answer and changed files with `Expected:`. Pass only if a reasonable user would accept it as is. Partial = fail, with what was missing.
- For each fail, name the most likely root cause: wrong or missing note, stale fact won (decay), routing (AGENTS.md or index), skill instruction, script bug, model behaviour.

## 4. Record (the only writes to the real brain)
1. `evals/results/<date>.md`: run context, then a table `case | expected | actual (short) | pass/fail | root cause`, then the totals.
2. Compare with the previous results file: list cases that regressed or got fixed.
3. Append to log.md: `## [date] evals | <passed>/<total>, <regressions> regressions | touched: evals/results/<date>.md`.
4. Delete the temporary copy.

## 5. Report
Score, regressions first, then each fail with its root cause and the smallest fix you suggest (a note to correct, a line for AGENTS.md, a skill change). Do not apply fixes here: the user decides, then re-runs brain-evals.
When the brain got something important wrong in real use, suggest adding it as a new case in evals.md.
