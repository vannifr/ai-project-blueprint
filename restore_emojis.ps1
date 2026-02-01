$docsDir = "c:\Users\frevanni\OneDrive - Telenet group\Documents\PM4AI\ai-project-playbook\docs"
$utf8NoBom = New-Object System.Text.UTF8Encoding $false

Write-Host "Starting final cosmetic emoji cleanup..."

# Emojis using Unicode sequences
$rocket = [char]::ConvertFromUtf32(0x1F680)
$book = [char]::ConvertFromUtf32(0x1F4D6)
$target = [char]::ConvertFromUtf32(0x1F3AF)
$shield = [char]::ConvertFromUtf32(0x1F6E1)
$people = [char]::ConvertFromUtf32(0x1F465)
$calendar = [char]::ConvertFromUtf32(0x1F4C5)
$toolbox = [char]::ConvertFromUtf32(0x1F9F0)
$paper = [char]::ConvertFromUtf32(0x1F4C4)
$balance = [char]::ConvertFromUtf32(0x2696)
$pin = [char]::ConvertFromUtf32(0x1F4CD)
$warning = [char]::ConvertFromUtf32(0x26A0) # ⚠️

# Mapping of patterns to emojis for cleanup
$cleanupMappings = [ordered]@{
    "📍ï¸"                   = "$pin"
    "\*\*Titel:\*\*\s*📍\s*" = "**Titel:** $rocket "
    "(?m)^# 📍 "             = "# $rocket "
    "📍\s*\*\*\[Leeswijzer"  = "$book **[Leeswijzer"
    "📍\s*\*\*\[90-Dagen"    = "$calendar **[90-Dagen"
    "📍\s*\*\*\[De toolkit"  = "$toolbox **[De toolkit"
    "📍 Ik ga bouwen"        = "$toolbox Ik ga bouwen"
    "📍 Hoe werkt dit"       = "$book Hoe werkt dit"
    "📍 Legenda"             = "$book Legenda"
    "📍 Doel:"               = "🎯 **Doel:**"
    "📍 Activiteit:"         = "📝 **Activiteit:**"
    "📍 Checklist:"          = "✅ **Checklist:**"
    "📍 Risico:"             = "$warning **Risico:**"
    "📍 Rollen:"             = "👥 **Rollen:**"
}

Get-ChildItem -Path $docsDir -Filter *.md -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    
    $modified = $false
    
    foreach ($key in $cleanupMappings.Keys) {
        if ($content -match $key) {
            $content = [regex]::Replace($content, $key, $cleanupMappings[$key])
            $modified = $true
        }
    }
    
    # Final check for any remaining ?? corruption
    if ($content -match "\?\?") {
        $content = $content -replace "\?\?", $pin
        $modified = $true
    }

    if ($modified) {
        Write-Host "Cleaned up: $filePath"
        [System.IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
    }
}

Write-Host "Cosmetic cleanup complete."
