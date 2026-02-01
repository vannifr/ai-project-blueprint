$docsDir = "c:\Users\frevanni\OneDrive - Telenet group\Documents\PM4AI\ai-project-playbook\docs"
$utf8NoBom = New-Object System.Text.UTF8Encoding $false

Write-Host "Updating document statuses and fixing rendering..."

Get-ChildItem -Path $docsDir -Filter *.md -Recurse | ForEach-Object {
    $filePath = $_.FullName
    try {
        # Read with UTF8
        $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
        
        $modified = $false
        
        # 1. Update Status to Draft
        if ($content -match "Status: Definitief") {
            $content = $content -replace "Status: Definitief", "Status: Draft"
            $modified = $true
        }
        if ($content -match "Status: Final") {
            $content = $content -replace "Status: Final", "Status: Draft"
            $modified = $true
        }

        # 2. Fix potential rendering issues by ensuring clean UTF8 and optionally removing problematic emojis from headers
        # If the user sees ?? it might be because the emoji is not supported.
        # Let's try to replace the most common ones with more stable versions or remove them from titles.
        
        # Replace the "?? " pattern if it actually exists in some files (due to previous bad saves)
        if ($content -match "\?\? ") {
            $content = $content -replace "\?\? ", ""
            $modified = $true
        }

        if ($modified) {
            Write-Host "Updated: $filePath"
            [System.IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
        }
    }
    catch {
        Write-Warning "Failed to process $filePath"
    }
}

Write-Host "Complete."
