# Karpathy LLM Wiki — outline (second-hand, NOT the original)
Fetched 2026-11-09 from https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (gist created 2026-04-04, 1 revision). Raw text not retrievable from the cloud session; this is a paraphrased structure only. Replace with the verbatim llm-wiki.md.
- Idea file to paste into an agent so it builds the specifics with you.
- Plain RAG re-derives answers per query; a persistent interlinked markdown wiki maintained by the LLM compounds instead.
- Three layers: immutable raw sources; LLM-owned wiki; schema file (CLAUDE.md / AGENTS.md) for structure and workflows.
- Operations: ingest (one source can touch 10-15 pages); query (good answers filed back); lint (contradictions, stale claims, orphans, missing links, gaps).
- index.md = catalog read first on queries; log.md = append-only, greppable dated prefix per entry (ingest/query/lint).
- Optional local markdown search tool once the index is not enough.
- Tips: Obsidian Web Clipper, local images, graph view, Marp, Dataview, wiki in git.
- Why: maintenance is the bottleneck, LLMs make bookkeeping near free (Memex lineage).
