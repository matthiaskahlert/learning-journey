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

Variablen sind Namen für Werte (wie Etiketten oder Behälter).

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