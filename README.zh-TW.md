# tw-dbskill

台灣創作者用的 AI skill 工具箱（AI 創業、AI Agent 實戰、一人公司）：內容創作與一人公司經營。改作自 dontbesilent 的 [dbskill](https://github.com/dontbesilent2025/dbskill)，CC BY-NC 4.0，**僅限非商業使用**，署名與修改說明見 [NOTICE.md](NOTICE.md)。

## Skill 清單
| Skill | 用途 |
|---|---|
| tw-dbs | 入口：不知道從哪開始時，判斷下一步用哪個 skill |
| tw-content | 把選題做成內容方案，交付 03-drafts 格式 |
| tw-title-cover-intro | 標題、封面字、影片開頭（參考 05-analytics） |
| tw-cover-text-9x16 | 直式封面字與安全區規格（新增） |
| tw-resonate | 診斷稿子哪裡沒打中受眾 |
| tw-script-flow | 檢查配音稿銜接與可能滑走的位置 |
| tw-threads-split | 拆 Threads 串文與 X 貼文（新增） |
| tw-plain-writing | 平鋪直敘寫產品／工具說明，可中英雙語 |
| tw-content-risk-check | 發布前風險檢查：平台規範、台灣法規、授權、AI 標示、事實 |
| tw-music-credit-check | 配樂授權與署名檢查（新增） |
| tw-benchmark | 對標帳號分析 |
| tw-diagnosis | 商業模式診斷 |
| tw-jtbd | 顧客任務分析 |
| tw-good-question | 把模糊問題／派工改寫成可驗證的說明書 |
| tw-decision | 長期決策紀錄與復盤 |
| tw-action | 拖延與執行阻滯診斷 |

## 研究
- `research/viral-patterns.md`：224 筆公開貼文與影片的爆紅模式、各平台比較、轉移矩陣、平台假設查證與 A/B 測試清單。
- `research/viral-dataset.csv`：原始資料（連結＋公開指標＋讀取日期）。
- `shared/benchmarks.md`：23 個對標帳號。

## 安裝與接入

所有 skill 的正本都在 `skills/<name>/SKILL.md`（符合 [Agent Skills](https://agentskills.io) 規格：每個資料夾一個 `SKILL.md`，frontmatter 有 `name` 與 `description`）。各工具的轉接檔只指向這裡，不複製內容。

先下載：

```bash
git clone https://github.com/bounce12340/tw-dbskill.git
cd tw-dbskill
```

### 一鍵安裝腳本
```bash
scripts/install.sh --target claude            # 裝到使用者全域（預設建立符號連結）
scripts/install.sh --target cursor --scope project --project ~/my-repo
scripts/install.sh --target codex --copy      # 複製而不是連結
scripts/install.sh --dest ~/any/skills        # 自訂資料夾
scripts/install.sh --target gemini --dry-run  # 只看會做什麼
```
Windows（PowerShell）：`.\scripts\install.ps1 -Target claude`，參數相同（`-Scope`、`-Project`、`-Copy`、`-Dest`、`-DryRun`）。沒開「開發人員模式」時符號連結可能失敗，腳本會自動改用複製。

腳本會另外放一份 `tw-dbskill-shared/`（即 `shared/`）在同一層，skill 裡提到的 `shared/USER-PROFILE.md` 就在那裡。用連結模式時 `git pull` 就會更新；用複製模式要重跑腳本。

| `--target` | 全域資料夾（`--scope user`） | 專案資料夾（`--scope project`） |
|---|---|---|
| `claude` | `~/.claude/skills` | `.claude/skills` |
| `codex` | `~/.codex/skills` | `.agents/skills` |
| `cursor` | `~/.cursor/skills` | `.cursor/skills` |
| `gemini` | `~/.gemini/skills` | `.gemini/skills` |
| `copilot` | `~/.copilot/skills` | `.github/skills` |
| `windsurf` | `~/.codeium/windsurf/skills` | `.windsurf/skills` |
| `cline` | `~/.cline/skills` | `.cline/skills` |
| `roo` | `~/.roo/skills` | `.roo/skills` |
| `opencode` | `~/.config/opencode/skills` | `.opencode/skills` |
| `openclaw` | `~/.openclaw/skills` | `skills` |
| `hermes` | `~/.hermes/skills` | `.hermes/skills` |
| `grok` | `~/.grok/skills` | `.grok/skills` |
| `agents`（通用） | `~/.agents/skills` | `.agents/skills` |

很多工具也會讀通用的 `.agents/skills`（Codex、Cursor、Gemini CLI、Copilot、Cline、OpenCode 等），不確定時用 `--target agents --scope project`。

### 各工具說明
- **Claude Code**：`scripts/install.sh --target claude`，對話中輸入 `/tw-dbs` 或直接描述需求，Claude 會依 description 自動選用。也可以當外掛市集安裝：`/plugin marketplace add bounce12340/tw-dbskill`，再 `/plugin install tw-dbskill@tw-dbskill`（skill 會變成 `/tw-dbskill:tw-dbs` 這種前綴）。在本 repo 裡開 Claude Code 時會讀 `CLAUDE.md`（指向 `AGENTS.md`）。
- **Cursor**：`--target cursor`（全域）或 `--scope project`。在本 repo 開啟時，Cursor 也會讀根目錄 `AGENTS.md` 與 `.cursor/rules/tw-dbskill.mdc`。對話中可用 `/tw-dbs` 呼叫。
- **OpenAI Codex CLI**：`--target codex`。Codex 會讀 `AGENTS.md`；skill 可用 `$tw-dbs` 或 `/skills` 叫出。
- **Gemini CLI**：`--target gemini`，用 `/skills list` 確認。也可以當擴充套件裝：`gemini extensions install https://github.com/bounce12340/tw-dbskill`（讀 `gemini-extension.json` 與 `GEMINI.md`）。在本 repo 裡會讀 `GEMINI.md`（匯入 `AGENTS.md`）。
- **GitHub Copilot**（VS Code、Copilot CLI、coding agent）：`--target copilot --scope project` 放進 `.github/skills`，或全域 `~/.copilot/skills`。repo 內另有 `.github/copilot-instructions.md`。
- **Windsurf**：`--target windsurf`；repo 內 `.windsurf/rules/tw-dbskill.md` 與 `AGENTS.md` 會被讀取。
- **Cline**：`--target cline`；repo 內 `.clinerules/tw-dbskill.md` 指向 `AGENTS.md`。
- **Roo Code**：`--target roo`。
- **OpenCode**：`--target opencode`。
- **OpenClaw**：`--target openclaw`（`~/.openclaw/skills`），或放到工作區的 `skills/`。
- **Hermes Agent**：`--target hermes`（`~/.hermes/skills`）。
- **Grok 與其他「SKILL.md 資料夾」型 agent**：`--target grok`，或用 `--dest` 指到該 agent 的 skills 資料夾；也可以直接叫 agent 讀 `skills/<name>/SKILL.md`。
- **任何 LLM／沒有 skill 功能的工具**：把 `AGENTS.md` 和要用的 `skills/<name>/SKILL.md`（加上 `shared/USER-PROFILE.md`）貼進系統提示或專案指示（例如 ChatGPT 專案、Claude Projects、Gemini Gems）即可。MCP 客戶端如果有檔案系統類 MCP，指向本 repo，叫模型先讀 `AGENTS.md`。

### 檢查
```bash
python3 tools/lint.py --skills   # 檢查每個 SKILL.md 的 frontmatter
```
各工具的路徑會隨版本調整，如果裝了卻沒出現，請以該工具的官方文件為準，再用 `--dest` 指定。

## 使用提醒
- 所有 skill 先讀 `shared/USER-PROFILE.md`。`$MEDIA_TEAM` 指你自己的內容工作資料夾（含 `00-profile/voice.md`、`01-leads`、`03-drafts`、`04-review`、`05-analytics`）；沒有的話可略過相關步驟。
- 私人設定放 `shared/PROFILE.local.md`（已列入 .gitignore）。
- 文字檢查：`python3 tools/lint.py --threads threads/1.txt`、`--x x_post.txt`。

## 沒收錄的上游 skill
見 [EXCLUDED.md](EXCLUDED.md)。後續優化見 [OPTIMIZATIONS.md](OPTIMIZATIONS.md)。

## 授權與署名
- 改作自 [dbskill](https://github.com/dontbesilent2025/dbskill)，原作者 [dontbesilent](https://x.com/dontbesilent)。
- 授權：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，見 [LICENSE](LICENSE)。本專案的新增內容同樣採 CC BY-NC 4.0。
- **僅限非商業使用。** 若要用於商業用途（接案、販售、付費課程等），請先向原作者取得授權。
- 本專案與原作者無隸屬或背書關係。
- 研究資料只收錄公開貼文的連結與公開指標，不含貼文全文；平台內容的著作權屬原作者。
