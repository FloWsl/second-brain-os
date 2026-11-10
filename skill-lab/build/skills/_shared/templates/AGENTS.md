# AGENTS.md — second brain map

Read this, then hot.md. Open other files only when the task needs them.
Full formats: contracts.md in the brain-* skills. Below is what every session needs.

## Where things live (read the folder's index.md first)
- context/   who I am, business, ICP, offer and prices, voice, config. Canonical. Edit only when I state a change.
- projects/<name>/about.md   entry point per project: status, decisions, next step. Link it as [[<name>]].
- clients/ people/   one file per entity, kebab-case: clients/acme-corp.md
- notes/daily/YYYY-MM-DD.md   today's state. notes/inbox.md   capture queue (use queue.py). notes/ideas.md
- wiki/   syntheses; wiki/sources/   summaries of raw documents.
- decisions.md   dated decisions with reason. log.md   append-only history. hot.md   this week.
- raw/ archive/   read-only.

## Rules (why in brackets)
- Find before you write: `python3 brain.py search "<terms>"`, open the top results only. [cheaper than grep, ranks fresh notes first]
- Extend the matching note; never create a near-duplicate. [duplicates drift apart]
- One fact, one file. Link with [[note-name]] instead of copying. [one edit updates everything]
- Frontmatter on every note: type, status, updated, review_by, summary. Bump `updated` on real edits only. [ranking and review]
- When a fact changes, rewrite it or mark the old note `status: superseded` with `superseded_by`. [stale facts win otherwise]
- Skip superseded notes unless I ask for history. If two active notes disagree, prefer the newer `updated` and tell me.
- Past `review_by`: say "as of <updated>" and check the live tool if there is one.
- Numbers carry their date and source. Write absolute dates, never "last week".
- Email, CRM, payments: read through the connector, do not copy into notes. Store insights only.
- Log decisions with their reason in decisions.md.
- After creating or renaming notes: `python3 brain.py index`.
- End of a working session: offer /done.
- Always act in the best interest of the business, based on our goals and strategy. If a request conflicts with that, say so instead of just agreeing.
