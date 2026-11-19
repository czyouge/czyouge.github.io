$ErrorActionPreference = 'Stop'
$blogRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $blogRoot
$hugoProgram = Join-Path $blogRoot '.tools\hugo.exe'
if (-not (Test-Path -LiteralPath $hugoProgram)) {
    python (Join-Path $PSScriptRoot 'install_hugo.py')
    if ($LASTEXITCODE -ne 0) { throw 'Hugo installation failed.' }
}
Write-Host 'Local preview: http://localhost:1313/ (drafts included; analytics disabled)'
& $hugoProgram server --bind 127.0.0.1 --port 1313 --buildDrafts --environment development --disableFastRender --destination .preview
