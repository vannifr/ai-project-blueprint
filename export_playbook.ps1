# Export Playbook Documentation
$repoRoot = "c:\Users\frevanni\OneDrive - Telenet group\Documents\PM4AI\ai-project-playbook"
$mkdocsYaml = Join-Path $repoRoot "mkdocs.yml"
$docsDir = Join-Path $repoRoot "docs"
$outputFile = Join-Path $repoRoot "FULL_PLAYBOOK_EXPORT.md"

if (Test-Path $outputFile) {
    Remove-Item $outputFile
}

# Simple regex to find markdown files in the nav section of mkdocs.yml
$content = Get-Content $mkdocsYaml -Raw
$matches = [regex]::Matches($content, '(?m)^\s*-\s*[^:]+:\s*([^\s]+.md)')

Add-Content $outputFile "# AI Project Playbook - Full Export`n`nGenerated on: $(Get-Date)`n`n---`n"

foreach ($match in $matches) {
    $relativePath = $match.Groups[1].Value
    $absolutePath = Join-Path $docsDir $relativePath
    
    if (Test-Path $absolutePath) {
        Write-Host "Processing: $relativePath"
        
        $title = $relativePath -replace '.md$', '' -replace '-', ' '
        Add-Content $outputFile "`n# Document: $title`n"
        Add-Content $outputFile "Source: $relativePath`n"
        Add-Content $outputFile "---`n"
        
        $fileContent = Get-Content $absolutePath -Raw
        Add-Content $outputFile $fileContent
        Add-Content $outputFile "`n`n---`n"
    } else {
        Write-Warning "File not found: $absolutePath"
    }
}

Write-Host "Export completed: $outputFile"
