---
name: tw-music-credit-check
description: 檢查影片是否有配樂、音樂授權是否允許使用，以及說明欄是否附正確的音樂署名（例如 CC BY 4.0）。發布前或交件時使用。
---

# tw-music-credit-check：配樂與署名檢查

使用者 新增（非上游）。團隊規則：每支影片都要有配樂與音樂署名。

1. 讀 `03-drafts/<slug>/credits.md`：每首曲子要有曲名、作者、授權、來源連結。
2. 授權判斷：CC BY 可商用但需署名；CC BY-NC 不可用於有營利的帳號，需 使用者 判斷；CC BY-ND 不可剪輯；來源不明一律擋發。
3. 署名格式（CC BY）：「Music: "曲名" by 作者 (來源連結), licensed under CC BY 4.0」。
4. 檢查 ig_caption.txt、YouTube 說明、TikTok 說明、Threads 最後一則都有署名（X 可省略時要註明理由）。
5. 輸出 `04-review/<slug>-music.md`：通過／缺少欄位。
