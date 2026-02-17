
# Meine Markdown notes Woche 4
## String-Grundlagen und reguläre Ausdrücke

- Ein **String** ist eine nicht änderbare Sequenz von Unicode-Zeichen.
- Ein String-Literal kann mit einfachen oder doppelten Anführungszeichen geschrieben werden: `'...'` oder `"..."`.
- Mit **Escape-Sequenzen** (beginnen mit `\`) können Sonderzeichen definiert werden, z.B. `\n` für einen Zeilenumbruch.
- In einem **Raw-String** (`r'...'`) werden Escape-Sequenzen ignoriert.
- Strings sind **Objekte** mit Methoden, die im Format `objekt.methode()` aufgerufen werden.
- Ein **regulärer Ausdruck** ist ein abstraktes Muster für eine bestimmte Art von Texten (z.B. zum Finden von Telefonnummern oder Datumsangaben).
- Ein String kann **Platzhalter** für variable Teile enthalten. Mit der Methode `format()` werden die Platzhalter durch konkrete Werte ersetzt.

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

#### Unicode facts
- jeder String ist eine Folge von Unicode-Zeichen
- Unicode ist ein internationaler Standard für Schriftzeichen und Symbole
- Unicode ordnet jedem sinntragenden Zeichen eine Nummer und einen eindeutigen Namen zu
- die Nummern werden von den Standardfunktionen ord() und chr() verwendet
- Unicode-Nummern werden meist angegeben als Hexadezimalzahlen (Zahl 16 als Zahlenbasis und die 16 Ziffern 0123456789ABCDEF)



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

#### escape sequencen facts

- zur Erstellung von Strings mit ungewöhnlichen Symbolen oder Sonderzeichen
- eine Escape-Sequenz ist eine Folge von Zeichen, die mit einem Backslash \ beginnt
- z.B.: \n - Zeilenumbruch, \" - Anführungszeichen in einem String
- erlaubt Einbau von Schriftzeichen aus anderen Sprachen in einen Text 



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

#### Projekt: Wie warm wird es heute?

Dieses Projekt ist ein Beispiel für **Webscraping**: Einer Webseite im Internet werden gezielt bestimmte Daten entnommen. In diesem Fall lädt das Programm die Startseite des WDR Köln herunter und sucht die Wetterprognose heraus.

**Grundidee:**

Die Webseite des WDR ist ein langer und komplexer HTML-Text (etwa 2500 Zeilen). Interessant für das Projekt ist die Passage, in der die Wetterprognose beschrieben ist.

Das Programm nutzt die Methode `split()`, um den HTML-Text so zu zerlegen, dass die beiden gesuchten Zahlenwerte (Höchsttemperaturen für heute und morgen) übrigbleiben.

**HTML-Struktur der Wetterprognose:**

```html
<span class="max-temperature">Max: 6°</span>
<span class="hidden"> / Tagestiefstemperatur </span>
<span class="min-temperature">Min: 4°</span>
</li>
<li class="dynamicWeatherInfo">
<span class="city-name hidden">Dortmund, </span>
<span class="date-desc">Morgen</span>
<span class="hidden">: leichter Regen</span>
<!-- ... -->
<span class="max-temperature">Max: 9°</span>
```

**Vorgehensweise:**

1. **Erster Split:** Der Text wird anhand des Trennstrings `'Max:'` aufgeteilt
   - Da `'Max:'` zweimal im Text vorkommt, entsteht eine Liste mit **drei Strings**
   - Die gesuchten Zahlen befinden sich am **Anfang des zweiten und dritten Strings**

2. **Zweiter Split:** Die beiden relevanten Strings werden weiter zerlegt
   - Nach dem Split sieht das so aus: `...6°</span>...` bzw. `...9°</span>...`
   - Trennstring: Gradsymbol `'°'`
   - Die jeweilige Zahl steht direkt **vor** dem Gradsymbol

**Programmcode:**

```py
# wdr_wetter.py
from urllib.request import urlopen

WDR = 'https://www1.wdr.de/index.html'
f = urlopen(WDR)  #1
htmltext = f.read().decode()  #2
f.close()

liste = htmltext.split('Max:')  #3
heute = liste[1].split('°')[0]  #4
morgen = liste[2].split('°')[0]  #5

print('Wie warm wird es?')
print(f'Höchsttemperatur heute: {heute} °C')
print(f'Höchsttemperatur morgen: ' + morgen + '°C')
```

**Erläuterung der Schritte:**

- **#1:** Die Webseite des WDR wird heruntergeladen mit `urlopen()`
- **#2:** Die Webseite wird als Bytestring gelesen und mit `decode()` in einen String überführt
- **#3:** Splitting mit `'Max:'` als Trennstring → es entsteht eine Liste mit drei Strings:
  - `liste[0]`: Text vor dem ersten `'Max:'`
  - `liste[1]`: Text zwischen erstem und zweitem `'Max:'` (enthält Temperatur für heute)
  - `liste[2]`: Text nach dem zweiten `'Max:'` (enthält Temperatur für morgen)
- **#4:** Der zweite String in der Liste (`liste[1]`) wird mit `'°'` gesplittet
  - Es entsteht eine Liste mit zwei Strings: `['6', '</span>...']`
  - Das erste Element (`[0]`) ist die Temperatur für heute
- **#5:** In gleicher Weise wird `liste[2]` analysiert und die Temperatur für morgen ermittelt

**Ausgabe:**

```
Wie warm wird es?
Höchsttemperatur heute: 6°C
Höchsttemperatur morgen: 9°C
```

**Hinweis:** Webscraping ist fragil - wenn die Webseite ihre HTML-Struktur ändert, funktioniert das Programm nicht mehr. Für robustere Lösungen sollte man Libraries wie BeautifulSoup oder offizielle Wetter-APIs verwenden.

#### Die format() Methode im Detail

Die `format()` Methode ersetzt Platzhalter (in geschweifte Klammern `{}`) in einem String durch konkrete Werte.

**Grundprinzip:**
```py
"Text mit {Platzhalter}".format(Wert)
```

##### Varianten der Platzhalter

**1. Leere Platzhalter `{}` - Automatische Reihenfolge**

```py
text = "Ich heiße {} und bin {} Jahre alt."
print(text.format("Max", 25))
# Ausgabe: Ich heiße Max und bin 25 Jahre alt.
```

- Erster `{}` = erstes Argument
- Zweiter `{}` = zweites Argument
- Reihenfolge ist fix

**2. Mit Positionsnummern `{0}`, `{1}`, `{2}` - Flexibel**

```py
text = "Ich heiße {0} und bin {1} Jahre alt."
print(text.format("Max", 25))
# Ausgabe: Ich heiße Max und bin 25 Jahre alt.

# Wiederverwendung möglich
text2 = "{0} mag {1}. {0} isst gerne {1}!"
print(text2.format("Anna", "Pizza"))
# Ausgabe: Anna mag Pizza. Anna isst gerne Pizza!

# Reihenfolge ändern
text3 = "{1} ist {0} Jahre alt."
print(text3.format(25, "Max"))
# Ausgabe: Max ist 25 Jahre alt.
```

- `{0}` = erstes Argument (Index 0)
- `{1}` = zweites Argument (Index 1)
- Platzhalter können mehrfach verwendet werden

**3. Mit Namen `{name}`, `{alter}` - Am lesbarsten**

```py
text = "Ich heiße {name} und bin {alter} Jahre alt."
print(text.format(name="Max", alter=25))
# Ausgabe: Ich heiße Max und bin 25 Jahre alt.

# Reihenfolge der Argumente spielt keine Rolle
text2 = "{name} wohnt in {stadt}."
print(text2.format(stadt="Berlin", name="Anna"))
# Ausgabe: Anna wohnt in Berlin.
```

##### Formatierungsoptionen

**Dezimalzahlen runden**

```py
preis = 19.99765
print("Preis: {:.2f} €".format(preis))
# Ausgabe: Preis: 19.99 €

# {:.2f} bedeutet: 2 Dezimalstellen, f = float
```

**Text ausrichten und auffüllen**

```py
# Links, Mitte, Rechts (Breite: 10 Zeichen)
print("{:<10}".format("links"))   # links     
print("{:^10}".format("mitte"))   #   mitte   
print("{:>10}".format("rechts"))  #     rechts

# Mit Füllzeichen
print("{:*^20}".format("Titel"))  # *******Titel********
```

**Zahlen formatieren**

```py
# Tausendertrennzeichen
zahl = 1234567
print("{:,}".format(zahl))
# Ausgabe: 1,234,567

# Prozent
anteil = 0.756
print("{:.1%}".format(anteil))
# Ausgabe: 75.6%
```

##### Vollständiges Beispiel

```py
name = "Helena"
alter = 28
gehalt = 3500.50

text = """
Name:   {0}
Alter:  {1} Jahre  
Gehalt: {2:.2f} €

{0} ist {1} Jahre alt.
"""

print(text.format(name, alter, gehalt))
```

**Ausgabe:**
```
Name:   Helena
Alter:  28 Jahre  
Gehalt: 3500.50 €

Lisa ist 28 Jahre alt.
```

##### Übersicht Formatierungszeichen

| Format | Bedeutung | Beispiel |
|--------|-----------|----------|
| `{:.2f}` | 2 Dezimalstellen | `{:.2f}".format(3.14159)` → `3.14` |
| `{:10}` | Mindestbreite 10 Zeichen | `"{:10}".format("Hi")` → `Hi        ` |
| `{:<10}` | Linksbündig, Breite 10 | `"{:<10}".format("Hi")` → `Hi        ` |
| `{:>10}` | Rechtsbündig, Breite 10 | `"{:>10}".format("Hi")` → `        Hi` |
| `{:^10}` | Zentriert, Breite 10 | `"{:^10}".format("Hi")` → `    Hi    ` |
| `{:,}` | Tausendertrennzeichen | `"{:,}".format(1000)` → `1,000` |
| `{:.1%}` | Prozent, 1 Dezimalstelle | `"{:.1%}".format(0.5)` → `50.0%` |#


### regEx

| Sonderzeichen | Bedeutung/Beispiel |
|---------------|-------------------|
| `.` | Jedes Zeichen außer Zeilenwechsel (`\n`). `'G.ld'` passt auf `'Gold'` und `'Geld'`. |
| `^` | Beginn eines Strings oder das erste Zeichen nach `\n`. `'^S'` passt auf `'Start'`, nicht aber auf `'der Start'`. |
| `[...]` | Definition einer Menge von Zeichen. Zum Beispiel bezeichnet `'[abc]'` ein Zeichen aus der Menge {a, b, c}. |
| `[^...]` | Komplement einer Zeichenmenge. Zum Beispiel steht `[^aeiouAEIOU]` für ein beliebiges Zeichen, das kein Vokal ist. |
| `*` | Beliebig häufiges (eventuell keinmaliges) Wiederholen des vorausgehenden regulären Ausdrucks. Zum Beispiel passt der reguläre Ausdruck `'a*'` auf `''`, `'a'` und `'aaaaa'`. |
| `+` | Ein- oder mehrmaliges Wiederholen des vorausgehenden regulären Ausdrucks. Zum Beispiel passt der reguläre Ausdruck `'0\d+'` auf `'01'` und `'098012'`, nicht aber auf `'0'`. |
| `?` | Null- oder einmaliges Auftreten des vorhergehenden regulären Ausdrucks |
| `*?`, `+?` | »Nicht gierige« (gierig - engl. greedy) Variante des Stern- bzw. Plusoperators. Die Verwendung bei `findall()` führt zum Finden der kürzesten passenden Textstellen. |
| `{m}` | Exakt m-maliges Wiederholen des vorausgehenden regulären Ausdrucks. Zum Beispiel passt der reguläre Ausdruck `'\d{5}'` auf `'10551'` und `'58452'`. |
| `{m,n}` | Mindestens m-maliges und höchstens n-maliges Wiederholen des vorausgehenden regulären Ausdrucks. |
| `\d` | Dezimalziffer, entspricht der Menge `[0-9]` |
| `\D` | Alle Zeichen außer Dezimalziffern |
| `\s` | Whitespace-Zeichen, d.h. ein Zeichen aus der Menge `[ \t\n\r\f\v]` |
| `\S` | Alle Zeichen außer Whitespace-Zeichen |
| `\w` | Irgendein alphanumerisches Zeichen aus `[a-zA-Z0-9_]` |
| `\W` | Irgendein nicht alphanumerisches Zeichen aus `[^a-zA-Z0-9_]` |
| `\Z` | Ende einer Zeichenkette |
| `\|` | oder (Alternation) |
| `(?:...)` | Zeichengruppe (non-capturing group), z.B. `(?:ha)` |



```py
from re import findall
text = 'Witten 58452 Berlin 10115'
reg = r'\d\d\d\d\d'
gefunden = findall(reg, text)
print(gefunden)
```

| Nr. | Aufgabe | Beispiele | Regex |
|----:|---------|-----------|-------|
| 1 | Positive Gleitkommazahlen als Dezimalbrueche (Python-Syntax) | 15.23, 0.1234 | `r'-?\d+\.\d+'` |
| 2 | Fuenfstellige positive oder negative Zahlen | 58454, -38812 | `r'-?\d{5}'` |
| 3 | Kleingeschriebene Woerter, die auf en enden | laufen, hoeren | `r'\b\w+en\b'` |
| 4 | Gleitkommazahlen als Dezimalbrueche (Python-Syntax) | -15.23, 0.1234 | `r'-?\d+\.\d+'` |
| 5 | Gleitkommazahlen in Exponentialschreibweise (Python-Syntax) | -I.23e4, I.2345E-19 | `r'-?\d+\.\d+[eE]-?\d+'` |
| 6 | Inlandstelefonnummern mit Vorwahl nach DIN 5008 | 0201 89775, 031 78455-53 | `r'\b\d{3,4}\s?-?\d{5,}\b'` |

### Formatangaben
Platzhalter können Formatangaben enthalten: {:n} reserviert n Stellen, hilfreich für Tabellen; Strings linksbündig, Zahlen rechtsbündig.
Für Gleitkommazahlen gibt {:n.mf} die Breite n und m Nachkommastellen an.
```py
text = 'Ergebnis: {:10.2f}'
print(text.format(12.3456))
```

## Zugriff auf die Systemumgebung
GrundIdee
### Modul os -  Funktionen zur Verzeichnis- und Dateiverwaltung
Das Modul os bietet eine plattformunabhängige Schnittstelle zum Betriebssystem und ermöglicht es, systemspezifische Funktionen (wie Dateiverwaltung, Verzeichnisoperationen) auf Windows, Unix und macOS einheitlich zu nutzen. Das Modul sys erlaubt es, die Arbeitsweise des Python-Interpreters zu beobachten und zu beeinflussen. Vorsicht ist geboten, da Betriebssystem-Routinen bei unsachgemäßer Nutzung das System beschädigen können.

| Funktion           | Erklärung |
|--------------------|-----------|
| chdir(path)        | Wechselt das Arbeitsverzeichnis, path ist ein String mit einem absoluten oder relativen Pfad. |
| getcwd()           | Gibt das aktuelle Arbeitsverzeichnis zurück. |
| listdir([path])    | Gibt den Inhalt des Arbeitsverzeichnisses als Liste von Strings zurück. Mit Argument path: Inhalt dieses Verzeichnisses. |
| path.exists(path)  | Testet, ob der angegebene Pfad existiert. |
| path.getatime(path)| Zeitpunkt des letzten Zugriffs (Sekunden seit dem 1.1.1970). |
| path.getmtime(path)| Zeitpunkt der letzten Änderung (Sekunden seit dem 1.1.1970). |
| path.getsize(path) | Dateigröße in Byte. |
| path.isdir(path)   | True, wenn path ein Verzeichnis ist, sonst False. |
| path.isfile(path)  | True, wenn path eine Datei ist, sonst False. |
| path.splitext(p)   | Trennt Dateiname und Extension, liefert Tupel (name, .ext). |
| walk(top)          | Durchläuft den gesamten Verzeichnisbaum ab top, liefert Folge von Tupeln: (Pfad, Unterverzeichnisse, Dateien). |

### Dateien und Verzeichnisse anlegen und umbenennen

Eine häufig vorkommende Routineaufgabe zur Dateiverwaltung ist das Umbenennen und Löschen von Dateien. Das Python-Modul `os` stellt dafür verschiedene Funktionen bereit.

Tabelle 10.2 beschreibt einige Funktionen des Moduls os, die sich mit dieser Thematik befassen:

| Funktion         | Beschreibung                                 |
|------------------|----------------------------------------------|
| mkdir(path)      | Erstellt ein neues Verzeichnis               |
| remove(path)     | Löscht eine Datei                            |
| removedirs(path) | Löscht ein Verzeichnis und ggf. übergeordnete, leere Verzeichnisse |
| rename(old, new) | Benennt eine Datei oder ein Verzeichnis um   |
| rmdir(path)      | Löscht ein (leeres) Verzeichnis              |

### Das Modul sys - die Schnittstelle zum Laufzeitsystem

Das Modul `sys` ermöglicht es, die Arbeitsweise des Python-Laufzeitsystems (Interpreter) zu beobachten und zu beeinflussen. Es stellt wichtige Variablen und Funktionen bereit, um z.B. Kommandozeilen-Argumente auszulesen, den Interpreter zu beenden oder Informationen zur Plattform und Version zu erhalten.

| Variable/Funktion   | Erklärung |
|---------------------|-----------|
| argv                | Liste mit Kommandozeilen-Argumenten |
| executable          | Pfad der ausführbaren Datei des Python-Interpreters |
| exit()              | Beendet das laufende Python-Skript |
| getrefcount(objekt) | Liefert die Anzahl der Referenzen auf ein Objekt |
| platform            | String mit Bezeichnung der aktuellen Plattform (z.B. Linux oder win32) |
| stdin, stdout, stderr | File-Objekte für Standard-Ein-/Ausgabe und Fehlerausgabe (umleitbar) |
| version             | String mit Versionsbezeichnung des Python-Interpreters |


#### Beispiele für stdin, stdout, stderr

```py
import sys

# Standardausgabe (stdout)
print('Hallo Welt!')
sys.stdout.write('Dies ist eine Zeile über stdout.\n')

# Standardeingabe (stdin)
# Eingabe von der Konsole lesen
# name = sys.stdin.readline().strip()
# print('Hallo,', name)

# Standardfehlerausgabe (stderr)
sys.stderr.write('Dies ist eine Fehlermeldung!\n')
```

Mit dem Modul `sys` kann ein Python-Programm Informationen über das aktuelle System abfragen, z.B. das Betriebssystem (`sys.platform`) und die Python-Version (`sys.version`).

Programme können über die Kommandozeile Argumente erhalten, die mit `sys.argv` ausgelesen werden. Das erste Element ist immer der Pfad zum Programm, danach folgen die übergebenen Argumente.

Das Modul sys bietet auch Funktionen, um den Speicherbedarf von Objekten zu prüfen (`sys.getsizeof()`) und wie viele Namen (Referenzen) auf ein Objekt zeigen (`sys.getrefcount()`).

Python gibt Speicherplatz automatisch frei, wenn Objekte nicht mehr gebraucht werden (Garbage Collection).
```py
import sys

# Betriebssystem und Python-Version abfragen
print(sys.platform)   # z.B. 'win32' oder 'linux'
print(sys.version)    # z.B. '3.10.5 (tags/v3.10.5:...)'

# Kommandozeilenargumente anzeigen
print(sys.argv)       # z.B. ['mein_programm.py', '100']

# Speicherbedarf eines Objekts
a = [1, 2, 3]
print(sys.getsizeof(a))

# Referenzanzahl eines Objekts
b = 42
print(sys.getrefcount(b))
```