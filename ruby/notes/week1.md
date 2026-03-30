Ruby Markdown Notes – Woche 1

Um das Gelernte anzuwenden, notiere ich Lerninhalte, Beispiele und Reflektionen.
[TOC]


📅 Tagesnotizen
# Tag 1 – Ruby / Entwicklungsumgebung aufsetzen

## Kurze Zusammenfassung:

Was war heute Schwerpunkt? Kurzer Überblick über Thema, Übungen oder Theorie.

## Vorgehensweise:

- ruby installieren auch mit empfohlener MSYS2 development toolchain. Ich entscheide mich für die neuste Ruby version 4.0.2.-1 inklusive Devkit. die MSYS2 toolchain ist umfangreich vom Datenvolumen her, aber wird empfohlen für
- nach der Ruby installation kümmere ich mich um die VSCode Extensions: 
  Extension "Ruby LSP" von Shopify installieren (shopify.ruby-lsp) — offizieller Language Server, ersetzt die alte ruby Extension
  
  als optional angegeben wurde der "Ruby Debugger" für Debugging-Support, die extension lass ich mal vorerst weg.

  damit die extension die ruby installation findet, musste ich die settings.json anpassen bzgl:
```json
  "rubyLsp.rubyVersionManager": {
    "identifier": "none"
  }
```

## MSYS2 toolchain

MSYS2 ist eine Unix-ähnliche Entwicklungsumgebung (GCC, Make, etc.) für Windows. Ruby selbst braucht sie nicht — aber viele Gems (Ruby-Pakete) enthalten native Erweiterungen, die in C geschrieben sind und zur Installationszeit kompiliert werden müssen.


Konkrete Beispiele:

nokogiri (XML/HTML-Parsing) — sehr häufig genutzt
bcrypt (Passwort-Hashing)
mysql2 / pg (Datenbank-Treiber)
ffi (Foreign Function Interface)
Ohne MSYS2 bekommst du bei solchen Gems einen Fehler.

## irb

IRB (Interactive Ruby) ist eine REPL-Umgebung, die Ruby-Code Zeile für Zeile ausführt und das Ergebnis sofort anzeigt — ideal zum schnellen Ausprobieren von Ausdrücken und Methoden, ohne eine Datei anlegen zu müssen. Im Gegensatz zum Run-Button bleibt der Zustand (Variablen, Objekte) zwischen den Eingaben erhalten.

Learningfacts
…

…

Beispiele / Code:

// Beispielcode oder Demo


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