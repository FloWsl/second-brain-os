#!/bin/bash
# PreToolUse hook (Edit|Write). Exit 2 blocks the call and shows stderr to the agent.
# raw/ and archive/ are always read-only; context/ is read-only in automated runs.
INPUT=$(cat)
if command -v jq >/dev/null 2>&1; then
  FILE=$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // empty')
else
  FILE=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))')
fi
case "$FILE" in
  */raw/*|*/archive/*)
    echo "raw/ and archive/ are read-only. Write to the compiled note instead." >&2; exit 2 ;;
  */context/*)
    if [ "$BRAIN_AUTOMATED" = "1" ]; then
      echo "context/ is human-owned. Propose the change in your report instead." >&2; exit 2
    fi ;;
esac
exit 0
