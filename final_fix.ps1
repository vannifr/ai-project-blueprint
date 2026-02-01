$docsDir = "c:\Users\frevanni\OneDrive - Telenet group\Documents\PM4AI\ai-project-playbook\docs"

# We will use [char]::ConvertFromUtf32 to avoid any encoding issues in this script itself
$rocket = [char]::ConvertFromUtf32(0x1F680)
$pin = [char]::ConvertFromUtf32(0x1F4CD)
$book = [char]::ConvertFromUtf32(0x1F4D6)

Write-Host "Updating all files to Status: Draft and fixing emoji artifacts..."

Get-ChildItem -Path $docsDir -Filter *.md -Recurse | ForEach-Object {
    $filePath = $_.FullName
    
    # Read as bytes and convert to string assuming UTF8
    $bytes = [System.IO.File]::ReadAllBytes($filePath)
    $content = [System.Text.Encoding]::UTF8.GetString($bytes)
    
    $modified = $false
    
    # 1. Update Status to Draft
    if ($content -match "Status: Definitief" -or $content -match "Status: Final") {
        $content = $content -replace "Status: Definitief", "Status: Draft"
        $content = $content -replace "Status: Final", "Status: Draft"
        $modified = $true
    }

    # 2. Fix the "?? " issue by replacing actual emojis with more stable ones or removing them if they are causing double question marks
    # If the user sees ??, it might be because of a previous bad save that actually put ?? in the file.
    
    # Let's try to find and fix literal ?? at the start of headers/lines
    if ($content -match "\?\?\s?") {
        $content = $content -replace "\?\?\s?", ""
        $modified = $true
    }

    if ($modified) {
        Write-Host "Processing: $filePath"
        # Write back as UTF8 WITHOUT BOM
        $utf8NoBom = New-Object System.Text.UTF8Encoding $false
        [System.IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
    }
}

Write-Host "Done."
