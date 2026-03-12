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
#>

param(
    [string]$FileName = "Matthias_Kahlert_Teilpruefung_02"
)

$root = "C:\Users\Matze\repositories\learning-journey"
$tmp = Join-Path $env:TEMP "abgabe_tp"
$javaFile = Join-Path $root "java\src\main\java\exercises\$FileName.java"
$zip = Join-Path $root "$FileName.zip"

# Prüfe ob Java-Datei existiert
if (-not (Test-Path $javaFile)) {
    Write-Host "✗ Datei nicht gefunden: $javaFile"
    exit
}

Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path "$tmp\src\main\java" -Force | Out-Null
Copy-Item $javaFile "$tmp\src\main\java\"

Remove-Item $zip -Force -ErrorAction SilentlyContinue
Compress-Archive -Path "$tmp\src" -DestinationPath $zip
Remove-Item $tmp -Recurse -Force

Write-Host "ZIP erstellt: $zip"

