#!/bin/bash
# Install the brain-* skills into a Claude Code skills folder.
# Usage: ./install.sh [--target DIR] [--force]
# Default target: ~/.claude/skills. Never overwrites without --force; with --force the old
# folders go to <target>/../skills-backup-<date>/ (outside the skills folder).
set -euo pipefail
SRC="$(cd "$(dirname "$0")/skills" && pwd)"
TARGET="$HOME/.claude/skills"; FORCE=0
while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --force) FORCE=1; shift ;;
    *) echo "unknown option $1" >&2; exit 1 ;;
  esac
done
mkdir -p "$TARGET"
ITEMS="_shared brain-setup brain-capture brain-daily brain-lint brain-ask brain-evals"
for i in $ITEMS; do
  if [ -e "$TARGET/$i" ] && [ $FORCE -ne 1 ]; then
    echo "$TARGET/$i exists. Re-run with --force to replace it (a backup is kept)." >&2; exit 1
  fi
done
STAMP=$(date +%Y%m%d-%H%M%S)
BACKUP="$(dirname "$TARGET")/skills-backup-$STAMP"
for i in $ITEMS; do
  if [ -e "$TARGET/$i" ]; then mkdir -p "$BACKUP"; mv "$TARGET/$i" "$BACKUP/$i"; fi
  cp -R "$SRC/$i" "$TARGET/$i"
done
chmod +x "$TARGET/_shared/hooks/"*.sh "$TARGET/_shared/scripts/"*.py
echo "Installed to $TARGET: $ITEMS"
echo "Next: open an empty folder for your brain in Claude Code and ask: set up my second brain (brain-setup)."
