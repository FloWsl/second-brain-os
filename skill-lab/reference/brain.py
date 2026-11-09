#!/usr/bin/env python3
"""brain.py - markdown-only second brain helper (stdlib only).
  python3 brain.py index              # rebuild index.md in every folder
  python3 brain.py search "acme price" [-n 5]
  python3 brain.py lint               # report problems, exit 1 if any
"""
import datetime as dt, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP = {"raw", "archive", ".git", ".obsidian", ".claude"}
SPECIAL = {"index.md", "AGENTS.md", "CLAUDE.md", "log.md", "hot.md"}
HALF_LIFE = {"project": 30, "entity": 180, "concept": 365, "source": 365,
             "log": 7, "inbox": 3}            # days; types absent = no decay
STATUS_MULT = {"active": 1.0, "draft": 0.8, "archived": 0.3, "superseded": 0.0}
W_REL, W_REC, W_IMP = 1.0, 1.0, 1.0
TODAY = dt.date.today()
LINK = re.compile(r"\[\[([^\]|#]+)")


def parse(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" in line and not line.startswith(" "):
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
            body = text[end + 4:]
    return meta, body


def date(s):
    try:
        return dt.date.fromisoformat(s[:10])
    except (TypeError, ValueError):
        return None


def notes():
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in SKIP or p.name in SPECIAL:
            continue
        meta, body = parse(p)
        yield p, meta, body


def score(meta, body, stem, terms):
    head = " ".join([stem.replace("-", " "), meta.get("title", ""),
                     meta.get("aliases", ""), meta.get("summary", "")]).lower()
    text = body.lower()
    hits = sum(2 if t in head else 1 if t in text else 0 for t in terms)
    relevance = hits / (2 * len(terms))
    if relevance == 0:
        return 0.0
    upd = date(meta.get("updated", "")) or TODAY
    hl = HALF_LIFE.get(meta.get("type", ""))
    recency = 1.0 if hl is None else 0.5 ** ((TODAY - upd).days / hl)
    importance = int(meta.get("importance", 3) or 3) / 5
    mult = STATUS_MULT.get(meta.get("status", "active"), 1.0)
    return mult * (W_REL * relevance + W_REC * recency + W_IMP * importance)


def cmd_search(query, n=5):
    terms = [t for t in query.lower().split() if len(t) > 2]
    ranked = sorted(((score(m, b, p.stem, terms), p, m) for p, m, b in notes()),
                    key=lambda x: x[0], reverse=True)
    for s, p, m in [r for r in ranked if r[0] > 0][:n]:
        print(f"{s:.2f}  {p.relative_to(ROOT)}  ({m.get('updated', '?')}) "
              f"{m.get('summary', '')}")


def cmd_index():
    by_dir = {}
    for p, m, _ in notes():
        by_dir.setdefault(p.parent, []).append((p, m))
    for d, items in by_dir.items():
        groups = {}
        for p, m in items:
            groups.setdefault(m.get("status", "active"), []).append((p, m))
        out = [f"# {d.relative_to(ROOT) or 'root'}/ index "
               f"(generated {TODAY}, {len(items)} notes)"]
        for status in ["active", "draft", "archived", "superseded"]:
            rows = sorted(groups.get(status, []),
                          key=lambda x: x[1].get("updated", ""), reverse=True)
            if rows:
                out.append(f"\n## {status}")
                out += [f"- [[{p.stem}]] (updated {m.get('updated', '?')}, "
                        f"imp {m.get('importance', '?')}): {m.get('summary', '')}"
                        for p, m in rows]
        (d / "index.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"indexed {sum(len(v) for v in by_dir.values())} notes "
          f"in {len(by_dir)} folders")


def cmd_lint():
    all_md = {p.stem for p in ROOT.rglob("*.md")}
    linked, problems, titles = set(), [], {}
    for p, m, b in notes():
        rel = p.relative_to(ROOT)
        for field in ("type", "status", "updated", "summary"):
            if not m.get(field):
                problems.append(f"{rel}: missing frontmatter '{field}'")
        targets = set(LINK.findall(b))
        for f in ("supersedes", "superseded_by", "sources"):
            targets |= set(LINK.findall(m.get(f, "")))
        for t in targets:
            linked.add(t.strip())
            if t.strip() not in all_md:
                problems.append(f"{rel}: broken link [[{t.strip()}]]")
        rb = date(m.get("review_by", ""))
        if rb and rb < TODAY and m.get("status", "active") == "active":
            problems.append(f"{rel}: review overdue since {rb}")
        if m.get("status") == "superseded" and not m.get("superseded_by"):
            problems.append(f"{rel}: superseded but no superseded_by")
        if len(b.splitlines()) > 300:
            problems.append(f"{rel}: over 300 lines, consider splitting")
        key = (m.get("title") or p.stem).lower()
        if key in titles:
            problems.append(f"{rel}: duplicate title of {titles[key]}")
        titles[key] = rel
    for p, m, _ in notes():
        if p.stem not in linked and m.get("type") not in ("log", "inbox", "context"):
            problems.append(f"{p.relative_to(ROOT)}: orphan (nothing links here)")
    print("\n".join(problems) or "clean")
    return 1 if problems else 0


if __name__ == "__main__":
    args = sys.argv[1:] or ["lint"]
    if args[0] == "index":
        cmd_index()
    elif args[0] == "search" and len(args) > 1:
        n = int(args[args.index("-n") + 1]) if "-n" in args else 5
        cmd_search(args[1], n)
    else:
        sys.exit(cmd_lint())
