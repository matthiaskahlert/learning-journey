# 📘 Meine Java Notes – Woche 3

## 🗓️ Tag X – Environment Setup (Java + Maven)

Heute ging es weniger um Java-Code und mehr um Entwicklungsumgebung.
Das ist wichtig, weil der beste Code nichts bringt, wenn Build-Tools nicht korrekt laufen.

## Was war das Problem?

- Der Befehl mvn wurde im Terminal nicht erkannt.
- Die VS Code Extension Maven for Java war installiert, aber Terminal-Befehle funktionierten trotzdem nicht.
- JAVA_HOME war nicht korrekt gesetzt.

## Was habe ich konkret gemacht?

1. Maven-Projektdatei erstellt:
- Datei: java/pom.xml
- Diese Datei beschreibt das Projekt und die Abhängigkeiten.

2. Setup geprüft:
- Geprüft, ob mvn im PATH vorhanden ist.
- Geprüft, ob Java installiert ist.
- Geprüft, ob Maven-Extension installiert ist.

3. Maven installiert:
- Maven lokal im Benutzerprofil installiert:
  C:/Users/.../tools/apache-maven-3.9.9

4. Umgebungsvariablen gesetzt:
- JAVA_HOME auf das JDK gesetzt:
  C:/Program Files/Java/jdk-25.0.2
- Maven bin in den Benutzer-PATH aufgenommen.

5. Funktion getestet:
- mvn -v lief erfolgreich.
- Maven-Compile im Projektordner lief erfolgreich.

## Warum war das nötig, obwohl die Extension installiert ist?

Die Extension in VS Code hilft beim Arbeiten im Editor (Maven-Ansicht, Ziele, Integration).
Sie ersetzt aber nicht automatisch eine systemweit verfügbare Maven-CLI im Terminal.

Kurz:
- Extension = Editor-Integration
- mvn im Terminal = braucht Maven-Installation + PATH

## Was ist Maven?

Maven ist ein Build- und Dependency-Tool für Java-Projekte.

Maven hilft bei:
- Projekt bauen (compile, package)
- Abhängigkeiten herunterladen (Libraries wie org.json)
- Projekt standardisieren (gleiche Struktur, gleiche Befehle)

Wichtigste Datei ist die pom.xml:
- Projektname, Version
- Java-Version
- Bibliotheken (Dependencies)
- Build-Konfiguration

## Wozu brauche ich Maven in meinem Lernprojekt?

- Damit externe Bibliotheken sauber eingebunden werden (z. B. JSON-Bibliothek).
- Damit du nicht manuell JAR-Dateien herunterladen und verlinken musst.
- Damit Build und Ausführung reproduzierbar sind.

## Wo muss ich die Befehle ausführen?

Im Java-Projektordner:
C:/Users/.../repositories/learning-journey/java

Typischer Ablauf:
1. cd C:/Users/.../repositories/learning-journey/java
2. mvn -v
3. mvn compile
4. mvn install

## Merksatz

Ohne korrektes Environment ist Java-Entwicklung mühsam.
Maven macht Builds und Bibliotheken reproduzierbar und deutlich einfacher.

## Anleitung für den zweiten Rechner (Schritt für Schritt)

### Ziel

Am Ende sollen diese Befehle im Projektordner funktionieren:

```powershell
mvn -v
mvn compile
```

### 1) Voraussetzungen installieren

1. JDK installieren (z. B. JDK 21 oder JDK 25).
2. VS Code installieren.
3. In VS Code das Java Extension Pack installieren.
4. Optional, aber empfohlen: Extension Maven for Java installieren.

### 2) Maven lokal installieren (ohne Admin)

1. Maven ZIP herunterladen:
  https://archive.apache.org/dist/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.zip
2. Entpacken nach:
  C:/Users/<DEIN_USER>/tools/apache-maven-3.9.9

### 3) Umgebungsvariablen setzen

PowerShell als normaler User öffnen und ausführen:

```powershell
setx JAVA_HOME "C:\Program Files\Java\jdk-25.0.2"
setx PATH "$env:PATH;C:\Users\<DEIN_USER>\tools\apache-maven-3.9.9\bin"
```

Wichtig:
- JDK-Pfad an deine Installation anpassen.
- <DEIN_USER> durch deinen Windows-Benutzernamen ersetzen.
- Danach VS Code komplett schließen und neu öffnen.

### 4) Im richtigen Ordner arbeiten

Maven-Befehle im Projektordner ausführen, dort wo die pom.xml liegt:

```powershell
cd C:\Users\<DEIN_USER>\repositories\learning-journey\java
mvn -v
mvn compile
```

### 5) Erfolgscheck

- mvn -v zeigt Maven-Version und Java-Version.
- mvn compile endet mit BUILD SUCCESS.

## Troubleshooting

### Problem: "mvn" wird nicht erkannt

- Ursache: Maven nicht im PATH.
- Lösung:
1. Prüfen, ob es die Datei gibt:
  C:/Users/<DEIN_USER>/tools/apache-maven-3.9.9/bin/mvn.cmd
2. PATH erneut setzen.
3. VS Code neu starten.

### Problem: Alles in src ist rot

- Ursache: VS Code Java Language Server hat die Projektstruktur/Source-Root nicht korrekt aktualisiert.
- Lösung:
1. Prüfen, dass die pom.xml im Ordner java liegt.
2. In VS Code: Command Palette -> Java: Clean Java Language Server Workspace.
3. Danach VS Code neu laden.
4. Im Ordner java einmal mvn compile ausführen.

### Problem: JAVA_HOME ist falsch

- Check:

```powershell
echo $env:JAVA_HOME
java -version
```

- Wenn der Pfad nicht zum installierten JDK passt, JAVA_HOME neu setzen und VS Code neu starten.

## Kurzfassung

1. JDK installieren.
2. Maven entpacken.
3. JAVA_HOME + PATH setzen.
4. VS Code neu starten.
5. Im Ordner java mit mvn -v und mvn compile testen.
