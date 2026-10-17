# 優化清單（依優先順序）

| # | 問題 | 優化做法 | 預期效果 | 是否已實作 |
|---|---|---|---|---|
| 1 | 原版風險檢查針對中國審查，對 使用者 無用 | 重寫 tw-content-risk-check：事實證據、Meta／YouTube／X 規範、藥事法、食安法、健康食品法、誹謗、肖像權、素材授權、AI 標示 | 發布前一次抓出最常見的擋發問題 | 是 |
| 2 | 每支片都要配樂與署名，常漏 | 新增 tw-music-credit-check | 不再漏署名或用錯授權 | 是 |
| 3 | Threads 500 字、X 加權 280 每次手算 | 新增 tw-threads-split＋tools/lint.py 字數檢查 | 拆稿一次過 | 是 |
| 4 | 破折號、簡體字、大陸用語反覆被退稿 | tools/lint.py 自動檢查 | 查核角色省時間 | 是 |
| 5 | 封面字常超出安全區、EP 編號未定 | 新增 tw-cover-text-9x16，含集數確認步驟 | 封面一次到位 | 是 |
| 6 | 各 skill 不知道團隊資料夾 | 每個 skill 加「使用者優化」掛點：01-leads、03-drafts、04-review、05-analytics | 產出可直接接流程 | 是 |
| 7 | 標題 skill 沒有回饋迴路 | tw-title-cover-intro 先讀 05-analytics；下一步做成腳本，把週報的標題型態與觀看數整理成表 | 標題依實際表現迭代 | 部分（規則已加，腳本未做） |
| 8 | 對標名單分散 | tw-benchmark 已指向 benchmark-candidates.md；需要 使用者確認每日看的 23 個帳號清單檔案位置，合併成 shared/benchmarks.md | 對標分析一致 | 是（shared/benchmarks.md，23 個；請 使用者確認） |
| 9 | X／LinkedIn 英文受眾 | tw-plain-writing、tw-threads-split 可輸出 zh-TW＋EN；下一步加英文用語規則（不誇大、標出處） | 擴大英文觸及 | 部分 |
| 10 | 事實查核仍靠人工 | 新增 facts-check 腳本：掃 script.txt 數字，比對 facts.md 是否有出處，沒對到就列出 | 減少捏造風險 | 否 |
| 11 | AI 腔問題 | 收錄並在地化上游 dbs-ai-check，接在查核角色流程 | 稿子更像 使用者 本人 | 否 |
| 12 | 復盤後不知為何某支爆 | 收錄 dbs-spread，給數據分析角色使用 | 復盤更有洞見 | 否 |
| 13 | 參考檔仍有中國案例 | 逐一改寫 references/ 內案例為台灣或國際案例（目前只做用語轉換） | 範例更貼近觀眾 | 部分（title-surfaces、benchmark cases 已換成真實案例） |
| 14 | skill 版本落後上游 | 寫同步腳本：比對上游 diff，人工決定是否合併 | 吸收上游改進 | 否 |
| 15 | 爆紅寫法靠感覺 | research/viral-patterns.md＋打分檢查，接入 6 個 skill | 有證據的檢查表 | 是 |
| 16 | 平台假設未驗證 | A/B 測試清單交數據分析角色 | 用自己資料定規則 | 否（待執行） |
