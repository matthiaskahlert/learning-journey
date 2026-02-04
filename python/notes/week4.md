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


### Datenstrukturen speichern mit pickle
Zweck des Moduls

pickle dient zum Speichern und Laden beliebiger Python-Datenstrukturen

Unterstützt z.B.:

Listen
Dictionaries
Tupel
Kombinationen davon

Speicherung erfolgt binär, nicht als Text

Grundprinzip

Objekte werden serialisiert → Umwandlung in eine Folge von Bytes
Beim Laden werden sie deserialisiert → Rückwandlung in das Originalobjekt

### Speichern von Daten (Serialisierung)
Voraussetzungen

Datei im Binärmodus zum Schreiben öffnen (wb)

Verwendung von pickle.dump()

Syntax
```py
pickle.dump(objekt, stream)
```

objekt → Datenstruktur (z.B. Liste, Dictionary)
stream → geöffnete Binärdatei

### Beispiel: Liste speichern
```py
import pickle

liste = [1, 2, 3]

with open('liste.dat', 'wb') as stream:
    pickle.dump(liste, stream)
```
Erklärung

* Es wird eine Binärdatei liste.dat erzeugt
* Die Liste wird in Bytes umgewandelt und gespeichert
* Durch with wird die Datei automatisch geschlossen

### Laden von Daten (Deserialisierung)
Voraussetzungen

Datei im Binärmodus zum Lesen öffnen (rb)

Verwendung von pickle.load()

Syntax
```py
daten = pickle.load(stream)
```

daten → Variable für die geladene Datenstruktur

stream → geöffnete Binärdatei

Beispiel: Liste laden
```py
import pickle

with open('liste.dat', 'rb') as stream:
    liste = pickle.load(stream)

print(liste)
```

Wichtige Merksätze

pickle funktioniert nur in Python
Daten sind nicht menschenlesbar

Immer:

wb zum Speichern
rb zum Laden
with + pickle = sichere Best Practice

Typische Einsatzfälle

Zwischenspeichern von Programmdaten
Sichern komplexer Datenstrukturen
Prototypen & Lernprojekte

### Daten im JSON-Format speichern
Motivation

pickle speichert beliebige Python-Objekte, aber:
Binärformat
nicht menschenlesbar
Python-spezifisch

JSON ist eine gut lesbare Textalternative

menschenlesbar
programmunabhängig
weit verbreitet (Web, APIs, Konfigurationsdateien)

Was ist JSON?

JSON (JavaScript Object Notation) beschreibt Datenstrukturen als Text
Obwohl aus JavaScript entstanden:
in fast allen Programmiersprachen nutzbar

In Python: Standardmodul json

JSON-Funktionen in Python
Datei-basiert

json.dump(obj, fp)
Wandelt ein Python-Objekt (obj) in JSON-Text um
Schreibt den Text in einen geöffneten Stream (fp)

json.load(fp)
Liest JSON-Text aus einem Stream (fp)
Wandelt ihn in Python-Datenstrukturen um, wird also zum decodieren verwendet

json.dumps(obj)
Liefert JSON-Text der das python objekt (obj) repräsentiert, gibt es als String zurück

json.loads(s)
Wandelt JSON-String (s) in Python-Datenstrukturen um

Aufbau eines JSON-Texts
JSON-Objekte

Sammlung von Name–Wert-Paaren
Entspricht einem Python-Dictionary

Schreibweise: { }

JSON-Arrays

Sequenz von Werten oder Objekten
Entspricht einer Python-Liste


Schreibweise: [ ]

Elementare Werte

Elementare Werte können ganze Zahlen, Gleitpunktzahlen oder Strings sein.

Beispiel: JSON-Objekt
```py
{
  "Tom": ["0172 567 343", "03202 67231"],
  "Anna": [],
  "Tina": ["0201 897551"]
}
```

➡️ Modelliert ein Telefonverzeichnis
➡️ Schlüssel = Namen, Werte = Listen von Telefonnummern

Praxistipp 💡

Zum Lernen & Testen:

lieber json.dumps() und json.loads() verwenden

Kein Dateizugriff nötig

Ideal zum Experimentieren

Grenzen von JSON ⚠️

JSON unterstützt nur einfache Datenstrukturen:
Nicht direkt serialisierbar
❌ Komplexe Zahlen (complex)
❌ Mengen (set)
⚠️ Tupel (tuple)

Werden als JSON-Arrays gespeichert

Beim Laden → Liste statt Tupel

Merksätze für die Prüfung

JSON = lesbar + plattformunabhängig
Nur Dictionaries, Listen & einfache Datentypen
Strings in JSON → immer doppelte Anführungszeichen
dump/load → Dateien
dumps/loads → Strings

### Daten aus dem Internet lesen

Grundidee

Daten können direkt aus dem www geladen und in Python verarbeitet werden
Dateien im Internet werden über eine URL (Uniform Resource Locator) adressiert

Zugriff mit urllib.request
```py
from urllib.request import urlopen
```
Grundschema
```py
from urllib.request import urlopen

with urlopen(url) as stream:
    daten = stream.read()
```
Erklärung

urlopen(url) öffnet eine Verbindung zu einer Internet-Ressource
s entsteht ein stream-artiges Objekt vom Typ HTTPResponse
read() liest den gesamten Inhalt

Bytes → Text umwandeln

read() liefert immer einen Bytestring
Für lesbaren Text → dekodieren
text = daten.decode()

➡️ Ergebnis ist ein normaler Python-String

### 8.11 Rückblick
• Eine Datei kann mit der Standardfunktion open() als Text- oder Binärdatei zum Lesen (Modus: r bzw. rb) oder Schreiben (Modus: w bzw. wb) geöffnet werden. 
Dann entsteht ein Stream, der den Zugriff auf die Datei ermöglicht.
• Stream-Objekte besitzen die Methoden read() und write() zum Lesen und Schreiben von Daten.
• Wenn eine Datei mit open() geöffnet worden ist, muss sie mit close() wieder geschlossen werden. 
Damit werden etwaige Änderungen physisch gespeichert, und die Datei ist für andere Anwendungen auf dem Computer wieder verfügbar.
• Beim Versuch, Dateien zu öffnen, kann es zu Laufzeitfehlern kommen, z.B. wenn eine Datei mit dem angegebenen Dateinamen nicht existiert.
• Laufzeitfehler können mit try...except...finally-Anweisungen abgefangen werden. 
Anweisungen der try-Klausel werden nur versuchsweise durchgeführt. 
Kommt es zu einem Problem, wird die Ausführung abgebrochen und stattdessen die except-Klausel ausgeführt.
Anweisungen einer (optionalen) finally-Klausel werden in jedem Fall ausgeführt.
• Eine with-Anweisung ermöglicht auf elegante Weise einen sicheren Zugriff auf Dateien. Sie sorgt dafür, dass eine geöffnete Datei auf jeden Fall auch wieder geschlossen wird.
• Mit dem pickle-Mechanismus können beliebige Objekte (z.B. Strings, Zahlen oder Listen) in einer Binärdatei gespeichert werden. 
Man verwendet aus dem Modul pickle die Funktion dump() zum Speichern und load() zum Laden eines gespeicherten Objekts.
• Mit der Funktion urlopen() aus dem Standardmodul urllib.request kann man auf Dateien im Internet zugreifen.
• Dictionaries können als JSON-Objekte in Textdateien gespeichert werden
