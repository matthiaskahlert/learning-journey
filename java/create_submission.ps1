<#
.SYNOPSIS
    Erstellt eine ZIP-Datei für eine Teilprüfungs-Abgabe in der Struktur src/main/java/

.DESCRIPTION
    Skript zum Verpacken einer Teilprüfung-Lösung (*.java) in ein ZIP-Archiv.
    Automatische Ordnerstruktur: src/main/java/[Dateiname].java
    Abhängig von: java/src/main/java/exercises/[FileName].java

.PARAMETER FileName
    Name der Java-Datei ohne .java (Standard: Matthias_Kahlert_Teilpruefung_01)
    Beispiele: "Matthias_Kahlert_Teilpruefung_02", "Matthias_Kahlert_Teilpruefung_3"

.EXAMPLE
    .\create_submission.ps1
    → Paketiert Matthias_Kahlert_Teilpruefung_01.java
    
    .\create_submission.ps1 -FileName "Matthias_Kahlert_Teilpruefung_02"
    → Paketiert Matthias_Kahlert_Teilpruefung_02.java

.OUTPUT
    ZIP-Datei im Repo-Root: [FileName].zip
    Enthält: src/main/java/[FileName].java

    gewünschtes sonderformat in javateilprüfung 5:
    jav_tpl_05_Matthias_Kahlert.zip
    dafür braucht man dann den befehl  .\create_submission.ps1 -ZipName "jav_tpl_05_Matthias_Kahlert.zip"
#>


param(
    [string]$FileName = "Matthias_Kahlert_Teilpruefung_06",
    [string]$ZipName = "",
    [string[]]$ExtraFiles = @()
)

$root = Join-Path $env:USERPROFILE "repositories\learning-journey"
$tmp = Join-Path $env:TEMP "abgabe_tp"
$javaFile = Join-Path $root "java\src\main\java\exercises\$FileName.java"
$zip = if ($ZipName -ne "") { Join-Path $root $ZipName } else { Join-Path $root "$FileName.zip" }

# Prüfe ob Java-Datei existiert
if (-not (Test-Path $javaFile)) {
    Write-Host "✗ Datei nicht gefunden: $javaFile"
    exit
}

# DBConfig automatisch mitliefern wenn FileName TP06 ist und DBConfig.java existiert
$dbConfigFile = Join-Path $root "java\src\main\java\exercises\DBConfig.java"
if ($FileName -like "*Teilpruefung_06*" -and (Test-Path $dbConfigFile)) {
    if ($ExtraFiles -notcontains $dbConfigFile) {
        $ExtraFiles += $dbConfigFile
    }
}

Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path "$tmp\src\main\java" -Force | Out-Null
Copy-Item $javaFile "$tmp\src\main\java\"

# Zusätzliche Dateien kopieren
foreach ($extra in $ExtraFiles) {
    if (Test-Path $extra) {
        Copy-Item $extra "$tmp\src\main\java\"
    }
    else {
        Write-Host "⚠ ExtraFile nicht gefunden: $extra"
    }
}

Remove-Item $zip -Force -ErrorAction SilentlyContinue
Compress-Archive -Path "$tmp\src" -DestinationPath $zip
Remove-Item $tmp -Recurse -Force

Write-Host "ZIP erstellt: $zip"

