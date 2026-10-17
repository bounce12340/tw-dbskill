# tw-dbskill 安裝腳本（Windows PowerShell）
# 用法：.\scripts\install.ps1 -Target claude [-Scope user|project] [-Project DIR] [-Copy] [-Dest DIR] [-DryRun]
param(
  [string]$Target = "",
  [ValidateSet("user","project")][string]$Scope = "user",
  [string]$Project = (Get-Location).Path,
  [switch]$Copy, [string]$Dest = "", [switch]$DryRun
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$H = $HOME
$user = @{ claude="$H\.claude\skills"; codex="$H\.codex\skills"; cursor="$H\.cursor\skills"; gemini="$H\.gemini\skills";
  copilot="$H\.copilot\skills"; windsurf="$H\.codeium\windsurf\skills"; cline="$H\.cline\skills"; roo="$H\.roo\skills";
  opencode="$H\.config\opencode\skills"; openclaw="$H\.openclaw\skills"; hermes="$H\.hermes\skills"; grok="$H\.grok\skills"; agents="$H\.agents\skills" }
$proj = @{ claude=".claude\skills"; cursor=".cursor\skills"; gemini=".gemini\skills"; copilot=".github\skills"; windsurf=".windsurf\skills";
  cline=".cline\skills"; roo=".roo\skills"; opencode=".opencode\skills"; openclaw="skills"; hermes=".hermes\skills"; grok=".grok\skills";
  codex=".agents\skills"; agents=".agents\skills" }
if (-not $Dest) {
  if (-not $Target) { Write-Host "請指定 -Target：$($user.Keys -join ' ')"; exit 2 }
  if ($Scope -eq "user") { $Dest = $user[$Target] } else { if ($proj[$Target]) { $Dest = Join-Path $Project $proj[$Target] } }
  if (-not $Dest) { Write-Error "不支援的 target：$Target"; exit 2 }
}
# 沒有開發人員模式或系統管理員權限時，符號連結可能失敗，改用複製
function Put($src, $dst) {
  if (Test-Path $dst) {
    $it = Get-Item $dst -Force
    if ($it.LinkType -or (Test-Path (Join-Path $dst ".tw-dbskill"))) { if (-not $DryRun) { Remove-Item $dst -Recurse -Force } }
    else { Write-Warning "略過（已存在且不是本工具安裝的）：$dst"; return }
  }
  if ($DryRun) { Write-Host "[dry-run] $src -> $dst"; return }
  $done = $false
  if (-not $Copy) { try { New-Item -ItemType SymbolicLink -Path $dst -Target $src | Out-Null; $done = $true } catch { Write-Warning "無法建立符號連結，改用複製：$dst" } }
  if (-not $done) { Copy-Item $src $dst -Recurse; New-Item -ItemType File (Join-Path $dst ".tw-dbskill") | Out-Null }
  Write-Host "  $dst"
}
Write-Host "安裝到：$Dest"
if (-not $DryRun) { New-Item -ItemType Directory -Force $Dest | Out-Null }
$n = 0
Get-ChildItem (Join-Path $Root "skills") -Directory | Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") } | ForEach-Object { Put $_.FullName (Join-Path $Dest $_.Name); $n++ }
Put (Join-Path $Root "shared") (Join-Path $Dest "tw-dbskill-shared")
Write-Host "完成：$n 個 skill。授權 CC BY-NC 4.0，僅限非商業使用，見 NOTICE.md。"
