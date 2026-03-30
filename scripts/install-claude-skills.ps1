$repoDir = Split-Path -Parent $PSScriptRoot | Resolve-Path
$src = Join-Path $repoDir 'skills'
$dest = if ($env:CLAUDE_SKILLS_DIR) { $env:CLAUDE_SKILLS_DIR } else { Join-Path $HOME '.claude/skills' }
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Get-ChildItem $src -Directory | ForEach-Object {
  $target = Join-Path $dest $_.Name
  if (Test-Path $target) { Write-Host "skip: $target already exists" }
  else { cmd /c mklink /J "$target" "$($_.FullName)" | Out-Null; Write-Host "linked: $target" }
}
