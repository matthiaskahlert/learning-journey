# Flutter Entwicklungsumgebung – Einrichtung

Getestet auf: Windows 11, VS Code, April 2026

---

## 1. Flutter SDK herunterladen

1. Gehe auf https://docs.flutter.dev/get-started/install/windows/desktop
2. Lade das aktuelle **stable** SDK-Archiv herunter (`.zip`)
3. Entpacke es nach `C:\flutter\` → der Inhalt liegt dann unter `C:\flutter\flutter\`
   - Kontrollpfad: `C:\flutter\flutter\bin\flutter.bat` muss existieren

---

## 2. PATH-Umgebungsvariable setzen

Öffne **PowerShell als Administrator** und führe aus:

```powershell
[System.Environment]::SetEnvironmentVariable(
  "Path",
  [System.Environment]::GetEnvironmentVariable("Path", "User") + ";C:\flutter\flutter\bin",
  [System.EnvironmentVariableTarget]::User
)
```

Danach ein **neues** Terminal öffnen und prüfen:

```powershell
flutter --version
```

---

## 3. Installation mit flutter doctor prüfen

```powershell
flutter doctor
```

Erwartete Ausgabe (Mindestanforderung für dieses Repository):

| Häkchen | Komponente |
|---------|------------|
| ✓ | Flutter (Channel stable) |
| ✓ | Windows Version |
| ✓ | Chrome |
| ✓ | Visual Studio (für Windows-Desktop-Apps) |

> Android SDK ist optional – nur nötig wenn Android-Apps entwickelt werden sollen.

---

## 4. VS Code konfigurieren

Die Einstellung `dart.flutterSdkPath` ist bereits in `.vscode/settings.json` des Repositories
gesetzt. Sobald das Repository geklont und das SDK unter `C:\flutter\flutter` liegt, erkennt
VS Code das SDK automatisch.

Benötigte VS Code Extensions:
- **Flutter** (von Dart Code) – installiert Dart automatisch mit
  - Extension ID: `Dart-Code.flutter`

Installation über Terminal:
```powershell
code --install-extension Dart-Code.flutter
```

---

## 5. Erste App erstellen (Funktionstest)

```powershell
cd C:\Users\Matze\repositories\learning-journey\flutter\projects
flutter create hello_flutter
cd hello_flutter
flutter run -d chrome
```

Bei Erfolg öffnet sich die Standard-Flutter-Demo im Browser.

---

## 6. Empfohlene zusätzliche Erweiterungen

Neben den grundlegenden Erweiterungen gibt es einige zusätzliche, die die Arbeit mit Flutter und Dart erleichtern:

- **Dart Data Class Generator**: Automatisiert das Erstellen von Datenklassen in Dart
- **Flutter Widget Snippets**: Bietet Code-Snippets für häufig verwendete Flutter-Widgets
- **Awesome Flutter Snippets**: Weitere nützliche Snippets für Flutter
- **Error Lens**: Hebt Fehler und Warnungen direkt im Code hervor
- **GitLens**: Erweitert die Git-Funktionalität von VS Code
- **Material Icon Theme**: Fügt Flutter- und Dart-spezifische Icons hinzu

---

## 7. Android Studio Installation

Android Studio wird für die Flutter-Entwicklung empfohlen, insbesondere für Android-Apps. Befolge diese Schritte zur Installation und Konfiguration:

1. **Android Studio herunterladen und installieren**:
   - Besuche die [offizielle Android Studio Website](https://developer.android.com/studio).
   - Lade die neueste Version für dein Betriebssystem herunter.
   - Folge den Installationsanweisungen auf der Website.

2. **Flutter-Plugin installieren**:
   - Öffne Android Studio.
   - Navigiere zu `Einstellungen` → `Plugins`.
   - Suche im Marketplace nach "Flutter".
   - Klicke auf "Installieren" (das Dart-Plugin wird automatisch mit installiert).
   - Starte Android Studio neu, wenn du dazu aufgefordert wirst.

3. **Flutter SDK-Pfad konfigurieren**:
   - Nach dem Neustart wirst du möglicherweise aufgefordert, den Flutter SDK-Pfad zu konfigurieren.
   - Wähle den Ordner, in dem Flutter installiert ist (z. B. `C:\flutter\flutter`).

4. **Android SDK-Komponenten installieren**:
   - Öffne Android Studio.
   - Navigiere zu `Configure` → `SDK Manager`.
   - Stelle sicher, dass die folgenden Komponenten installiert sind:
     - Android SDK Platform (neueste stabile Version)
     - Android SDK Command-line Tools
     - Android SDK Build-Tools
     - Android Emulator
     - Android SDK Platform-Tools

5. **Installation überprüfen**:
   - Öffne ein Terminal und führe aus:
     ```powershell
     flutter doctor
     ```
   - Stelle sicher, dass es keine Probleme mit der Android-Toolchain gibt.

---

## 8. Android SDK-Komponenten und Emulator einrichten

### Android SDK-Komponenten installieren
Nach der Installation von Android Studio:

1. **SDK Manager öffnen**:
   - Starte Android Studio.
   - Navigiere zu `Configure` → `SDK Manager`.

2. **Notwendige Komponenten installieren**:
   - Stelle sicher, dass die folgenden Komponenten installiert sind:
     - Android SDK Platform (neueste stabile Version)
     - Android SDK Command-line Tools
     - Android SDK Build-Tools
     - Android Emulator
     - Android SDK Platform-Tools

### Android Emulator einrichten
Um Apps ohne physisches Gerät zu testen, richte einen Android Emulator ein:

1. **AVD Manager öffnen**:
   - Gehe in Android Studio zu `Tools` → `Device Manager` (früher "AVD Manager").

2. **Virtuelles Gerät erstellen**:
   - Klicke auf **Create Device**.
   - Wähle ein Geräteprofil (z. B. Pixel 10) und klicke auf **Next**.

3. **System-Image auswählen**:
   - Wähle ein **x86** oder **x86_64** System-Image (empfohlen: mit Google Play).
   - Falls keine System-Images angezeigt werden, klicke auf **Download** neben dem gewünschten Image.

4. **Gerät konfigurieren**:
   - Passe die Einstellungen nach Bedarf an (z. B. RAM, Speicher).
   - Klicke auf **Finish**, um das virtuelle Gerät zu erstellen.

5. **Emulator starten**:
   - Klicke im **Device Manager** auf das Play-Symbol neben deinem virtuellen Gerät.

---

## 9. Visual Studio für Windows-Desktop-Apps einrichten

Falls du Windows-Desktop-Apps mit Flutter entwickeln möchtest, ist Visual Studio erforderlich. Hier sind die Schritte zur Installation und Konfiguration:

1. **Windows-Desktop-Unterstützung in Flutter aktivieren**:
   ```powershell
   flutter config --enable-windows-desktop
   ```

2. **Web-Unterstützung in Flutter aktivieren**:
   ```powershell
   flutter config --enable-web
   ```

3. **Visual Studio herunterladen und installieren**:
   - Besuche die [offizielle Visual Studio Website](https://visualstudio.microsoft.com/).
   - Lade die **Community Edition** herunter und installiere sie.

4. **Workloads auswählen**:
   - Während der Installation wähle die folgenden Workloads aus:
     - **Desktopentwicklung mit C++**
     - **Entwicklung von universellen Windows-Plattform-Apps (UWP)**

5. **Visual Studio Build Tools 2019 installieren** (optional):
   - Falls du ältere Projekte oder spezifische Build-Tools benötigst, lade die **Visual Studio 2019 Build Tools** herunter und installiere sie.

6. **Installation überprüfen**:
   - Nach der Installation führe im Terminal den Befehl aus:
     ```powershell
     flutter doctor
     ```
   - Stelle sicher, dass die **Windows-Toolchain** korrekt erkannt wird (Häkchen bei "Visual Studio").

> Hinweis: Visual Studio wird nur benötigt, wenn du Windows-Desktop-Apps entwickeln möchtest. Für Web- oder Android-Apps ist es nicht erforderlich.

---

## 10. Problembehebung: Emulator-Kompatibilität und Einrichtung

### Ausgangslage
- Ziel: Einrichten einer Flutter-Entwicklungsumgebung, Erstellen einer "Hallo Welt"-App und Ausführen auf einem Android-Emulator.
- Entwicklungsumgebung: Windows 11, VS Code, Flutter SDK, Android Studio.
- Problem: Schwierigkeiten bei der Einrichtung eines funktionierenden Android-Emulators.

### Schritte zur Problemlösung

1. **Flutter SDK und Umgebung einrichten**:
   - Flutter SDK wurde gemäß den Anweisungen heruntergeladen und entpackt.
   - `flutter doctor` wurde ausgeführt, um die Installation zu überprüfen.
   - Android Studio wurde installiert, und notwendige SDK-Komponenten wurden hinzugefügt.

2. **Erstellen der "Hallo Welt"-App**:
   - Mit dem Befehl `flutter create hallo_welt` wurde ein neues Projekt erstellt.
   - Die Standard-Demo-App wurde in der Datei `main.dart` überprüft und als funktional bestätigt.

3. **Emulator-Einrichtung**:
   - Ein Pixel 10-Emulator wurde erstellt, jedoch als "unsupported" markiert.
   - Ursache: Inkompatibles System-Image.
   - Lösung: Wechsel zu einem Pixel 4-Emulator mit einem kompatiblen System-Image (API 30, Google Play x86).

4. **System-Image installieren**:
   - Über den Android Studio SDK Manager wurde das passende System-Image heruntergeladen.
   - Nach der Installation wurde der Emulator erneut getestet.

5. **Erfolgskontrolle**:
   - Nach Abschluss der Einrichtung wurde die "Hallo Welt"-App erfolgreich auf dem Pixel 4-Emulator ausgeführt.

### Fazit
- Die Hauptprobleme lagen in der Kompatibilität des Emulators und der Auswahl des richtigen System-Images.
- Durch die schrittweise Fehlerbehebung konnte die App erfolgreich ausgeführt werden.
- Zukünftige Emulator-Einrichtungen sollten sicherstellen, dass ein kompatibles System-Image (z. B. x86 mit Google Play) verwendet wird.

---

## 11. Problemdokumentation: Java- und Gradle-Kompatibilität bei Flutter/Android

**Ausgangslage:**  
Beim Versuch, ein Flutter-Projekt für Android zu bauen, trat folgender Fehler auf:
- Die verwendete Gradle-Version war zu alt (8.9 statt mindestens 8.13).
- Die installierte Java-Version war zu neu (Java 25), während das Android-Gradle-Plugin nur Java 21 (LTS) unterstützt.

**Lösungsschritte:**
1. Die `gradle-wrapper.properties` wurde auf Gradle 8.13 aktualisiert:
   ```
   distributionUrl=https\://services.gradle.org/distributions/gradle-8.13-bin.zip
   ```
2. Es wurde festgestellt, dass Java 21 nicht installiert war.
3. Java 21 wurde von der offiziellen Oracle-Seite heruntergeladen und unter `C:\Program Files\Java\jdk-21.0.10\` installiert.
4. Die Umgebungsvariable `JAVA_HOME` wurde auf diesen Pfad gesetzt und `%JAVA_HOME%\bin` zur Systemvariable `Path` hinzugefügt.
5. Nach einem Neustart des Terminals zeigte `java -version` die korrekte Java-Version 21 an.
6. Hinweis: Durch das Setzen von `JAVA_HOME` und `Path` nutzen alle Java-Programme standardmäßig Java 21. Für Projekte, die andere Versionen benötigen, kann die Variable temporär angepasst oder in der IDE projektspezifisch gesetzt werden.

**Lernpunkt:**  
Android/Flutter-Projekte benötigen oft spezifische Java- und Gradle-Versionen. Zu neue Java-Versionen werden vom Android-Gradle-Plugin meist nicht unterstützt. Es ist wichtig, die Kompatibilität der eingesetzten Tools zu prüfen und die Umgebungsvariablen entsprechend zu setzen.

---

