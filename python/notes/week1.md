# Meine Markdown Notes – Woche 1

Um das Gelernte anzuwenden, notiere ich Lerninhalte, Beispiele und Reflektionen.


✅ Todo Liste

 Wöchentliches Kompetenzprotokoll vorbereiten
 Themengebiete eingrenzen
 Vier Kategorien beschreiben & Kernfragen beantworten
 Protokoll abschicken zur Bewertung

 Recherche / Tools
 …
 Lernfragen / Nacharbeiten
 …
 Offene Punkte für nächste Woche
 …

## 📅 Tagesnotizen
## 🗓️ Tag 1 – Einstieg in Python programmierung 

### Kurze Zusammenfassung:

Der Schwerpunkt heute liegt auf dem Einrichten der Entwicklungsumgebung und dem Kennenlernen der Grundprinzipien von Python, wie 
- der klaren und gut lesbaren Syntax, 
- der dynamischen Typisierung, 
- dem Arbeiten mit einfachen Datenstrukturen, 
- der Nutzung von Funktionen sowie 
- dem Verständnis grundlegender Programmierkonzepte wie Kontrollstrukturen und Modulen.

###  Anweisungen sind die Grundbausteine eines Programms.
Es gibt einfache und zusammengesetzte Anweisungen. Einfache Anweisungen bestehen oft aus Ausdrücken, wie Zahlen, Zeichenketten oder Rechenoperationen, die vom Interpreter ausgewertet werden. Auch Vergleiche sind Ausdrücke und liefern True oder False.
Funktionsaufrufe sind ebenfalls Anweisungen: Eine Funktion erhält Argumente, verarbeitet sie und gibt ein Ergebnis zurück (z. B. round(1.7) oder min(...)).

### Zuweisungen & Variablen in Python
#### Grundprinzip

Zuweisungen sind sehr häufig und haben die Form:
```python 
name = wert
```
Beispiel:
```python 
x = 1
```

= → Zuweisung

== → Vergleich

Beispiel Vergleich:
```python 
x == 1  # True oder False
```
#### Variablen – Vorstellung & Verhalten


Wert anzeigen:
```python 
x = 1
x        # Ausgabe: 1
```

Wert überschreiben:
```python 
x = 1
x = 5    # ersetzt den alten Wert
```
#### Variablen in Ausdrücken

Variablen können in Berechnungen verwendet werden.
```python 
x = 2
y = x + 3   # y = 5
```
🔹 Werte übertragen

Den Wert einer Variablen an eine andere weitergeben:
```python 
x = 7
y = x       # y = 7
```
#### Mehrere Zuweisungen

Gleicher Wert für mehrere Variablen:
```python 
a = b = c = 10
```

Mehrere Werte gleichzeitig:
```python 
x, y = 1, 2
```

Werte tauschen:
```python 
x, y = y, x
```
#### Regeln für gültige Variablennamen

Erlaubt:

Buchstaben (a–z, A–Z)
Ziffern (0–9)
Unterstrich _
Muss mit Buchstabe oder _ beginnen

Nicht erlaubt:

Unerlaubte Zeichen (-, Leerzeichen, Sonderzeichen)
Beginn mit Ziffer
Schlüsselwörter (z. B. True, if, while, def)

Gültige Beispiele:

a
zahl
zahl_1
geldbetrag
_körpergröße


Ungültige Beispiele:

1_zahl
Atem-Frequenz

#### Variablennamen in Python – Schreibweise (PEP 8)

Empfohlene Schreibweise:
snake_case
→ Standard für Variablen, Funktionen und Methoden.
```py 
user_name = "Anna"
total_price = 19.99
max_speed = 120
```

Nicht empfohlen:
camelCase
→ Technisch möglich, aber unpythonic und nicht PEP-8-konform.
```py 
userName = "Anna"  # nicht empfohlen
```

Ausnahme:
PascalCase
→ Wird für Klassen verwendet.
```py 
class CarModel:
    pass
```

Kurzfazit:
➡️ snake_case für alles,
➡️ PascalCase nur für Klassen,
➡️ camelCase vermeiden

### Erweiterte Zuweisungen & Zahlenverarbeitung in Python

Erweiterte Zuweisung: Kombination aus Zuweisung + Rechenoperation
```py
x += 1  # x um 1 erhöhen, entspricht x = x + 1
x *= 2  # Multiplikation
```

Python als Taschenrechner: Ausdruck eingeben → Ergebnis wird angezeigt
```py
(3 + 2) / 2  # 2.5, Dezimalpunkt beachten
2**8         # Potenzieren, 2 hoch 8
5 % 2        # Modulo: Rest der Division, hier 1
```
Ganzzahlige Division in Python (//)
Die ganzzahlige Division (//) teilt zwei Zahlen und gibt nur den ganzzahligen Anteil zurück – ohne Dezimalstellen.
// rundet immer ab (zu minus unendlich), nicht zur nächsten ganzen Zahl:

```py
# Positive Zahlen
10 // 3    # 3
7 // 2     # 3

# Negative Zahlen (wichtig!)
-10 // 3   # -4  (nicht -3!)
-7 // 2    # -4  (nicht -3!)
```


| Operator      | Erklärung                                  |
|---------------|-------------------------------------------|
| `()`          | Klammern                                   |
| `**`          | Potenzieren                                |
| `*` `/` `//` `%` | Multiplikation, Division, ganzzahlige Division, Modulo |
| `+` `-`       | Addition, Subtraktion                      |

### Python & VS Code Workflow – Checkliste

System-Check
- **Python:** `python --version` → z. B. `3.14.2`
- **pip:** `python -m pip --version` → z. B. `25.3`
- **Jupyter Notebook:** `python -m notebook --version` → z. B. `7.5.0`
- **Python-Skript testen:** `python datei.py` → Ausgabe prüfen
- **Code Runner testen** `strg + alt + n`→ Datei wird im VSCode Terminal ausgeführt

Anstatt immer das Terminal zu öffnen habe ich die extension code runner installiert. ich aktiviere sie mit strg + alt + n


### Zahlenverarbeitung
| Ausdruck       | Ergebnis | Erklärung (ultrakurz) |
|----------------|---------|----------------------|
| 2 + 3 * 2      | 8       | * zuerst, dann +     |
| (2 + 3) * 2    | 10      | Klammern zuerst      |
| 10 / 2         | 5.0     | normale Division     |
| 10 // 3        | 3       | ganzzahlig, abrunden |
| -10 // 3       | -4      | floor Division       |
| 10 % 3         | 1       | Rest der Division    |
| 11 % 3         | 2       | Rest der Division    |
| 12 % 3         | 0       | Rest = 0             |
| 2 ** 3         | 8       | Potenz 2³            |
| 4 ** 0.5       | 2.0     | Wurzel (√4)          |
| 2 + -2         | 0       | Addition/Negation    |
| 1,5 * 2        | ❌       | falsche Syntax       |
| 1.5 * 2        | 3.0     | float Multiplikation |
| 2 + * 3        | ❌       | Syntax Fehler        |
| round(1.23)    | 1       | runden auf int       |
| 1 > 2          | False   | Vergleich            |
| 1 == 1.0       | True    | Gleichheit           |

| Anweisung         | Ergebnis | Erklärung (ultrakurz)           |
|------------------|---------|--------------------------------|
| a = b = 1        | a=1, b=1 | mehrere Variablen gleichzeitig |
| a = a + 2        | a=3     | alte a + 2                     |
| b += 1           | b=2     | erweiterte Zuweisung           |
| c = a + b        | c=5     | Summe a+b                       |
| c = 2 * c        | c=10    | Verdopplung                     |
| a, b = 2.0, 2    | a=2.0, b=2 | mehrere Werte gleichzeitig     |
| c = a / b        | c=1.0   | Division (float)               |
 
 ### 2 Datentyp Hierarchie
 ### Python Typ-Hierarchie

- **Datentyp**
  - **Zahl**
    - `int` → Ganze Zahl, z. B. `123` (unveränderbar)
    - `float` → Gleitkommazahl, z. B. `12.345` (unveränderbar)
    - `complex` → Komplexe Zahl, z. B. `12 + 3j` (unveränderbar)
  - **Wahrheitswert**
    - `bool` → True / False (unveränderbar)
  - **Leeres Objekt**
    - `NoneType` → `None` (unveränderbar)
  - **Kollektion**
    - **Sequenzen**
      - `str` → Zeichenkette, z. B. `'Wort'` (unveränderbar)
      - `tuple` → Tupel, z. B. `(1, 'a')` (unveränderbar)
      - `list` → Liste, z. B. `[1, 2]` (veränderbar)
    - **Mengen**
      - `set` → Menge, z. B. `{1, 2}` (veränderbar)
    - **Abbildungen**
      - `dict` → Dictionary, z. B. `{'A':65,'B':66}` (veränderbar)

### Mutable vs. Immutable

| Typ                | Veränderbarkeit | Beispiel                       | Erklärung kurz |
|-------------------|----------------|--------------------------------|----------------|
| **Immutable**      | unveränderbar  | `int`, `float`, `str`, `tuple` | Inhalt des Objekts kann **nicht direkt geändert** werden. Neue Werte erzeugen ein **neues Objekt**. |
| **Mutable**        | veränderbar    | `list`, `dict`, `set`           | Inhalt des Objekts kann **direkt geändert** werden. |
| **Konstante**      | nicht zwingend | `PI = 3.14`                     | Variable soll **nicht neu zugewiesen** werden (nur Konvention in Python). |

### strings
Strings sind also unveränderbar. Beispiel:
```py
# Dieser Code funktioniert nicht:
s = "Hallo"
s[0] = "X"   # ❌ Fehler: str is immutable

# Aber das geht:
s = "Hallo"
s = "X" + s[1:]   # 👍 neuer String wird erzeugt.
# man kann auch replace nutzen mit dot.notation:
s = s.replace("o", "X")
print(s)  # XallX
```

Normale Strings dürfen NICHT über mehrere Zeilen gehen.
Nur Strings mit drei Anführungszeichen (''' oder """) dürfen das.
Warum?
Weil Python den Zeilenumbruch als Ende der Anweisung interpretiert — außer man nutzt Triple-Quoted Strings, die ausdrücklich Mehrzeiligkeit erlauben.
man kann einen zeilenumbruch aber auch mit eine escape sequenz lösen: \n in einem String erzeugt eine neue Zeile. bei größeren Texten nimmt man aber der einfachheit haber ein triple quote"""


```py
# formatted strings
first = "Matthias"
last = "Kahlert"
# klassische Konkatenation (funktioniert, aber ist weniger elegant)
full1 = first + " " + last # anstatt dieses ausdrucks gibt es formatierte strungs mit geschweiften klammern
print(full1)

# f-string empfohlen, ist moderner, schneller, eleganter
full_formatted_string = f"{first} {last}"
print(full_formatted_string)

# geht auch mehrzeilig
text = f"""
Name: {first} {last}
Status: Aktiv
"""
print(text)
```
### 2.3 StandardTypen

#### Integer (int) – Varianten Dezimal, Binär, Hexadezimal, Oktal


- **Dezimal** (Basis 10, Standard)
```py
x = 42
y = 1234567890
```
Binär (Basis 2, Präfix 0b oder 0B)

```py
b = 0b1010  # 10 in Dezimal
bin(10)     # '0b1010'
```
Hexadezimal (Basis 16, Präfix 0x oder 0X)

```py
h = 0x1a5   # 421 in Dezimal
hex(421)    # '0x1a5'
```
Oktal (Basis 8, Präfix 0o oder 0O)

```py
o = 0o21    # 17 in Dezimal
```
💡 Merkpunkte:

- Ganze Zahlen können beliebig groß sein.
- Dezimalzahlen dürfen nicht mit führender Null beginnen (z. B. 09 ❌).
- Binär, Hex und Oktal sind praktisch für Bits, Farben, Speicheradressen.

| Zahlensystem   | Basis | Präfix        | Beispiel       | Dezimalwert |
|----------------|-------|---------------|----------------|------------|
| Dezimal        | 10    | –             | 42             | 42         |
| Binär          | 2     | 0b / 0B       | 0b1010         | 10         |
| Hexadezimal    | 16    | 0x / 0X       | 0x1a5          | 421        |
| Oktal          | 8     | 0o / 0O       | 0o21           | 17         |

#### Weitere grundlegende Datentypen – float, complex, string

| Typ       | Beschreibung / Besonderheit | Beispiel |
|-----------|----------------------------|----------|
| **float** | Gleitkommazahl, Dezimal oder Exponentialschreibweise | 3.14, 0.23, 2e3 |
| **complex** | Komplexe Zahl: Realteil + Imaginärteil j | 2+3j, 1.5-0.5j |
| **str**   | Zeichenkette, unveränderbar | 'Python', "Hallo Welt" |
💡 Kurz erklärt:

- float: Zahlen mit Nachkommastellen, sehr groß/klein auch als 2e3 (=2000) möglich.
- complex: Reelle + imaginäre Teile, j statt i.
- str: Text, unveränderbar, ein- oder doppelte Anführungszeichen, längere Strings mit """...""".

#### Weitere Python-Grundtypen – Tupel, list, set, dict, bool, NoneType

| Typ       | Beschreibung / Besonderheit | Beispiel |
|-----------|----------------------------|----------|
| **tuple** | Unveränderbare Sequenz beliebiger Objekte | (1, 'a'), (Name, Jahr) |
| **list**  | Veränderbare Sequenz beliebiger Objekte | [1, 2, 3], ['a', 'b'] |
| **set**   | Ungeordnete Kollektion ohne Duplikate | {1, 2, 3}, set() |
| **dict**  | Schlüssel:Wert-Paare, Zugriff über Schlüssel | {'A':65, 'B':66} |
| **bool**  | Wahrheitswert True/False, alle Objekte haben bool-Wert | True, False, bool([]) → False |
| **NoneType** | Leeres Objekt, signalisiert „kein Wert“ | None, z.B. Rückgabewert von print() |
💡 Kurz erklärt:

- tuple: wie ein Container, unveränderbar, auch für „einzelnes Element“ Komma nötig (1,).
- list: veränderbar, Elemente können ersetzt oder hinzugefügt werden.
- set: keine Duplikate, keine Reihenfolge, leere Menge = set().
- dict: Schlüssel → Wert, schnelles Nachschlagen wie Wörterbuch.
- bool: True/False, leere Sequenzen und 0 → False, sonst True.
- NoneType: „kein Wert“, oft Rückgabe von Funktionen, bool(None) → False.

#### Kollektionen – gemeinsame Operationen

- **Kollektion:** Sammlung von Daten (Items), z. B. String, Liste, Tupel, Set, Dict  
- **Sequenz:** geordnete Kollektion (String, Liste, Tupel)  
- **Ungereihte Kollektion:** Set, Dict (keine feste Reihenfolge)  

**Gemeinsame Operationen:**
- **Vorkommen prüfen:** `item in collection` → True/False  
- **Anzahl Items:** `len(collection)`  
- **Iteration:** `for item in collection:` → alle Items durchlaufen  

💡 Hinweis: Diese Operationen gelten für **fast alle Kollektionstypen**.

### Beispiele / Code:

// Beispielcode oder Demo
```py

# Python Grundtypen kompakt

# Integer (ganze Zahl)
i = 42          # Dezimal
b = 0b1010      # Binär → 10
h = 0x1f        # Hex → 31
o = 0o21        # Oktal → 17

# Float (Gleitkommazahl)
f1 = 3.14
f2 = 2e3        # 2000.0

# Complex (komplexe Zahl)
c = 2 + 3j

# String (Zeichenkette)
s = "Python"

# Tuple (unveränderbar)
t = (1, 'a', 3.14)

# List (veränderbar)
l = [1, 2, 3]
l[0] = 10       # ändern erlaubt

# Set (ungeordnet, keine Duplikate)
st = {1, 2, 3}
st.add(4)

# Dictionary (Schlüssel: Wert)
d = {'A': 65, 'B': 66}
d['C'] = 67     # hinzufügen erlaubt

# Bool (Wahrheitswert)
b1 = True
b2 = False
b3 = bool([])   # False, leere Liste → False

# NoneType
n = None        # kein Wert, bool(None) → False

# Ausgabe aller Typen
print("int:", i, b, h, o)
print("float:", f1, f2)
print("complex:", c)
print("str:", s)
print("tuple:", t)
print("list:", l)
print("set:", st)
print("dict:", d)
print("bool:", b1, b2, b3)
print("NoneType:", n)
```

### 2.4 Gemeinsame Operationen für Kollektionen – Zusammenfassung

Kollektion: Zusammenfassung mehrerer Daten (Items).
Sequenzen: geordnete Kollektionen → String, Liste, Tupel
Mengen/Dictionary: ungeordnet, keine feste Reihenfolge

Allgemeine Operationen für alle Kollektionen:

Test auf Vorkommen: item in kollektion → True/False
Anzahl der Items: len(kollektion)
Iteration: Items nacheinander durchlaufen (for item in kollektion)
Sequenz-spezifische Operationen:

Index: Zugriff über Position, 0-basiert, negative Indizes zählen von hinten
```py
s = "Python"
s[0]   # 'P'
s[-1]  # 'n'
```

Konkatenation (+): Zwei Sequenzen gleicher Art verbinden → neue Sequenz
```py
[1,2] + [3,4]   # [1, 2, 3, 4]
"Hi" + "!"      # "Hi!"
```

### 2.5 Typumwandlung

In Python haben Literale einen festen Datentyp:

123 → int

'123' → str
(sieht aus wie eine Zahl, ist aber Text)

Wenn du einen Wert in einen anderen Typ überführen möchtest, nutzt du sogenannte Casting-Funktionen wie int(), float(), str(), list(), set() usw.

🔍 Was bedeutet „Casting“ in Python?

Bei einer Typumwandlung wird kein vorhandenes Objekt verändert.
Python erzeugt ein neues Objekt des gewünschten Typs.

Beispiel:
```py
int("123")   # ergibt die ganze Zahl 123
```

➡️ Die Zeichenkette "123" bleibt bestehen – zusätzlich wird ein neues int-Objekt erzeugt.

#### 2.5.1 Casting zwischen grundlegenden Typen
String → int

Nur möglich, wenn der String tatsächlich eine gültige Zahl enthält:
```py
int("123")      # 123
int("  42 ")    # 42 (Leerzeichen sind erlaubt)
```

Nicht möglich:
```py
int("12a")      # Fehler
int("3.14")     # Fehler, da Dezimalpunkt → float!
```

Casting zu str()

Mit str() kannst du fast jedes Objekt in eine Zeichenkette umwandeln:
```py
str(123)        # "123"
str(3.14)       # "3.14"
str([1, 2, 3])  # "[1, 2, 3]"
```

#### 2.5.2 Casting zu list()

list() erzeugt aus jeder Kollektion oder jedem iterierbaren Objekt eine Liste.

Beispiele:
```py
list("Python")        # ['P', 'y', 't', 'h', 'o', 'n']
list((1, 2, 3))        # [1, 2, 3]
list({10, 20, 30})     # [10, 20, 30] (Reihenfolge beliebig)
```

Nicht möglich:
```py
list(123)  # ❌ Fehler: int ist nicht iterierbar
```

#### 2.5.3 Casting zu set()

set() erzeugt eine Menge aus einer Kollektion oder einem anderen iterierbaren Objekt.
Sets haben zwei wichtige Eigenschaften:

- Sie sind ungeordnet.
- Sie beinhalten keine Duplikate.

Beispiele:
```py
set([1, 2, 2, 3])      # {1, 2, 3}
set("Hallo")           # {'H', 'a', 'l', 'o'} (Reihenfolge beliebig)
set((1, 1, 2, 3))      # {1, 2, 3}
```

Nicht möglich:
```py
set(123)  # ❌ Fehler, int ist nicht iterierbar
```

#### 2.5.4 Wann funktioniert ein Casting – und wann nicht?

Faustregel:
Casting funktioniert nur, wenn Python den Inhalt sinnvoll interpretieren kann.

✔️ sinnvoll:

"123" → Zahl
[1,2,3] → Menge
"abc" → Liste von Zeichen

❌ nicht sinnvoll / Fehler:

"12a" → ganze Zahl
123 → Liste oder Menge
3.14 → int (geht, aber nur durch Abschneiden!)

Beispiele zur Verdeutlichung

✔️ funktioniert
```py
int(3.7)     # 3   (wird abgeschnitten, nicht gerundet!)
float("4.2") # 4.2
list("ab")   # ['a', 'b']
set([1,1,2]) # {1,2}
```

❌ funktioniert NICHT
```py
int("3.14")  # Fehler
set(3)       # Fehler
list(7)      # Fehler
Nicht anwendbar auf Mengen: Keine feste Reihenfolge → Verkettung macht keinen Sinn
Was ich morgen lernen will:
```

### 2.6 Dynamische Typisierung (Kurz & verständlich)

Python verwendet dynamische Typisierung.
Das bedeutet:

Ein Name wird einfach an ein Objekt gebunden:

a = 1


Das Objekt hat einen Typ (int), aber der Name selbst hat keinen festen Typ.
Ein Name kann später problemlos auf ein Objekt anderen Typs zeigen:
```py
a = 1
a = "Hallo"   # jetzt ein str
```

Unterschied zu statisch typisierten Sprachen (Java, C++)

In Java oder C++ muss der Typ vorher festgelegt werden:

int a = 1;


→ a kann dort nur ganze Zahlen speichern.
In Python dagegen wird der Typ erst zur Laufzeit bestimmt – abhängig vom Objekt.

#### Vorteile der dynamischen Typisierung

Weniger Code, leichter lesbar
Flexibler Umgang mit Daten
Schnelles Prototyping

#### Nachteile der dynamischen Typisierung

Einige Typfehler werden erst zur Laufzeit sichtbar
(z. B. wenn versehentlich unterschiedliche Datentypen kombiniert werden)


…

## 🗓️ Tag 2 – Thema / Schwerpunkt

Learningfacts:

### slicing
✅ Grundsyntax
liste[start:stop:step]


start → Index, bei dem das Slicing beginnt (inklusive)

stop → Index, bei dem das Slicing endet (exklusive)

step → Schrittweite (Standard = 1)

Alle drei Teile sind optional.

🔹 Beispiele
1. Vom Anfang bis zu einem Index
liste[:stop]


Beispiel:

zahlen = [10, 20, 30, 40, 50]
print(zahlen[:3])
# [10, 20, 30]

2. Ab einem Index bis zum Ende
liste[start:]


Beispiel:

print(zahlen[2:])
# [30, 40, 50]

3. Zwischen zwei Indizes
liste[start:stop]


Beispiel:

print(zahlen[1:4])
# [20, 30, 40]

4. Mit Schrittweite
liste[start:stop:step]


Beispiel:

print(zahlen[0:5:2])
# [10, 30, 50]

5. Rückwärts Slicing
liste[::-1]


Beispiel:

print(zahlen[::-1])
# [50, 40, 30, 20, 10]

6. Rückwärts mit Start/Stop
liste[stop:start:-1]


Beispiel:

print(zahlen[4:1:-1])
# [50, 40, 30]

Übungen z.b. 
[Übung 2.3.Ü.01](python\notes\week1.md)



## 🗓️ Tag 3 – Interaktive Programme (Kapitel 3)
Learningfacts

Interaktive Programme folgen dem EVA-Prinzip:

- Eingabe (E): Daten vom Benutzer (input())
- Verarbeitung (V): Berechnung oder Manipulation der Daten
- Ausgabe (A): Ergebnis anzeigen (print())

Python-Programme werden als .py-Dateien im VS Code erstellt, gespeichert und ausgeführt.
input() liefert immer str; für Berechnungen ggf. int() oder float() nutzen.
Kommentare mit # verbessern die Lesbarkeit.
Einrückungen strukturieren Python-Code; falsches Einrücken → SyntaxError.

Codebeispiele
Einfaches interaktives Programm
```py
name = input("Name: ")           # Eingabe
gruß = f"Hallo {name}!"          # Verarbeitung + f-string
print(gruß)                      # Ausgabe

# Volumen eines Zylinders (EVA-Prinzip)
h = float(input("Höhe in m: "))       # Eingabe
d = float(input("Durchmesser in m: ")) # Eingabe
V = 3.14 * (d/2)**2 * h               # Verarbeitung
print(f"Volumen des Zylinders: {V:.2f} m³") # Ausgabe
```
VS Code Workflow für Kapitel 3

Datei speichern: Strg + S
Skript ausführen: Strg + Alt + N (Code Runner)
Ausgabe prüfen → Fehler analysieren → Code anpassen → erneut ausführen
Kommentare & Einrückungen beachten → sauberen, lesbaren Code schreiben


### Bugs finden

Debugging: Fehler finden & beheben, wichtigste Lernquelle über Python und Logik.


Fehlertypen

Syntaxfehler → Verstöße gegen Python-Regeln, Programm startet nicht
Laufzeitfehler → Fehler während der Ausführung, z. B. Division durch 0
Semantischer Fehler → Logischer Fehler, Programm läuft, Ergebnis falsch

Tipps zum Fehlerfinden

Sauberer, gut lesbarer Code → Fehler vermeiden
Selbstkritisch testen, kleine Details prüfen
Schrittweise entwickeln & testen → Fehler früh erkennen
Fehler eingrenzen → problematische Stellen auskommentieren (##)

Praxisbeispiele

Syntaxfehler: print("Hallo → fehlendes "

Laufzeitfehler: Division durch 0

Semantischer Fehler: statt Quadrat wird Zahl verdoppelt



### ValueError ist eine Fehlermeldung

In Python wird ein ValueError ausgelöst, wenn ein Wert nicht in den erwarteten Typ konvertiert werden kann.

Beispiele:
```py
int("123")   # klappt, liefert 123
int("abc")   # löst einen ValueError aus, weil "abc" keine Zahl ist
float("3.14")  # klappt, liefert 3.14
float("abc")   # ValueError
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

Kompetenzprotokoll Woche 7

Ziel: Das Gelernte in vier Kategorien reflektieren, um Theorie, Praxis und Relevanz zu verknüpfen.

Kompetenzprotokoll 3 – Einstieg in Python

Dieses Kompetenzprotokoll dokumentiert meine Lernfortschritte der siebten Woche, in der ich erstmals intensiv mit Python gearbeitet habe. Im Fokus standen grundlegende Pythonkonzepte wie Variablen, Datentypen, Operatoren sowie der Unterschied zwischen veränderbaren und unveränderbaren Objekten.

1. Einordnen und Strukturieren (Theorie)
Variablen und Zuweisungen
In Python erfolgt eine Zuweisung über den Ausdruck: name = wert.

Eine Variable ist dabei kein Container, sondern ein Verweis (Reference) auf ein Objekt im Speicher. Wird ein neuer Wert zugewiesen, verweist der Variablenname auf ein neues Objekt.

Beispiel:
```py
x = 1
x = 5   # x verweist nun auf ein neues Objekt
```

Im Gegensatz zu JavaScript, wo Zuweisungen mit destructure eher als Zusatzfeature existieren, bietet Python native und besonders einfache Mehrfach- und Parallelzuweisungen:
```py
a = b = 10
x, y = 1, 2
```
Datentypen und Typ-Hierarchie
Python stellt verschiedene grundlegende Datentypen bereit: Zahlen ( int, float, complex), Wahrheitswerte (bool), Leerer Wert (NoneType ), Sequenzen (str, tuple, list), Mengen (set) und Abbildungen (dict). Diese Datentypen unterscheiden sich insbesondere darin, ob sie veränderbar (mutable) oder unveränderbar (immutable) sind.

Bei Mutable Datentypen (list, dict, set) finden die Änderungen direkt am Objekt statt, während bei  Immutable Datentypen (int, float, strings, Tupel) Änderungen immer ein neues Objekt erzeugen. 
Warum ist das wichtig? weil dieses Konzept entscheidend sein kann für ein korrektes Verständnis von Python, insbesondere im Umgang mit Speicherverwaltung, Referenzen und Funktionen. Es erklärt z.B., warum Listen in funktionen "verändert zurückkommen" können, Zahlen oder Strings jedoch nicht.

2. Verstehen und Verknüpfen (Praxisbeispiele)
Es folgen einige Praxisbeispiele über Unveränderbarkeit von Strings, welche ich in diesem Kompetenzprotokoll reflektieren möchte. Es zeigt: Strings sind unveränderbar. Der Versuch, ein einzelnes Zeichen zu verändern, führt zu einem "TypeError" Fehler.
```py
s = "Hallo"
s[0] = "X"   # TypeError: 'str' object does not support item assignment
```

Um einen geänderten String zu erzeugen, muss ein neues Objekt gebaut werden:
```py
s = "Hallo"
s = "X" + s[1:]
```
Betrachtet man den Unterschied zwischen list und set, erkennt man: Listen erlauben Duplikate, wohingegen Sets doppelte Werte automatisch entfernen.
```py
l = [1, 2, 2, 3]
s = {1, 2, 2, 3}   # doppelte Elemente werden entfernt - > {1, 2, 3}
```
Die Unveränderbarkeit kann man super mit einer Funktion für Speicheradressen und Objektidentität ("id()") untersuchen. Die Funktion id() zeigt die Identität eines Objekts (intern oft dessen Speicheradresse). dafür schauen wir auf ein Beispiel mit immutable - Bei einer Typkonvertierung entsteht hier also ein neues Objekt und  - wie sich herausstellt - daher eine neue ID:
```py
c = 42
print("Wert:", c, "Typ:", type(c), "ID:", id(c)) 
# print ausgabe ist Wert: 42 Typ: <class 'int'> ID: 140709883144264

c = str(c)   # Typecast: int → str
print("Wert:", c, "Typ:", type(c), "ID:", id(c)) 
# print ausgabe ist Wert: 42 Typ: <class 'str'> ID: 21627135164644
```
Obiges Praxisbeispiel zeigt, dass bei Änderungen von immutable objects oder Typecasts bzw Typenkonvertierungen neue Objekte entstehen! Es ändert sich die ID und damit die interne Speicheradresse. Diese Adressen unterscheiden sich auf jedem System, aber es zeigt, dass es ein neues Objekt ist, das auf einen anderen Bereich im Speicher verweist. Gleiches Vorgehen untersuchen wir nun anhand eines mutable Datentyps. Es stellt sich heraus, die Änderungen erfolgen am selben Objekt: 
```py
l = [1, 2, 3]
print("Wert:", l, "Typ:", type(l), "ID:", id(l)) #Wert: [1, 2, 3] Typ: <class 'list'> ID: 2047573815232

l.append(4)
print("Wert:", l, "Typ:", type(l), "ID:", id(l)) #Wert: [1, 2, 3, 4] Typ: <class 'list'> ID: 2047573815232
```
Man erkennt: Listen werden "in-place" verändert, weshalb die Identität und der Speicherwert unverändert bleiben.
Diese Beobachtungen verdeutlichen den grundlegenden Unterschied zwischen veränderbaren und unveränderbaren Datentypen und zeigen wie Python mit Objekten und Referenzen arbeitet

3. Anwenden und Bewerten (berufliche Relevanz)

Die behandelten Grundlagen sind für meine zukünftige Arbeit im Softwaretesting und in der testgetriebenen Entwicklung besonders relevant. Das gewonnene Verständnis von Datentypen und deren veränderbarkeit kann sich zukünftig auf die Qualität und Zuverlässigkeit meiner Tests auswirken.
Zu wissen, wann eine Variable auf ein neues Objekt zeigt und wann ein bestehendes Objekt verändert wird kann entscheidens sein für Fehlersuche und Debugging, Reproduzierbarkeit und Rückverfolgbarkeit von Testergebnissen, das Verstehen von Funktionsparametern und auch für das Vermeiden von Seiteneffekten in Testfällen.

Die Praxisbeispiele von Mutable/Immutable im Testkontext / Softwaretesting und beim Arbeiten mit Testdaten zeigen: Es ist wichtig einschätzen zu können, wann meine Testdaten (z.B. input daten bei Unit-Tests) unverändert bleiben, wann möglicherweise Seiteneffekte auftreten, z.B. wenn ich eine Liste an eine Funktion übergeben muss, wie Datenstrukturen eventuell ungewollt verändert werden und wie man eine sichere Testdatenbasis schafft
Datenaustausch findet ja häufig in Form von JSON-Strukturen oder XML-Modelle statt. Das Konzept hilft mir am Ende des Tages, damit sauberer umzugehen um damit fehlerhafte Testergebnisse zu vermeiden.
Die Grundlagen können mir in Bezug auf Automatisierung auch den Einstieg in Frameworks wie PyTest oder Robot Framework erleichtern z.B. bei der validierung von API-Daten.

4. Reflektieren und Hinterfragen (Weiterentwicklung)

Die erste Python-Woche hat mir einige Bausteine für ein stabiles Fundament vermittelt. Mein bisheriger Kurs und der PYthon kurs sind auch didaktisch unterschiedlich aufgebaut, ich habe den Eindruck dass der Selbststudium anteil in Python höher ist, komme aber aufgrund der Vorkenntnisse aus dem JavaScript kurs ganz okay zurecht damit. Gleichzeitig sind dabei neue Fragen entstanden, die ich versuchen werde, in den kommenden Wochen zu vertiefen:


- Worin unterscheiden sich Shallow Copy und Deep Copy?

- Welche Datenstrukturen eignen sich besonders für umfangreiche Testdaten?

- Wie lassen sich moderne Testing-Konzepte wie Test Driven Develeopment mit Python umsetzen?

- Wie schreibe ich gute Unit-Tests mit Python?

In der nächsten Woche möchte ich bewusst kleine Programme schreiben, um ein besseres Gefühl für Unis-Tests in Python zu bekommen.


## 🗓️ Tag 4 – Interaktive Programme (Kapitel 4)
if … else – Zweiseitige Verzweigung

Wenn Bedingung wahr → if-Block
Sonst → else-Block

alter = int(input("Wie alt bist du? "))

if alter < 18:
    print("Du bekommst eine Kinderkarte.")
else:
    print("Du bekommst eine reguläre Karte.")

 if … elif … else – Mehrere Fälle unterscheiden

Wenn es mehr als zwei Möglichkeiten gibt, benutzt man elif.

Syntax:

if bedingung1:
    ...
elif bedingung2:
    ...
else:
    ...
```py
frage = input("Bitte stellen Sie Ihre Frage: ")

if "Wann" in frage:
    thema = "zum Liefertermin"
    zustaendig = "Carla"
elif "Rechnung" in frage:
    thema = "zur Rechnung"
    zustaendig = "Tom"
else:
    thema = ""
    zustaendig = "Kim"

print("Vielen Dank für Ihre Frage " + thema + ".")
print(zustaendig + " hilft Ihnen gerne weiter.")

```
### Einrückung ist entscheidend!

Alle Anweisungen eines Blocks müssen gleich eingerückt sein (meist 4 Leerzeichen)

if, elif und else müssen bündig untereinander stehen

Einrückungen und Blöcke

In Python entstehen Blöcke durch Einrückung, nicht durch {} wie in anderen Sprachen.

Beispiel:
```py
if x > 10:
    print("x ist größer als 10")  # gehört zum Block
print("fertig")  # außerhalb des Blocks
```
Üblich: 4 Leerzeichen

Nach einem Doppelpunkt beginnt immer ein neuer Block

Leerer Block benötigt pass:
```py
if x > 10:
    pass  # Block muss existieren

```
### Operatoren

| Beispiel                  | Operator | Erklärung               | Wahrheitswert |
|---------------------------|----------|--------------------------|----------------|
| 2 > 1                     | >        | größer                   | True           |
| 1 > 1                     | >        | größer                   | False          |
| 1 >= 1                    | >=       | größer oder gleich       | True           |
| 2 >= 1                    | >=       | größer oder gleich       | True           |
| 1 < 2                     | <        | kleiner                  | True           |
| 1 <= 2                    | <=       | kleiner oder gleich      | True           |
| 1 = 1 *(Syntaxfehler)*    | —        | Zuweisung, kein Vergleich | ❌ Fehler      |
| 1 == 1.0                  | ==       | gleich                   | True           |
| 'Mensch ' == 'Mensch '    | ==       | gleich                   | True           |
| {1, 2} == {2, 1}          | ==       | gleich (ungeordnete Menge) | True         |
| 2 != 3                    | !=       | ungleich                 | True           |
| 2 != 2                    | !=       | ungleich                 | False          |
| 'a' in 'Banane'           | in       | enthalten in             | True           |
| 1 in {1, 2}               | in       | enthalten in             | True           |
| 'I' not in 'Team'         | not in   | nicht enthalten in       | True           |

Logische Operatoren: and, or, not
```py
a = True
b = False

a and b   # False (beide müssen True sein)
a or b    # True  (mindestens einer True)
not a     # False

```
### while schleife
```py
summe = 0
eingabe = input("Zahl: ")

while eingabe:
    summe += float(eingabe)
    eingabe = input("Zahl: ")

print(summe) 
// Eingabe leer → leerer String → boolean False → Schleife endet
```

Kurz-Zusammenfassung: Endloswiederholung, for-Schleifen & range()
1. Endloswiederholung (Endlosschleife)

Eine while-Schleife, deren Bedingung immer True ist, läuft unendlich weiter:

while True:
    print("läuft immer weiter")


Das Programm stoppt nicht von selbst.
Abbrechen:

Strg + C

Fenster schließen

2. Iterationen (for-Schleifen)

Eine Iteration bedeutet: Eine Kollektion (Liste, String, Menge ...) der Reihe nach durchlaufen und für jedes Element denselben Block ausführen.

Beispiel:

for i in [1, 2, 3]:
    print(i)


Ausgabe:

1
2
3

Eigenschaften:

Laufvariable (i) nimmt nacheinander die Werte der Kollektion an.

Reihenfolge bei Listen: fest

Reihenfolge bei Mengen: zufällig, da Mengen ungeordnet sind.

3. Tabellen oder Serien berechnen

Beispiel: Werte von x und x² ausgeben:

for x in [0, 1, 2, 3]:
    print(x, x**2)

### Wiederholungen mit range()

range() erzeugt Zahlenfolgen.

Standardform:
range(n)


liefert:

0, 1, 2, ..., n-1


Beispiel:

for i in range(4):
    print(i)


Ausgabe:

0
1
2
3

Mit Start- und Stop-Wert:
range(start, stop)


liefert:

start, start+1, ..., stop-1


Beispiel:

for i in range(3, 7):
    print(i)


Ausgabe:

3
4
5
6

Liste aus range machen:
list(range(5))


→ [0, 1, 2, 3, 4]

5. Wichtigste Punkte (Rückblick)

Block = Anweisungen mit gleicher Einrückung.

if führt nur aus, wenn Bedingung wahr ist.

if…else entscheidet zwischen zwei Blöcken.

if…elif…else entscheidet zwischen mehreren Fällen.

while wiederholt, solange eine Bedingung wahr ist.

for durchläuft eine Kollektion oder ein range-Objekt.

range() erzeugt Zahlenfolgen effizient.


### Funktionen
Grundaufbau einer Funktion
```py
def funktionsname(parameter):
    # Codeblock (wird ausgeführt, wenn die Funktion aufgerufen wird)
    return ergebnis

⭐ Beispiel 1: einfache Funktion
def hallo():
    print("Hallo Welt!")

```
Aufruf:
```py
hallo()
```
⭐ Beispiel 2: Funktion mit Parametern
```py
def begruessen(name):
    print("Hallo", name)
```

Aufruf:
```py
begruessen("Matthias")
```

⭐ Beispiel 3: Funktion mit Rückgabewert (return)
```py
def quadrat(x):
    return x * x
```

Aufruf:
```py
erg = quadrat(4)
print(erg)   # Ausgabe: 16
```


⭐ Wichtig:

def leitet die Funktionsdefinition ein

Eine Funktion

kann Parameter bekommen
kann Werte zurückgeben (return)
kann beliebig oft verwendet werden


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