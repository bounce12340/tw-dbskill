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

## 怎麼用
- Grok Bot：直接讀 `skills/<name>/SKILL.md` 照做。
- Claude Code：複製或連結到 `~/.claude/skills/`：`ln -s $PWD/skills/tw-* ~/.claude/skills/`。
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
