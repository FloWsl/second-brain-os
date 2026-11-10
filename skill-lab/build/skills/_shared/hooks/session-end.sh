#!/bin/bash
# SessionEnd hook. If the session was not captured with /done (brain-capture),
# queue a one-line stub so brain-daily can ask about it. Never runs an agent.
[ "$BRAIN_AUTOMATED" = "1" ] && exit 0
INPUT=$(cat)
get() { printf '%s' "$INPUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('$1',''))"; }
SID=$(get session_id); TRANSCRIPT=$(get transcript_path)
[ -n "$TRANSCRIPT" ] && [ -f "$TRANSCRIPT" ] || exit 0
grep -q -e 'brain-capture' -e 'queue.py add' "$TRANSCRIPT" && exit 0
# skip trivial sessions (fewer than 4 user turns)
[ "$(grep -c '"type":"user"' "$TRANSCRIPT")" -lt 4 ] && exit 0
cd "${CLAUDE_PROJECT_DIR:-.}" && python3 queue.py add --source claude-code \
  --session "$SID" --facts "UNCAPTURED session, transcript: $TRANSCRIPT" >/dev/null
exit 0
