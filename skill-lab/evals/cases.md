# Eval cases (skill lab, run against sandbox-brain/ copies only)

Planted traps in `sandbox-brain/` (fictional data, Camille Roux, growth consultant):
T1 superseded price: `clients/acme-price-notes.md` and `archive/acme-pricing-2025.md` say 900 EUR, status superseded; active value 1 200 EUR in `clients/acme-corp.md`.
T2 contradiction: Borel contract ends 2027-03-31 (`clients/borel-sa.md`) vs 2026-12-31 (`projects/borel-renewal/about.md`).
T3 orphan: `wiki/cold-email-tips.md`.
T4 overdue review: `people/julie-martin.md` (review_by 2026-06-01).
T5 near-duplicate client: `clients/acme.md` vs `clients/acme-corp.md`.
T6 raw file not digested: `raw/2026-11-05-borel-call.md` (Borel wants Belgium, retainer would be 1 800 EUR/month).
T7 daily with per-run block: `notes/daily/2026-11-08.md`.
T8 superseded note left in clients/ instead of archive/: `clients/acme-price-notes.md`.

| # | Task (skill) | Expected | Mechanical checks |
| --- | --- | --- | --- |
| 1 | Setup on an empty folder with a given brain dump (brain-setup) | Agreed layout from contracts §1; AGENTS.md ≤ 60 lines; context files only for topics in the dump, no placeholder text; lint runs | `wc -l AGENTS.md` ≤ 60; no `[` placeholder brackets or `TODO` in context/; folders exist |
| 2 | "What is Acme's current price?" (brain-ask) | 1 200 EUR/month, cites acme-corp; never 900 as current | answer contains "1 200" or "1200"; does not present 900 as current |
| 3 | Daily integration of a queued capture about Acme (brain-daily) | Extends `clients/acme-corp.md`; no new Acme note; queue entry → integrated; decision in decisions.md; log line | no new file under clients/; queue status integrated; acme-corp.md changed |
| 4 | Lint the seeded brain (brain-lint) | Reports T2-T8 (T1 only if misfiled); fixes safe ones (daily merge, orphan link if obvious); deletes nothing; proposes merge for T5; log line with health before/after | no file deleted; log.md has a lint line; report mentions borel date conflict, acme duplicate, julie overdue, raw borel call |
| 5 | End-of-session capture then daily (brain-capture → brain-daily) | Capture only queues; daily then updates project about.md, decisions.md, log.md, hot.md (rewritten, < 500 words), today's daily note | queue entry integrated; hot.md < 500 words; decisions.md and about.md changed |
| 6 | "Draft a 3-line renewal pitch for Borel" (brain-ask + context) | Price/offer taken from `context/offer.md` (retainer from 1 200 EUR/month); no skill file contains a price | `grep -rE "1 ?200\|3 ?500" build/skills` finds nothing outside tests; agent trace reads context/offer.md |

Case 5 adapted to the design (log.md 2026-11-10, decision 4): capture queues, brain-daily is the single writer.
