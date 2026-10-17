# 授權與署名

本專案改作自 **dbskill**，原作者 **dontbesilent**（https://x.com/dontbesilent），上游：https://github.com/dontbesilent2025/dbskill（commit a4a3cc8，2026-10-18 取得）。
授權：CC BY-NC 4.0（https://creativecommons.org/licenses/by-nc/4.0/），見 LICENSE。本改作沿用同一授權，**僅限非商業使用**。

## 修改內容
- 選用 13 個 skill，改名為 tw-*；以 OpenCC s2twp 轉台灣繁中後人工修正台灣用語，「」引號、移除破折號。
- 平台由小紅書、抖音、視頻號、B 站、微信改為 IG Reels、Threads、X、YouTube Shorts、TikTok、LinkedIn、Facebook。
- tw-content-risk-check 全面重寫（原版為中國平台審查與敏感詞）。
- 各 skill 加入 使用者 個人設定與團隊流程掛點；新增 tw-threads-split、tw-cover-text-9x16、tw-music-credit-check 與 tools/lint.py（使用者 原創，同樣以 CC BY-NC 4.0 釋出）。
- 未收錄上游的推文語料、知識庫（知识库/）與 books/，需要時請看上游。
- 新增 research/（公開資料整理）與 shared/benchmarks.md；研究中引用的平台官方文件與法規連結均附出處。
- 本專案與 dontbesilent 無隸屬或背書關係。
- 新增多 agent 接入：AGENTS.md 索引、CLAUDE.md／GEMINI.md／Copilot／Cursor／Windsurf／Cline 轉接檔、Claude Code 外掛市集設定、Gemini 擴充套件設定、scripts/install.sh 與 install.ps1（同樣以 CC BY-NC 4.0 釋出）。
