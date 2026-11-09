#!/bin/bash
# .claude/hooks/protect.sh : exit code 2 blocks the tool call and shows stderr to the agent
FILE=$(jq -r '.tool_input.file_path // empty')
case "$FILE" in
  */raw/*|*/archive/*) echo "raw/ and archive/ are read-only. Write to the compiled note instead." >&2; exit 2 ;;
esac
exit 0
