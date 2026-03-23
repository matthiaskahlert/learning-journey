# PowerShell-Skript zum Starten der Derby ij Konsole mit relativen Pfaden
# Dieses Skript funktioniert auf verschiedenen Rechnern, solange die Ordnerstruktur gleich ist

# Wechsle zum java-Verzeichnis (Verzeichnis, in dem dieses Skript sich befindet)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Überprüfe, ob die erforderlichen JAR-Dateien existieren
if (-not (Test-Path "lib/derbytools.jar") -or -not (Test-Path "lib/derby.jar")) {
    Write-Host "Fehler: JAR-Dateien nicht gefunden!" -ForegroundColor Red
    Write-Host "Stelle sicher, dass sich derbytools.jar und derby.jar in ./lib/ befinden."
    exit 1
}

Write-Host "Starte Derby ij Konsole mit relativen Pfaden..."
Write-Host "Aktuelles Verzeichnis: $(Get-Location)"
Write-Host ""

# Starte die ij Konsole mit relativen Pfaden
java -cp "lib/derbytools.jar;lib/derby.jar" org.apache.derby.tools.ij

