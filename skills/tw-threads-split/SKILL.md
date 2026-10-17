---
name: tw-threads-split
description: 把長稿拆成 Threads 串文（每則 500 字以內）與 X 貼文（加權 280），保留重點、出處與順序。使用者要「拆 Threads」「做串文」「改成 X 版」時使用。
---

# tw-threads-split：串文拆分

使用者 新增（非上游）。先讀 `shared/USER-PROFILE.md`。

1. 讀 `03-drafts/<slug>/threads.txt` 或 ig_caption.txt、script.txt。
2. 第 1 則：鉤子＋這支的賣點，能單獨被看懂。中間每則一個重點；最後一則放出處連結、影片連結位置與一個問題收尾。
3. 每則 ≤ 500 字；用 `python3 tools/lint.py --threads <檔>` 檢查字數、破折號、簡體字。
4. X 版：加權 280（中日韓字算 2），用 `tools/lint.py --x <檔>` 檢查；有原貼文時優先寫成引用貼文。需要時另附英文版。
5. 輸出到 `threads/1.txt…N.txt` 與 `x_post.txt`，不發文。
