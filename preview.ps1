param([int]$Port=8768,[string]$Python='python')
$ErrorActionPreference='Stop'
Write-Output "Local preview: http://127.0.0.1:$Port/"
Write-Output 'Press Ctrl+C to stop. This does not publish the book.'
& $Python -m http.server $Port --bind 127.0.0.1 --directory (Join-Path $PSScriptRoot 'dist')
