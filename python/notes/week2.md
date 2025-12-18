# Meine Markdown Notes – Woche 2



## 📅 Tagesnotizen
## 🗓️ Tag 6 – Funktionen in Python
### Kurze Zusammenfassung:

Der Schwerpunkt heute liegt auf Funktionen in Python.

Funktionen (Überblick)

Funktionen kapseln Teilaufgaben eines Programms. Sie machen Code übersichtlicher, wiederverwendbar und ermöglichen rekursive Algorithmen sowie GUI-Programmierung.

Python kennt vordefinierte Funktionen (len(), round()) und benutzerdefinierte Funktionen.

### 5.1 Warum Funktionen?

Zerlegung komplexer Probleme in Teilprobleme

Wiederverwendbarer Code

Grundlage für Rekursion

Notwendig für Ereignisse (z.B. Button-Klicks in GUIs)

### 5.2 Definition und Aufruf von Funktionen
Allgemeine Struktur
```py
def funktionsname(parameter1, parameter2):
    # Funktionskörper
    return ergebnis
```

Funktionskopf: def, Name, Parameterliste, :

Funktionskörper: eingerückter Codeblock

return gibt einen Wert zurück (optional)

Beispiel
```py
def fallhoehe(t):
    g = 9.81
    return 0.5 * g * t**2

hoehe = fallhoehe(2.5)
```

Argumentname beim Aufruf ≠ Parametername im Funktionskopf

Variablen in Funktionen haben einen eigenen Namensraum

### 5.3 Optionale Parameter & Default-Werte

Parameter können voreingestellte Werte haben → optional.
```py
def fallhoehe(t, g=9.81):
    return 0.5 * g * t**2

fallhoehe(2)          # nutzt g = 9.81
fallhoehe(2, 1.62)    # Mond
```

### 5.4 Funktionen in der Shell testen

Nach dem Ausführen eines Skripts können Funktionen direkt in der Python-Shell aufgerufen werden:
```py
fallhoehe(3)
```

### 5.5 Die return-Anweisung

Gibt einen Wert zurück

Beendet sofort die Funktion

Prozedur (ohne Rückgabewert)

```py
def begruessung(name):
    print("Hallo", name)
```
Mehrere return
```py
def enthalten(liste, wert):
    for x in liste:
        if abs(x - wert) < 0.01:
            return True
    return False
```

### 5.6 Positions- vs. Schlüsselwortargumente
Positionsargumente
```py
fallhoehe(2, 9.81)
```

→ Zuordnung erfolgt über Reihenfolge

Schlüsselwortargumente
```py
fallhoehe(g=1.62, t=2)
```

Vorteile:

bessere Lesbarkeit
Reihenfolge egal
ideal bei vielen optionalen Parametern

### 5.7 Guter Programmierstil
Funktionsnamen
Kleinbuchstaben
sprechend, z.B. berechne_summe, fallhoehe

Funktionsannotationen (Typangaben)
Funktionskopf mit Typangaben für Parameter
```py
def addiere(a: int, b: int):
    return a + b
```

a: int → a soll ein Integer sein
b: int → b soll ein Integer sein


Typangabe für den Rückgabewert
```py
def fallhoehe(t: float, g: float = 9.81) -> float:
    return 0.5 * g * t**2
```
-> int nach der Parameterliste sagt: Die Funktion gibt einen Integer zurück

Python prüft das nicht, aber Tools/IDEs können Warnungen geben, z. B. wenn du return "text" machst
Nur Hinweise, keine automatische Typprüfung

Von IDEs ausgewertet

Docstrings
```py
def fallhoehe(t: float, g: float = 9.81) -> float:
    """
    Berechnet die Fallhöhe eines Körpers.
    
    t: Fallzeit in Sekunden
    g: Gravitationsbeschleunigung (m/s²)
    """
    return 0.5 * g * t**2
```

Wird von help() und Calltips genutzt

### 5.8 Die print()-Funktion
```py
print("A", "B", sep="-", end="!")
```

Wichtige Parameter:

*value: beliebig viele Positionsargumente

sep: Trennzeichen (Standard: " ")
end: Zeilenende (Standard: "\n")
file, flush: meist unverändert

### 5.9 Lokale und globale Namen
```py
def f():
    x = 1

print(x)  # Fehler: x ist lokal
```
Global machen
```py
def f():
    global x
    x = 1
```

Globale Variablen sparsam verwenden

### 5.10 Rekursive Funktionen

Eine rekursive Funktion ruft sich selbst auf.

Wichtig: Abbruchbedingung, sonst Endlosrekursion.

Beispiel (ohne Abbruch → Fehler)
```py
def f(x):
    print(x)
    f(x / 2)
```
Korrektes Muster
```py
def f(x):
    if x <= 1:
        return
    print(x)
    f(x / 2)
```

### Lambda funktion
Lambda Funktionen sind funktionsausdrücke in einer Zeile

lambda Parameter: Ausdruck

man nutzt es zv für map, filter, sort
```py
# lambda funktion mit einem input value
multiplikation = lambda x: x*2
print(multiplikation(2))
# lambda funtkion mit zwei input values
addiere = lambda x,y: x + y
print(addiere(5,3))

```
man braucht ein input (hier x) und eine expression (was pasiert mit input, hier x * 2) für eine lambda funktion. das ganze geht in den output (hier multiplikation). der output als variable speichert also die lambda funktion.

Man kann die Funktion direkt aufrufen, indem du die Lambda-Form in Klammern setzt und dahinter in Klammern die Argumente schreibst.
division = lambda a, b: a/b (10,2)


Welche Werte liefern die Ausdrucke?

Ausdruck                            | Wert
(lambda x, y: x + y) (1, 2)         | 3
(lambda x:x ** 3) (2)               | 8
(1ambda :2) ()                      | 0
(lambda x, y: (y, x)) (1, 2)        | x = 1, y= 2 wird übergeben, (y,x) die lambda funktion liefert als ergebnis das neue tupel (2,1)
(lambda x, y: x[y]) ('Python', 1)   | der lambda funktion wird ('Python', 1) übergeben und liefert das Element an diesem Index des Strings, in dem Fall 'y'
x = 'Python'
y = 1
x[y]  # → 'y'

prices = ['$12.50', '$9.99', '$100.00'] # liste von strings
p = '$12.50'
print(p.replace('$', ''))
print(p)
### map()
Mapping mit map()

Die Funktion map() wendet eine Funktion auf jedes Element einer oder mehrerer Kollektionen an und liefert ein map-Objekt, das die Ergebnisse enthält.

Syntax:
```py
map(Funktion, Kollektion1, Kollektion2, ...)
```

Funktion: Name einer Funktion (ohne Klammern) oder eine Lambda-Funktion.

Kollektion(en): Liste, Tupel oder andere iterierbare Objekte.

Beispiel 1: Länge von Strings berechnen
```py
tiere = ["Wolf", "Rentier", "Maus"]
wortlängen = map(len, tiere)        # map-Objekt
liste_wortlängen = list(wortlängen) # in Liste umwandeln
print(liste_wortlängen)
```

Ausgabe:

[4, 7, 4]


Erläuterung:

len wird auf jedes Element der Liste tiere angewendet.
Ergebnis: Sequenz der Längen als map-Objekt.
Um sie zu sehen, wird das map-Objekt in eine Liste umgewandelt.

Beispiel 2: Zwei Listen paarweise verarbeiten
```py
def addiere(a, b):
    return a + b

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
ergebnis = map(addiere, liste1, liste2)
print(list(ergebnis))
```


Ausgabe:

[5, 7, 9]


Erläuterung:

addiere nimmt zwei Argumente.
map() verarbeitet zwei Listen paarweise (1+4, 2+5, 3+6).
Ergebnis: map-Objekt → in Liste umwandeln, um die Werte zu sehen.

Beispiel 3: Mit Lambda-Funktion
```py
liste = [1, 2, 3, 4]
quadriert = map(lambda x: x**2, liste)
print(list(quadriert))
```

Ausgabe:

[1, 4, 9, 16]


Erläuterung:

Lambda-Funktion wird auf jedes Element angewendet.
Sehr praktisch für kurze, einmalige Funktionen.

Merksatz:

map() = Funktion + Kollektion(en) → map-Objekt mit transformierten Werten.

### filter()
filter() – Kurz & Knapp

Zweck: Wählt Elemente aus einer Kollektion aus, für die eine Testfunktion True zurückgibt → liefert ein filter-Objekt.

Syntax:
```py
filter(Funktion, Kollektion)
```

Wichtig:

Funktion = Testfunktion (Name oder Lambda) → muss True/False zurückgeben

filter-Objekt muss oft mit list() umgewandelt werden, um die Werte zu sehen

Beispiele

1️⃣ Zahlen filtern
```py
zahlen = filter(lambda x: x % 4 == 0, range(20))
print(list(zahlen))  # [0, 4, 8, 12, 16]
```

2️⃣ Strings filtern
```py
tiere = ["Hund", "Katze", "Fuchs", "Eule"]
kurze = filter(lambda s: len(s) <= 4, tiere)
print(list(kurze))  # ['Hund', 'Fuchs', 'Eule']
```

Merksatz:

filter() = Nur Elemente behalten, für die die Testfunktion True liefert

### Imperativ vs. Funktional in Python
1️⃣ Imperatives Programm
```py
a1 = float(input('a1: '))
b1 = float(input('b1: '))
ergebnis = a1 ** 2 + b1 ** 2
print(ergebnis)
```

Schritt für Schritt
Werte in Variablen gespeichert
Klassischer, „befehlsorientierter“ Stil

2️⃣ Funktional verschachtelt
```py
a2 = float(input('a2: '))
b2 = float(input('b2: '))
print((lambda a,b: a**2 + b**2)(a2, b2))
```

Lambda-Funktion
Inputs in Variablen
Funktional, kein explizites Zwischenspeichern des Ergebnisses

3️⃣ Maximal verschachtelt
```py
print("Maximal verschachtelt:", (lambda a,b: a**2 + b**2)(float(input('a: ')), float(input('b: '))))
```

Alles inline
Direkt im print()
Zeigt die rein funktionale Verschachtelung

💡 Merksatz:

Imperativ → beschreibe wie etwas passiert
Funktional → beschreibe was passieren soll

### Rückblick Kapitel 5
Funktionen ermöglichen es, lange Programme zu strukturieren und
übersichtlich zu gestalten.
• In einer def-Anweisung wird eine Funktion definiert und ihr ein Name gegeben. 
Mit diesem Namen kann die Funktion später aufgerufen werden.
• Eine Funktionsdefinition besteht aus einem Kopf und einem Körper. Im Kopf werden die Argumente (Parameter) festgelegt. 
Der Funktionskörper besteht aus Anweisungen, die ausgeführt werden, wenn die Funktion aufgerufen wird.
• Eine Funktion übernimmt Objekte als Argumente (Parameter) und verarbeitet sie. 
In einer return-Anweisung gibt sie ihr Berechnungsergebnis zurück.
• In Funktionsannotationen können die Typen der Argumente und des zurückgegebenen Objekts angegeben werden.
• Der Name einer Funktion darf nur aus Buchstaben, Ziffern und Unterstrichen _ bestehen und muss mit einem Buchstaben oder Unterstrich beginnen.
• Guter Programmierstil: Der Name einer Funktion sollte eine Operation oder das Berechnungsergebnis zum Ausdruck bringen.
• Durch eine Lambda-Form kann eine anonyme Funktion (ohne Namen) definiert werden (Lambda-Funktion).
• Funktionen werden von Python wie Datenobjekte behandelt. Man kann ihnen Namen zuweisen und sie bei Funktionsaufrufen als Argumente übergeben.
• Die Funktionen map() und filter() nehmen als Argumente Funktionen und Kollektionen und berechnen daraus neue Kollektionen.

## Unit-Tests in Python

### Zweck
Mit Unit-Tests überprüft man automatisch, ob eine Funktion korrekt arbeitet.  
Praktisch für kleine Funktionen und Übungen, bevor man das `unittest`-Modul benutzt.

### Aufbau
- `assert <Bedingung>` prüft, ob die Bedingung **wahr** ist.
- Bei `False` wirft Python einen Fehler.
- Am Ende kann eine Erfolgsmeldung ausgegeben werden.

### Beispiel: Durchschnitt berechnen

```python
def berechne_durchschnitt(zahlen: list[float]) -> float | None:
    if len(zahlen) == 0:
        return None
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe / len(zahlen)

def test_berechne_durchschnitt():
    assert berechne_durchschnitt([10, 20, 30]) == 20
    assert berechne_durchschnitt([42]) == 42
    assert berechne_durchschnitt([]) is None
    assert berechne_durchschnitt([-10, 0, 10]) == 0
    print("Alle Tests bestanden ✅")

test_berechne_durchschnitt()
```

### Minimalistische Tests mit assert

Direkt im Skript einsetzbar, für kleine Aufgaben ideal.

Prüft, ob eine Bedingung wahr ist, sonst wird ein AssertionError ausgelöst.

Beispiel:
```py
def berechne_durchschnitt(liste):
    if not liste:
        return None
    return sum(liste) / len(liste)

# Tests
assert berechne_durchschnitt([10, 20, 30]) == 20
assert berechne_durchschnitt([]) is None
```

Vorteile:

Einfach und schnell.
Kein zusätzliches Modul nötig.

Nachteile:

Keine strukturierten Testberichte.
Nicht ideal für größere Projekte.

### Professionelle Tests mit unittest bibliothek

Standardbibliothek in Python.
Tests werden in Klassen organisiert.

Bietet automatischen Testlauf mit Bericht über Erfolg/Misserfolg.

Beispiel:
```py
import unittest

def berechne_durchschnitt(liste):
    if not liste:
        return None
    return sum(liste) / len(liste)

class TestDurchschnitt(unittest.TestCase):
    def test_normale_liste(self):
        self.assertEqual(berechne_durchschnitt([10, 20, 30]), 20)
    
    def test_leere_liste(self):
        self.assertIsNone(berechne_durchschnitt([]))
    
    def test_ein_element(self):
        self.assertEqual(berechne_durchschnitt([42]), 42)

if __name__ == "__main__":
    unittest.main()
```

Vorteile:

Übersichtliche Testberichte.
Gruppierung von Tests möglich.
Skalierbar für größere Projekte.

Nachteile:

Etwas mehr Setup nötig als mit assert.
