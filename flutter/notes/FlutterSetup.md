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

### **8. Android SDK-Komponenten und Emulator einrichten**

#### **Android SDK-Komponenten installieren**
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

#### **Android Emulator einrichten**
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

### **9. Visual Studio für Windows-Desktop-Apps einrichten**

Falls du Windows-Desktop-Apps mit Flutter entwickeln möchtest, ist Visual Studio erforderlich. Hier sind die Schritte zur Installation und Konfiguration:

1. **Windows-Desktop-Unterstützung in Flutter aktivieren**:
   ```powershell
   flutter config --enable-windows-desktop
   ```

1. **Web-Unterstützung in Flutter aktivieren**:
   ```powershell
   flutter config --enable-web
   ```

2. **Visual Studio herunterladen und installieren**:
   - Besuche die [offizielle Visual Studio Website](https://visualstudio.microsoft.com/).
   - Lade die **Community Edition** herunter und installiere sie.

2. **Workloads auswählen**:
   - Während der Installation wähle die folgenden Workloads aus:
     - **Desktopentwicklung mit C++**
     - **Entwicklung von universellen Windows-Plattform-Apps (UWP)**

3. **Visual Studio Build Tools 2019 installieren** (optional):
   - Falls du ältere Projekte oder spezifische Build-Tools benötigst, lade die **Visual Studio 2019 Build Tools** herunter und installiere sie.

4. **Installation überprüfen**:
   - Nach der Installation führe im Terminal den Befehl aus:
     ```powershell
     flutter doctor
     ```
   - Stelle sicher, dass die **Windows-Toolchain** korrekt erkannt wird (Häkchen bei "Visual Studio").

> Hinweis: Visual Studio wird nur benötigt, wenn du Windows-Desktop-Apps entwickeln möchtest. Für Web- oder Android-Apps ist es nicht erforderlich.

---

## Hinweise zur Repository-Struktur

- Das Flutter SDK gehört **nicht** ins Repository (liegt in `.gitignore`)
- Eigene Projekte → `flutter/projects/`
- Übungsaufgaben → `flutter/exercises/`
- Notizen → `flutter/notes/`
- Das SDK liegt bei mir lokal unter `C:\flutter\flutter\` (nicht versioniert)
- das android sdk musste ich umziehen, da der benutzername und somit auch der profilordner einen leerzeichen beinhaltete.
- **Hinweis für andere Rechner**: Falls das Android SDK auf einem anderen Pfad liegt, passe den Pfad wie folgt an:
  1. **Flutter**: Führe im Terminal aus:
     ```powershell
     flutter config --android-sdk "<Pfad-zum-SDK>"
     ```
  2. **Android Studio**: Gehe zu `File > Settings > Appearance & Behavior > System Settings > Android SDK` und wähle den korrekten SDK-Pfad aus.

