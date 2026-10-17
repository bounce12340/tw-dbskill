# AGENTS.md：tw-dbskill 給 AI agent 的入口

本檔是給所有 AI coding agent（Codex、Cursor、Copilot、Gemini CLI、Windsurf、Cline、Roo 等）讀的總索引。內容的唯一正本在 `skills/<name>/SKILL.md`，其他轉接檔只指向這裡，不複製內容。

## 使用規則
1. 使用者的需求符合下表某個 skill 的「何時使用」時，先完整讀該 `SKILL.md` 再照做；不確定用哪個，先讀 `skills/tw-dbs/SKILL.md`。
2. 執行前先讀 `shared/USER-PROFILE.md`；有 `shared/PROFILE.local.md`（私人設定，不進版控）時一併讀，衝突以 local 為準。skill 安裝到別的資料夾時，`shared/` 會放在同層的 `tw-dbskill-shared/`。
3. `$MEDIA_TEAM` 指使用者自己的內容工作資料夾；不存在就略過相關步驟，不要自己捏造檔案。
4. 文字用台灣繁中、「」引號、不用破折號；可用 `python3 tools/lint.py` 檢查。
5. 只產出草稿與建議，不代替使用者發文；數字與事實沒有出處就寫「無資料」。
6. 授權：CC BY-NC 4.0，改作自 dontbesilent 的 dbskill，僅限非商業使用，見 `NOTICE.md`。

## Skill 索引
| Skill | 檔案 | 何時使用 |
|---|---|---|
| `tw-action` | `skills/tw-action/SKILL.md` | 用阿德勒心理學框架診斷執行阻滯。使用者知道該做什麼卻遲遲不做、反覆拖延或行動中斷時使用。 |
| `tw-benchmark` | `skills/tw-benchmark/SKILL.md` | 用五重過濾法尋找值得模仿的對標，並排除主體差異造成的噪音。使用者要求找對標、選擇模仿物件或分析競爭參照時使用。 |
| `tw-content-risk-check` | `skills/tw-content-risk-check/SKILL.md` | 使用者 版發布前風險檢查。逐句、逐畫面檢查 IG Reels、Threads、X、YouTube Shorts、TikTok、LinkedIn、Facebook 的標題、說明、字幕、配音稿與畫面，判斷平台規範、台灣法規、著作權與授權、AI 標示、事實捏造等風險，給出位置與最小修改。使用者說「發布前排雷」「這篇能不能發」「檢查風險」時使用。保留強觀點與個人風格。 |
| `tw-content` | `skills/tw-content/SKILL.md` | 圍繞已經確定的選題診斷內容怎麼組織、論證和表達，形成創作方案。使用者要把選題做成內容時使用；已有稿件的共鳴刪改、整體流量價值評估、標題開頭生成和成片導航分別交由對應專用能力處理。 |
| `tw-cover-text-9x16` | `skills/tw-cover-text-9x16/SKILL.md` | 為 9:16 Reels／Shorts 封面與 Threads 1080x1350 封面寫封面字並給版面規格（安全區、字數、集數標記）。使用者要封面字、封面候選時使用。不生成圖片。 |
| `tw-dbs` | `skills/tw-dbs/SKILL.md` | 使用者 個人商業與內容工具箱（改作自 dontbesilent dbskill）主入口，根據當前問題和反饋選擇下一步，在對話中直接執行、澄清、組合或對照嘗試正式 Skill。使用者不知道從哪裡開始、需要調整處理方法、第一次使用 dbskill、輸入三位編號或查詢隱藏款目錄時使用；僅需推薦或可複製提示詞時按請求交付。 |
| `tw-decision` | `skills/tw-decision/SKILL.md` | 把需要長期跟蹤的業務、關係、健康、職業、學習或投資問題建成本機決策知識工程。使用者要求決策立案、結果回填、狀態畫像或長期覆盤時使用。 |
| `tw-diagnosis` | `skills/tw-diagnosis/SKILL.md` | 自動識別使用者是在解決具體商業問題，還是希望全面檢查商業模式，並進入對應診斷流程。使用者希望拆解業務、檢查商業模式或消解具體商業困境時使用。 |
| `tw-good-question` | `skills/tw-good-question/SKILL.md` | 把模糊提問改寫成 Agent 可推理、可批評、可驗證的問題說明書，並判斷自動化可解程度。使用者要改進問題表述、研究問題或評估 Agent 可解性時使用；任務交付目標已明確時不重複澄清目標。 |
| `tw-jtbd` | `skills/tw-jtbd/SKILL.md` | 用 Jobs to Be Done 識別具體情境中使用者想推進的進展、切換方案的力量和選擇標準，解釋產品、服務或內容為何被選擇。使用者要求分析顧客任務、購買動機、替代方案或明確用 JTBD 重寫提示詞時使用；普通任務驗收標準澄清無需套用該框架。 |
| `tw-music-credit-check` | `skills/tw-music-credit-check/SKILL.md` | 檢查影片是否有配樂、音樂授權是否允許使用，以及說明欄是否附正確的音樂署名（例如 CC BY 4.0）。發布前或交件時使用。 |
| `tw-plain-writing` | `skills/tw-plain-writing/SKILL.md` | 按事實與功能順序直接撰寫、改寫或檢查產品、工具、功能、專案和更新說明，內建 ASD-STE100 清晰表達原則，核對主體、動作、指代、術語、條件與承諾強度，保留原意和使用者鎖定的文字，不加營銷鉤子、痛點渲染和抽象包裝。使用者要求平鋪直敘地寫、不要營銷腔、把能力逐條寫清、檢查措辭歧義或只改指定一處時使用；中文為原則適配，不等於官方符合性認證。 |
| `tw-resonate` | `skills/tw-resonate/SKILL.md` | 診斷已經寫成的稿件哪裡沒有打中目標受眾，結合原句解釋共鳴斷點並提出具體刪改建議。適用於稿件修訂；不負責整體流量與商業價值評估，也不以解釋已發布內容的傳播機制為主要交付。 |
| `tw-script-flow` | `skills/tw-script-flow/SKILL.md` | 檢查短影音逐字稿的段落銜接、資訊密度和口播流暢度，定位觀眾可能滑走的位置。使用者要求檢查邏輯延續、文稿順暢度或流失風險時使用。 |
| `tw-threads-split` | `skills/tw-threads-split/SKILL.md` | 把長稿拆成 Threads 串文（每則 500 字以內）與 X 貼文（加權 280），保留重點、出處與順序。使用者要「拆 Threads」「做串文」「改成 X 版」時使用。 |
| `tw-title-cover-intro` | `skills/tw-title-cover-intro/SKILL.md` | 為短影音、圖文和文章生成或修改文字標題、封面文字和影片開頭。先按稿件與拍攝狀態把素材擴展成面向不同人群的選題供使用者挑選，並詢問能讓觀眾相信作者的經歷或數字，再一次交付IG／Threads、YouTube、IG Reels／TikTok、YouTube Shorts的標題、封面與開頭。使用者要寫標題、封面文字、開頭、冷開場或多平台適配時使用；不生成封面圖片、影片章節導航或發布風險宣告。 |

## 研究資料
- `research/viral-patterns.md`：爆紅模式、各平台差異與待驗證假設。
- `shared/benchmarks.md`：對標帳號清單。
