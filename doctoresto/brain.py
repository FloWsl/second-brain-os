#!/usr/bin/env python3
"""brain.py - markdown-only second brain helper (stdlib only).
  python3 brain.py init <target>      # scaffold a brain (never overwrites)
  python3 brain.py index              # rebuild index.md in every folder
  python3 brain.py search "acme price" [-n 5]
  python3 brain.py lint               # report problems + health score, exit 1 if any
Based on reference/brain.py from the guide; lint checks and score added for the skill lab.
"""
import datetime as dt, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP = {"raw", "archive", "evals", ".git", ".obsidian", ".claude"}
SPECIAL = {"index.md", "AGENTS.md", "CLAUDE.md", "log.md", "hot.md", "evals.md"}
HALF_LIFE = {"project": 30, "entity": 180, "concept": 365, "source": 365,
             "log": 7, "inbox": 3}            # days; types absent = no decay
STATUS_MULT = {"active": 1.0, "draft": 0.8, "archived": 0.3, "superseded": 0.0}
W_REL, W_REC, W_IMP = 1.0, 1.0, 1.0
TODAY = dt.date.today()
# Defaults above are overridden by context/config.md (decay_* keys), see load_config().
LINK = re.compile(r"\[\[([^\]|#]+)")
QUEUE_HEAD = re.compile(r"^## (q-(\d{8})-\d{4,6}) \| (\w+)\s*$", re.M)
ROOT_MAX, HOT_MAX_WORDS, QUEUE_MAX_DAYS = 60, 500, 2
DIRS = ["context", "projects", "clients", "people", "notes/daily", "wiki/sources",
        "raw", "archive", "evals/results", ".claude/hooks"]
# severity per check: fail costs 5, warn costs 1, each check capped at 25 (Ben AI score idea)
SEVERITY = {"frontmatter": "fail", "broken-link": "fail", "superseded": "fail",
            "root-size": "fail", "overdue": "warn", "size": "warn", "duplicate": "warn",
            "orphan": "warn", "index": "warn", "hot-size": "warn", "queue": "warn",
            "daily-log": "warn", "marker": "warn"}


def _pairs(value):
    """'project=30, entity=180' -> {'project': 30.0, 'entity': 180.0}; bad items skipped."""
    out = {}
    for item in value.split("#")[0].split(","):
        if "=" in item:
            k, v = item.split("=", 1)
            try:
                out[k.strip()] = float(v)
            except ValueError:
                pass
    return out


def load_config():
    """Read decay settings from context/config.md so they can be tuned without code."""
    global W_REL, W_REC, W_IMP
    cfg = ROOT / "context" / "config.md"
    if not cfg.exists():
        return
    for line in cfg.read_text(encoding="utf-8").splitlines():
        if not line.startswith("- ") or ":" not in line:
            continue
        key, value = line[2:].split(":", 1)
        key = key.strip()
        if key == "decay_half_life":
            for t, v in _pairs(value).items():
                if v <= 0:
                    HALF_LIFE.pop(t, None)      # 0 = no decay for this type
                else:
                    HALF_LIFE[t] = v
        elif key == "decay_status_mult":
            STATUS_MULT.update(_pairs(value))
        elif key == "decay_weights":
            w = _pairs(value)
            W_REL, W_REC, W_IMP = (w.get("relevance", W_REL), w.get("recency", W_REC),
                                   w.get("importance", W_IMP))


def name(p):
    """Link name of a note: a project's about.md is named after its folder."""
    return p.parent.name if p.name == "about.md" else p.stem


def parse(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" in line and not line.startswith(" "):
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.split(" #")[0].strip().strip('"')
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
    try:
        importance = int(meta.get("importance", 3) or 3) / 5
    except ValueError:
        importance = 0.6
    mult = STATUS_MULT.get(meta.get("status", "active"), 1.0)
    return mult * (W_REL * relevance + W_REC * recency + W_IMP * importance)


def cmd_search(query, n=5):
    terms = [t for t in query.lower().split() if len(t) > 2] or query.lower().split()
    ranked = sorted(((score(m, b, name(p), terms), p, m) for p, m, b in notes()),
                    key=lambda x: x[0], reverse=True)
    for s, p, m in [r for r in ranked if r[0] > 0][:n]:
        print(f"{s:.2f}  {p.relative_to(ROOT)}  ({m.get('status', 'active')}, "
              f"updated {m.get('updated', '?')}) {m.get('summary', '')}")


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
                out += [f"- [[{name(p)}]] (updated {m.get('updated', '?')}, "
                        f"imp {m.get('importance', '?')}): {m.get('summary', '')}"
                        for p, m in rows]
        (d / "index.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"indexed {sum(len(v) for v in by_dir.values())} notes "
          f"in {len(by_dir)} folders")


def lint_problems():
    """Return a list of (check, message)."""
    all_md = {name(p) for p in ROOT.rglob("*.md")}
    linked, out, titles, per_dir = set(), [], {}, {}
    for p, m, b in notes():
        rel = p.relative_to(ROOT)
        per_dir[p.parent] = per_dir.get(p.parent, 0) + 1
        for field in ("type", "status", "updated", "summary"):
            if not m.get(field):
                out.append(("frontmatter", f"{rel}: missing frontmatter '{field}'"))
        targets = set(LINK.findall(b))
        for f in ("supersedes", "superseded_by", "sources"):
            targets |= set(LINK.findall(m.get(f, "")))
        for t in targets:
            linked.add(t.strip())
            if t.strip() not in all_md:
                out.append(("broken-link", f"{rel}: broken link [[{t.strip()}]]"))
        rb = date(m.get("review_by", ""))
        if rb and rb < TODAY and m.get("status", "active") == "active":
            out.append(("overdue", f"{rel}: review overdue since {rb}"))
        if m.get("status") == "superseded" and not m.get("superseded_by"):
            out.append(("superseded", f"{rel}: superseded but no superseded_by"))
        if len(b.splitlines()) > 300:
            out.append(("size", f"{rel}: over 300 lines, consider splitting"))
        key = (m.get("title") or name(p)).lower()
        if key in titles:
            out.append(("duplicate", f"{rel}: duplicate title of {titles[key]}"))
        titles[key] = rel
        if rel.parts[:2] == ("notes", "daily"):
            heads = re.findall(r"^## (.+)$", b, re.M)
            if len(heads) != len(set(heads)) or re.search(r"\b(\d+(st|nd|rd|th) pass|run at \d)", b, re.I):
                out.append(("daily-log", f"{rel}: daily has repeated sections or per-run blocks (daily is state)"))
    for p, m, _ in notes():
        if (name(p) not in linked and m.get("type") not in ("log", "inbox", "context", "decision")
                and m.get("status", "active") not in ("superseded", "archived")):
            out.append(("orphan", f"{p.relative_to(ROOT)}: orphan (nothing links here)"))
    for d, n in per_dir.items():
        if n >= 2 and not (d / "index.md").exists():
            out.append(("index", f"{d.relative_to(ROOT) or '.'}/: {n} notes but no index.md (run brain.py index)"))
    agents = ROOT / "AGENTS.md"
    if agents.exists() and len(agents.read_text(encoding="utf-8").splitlines()) > ROOT_MAX:
        out.append(("root-size", f"AGENTS.md: over {ROOT_MAX} lines"))
    marker = ROOT / ".claude" / "automated-run"
    if marker.exists() and dt.datetime.now().timestamp() - marker.stat().st_mtime > 3 * 3600:
        out.append(("marker", ".claude/automated-run is over 3 h old: a routine crashed? delete it to unlock context/"))
    hot = ROOT / "hot.md"
    if hot.exists() and len(hot.read_text(encoding="utf-8").split()) > HOT_MAX_WORDS:
        out.append(("hot-size", f"hot.md: over {HOT_MAX_WORDS} words"))
    inbox = ROOT / "notes" / "inbox.md"
    if inbox.exists():
        for qid, day, status in QUEUE_HEAD.findall(inbox.read_text(encoding="utf-8")):
            d = date(f"{day[:4]}-{day[4:6]}-{day[6:]}")
            if status == "new" and d and (TODAY - d).days > QUEUE_MAX_DAYS:
                out.append(("queue", f"notes/inbox.md: {qid} still new after {QUEUE_MAX_DAYS} days"))
    return out


def health(problems):
    cost = {}
    for check, _ in problems:
        cost[check] = cost.get(check, 0) + (5 if SEVERITY.get(check) == "fail" else 1)
    return max(0, 100 - sum(min(c, 25) for c in cost.values()))


def cmd_lint():
    problems = lint_problems()
    print("\n".join(msg for _, msg in problems) or "clean")
    print(f"health: {health(problems)}/100")
    return 1 if problems else 0


def cmd_init(target):
    """Create the frozen layout and copy shared files. Never overwrites."""
    here = Path(__file__).resolve().parent.parent      # _shared/
    dst = Path(target).resolve()
    for d in DIRS:
        (dst / d).mkdir(parents=True, exist_ok=True)
    copies = {here / "scripts" / "brain.py": dst / "brain.py",
              here / "scripts" / "queue.py": dst / "queue.py",
              here / "hooks" / "protect.sh": dst / ".claude/hooks/protect.sh",
              here / "hooks" / "session-end.sh": dst / ".claude/hooks/session-end.sh"}
    for src in (here / "templates").rglob("*"):
        if src.is_file():
            rel = src.relative_to(here / "templates")
            name = ".claude/settings.json" if rel.name == "settings.json" else str(rel)
            copies[src] = dst / name
    made = []
    for src, out in copies.items():
        if not out.exists():
            out.parent.mkdir(parents=True, exist_ok=True)
            text = src.read_text(encoding="utf-8")
            if "templates" in src.parts:
                text = text.replace("{{TODAY}}", str(TODAY))
            out.write_text(text, encoding="utf-8")
            if out.suffix in (".sh", ".py"):
                out.chmod(0o755)
            made.append(str(out.relative_to(dst)))
    print("created: " + (", ".join(made) or "nothing (all present)"))


if __name__ == "__main__":
    load_config()
    args = sys.argv[1:] or ["lint"]
    if args[0] == "init" and len(args) > 1:
        cmd_init(args[1])
    elif args[0] == "index":
        cmd_index()
    elif args[0] == "search" and len(args) > 1:
        n = int(args[args.index("-n") + 1]) if "-n" in args else 5
        cmd_search(args[1], n)
    else:
        sys.exit(cmd_lint())
