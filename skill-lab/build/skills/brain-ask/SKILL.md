---
name: brain-ask
description: Answer a question from the second brain with ranked search and citations, flag stale or conflicting notes, check live values through connectors, and file valuable answers back as notes. Use for any question about the user's business, clients, people, projects, prices, past decisions or "what did we decide / when / why", before answering from memory.
---

# brain-ask

Shared rules: `../_shared/contracts.md` §3 (decay) and §7 (write discipline).
Search before answering: a wrong answer from guessing costs more than a search. Skip the search only for self-contained tasks, when the user gave all the context, or when this session already searched the topic. [Cole SOUL recall rule]

## 1. Search (script first)
1. Pick 2-4 search terms: the entity names plus the literal words a note would use (price, rate, tarif, EUR; aliases).
2. `python3 brain.py search "<terms>" -n 8` from the brain root. Results are ranked by relevance, freshness by note type and importance; superseded notes score 0. [guide §5.1]
3. Open only the top results that look relevant (usually 1-3), plus the folder `index.md` if the results are thin. Fall back to `grep -ril` on the terms only if search finds nothing.
4. Asked for history ("what was the price in 2025", "why did we change") → also read superseded and archived notes and `## History` sections, and decisions.md.

## 2. Judge freshness before answering
- Active note past `review_by` → say "as of <updated>". If a connector holds the live value (billing, CRM, calendar), check it and use it; mention the difference if any.
- Two active notes disagree → give the one with the newer `updated` and newer source, say there is a conflict, name both notes. Add one line to the answer: "brain-lint will list it" (do not fix it here).
- `certainty`/draft or `## Open questions` content → present it as unconfirmed.
- Changing operational data (a specific email, today's pipeline) → read the connector; the brain stores insights, not that data.

## 3. Answer
Answer first, in one or two sentences, then the detail. Cite the notes used as `[[note-name]]` (with `updated` date when freshness matters). Say plainly when the brain has no answer, and which note would be the right home for it.

## 4. File good answers back
When the answer is a synthesis worth reusing (comparison, analysis, timeline, decision rationale assembled from several notes), offer once: "Save this as a note?" If yes:
- search first; extend the matching concept or project note if one exists;
- otherwise create `wiki/<kebab-title>.md` with `type: concept`, `sources:` listing the notes used, `summary` answer-first;
- `python3 brain.py index`; append `## [date] ask | <question> | touched: <note>` to log.md.
Plain lookups ("what is Acme's price") are not filed back. [Karpathy query, guide §5]

## 5. Misses
If a search found nothing for something the user expected the brain to know, append `## [date] ask | not found: <terms>` to log.md. brain-lint uses these lines to detect retrieval pressure.
