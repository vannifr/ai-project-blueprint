$docsDir = "c:\Users\frevanni\OneDrive - Telenet group\Documents\PM4AI\ai-project-playbook\docs"

Write-Host "Cleaning up redundant footer rules..."

Get-ChildItem -Path $docsDir -Filter *.md -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    $modified = $false
    
    # Replace triple dash on last line or double dashes at end
    if ($content -match "\n---\s*\n---\s*$") {
        $content = $content -replace "\n---\s*\n---\s*$", "`n---`n"
        $modified = $true
    }
    
    # Also fix case where there's text then --- then ---
    if ($content -match "\n---\s*\n---\s*\n") {
        $content = $content -replace "\n---\s*\n---\s*\n", "`n---`n"
        $modified = $true
    }

    if ($modified) {
        Write-Host "Cleaned: $filePath"
        [System.IO.File]::WriteAllText($filePath, $content, (New-Object System.Text.UTF8Encoding $false))
    }
}
