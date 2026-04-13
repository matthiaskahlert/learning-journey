## a)
Erkläre, was ein Ruby-Source-Code-File ist und welche Dateiendung es typischerweise hat.

Ein Ruby-Source-Code-File ist eine Datei, die Ruby-Code enthält. Diese Dateien haben typischerweise die Dateiendung `.rb`. 
Sie können Ruby-Programme, Klassen, Module oder Skripte enthalten, die in der Ruby-Programmiersprache geschrieben sind.

## b)
Beschreibe, wie ein Ruby-Source-Code-File in verschiedenen Betriebssystemen (Windows, Mac OS X/macOS, Linux und andere UNIX-basierte Systeme) ausgeführt wird. Gib für jedes Betriebssystem spezifische Anweisungen.

### Windows:
1. Öffne die Eingabeaufforderung (cmd) oder PowerShell.
2. Navigiere mit dem Befehl `cd` in das Verzeichnis, in dem sich die Ruby-Datei befindet.
3. Führe das Skript mit dem Befehl `ruby <dateiname>.rb` aus.

### macOS und Linux:
1. Öffne das Terminal.
2. Navigiere mit dem Befehl `cd` in das Verzeichnis, in dem sich die Ruby-Datei befindet.
3. Stelle sicher, dass Ruby installiert ist, indem du `ruby -v` ausführst.
4. Führe das Skript mit dem Befehl `ruby <dateiname>.rb` aus.

**Hinweis:** Unter macOS und Linux können Ruby-Dateien auch direkt ausführbar gemacht werden, indem die erste Zeile der Datei mit `#!/usr/bin/env ruby` beginnt und die Datei mit `chmod +x <dateiname>.rb` ausführbar gemacht wird. Danach kann das Skript mit `./<dateiname>.rb` ausgeführt werden.

## c)
Erkläre, warum es manchmal notwendig ist, Ruby-Scripts von der Befehlszeile oder Terminal aus auszuführen, auch wenn es Möglichkeiten gibt, den Code direkt aus dem Editor auszuführen.

Das Ausführen von Ruby-Skripten über die Befehlszeile oder das Terminal ist notwendig, um:
- Parameter an das Skript zu übergeben.
- Die Umgebung zu simulieren, in der das Skript in der Produktion ausgeführt wird.
- Fehler und Ausgaben direkt zu sehen, insbesondere bei der Entwicklung von Skripten, die mit Dateien, Netzwerken oder anderen Systemressourcen interagieren.
- Sicherzustellen, dass das Skript unabhängig von der IDE oder dem Editor funktioniert.
