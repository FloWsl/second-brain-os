#!/usr/bin/env python3
"""queue.py - capture queue in notes/inbox.md (stdlib only). See contracts.md §6.
  python3 queue.py add --source claude-code --session "<id>" --entities "a; b" \
      --facts "..." --decisions "what | why: ..." --open-loops "..." \
      --certainty fact|hypothesis --verbatim "exact user sentence"
  python3 queue.py list [--status new]
  python3 queue.py set <id> integrated|rejected "<result>"
"""
import argparse, datetime as dt, re, sys
from pathlib import Path

INBOX = Path(__file__).resolve().parent / "notes" / "inbox.md"
HEAD = re.compile(r"^## (q-\d{8}-\d{4,6}) \| (\w+)\s*$", re.M)
FIELDS = ["date", "source", "session", "certainty", "entities", "facts", "decisions",
          "open_loops", "verbatim", "result"]


def read():
    return INBOX.read_text(encoding="utf-8") if INBOX.exists() else ""


def add(a):
    now = dt.datetime.now()
    qid = now.strftime("q-%Y%m%d-%H%M%S")
    vals = {"date": now.date().isoformat(), "source": a.source, "session": a.session,
            "certainty": a.certainty, "entities": a.entities, "facts": a.facts,
            "decisions": a.decisions, "open_loops": a.open_loops,
            "verbatim": a.verbatim, "result": ""}
    block = f"\n## {qid} | new\n" + "".join(f"- {k}: {vals[k] or ''}\n" for k in FIELDS)
    INBOX.parent.mkdir(parents=True, exist_ok=True)
    with INBOX.open("a", encoding="utf-8") as f:
        f.write(block)
    print(qid)


def entries():
    text = read()
    heads = list(HEAD.finditer(text))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        yield h.group(1), h.group(2), text[h.end():end].strip()


def list_(status):
    for qid, st, body in entries():
        if status in (None, st):
            print(f"## {qid} | {st}\n{body}\n")


def set_(qid, status, result):
    if status not in ("integrated", "rejected"):
        sys.exit("status must be integrated or rejected")
    text = read()
    pat = re.compile(rf"^## {re.escape(qid)} \| \w+\s*$(.*?)(?=^## q-|\Z)", re.M | re.S)
    m = pat.search(text)
    if not m:
        sys.exit(f"{qid} not found")
    body = re.sub(r"^- result:.*$", f"- result: {result}", m.group(1), count=1, flags=re.M)
    INBOX.write_text(text[:m.start()] + f"## {qid} | {status}" + body + text[m.end():],
                     encoding="utf-8")
    print(f"{qid} -> {status}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    ad = sub.add_parser("add")
    for f in ["source", "session", "entities", "facts", "decisions", "open-loops", "verbatim"]:
        ad.add_argument(f"--{f}", default="")
    ad.add_argument("--certainty", choices=["fact", "hypothesis"], default="fact")
    ls = sub.add_parser("list")
    ls.add_argument("--status")
    st = sub.add_parser("set")
    st.add_argument("id"); st.add_argument("status"); st.add_argument("result")
    a = p.parse_args()
    if a.cmd == "add":
        add(a)
    elif a.cmd == "list":
        list_(a.status)
    else:
        set_(a.id, a.status, a.result)
