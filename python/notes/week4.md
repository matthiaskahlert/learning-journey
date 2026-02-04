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
open(file, mode='r', encoding=None)


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
