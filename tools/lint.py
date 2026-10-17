#!/usr/bin/env python3
"""使用者 文字檢查：破折號、簡體字、大陸用語、Threads 500 字、X 加權 280。
用法：lint.py [--threads|--x] 檔案...   需要 opencc-python-reimplemented（選用）"""
import sys,re,unicodedata
TERMS={"數據":"資料","算力":"運算資源","語料":"訓練資料","視頻":"影片","質量":"品質","軟件":"軟體","網絡":"網路","賽道":"領域","內卷":"內捲","用戶":"使用者","賬號":"帳號","博主":"創作者","信息":"資訊","默認":"預設","優化":"優化","項目":"專案（視語境）"}
TERMS.pop("優化")
try:
  import opencc; cc=opencc.OpenCC('s2t')
except Exception: cc=None
def xlen(s): return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in re.sub(r'https?://\S+','x'*23,s))
OK=set("台群游斗准秘干里于后面只才志")
mode=None; rc=0
for a in sys.argv[1:]:
  if a in('--threads','--x'): mode=a; continue
  t=open(a,encoding='utf-8').read()
  for n,l in enumerate(t.splitlines(),1):
    if '—' in l: print(f"{a}:{n}: 破折號"); rc=1
    for k,v in TERMS.items():
      if k in l: print(f"{a}:{n}: 「{k}」建議改「{v}」"); rc=1
    if cc:
      d=[c for c in l if c not in OK and cc.convert(c)!=c]
      if d: print(f"{a}:{n}: 可能是簡體字 {''.join(d)}"); rc=1
  if mode=='--threads' and len(t.strip())>500: print(f"{a}: {len(t.strip())} 字，超過 Threads 500"); rc=1
  if mode=='--x' and xlen(t.strip())>280: print(f"{a}: 加權 {xlen(t.strip())}，超過 X 280"); rc=1
sys.exit(rc)
