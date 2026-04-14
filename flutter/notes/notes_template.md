📘 Meine Flutter Notes – Woche X

Um das Gelernte anzuwenden, notiere ich Lerninhalte, Beispiele und Reflektionen.


📅 Tagesnotizen
🗓️ Tag 1 – Thema / Schwerpunkt Environmentsetup

Kurze Zusammenfassung:

## Flutter CLI – Erste Schritte

Das Flutter CLI ist eine Sammlung von Kommandozeilenbefehlen, mit denen Flutter-Projekte erstellt, verwaltet, getestet, gebaut und deployt werden können – unabhängig von einer IDE.

**Grundsyntax:**
```
flutter [Befehl] [Unterbefehl] [Argumente] [Optionen]
```

---

### Hilfe

```bash
flutter help              # Liste aller Befehle
flutter help [Befehl]     # Hilfe zu einem bestimmten Befehl
```

---

### Projektmanagement

```bash
flutter create meine_app                                        # Neues Projekt erstellen
flutter create --org com.firma --template=app --platforms=android,ios --project-name=MeineApp mein_projekt
```

**Wichtige `create`-Optionen:**
| Option            | Bedeutung                                              |
|-------------------|--------------------------------------------------------|
| `--org`           | Organisations-ID (z. B. `com.meinefirma`)              |
| `--template`      | Projekttyp: `app`, `package`, `plugin`                 |
| `--platforms`     | Zielplattformen: `android`, `ios`, `web`, `windows` …  |
| `--project-name`  | Offizieller App-Name (darf Großbuchstaben enthalten)   |
| `--description`   | Projektbeschreibung                                    |

**Projektstruktur (Auszug):**
```
meine_app/
├── lib/
│   └── main.dart       # Einstiegspunkt der App
├── test/               # Testdateien
├── pubspec.yaml        # Metadaten & Abhängigkeiten
└── README.md
```

---

### Abhängigkeiten (pub)

```bash
flutter pub get                    # Abhängigkeiten herunterladen
flutter pub upgrade                # Abhängigkeiten aktualisieren
flutter pub outdated               # Veraltete Pakete anzeigen
flutter pub add package_name       # Paket hinzufügen
flutter pub remove package_name    # Paket entfernen
```

---

### App ausführen & debuggen

```bash
flutter devices                    # Verfügbare Geräte auflisten
flutter run                        # App im Debug-Modus starten
flutter run -d device_id           # App auf bestimmtem Gerät starten
flutter run -d chrome              # Web (Chrome)
flutter run -d windows             # Windows Desktop
```

**Laufzeit-Shortcuts:**
| Taste | Aktion                                          |
|-------|-------------------------------------------------|
| `r`   | Hot Reload (UI aktualisieren, ohne Neustart)    |
| `R`   | Hot Restart (App neu starten)                   |
| `h`   | Alle Befehle anzeigen                           |
| `d`   | DevTools im Browser öffnen                      |
| `q`   | App beenden                                     |

---

### Testing & Analyse

```bash
flutter test                         # Alle Tests ausführen
flutter test test/my_test.dart       # Einzelnen Test ausführen
flutter analyze                      # Statische Codeanalyse
flutter format lib                   # Code formatieren (Dart Style)
```

---

### Build & Deployment

```bash
# Android
flutter build apk           # APK erstellen
flutter build appbundle     # App Bundle für Play Store

# iOS (nur macOS)
flutter build ios           # iOS-Archiv → danach Xcode für Signierung

# Web
flutter build web           # Web-Version erstellen
```

Ausgabedateien: `build/app/outputs/`

---


Was ich morgen lernen will:

…

🗓️ Tag 2 – Thema / Schwerpunkt

Learningfacts:

…

…

Übungsaufgabe / Beispiel:

// Beispiel oder Übung


Reflexion:

…

Was ich morgen lernen will:

…

Tag 3 – Thema / Schwerpunkt

Learningfacts:

…

…

Codebeispiele:

// Beispielcode


Was ich morgen lernen will:

…

Kompetenzprotokoll Woche X

Ziel: Das Gelernte in vier Kategorien reflektieren, um Theorie, Praxis und Relevanz zu verknüpfen.

1️⃣ Einordnen & Strukturieren (Theorie erklären)

…

2️⃣ Verstehen & Verknüpfen (Praxisbeispiel erläutern)

…

3️⃣ Anwenden & Bewerten (Berufliche Relevanz erörtern)

…

4️⃣ Reflektieren & Hinterfragen (Lernprozess reflektieren / Fragen formulieren)

…

Offene Fragen:

…

…

🧩 Zusammenfassung der Woche

Wichtigste Erkenntnisse:

…

…

Tools / Konzepte, die ich neu verstanden habe:

…

…

Schwierigkeiten / To-do für nächste Woche:

…

…

💡 Nächste Woche – Fokus / Lernziele

…

…

…