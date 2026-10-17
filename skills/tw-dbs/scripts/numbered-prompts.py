#!/usr/bin/env python3
"""Read the public numbered catalog and prompts from the dbskill GitHub repository."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE_URL = (
    "https://raw.githubusercontent.com/dontbesilent2025/dbskill/"
    "main/skills/dbs/numbered-prompts"
)
ROOT = Path(__file__).resolve().parents[1] / "numbered-prompts"
CODE = re.compile(r"[0-9]{3}\Z")
DIGEST = re.compile(r"[0-9a-f]{64}\Z")
TITLE = re.compile(r"^# ([0-9]{3})｜(.+)$", re.MULTILINE)
SECTIONS = (
    "## 使用者要完成的事",
    "## 需要的輸入",
    "## 執行步驟",
    "## 交付結果",
    "## 驗收標準",
    "## 適用邊界",
)


class CatalogError(Exception):
    pass


def read_remote(path: str, limit: int) -> bytes:
    # A unique query prevents a recently published file from being obscured by a stale CDN response.
    url = f"{BASE_URL}/{path}?v={time.time_ns()}"
    request = Request(
        url,
        headers={"User-Agent": "dbskill-numbered-prompts", "Cache-Control": "no-cache"},
    )
    try:
        with urlopen(request, timeout=10) as response:
            if response.geturl().split("/", 3)[2] != "raw.githubusercontent.com":
                raise CatalogError("GitHub 原始檔案發生意外跳轉")
            content = response.read(limit + 1)
    except (HTTPError, URLError, TimeoutError, OSError) as error:
        raise CatalogError(f"無法從 GitHub 讀取編號內容：{error}") from error
    if len(content) > limit:
        raise CatalogError("GitHub 編號檔案超過大小限制")
    return content


def validate_catalog(raw: bytes) -> list[dict[str, str]]:
    try:
        document = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CatalogError("編號目錄不是有效的 UTF-8 JSON") from error
    if not isinstance(document, dict) or document.get("schema_version") != 1:
        raise CatalogError("編號目錄格式版本不正確")
    items = document.get("items")
    if not isinstance(items, list) or len(items) > 1000:
        raise CatalogError("編號目錄條目數量無效")
    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            raise CatalogError("編號目錄條目格式錯誤")
        code = item.get("id")
        if not isinstance(code, str) or CODE.fullmatch(code) is None or code in seen:
            raise CatalogError("編號目錄包含無效或重複編號")
        seen.add(code)
        if any(not isinstance(item.get(key), str) or not item[key].strip() for key in ("title", "purpose")):
            raise CatalogError(f"編號 {code} 缺少標題或用途")
        if any(len(item[key]) > 500 or "\n" in item[key] or "\r" in item[key] for key in ("title", "purpose")):
            raise CatalogError(f"編號 {code} 的標題或用途格式錯誤")
        if not isinstance(item.get("sha256"), str) or DIGEST.fullmatch(item["sha256"]) is None:
            raise CatalogError(f"編號 {code} 缺少有效的內容校驗值")
    if [item["id"] for item in items] != sorted(seen):
        raise CatalogError("編號目錄沒有按編號排序")
    return items


def catalog() -> tuple[list[dict[str, str]], bool]:
    try:
        return validate_catalog(read_remote("catalog.json", 1024 * 1024)), True
    except CatalogError as remote_error:
        local = ROOT / "catalog.json"
        if not local.is_file():
            raise remote_error
        try:
            items = validate_catalog(local.read_bytes())
        except (OSError, CatalogError):
            raise remote_error
        print("GitHub 暫時不可用；以下只包含安裝包自帶的舊目錄。", file=sys.stderr)
        return items, False


def get_prompt(code: str) -> str:
    items, online = catalog()
    entry = next((item for item in items if item["id"] == code), None)
    if entry is None:
        if online:
            raise CatalogError(f"編號 {code} 尚未在 GitHub 目錄中發布")
        raise CatalogError(f"無法連線 GitHub，安裝包中也沒有編號 {code}")
    if online:
        raw = read_remote(f"{code}/PROMPT.md", 256 * 1024)
    else:
        path = ROOT / code / "PROMPT.md"
        if not path.is_file():
            raise CatalogError(f"離線目錄中沒有編號 {code} 的內容")
        raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != entry["sha256"]:
        raise CatalogError(f"編號 {code} 的目錄與正文校驗值不一致，請稍後重試")
    try:
        content = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise CatalogError(f"編號 {code} 的正文不是 UTF-8") from error
    title = TITLE.search(content)
    if title is None or title.group(1) != code or any(section not in content for section in SECTIONS):
        raise CatalogError(f"編號 {code} 的正文結構不完整")
    return content


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    get = sub.add_parser("get")
    get.add_argument("code")
    args = parser.parse_args()
    try:
        if args.command == "list":
            items, online = catalog()
            place = "GitHub" if online else "本機安裝包"
            if not items:
                print(f"{place} 當前還沒有可用的編號隱藏款。")
            else:
                print(f"{place} 當前共有 {len(items)} 個編號隱藏款：")
                for item in items:
                    print(f"- /dbs {item['id']}｜{item['title']}：{item['purpose']}")
        else:
            if CODE.fullmatch(args.code) is None:
                raise CatalogError("編號必須是三位數字，保留前導零")
            print(get_prompt(args.code), end="")
    except CatalogError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
