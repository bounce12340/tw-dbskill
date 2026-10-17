#!/usr/bin/env bash
# tw-dbskill 安裝腳本：把 skills/ 連結或複製到指定 agent 的 skills 資料夾。
# 用法：scripts/install.sh --target <agent> [--scope user|project] [--project DIR] [--copy] [--dest DIR] [--dry-run]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET=""; SCOPE=user; PROJ="$PWD"; MODE=link; DEST=""; DRY=0
usage(){ cat <<U
用法：$0 --target <agent> [選項]
agent：claude codex cursor gemini copilot windsurf cline roo opencode openclaw hermes grok agents（通用 .agents/skills）
選項：
  --scope user|project  安裝到使用者全域（預設）或專案資料夾
  --project DIR         專案根目錄（預設目前目錄）
  --copy                複製而不是建立符號連結
  --dest DIR            自訂目的資料夾（覆蓋 --target 的預設路徑）
  --dry-run             只顯示會做什麼
U
}
while [ $# -gt 0 ]; do case "$1" in
  --target) TARGET="$2"; shift 2;; --scope) SCOPE="$2"; shift 2;;
  --project) PROJ="$2"; shift 2;; --dest) DEST="$2"; shift 2;;
  --copy) MODE=copy; shift;; --dry-run) DRY=1; shift;;
  -h|--help) usage; exit 0;; *) echo "未知參數：$1" >&2; usage; exit 2;; esac; done
[ -n "$TARGET$DEST" ] || { usage; exit 2; }
H="$HOME"
if [ -z "$DEST" ]; then
  if [ "$SCOPE" = user ]; then case "$TARGET" in
    claude) DEST="$H/.claude/skills";; codex) DEST="$H/.codex/skills";;
    cursor) DEST="$H/.cursor/skills";; gemini) DEST="$H/.gemini/skills";;
    copilot) DEST="$H/.copilot/skills";; windsurf) DEST="$H/.codeium/windsurf/skills";;
    cline) DEST="$H/.cline/skills";; roo) DEST="$H/.roo/skills";;
    opencode) DEST="$H/.config/opencode/skills";; openclaw) DEST="$H/.openclaw/skills";;
    hermes) DEST="$H/.hermes/skills";; grok) DEST="$H/.grok/skills";;
    agents) DEST="$H/.agents/skills";;
    *) echo "不支援的 target：$TARGET" >&2; exit 2;; esac
  else case "$TARGET" in
    claude) DEST="$PROJ/.claude/skills";; cursor) DEST="$PROJ/.cursor/skills";;
    gemini) DEST="$PROJ/.gemini/skills";; copilot) DEST="$PROJ/.github/skills";;
    windsurf) DEST="$PROJ/.windsurf/skills";; cline) DEST="$PROJ/.cline/skills";;
    roo) DEST="$PROJ/.roo/skills";; opencode) DEST="$PROJ/.opencode/skills";;
    openclaw) DEST="$PROJ/skills";; hermes) DEST="$PROJ/.hermes/skills";;
    grok) DEST="$PROJ/.grok/skills";; codex|agents) DEST="$PROJ/.agents/skills";;
    *) echo "不支援的 target：$TARGET" >&2; exit 2;; esac
  fi
fi
run(){ if [ $DRY = 1 ]; then echo "[dry-run] $*"; else "$@"; fi; }
put(){ src="$1"; dst="$2"
  if [ -e "$dst" ] || [ -L "$dst" ]; then
    if [ -L "$dst" ] || [ -f "$dst/.tw-dbskill" ]; then run rm -rf "$dst"; else echo "略過（已存在且不是本工具安裝的）：$dst" >&2; return; fi
  fi
  if [ $MODE = link ]; then run ln -s "$src" "$dst"; else run cp -R "$src" "$dst"; [ $DRY = 1 ] || touch "$dst/.tw-dbskill"; fi
  echo "  $dst"; }
echo "安裝到：$DEST（$MODE）"
run mkdir -p "$DEST"
n=0; for s in "$ROOT"/skills/*/; do s="${s%/}"; [ -f "$s/SKILL.md" ] || continue; put "$s" "$DEST/$(basename "$s")"; n=$((n+1)); done
put "$ROOT/shared" "$DEST/tw-dbskill-shared"
echo "完成：$n 個 skill。共用設定在 $DEST/tw-dbskill-shared。授權 CC BY-NC 4.0，僅限非商業使用，見 $ROOT/NOTICE.md。"
