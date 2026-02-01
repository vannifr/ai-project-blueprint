$docsDir = "c:\Users\frevanni\OneDrive - Telenet group\Documents\PM4AI\ai-project-playbook\docs"
$utf8NoBom = New-Object System.Text.UTF8Encoding $false

# Define emojis using hex codes to avoid script corruption
$rocket = [char]::ConvertFromUtf32(0x1F680)
$book = [char]::ConvertFromUtf32(0x1F4D6)
$target = [char]::ConvertFromUtf32(0x1F3AF)
$people = [char]::ConvertFromUtf32(0x1F465)
$calendar = [char]::ConvertFromUtf32(0x1F4C5)
$toolbox = [char]::ConvertFromUtf32(0x1F9F0)
$paper = [char]::ConvertFromUtf32(0x1F4C4)
$balance = [char]::ConvertFromUtf32(0x2696)
$pin = [char]::ConvertFromUtf32(0x1F4CD)

# Mappings (using ASCII only in the keys)
$mappings = [ordered]@{
    "(?m)^# \?\? "            = "# $rocket "
    "(?m)^Titel: \?\? "       = "Titel: $rocket "
    "(?m)^## \?\? "           = "## $book "
    "(?m)^### \?\? "          = "### $target "
    "\?\? \*\*\[Leeswijzer"   = "$book **[Leeswijzer"
    "\?\?\?\?\? \*\*\[Rollen" = "$people **[Rollen"
    "\?\?\? \*\*\[90-Dagen"   = "$calendar **[90-Dagen"
    "\?\?\? \*\*\[De toolkit" = "$toolbox **[De toolkit"
}

# Cleanup and Status Update
$cleanup = [ordered]@{
    "(?m)^Status:\s*Definitief" = "Status: Draft"
    "(?m)^Status:\s*Final"      = "Status: Draft"
}

Write-Host "Starting ASCII-safe restoration..."

Get-ChildItem -Path $docsDir -Filter *.md -Recurse | ForEach-Object {
    $filePath = $_.FullName
    try {
        $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
        $modified = $false

        foreach ($key in $mappings.Keys) {
            if ($content -match $key) {
                $content = [regex]::Replace($content, $key, $mappings[$key])
                $modified = $true
            }
        }

        foreach ($key in $cleanup.Keys) {
            if ($content -match $key) {
                $content = [regex]::Replace($content, $key, $cleanup[$key])
                $modified = $true
            }
        }
        
        # Replace any remaining clusters of ? with a pin
        if ($content -match "\?{2,}") {
            $content = [regex]::Replace($content, "\?{2,}", $pin)
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

Write-Host "Completed."
