$docsDir = "c:\Users\frevanni\OneDrive - Telenet group\Documents\PM4AI\ai-project-playbook\docs"
$utf8NoBom = New-Object System.Text.UTF8Encoding $false

Write-Host "Starting final emoji restoration, status update to Draft, and encoding fix..."

# Use Unicode escapes for EVERYTHING to avoid script corruption
$rocket = [char]::ConvertFromUtf32(0x1F680)
$book = [char]::ConvertFromUtf32(0x1F4D6)
$target = [char]::ConvertFromUtf32(0x1F3AF)
$people = [char]::ConvertFromUtf32(0x1F465)
$calendar = [char]::ConvertFromUtf32(0x1F4C5)
$toolbox = [char]::ConvertFromUtf32(0x1F9F0)
$paper = [char]::ConvertFromUtf32(0x1F4C4)
$balance = [char]::ConvertFromUtf32(0x2696)
$pin = [char]::ConvertFromUtf32(0x1F4CD)
$warning = [char]::ConvertFromUtf32(0x26A0)

# 1. Primary restoration of ?? patterns
$mappings = [ordered]@{
    "(?m)^# \?\? "            = "# $rocket "
    "(?m)^Titel: \?\? "       = "Titel: $rocket "
    "(?m)^## \?\? "           = "## $book "
    "(?m)^### \?\? "          = "### $target "
    "\?\? \*\*\[Leeswijzer"   = "$book **[Leeswijzer"
    "\?\?\?\?\? \*\*\[Rollen" = "$people **[Rollen"
    "\?\?\? \*\*\[90-Dagen"   = "$calendar **[90-Dagen"
    "\?\?\? \*\*\[De toolkit" = "$toolbox **[De toolkit"
    "\?\? \[TMP-09-06"        = "$paper [TMP-09-06"
    "\?\? \[TMP-09-07"        = "$paper [TMP-09-07"
}

# 2. Cleanup of semi-restored artifacts from previous failed attempts
$cleanup = [ordered]@{
    "📍ï¸"                      = $pin
    "\*\*Titel:\*\*\s*📍\s*"    = "**Titel:** $rocket "
    "(?m)^# 📍 "                = "# $rocket "
    "📍\s*\*\*\[Leeswijzer"     = "$book **[Leeswijzer"
    "📍\s*\*\*\[90-Dagen"       = "$calendar **[90-Dagen"
    "📍\s*\*\*\[De toolkit"     = "$toolbox **[De toolkit"
    "(?m)^Status:\s*Definitief" = "Status: Draft"
}

Get-ChildItem -Path $docsDir -Filter *.md -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    $modified = $false

    # Apply Mappings
    foreach ($key in $mappings.Keys) {
        if ($content -match $key) {
            $content = [regex]::Replace($content, $key, $mappings[$key])
            $modified = $true
        }
    }

    # Apply Cleanup & Status Update
    foreach ($key in $cleanup.Keys) {
        if ($content -match $key) {
            $content = [regex]::Replace($content, $key, $cleanup[$key])
            $modified = $true
        }
    }
    
    # Generic cleanup: replace any remaining ?? or groups of ? with a pin
    if ($content -match "\?{2,}") {
        $content = [regex]::Replace($content, "\?{2,}", $pin)
        $modified = $true
    }

    if ($modified) {
        Write-Host "Updated: $filePath"
    }
    
    # Save as UTF-8 No BOM
    [System.IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
}

Write-Host "Process complete."
