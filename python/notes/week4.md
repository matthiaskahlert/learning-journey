# Meine Markdown notes Woche 4
## Datenspeicherung - Daten speichern in Python
Grundidee

Während ein Programm läuft, liegen alle Daten im Arbeitsspeicher (RAM).
RAM ist flüchtig → Daten gehen beim Ausschalten verloren.
Für dauerhafte Speicherung müssen Daten in Dateien auf Peripheriespeichern (Festplatte, SSD) gesichert werden.


### Dateien und Streams

Der Zugriff auf Dateien erfolgt über einen Stream.
Ein Stream funktioniert wie ein sequentielles Band mit Lese-/Schreibkopf.
Lesen und Schreiben ist nur nacheinander, nicht beliebig (kein Direktzugriff).

Dateien öffnen: open()
```py
open(file, mode='r', encoding=None)
```

file: Pfad oder Dateiname
mode: Öffnungsmodus
encoding: Zeichencodierung (meist utf-8, nur für Textdateien relevant)

Wichtige Modi

r → Lesen (Text, Standard)

w → Schreiben (überschreibt Datei oder erstellt neue)

a → Anhängen (schreibt am Dateiende)

rb → Lesen (Binärdatei, liefert Bytes)

wb → Schreiben (Binärdatei, erwartet Bytes)


### Stream-Methoden

read() → Liest gesamten Inhalt

write(s) → Schreibt String oder Bytes

flush() → Speichert ohne zu schließen

close() → Schließt und speichert die Datei endgültig

Textdateien speichern

Ablauf:

* Datei im Modus w öffnen
* Text schreiben
* Datei schließen
```py
f = open('text.txt', 'w')
f.write('Annelies Geburtstag: 15. November')
f.close()
```

Textdateien lesen

Ablauf:

* Datei im Modus r öffnen
* Inhalt lesen
* Datei schließen

```py
g = open('text.txt', 'r')
inhalt = g.read()
g.close()
print(inhalt)
```


### Binärdateien & Bytestrings

Binärdateien speichern Rohdaten (z.B. Bilder, Videos, Audio). 
Beim Lesen (rb) erhält man einen Bytestring (bytes).
Bytestrings bestehen aus Zahlen von 0–255, nicht aus Zeichen.

```py
b = b'fdfwjjs-'
list(b)
# [102, 100, 102, 119, 106, 106, 115, 45]
```

Falls Bytes Text darstellen → mit decode() in String umwandeln.


### Laufzeitfehler beim Arbeiten mit Dateien
Typische Probleme

* Datei existiert nicht → open() erzeugt einen Laufzeitfehler

* Datei nicht geschlossen → Datei bleibt gesperrt für andere Prozesse

Ziel:
➡️ Fehler abfangen
➡️ Dateien zuverlässig schließen

### try ... except – Laufzeitfehler abfangen
Grundstruktur
```py
try:
    # kritische Anweisungen
except:
    # Fehlerbehandlung
```

Code im try-Block wird versuchsweise ausgeführt

Tritt ein Laufzeitfehler auf:

* try wird abgebrochen
* except wird ausgeführt
* Programm läuft weiter

Beispiel: Datei sicher lesen
```py
try:
    stream = open('text.txt', 'r')
    daten = stream.read()
    stream.close()
except:
    print('Fehler!')
```
Erklärung

Fehler beim Öffnen, Lesen oder Schließen wird abgefangen

Programm stürzt nicht ab

Nachteil

Fehlersuche wird erschwert, da:

* konkrete Fehlermeldungen unterdrückt werden

* Ursache des Fehlers nicht sichtbar ist

### finally – garantiertes Aufräumen
Problem

Fehler tritt nach dem Öffnen, aber vor dem Schließen der Datei auf

Lösung: finally
```py
try:
    Anweisungen
except:
    Anweisungen
finally:
    Anweisungen
```

finally wird immer ausgeführt

Auch bei Laufzeitfehlern oder Programmabbruch

Beispiel
```py
stream = open('text.txt', 'w')
try:
    stream.write('Meine Daten')
except:
    print('Fehler!')
finally:
    stream.close()
```
Wichtig

finally läuft auch ohne except

Fehlt except:

Programm bricht ab
finally wird trotzdem ausgeführt

### with-Anweisung – die empfohlene Lösung
Grundidee

Automatisches Öffnen und Schließen von Dateien

Sicher auch bei Laufzeitfehlern

Struktur
```py
with A as a:
    Anweisungen
```

A = Objekt (z.B. Stream)
a = Name im Codeblock

Beispiel: Datei schreiben mit with
```py
with open('text.txt', 'w') as stream:
    stream.write('Meine Daten')
```
Eigenschaften

Datei wird automatisch geschlossen
Datei wird immer gespeichert
Sicher bei Laufzeitfehlern
Kürzer und übersichtlicher als try...finally

Entspricht funktional:
```py
stream = open('text.txt', 'w')
try:
    stream.write('Meine Daten')
finally:
    stream.close()
```
Merksätze

* try...except → Fehler abfangen
* finally → Ressourcen immer freigeben
* with → beste Praxis für Dateien in Python

### Vergleich: try...except...finally vs. with
| Aspekt                          | `try...except...finally`                      | `with`-Anweisung                      |
| ------------------------------- | --------------------------------------------- | ------------------------------------- |
| Hauptzweck                      | Fehlerbehandlung **und** Ressourcen freigeben | Automatisches Ressourcen-Management   |
| Datei öffnen                    | Manuell mit `open()`                          | Direkt im `with`-Kopf                 |
| Datei schließen                 | Explizit in `finally` nötig                   | **Automatisch**, kein `close()` nötig |
| Sicherheit bei Fehlern          | Hoch (wenn korrekt geschrieben)               | **Sehr hoch**, standardmäßig sicher   |
| Code-Länge                      | Relativ lang und fehleranfällig               | **Kurz & übersichtlich**              |
| Lesbarkeit                      | Mittel                                        | **Sehr gut**                          |
| Risiko Datei nicht zu schließen | Möglich (bei vergessenem `finally`)           | **Praktisch ausgeschlossen**          |
| Fehlerbehandlung                | Flexibel (verschiedene `except`s möglich)     | Nur indirekt, kombiniert mit `try`    |
| Best Practice für Dateien       | Eher Ausnahmefälle                            | **Empfohlene Standardlösung**         |

Typische Einsatzszenarien
try...except...finally sinnvoll, wenn:

verschiedene Fehlertypen unterschiedlich behandelt werden sollen

zusätzliche Aufräumarbeiten nötig sind (mehr als nur close())

mehrere Ressourcen koordiniert werden müssen

with sinnvoll, wenn:

mit Dateien oder Streams gearbeitet wird

sichergestellt werden soll, dass Ressourcen immer freigegeben werden

Code kurz, sauber und wartbar bleiben soll
