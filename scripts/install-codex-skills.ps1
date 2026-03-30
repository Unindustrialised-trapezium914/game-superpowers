$repoDir = Split-Path -Parent $PSScriptRoot | Resolve-Path
$src = Join-Path $repoDir 'skills'
$destBase = if ($env:CODEX_SKILLS_DIR) { $env:CODEX_SKILLS_DIR } else { Join-Path $HOME '.agents/skills' }
New-Item -ItemType Directory -Force -Path $destBase | Out-Null
$target = Join-Path $destBase 'game-superpowers'
if (Test-Path $target) { Write-Host "skip: $target already exists" }
else { cmd /c mklink /J "$target" "$src" | Out-Null; Write-Host "linked: $target" }
