# Meine Markdown notes Woche 4
## Textverarbeitung in Python
Grundidee

Dieser Abschnitt soll folgende Fragestellungen beinhalten:

- Wie fügt man ungewöhnliche Zeichen (z.B. chinesische Zeichen), die nicht auf einer normalen Tastatur vorkommen, in einen String ein?
- Wie kann man aus Webseiten oder Textdateien gezielt bestimmte Daten herauslesen?
- Wie kann man mit regulären Ausdrücken Textpassagen finden?
- Wie kann man Texte mit variablen Teilen generieren?


### Unicode Nummern für Zeichen


Unicode ordnet jedem sinntragenden Zeichen eine **Nummer** und einen **eindeutigen Namen** zu. Diese Nummern werden von den Standardfunktionen `ord()` und `chr()` verwendet.

### Funktionen für Unicode-Zeichen

#### `ord()` - Zeichen zu Nummer

Die Funktion `ord(c)` liefert zu einem einzelnen Schriftzeichen `c` (String der Länge 1) die Unicode-Nummer als Dezimalzahl.

```py
for buchstabe in 'Abend':
    print(ord(buchstabe), end=' ')
# Ausgabe: 65 98 101 110 100
```

#### `chr()` - Nummer zu Zeichen

Die Funktion `chr(n)` liefert zu einer Unicode-Nummer `n` das zugehörige Zeichen.

```py
print(chr(65))   # A
print(chr(98))   # b
print(chr(101))  # e
```

### UTF-8 Codierung

Die am häufigsten verwendete Codierung für Unicode-Texte ist **UTF-8** (Unicode Transformation Format, 8 Bit).

**Eigenschaften:**
- Zeichen mit Unicode-Nummern **0 bis 127**: jeweils **1 Byte** (8 Bits)
- Übrige Zeichen: **2 bis 4 Bytes**

Dies macht UTF-8 besonders effizient für Texte mit vielen ASCII-Zeichen.

### Escape-Sequenzen

Um Strings mit ungewöhnlichen Symbolen oder Sonderzeichen zu erstellen, verwendest du **Escape-Sequenzen**. Eine Escape-Sequenz ist eine Folge von Zeichen, die mit einem Backslash `\` beginnt.

Mit Escape-Sequenzen kannst du beispielsweise Schriftzeichen aus anderen Sprachen in einen Text einbauen.

#### Übersicht wichtiger Escape-Sequenzen

| Escape-Sequenz | Bedeutung |
|----------------|-----------|
| `\\` | Backslash in einem String |
| `\n` | Zeilenumbruch |
| `\"` | Anführungszeichen in einem String |
| `\N{Name}` | Zeichen mit einem Namen aus der Unicode-Datenbank |
| `\uxxxx` | Zeichen, dessen Unicode-Nummer durch eine vierstellige Hexadezimalzahl angegeben wird |

#### Beispiele

```py
# Backslash und Anführungszeichen
print("Ein Backslash: \\ und ein \"Zitat\"")
# Ausgabe: Ein Backslash: \ und ein "Zitat"

# Zeilenumbruch
print("Erste Zeile\nZweite Zeile")
# Ausgabe:
# Erste Zeile
# Zweite Zeile

# Unicode-Zeichen mit Hexadezimalzahl
print('Pferd heißt auf Chinesisch \u99ac.')
# Ausgabe: Pferd hei��t auf Chinesisch 馬.

# Unicode-Zeichen mit Namen
print('\N{GREEK CAPITAL LETTER DELTA}')
# Ausgabe: Δ
```

### String-Methoden

Strings sind Sequenzen. Über die gemeinsamen Operationen der Sequenzen hinaus gibt es noch einige spezielle Operationen für Strings.

**Wichtig:** Strings sind **unveränderbare Objekte**. Das heißt, keine Methode verändert den String – auch wenn der Name der Methode manchmal so klingt. Stattdessen wird immer ein neuer String zurückgegeben.

#### Übersicht wichtiger String-Methoden

| Methode | Erklärung |
|---------|-----------|
| `s.count(sub)` | Liefert die Anzahl der Vorkommen des Strings `sub` im String `s` |
| `s.endswith(suffix)` | Liefert `True`, falls der String mit der Zeichenkette `suffix` endet, sonst `False` |
| `s.startswith(prefix)` | Liefert `True`, falls der String mit der Zeichenkette `prefix` beginnt, sonst `False` |
| `s.format(...)` | Der String `s` enthält Platzhalter mit geschweifte Klammern, z.B. `{}`. Zurückgegeben wird ein String, in dem die Platzhalter durch Werte ersetzt worden sind |
| `s.join(kollektion)` | Das Argument ist eine Kollektion von Strings. Zurückgegeben wird ein String, in dem alle Elemente der Kollektion über den String `s` als Bindeglied miteinander verbunden sind |
| `s.lower()` | Liefert eine Kopie des Strings aus lauter kleinen Buchstaben |
| `s.upper()` | Liefert eine Kopie des Strings aus lauter Großbuchstaben |
| `s.replace(old, new)` | Liefert eine Kopie der Zeichenkette, bei der alle Vorkommen der Zeichenkette `old` durch `new` ersetzt worden sind |
| `s.split([sep])` | Zurückgegeben wird eine Liste aus Strings, die durch Aufspalten des Strings entstanden sind. Dabei wird das optionale Argument `sep` als Trennstring verwendet. Fehlt das Argument, wird *Leerraum* (Leerzeichen, Zeilenumbruch etc.) als Trennstring verwendet |
| `s.strip()` | Liefert eine Kopie des Strings `s`, bei der am Anfang und Ende Leerraum (Leerzeichen, Zeilenumbruch etc.) entfernt worden ist |
| `s.translate(d)` | Das Argument `d` ist ein Dictionary mit Zuordnungen der Form `nr: zeichenkette`. Die Methode liefert eine Kopie des Strings, in der alle Zeichen mit Unicode-Nummer `nr` durch den String `zeichenkette` ersetzt worden sind |

#### Beispiele

**endswith() - Prüfen ob String mit Zeichenkette endet**

```py
text = 'Python'
print(text.endswith('on'))  # True
print(text.endswith('py'))  # False
```

**replace() - Zeichenketten ersetzen**

```py
text = 'Python'
neuer_text = text.replace('on', 'ons')
print(neuer_text)  # Pythons

# Der ursprüngliche String bleibt unverändert
print(text)  # Python
```

**strip() - Leerraum entfernen**

```py
text = '   \n  Python  \n  '
print(text.strip())  # Python
```

**split() - String in Liste aufspalten**

```py
text = 'Python ist toll'
woerter = text.split()
print(woerter)  # ['Python', 'ist', 'toll']

# Mit eigenem Trennzeichen
text2 = 'eins,zwei,drei'
teile = text2.split(',')
print(teile)  # ['eins', 'zwei', 'drei']
```

**join() - Liste zu String verbinden**

```py
woerter = ['Python', 'ist', 'toll']
text = ' '.join(woerter)
print(text)  # Python ist toll

# Mit anderem Bindeglied
text2 = '-'.join(woerter)
print(text2)  # Python-ist-toll
```

**lower() und upper() - Groß-/Kleinschreibung**

```py
text = 'Python'
print(text.lower())  # python
print(text.upper())  # PYTHON
```

**count() - Vorkommen zählen**

```py
text = 'Ananas'
print(text.count('a'))  # 2
print(text.count('na'))  # 2
```

#### Projekt: Goethes Wortschatz

Dieses Projekt verwendet verschiedene String-Methoden, um herauszufinden, wie viele unterschiedliche Wörter in Goethes "Faust" enthalten sind.

**Vorbereitung:**
- Textdatei von Faust herunterladen (z.B. von [GitHub](https://github.com/martinth/mobverdb/blob/master/faust.txt))
- Als `faust.txt` im Projektverzeichnis speichern
- Kodierung: UTF-8

**Verfahren:**

1. Mit `lower()` werden alle Wörter kleingeschrieben → "der" und "Der" werden als gleich erkannt
2. Mit `replace()` werden alle Satzzeichen entfernt → "laufen" und "laufen." werden als gleich erkannt
3. Mit `split()` wird eine Liste von Wörtern gebildet
4. Mit `set()` wird aus der Liste eine Menge gebildet → alle Duplikate werden automatisch entfernt

**Programmcode:**

```py
# wortschatz.py
PFAD = 'faust.txt'
f = open(PFAD, mode='r', encoding='utf-8')  #2
text = f.read()  #3
f.close()

text = text.lower()  #4

# Alle Satzzeichen durch Leerzeichen ersetzen
for p in '.,:;-?!()_/[]':  #5
    text = text.replace(p, ' ')

wortliste = text.split()  #6
wortmenge = set(wortliste)  #7

print('Wörter insgesamt:', len(wortliste))
print('Unterschiedliche Wörter:', len(wortmenge))
print(list(wortmenge)[:50])  #8 - Erste 50 unterschiedliche Wörter
```

**Erklärung der wichtigsten Zeilen:**

- **#2:** Datei im Lesemodus (`'r'`) mit UTF-8 Kodierung öffnen
- **#3:** Gesamten Dateiinhalt als String einlesen
- **#4:** Alle Buchstaben in Kleinbuchstaben umwandeln
- **#5:** Schleife über alle Satzzeichen, die entfernt werden sollen
- **#6:** Text in Liste von Wörtern aufteilen (bei Leerzeichen)
- **#7:** Menge erstellen → automatisches Entfernen von Duplikaten
- **#8:** Erste 50 unterschiedliche Wörter ausgeben
