# Meine Markdown notes Woche 6
## Fehler finden und beseitigen
Debugging hilft bei der Fehlersuche. in VScode gibt es  verschiedene Arten von breakpoints, linebreaks, conditional breakpoints (stoppen nur bei bestimmten Bedingungen),  Logpoints (geben Nachrichten in der Konsole aus, ohne die Ausführung zu unterbrechen) oder Exception-Breakpoints (Im debug menü aktivierbar, hilfreich um Fehler genau an der Entstehungsstelle zu finden).

Es kann zwischen Synthaktischen und Semantischen Fehlern unterschieden werden.
Syntaxfehler werden beim parsen vom PythonInterpreter und und Laufzeitfehler werden während der Ausführung des Programms angezeigt.
Semantische Fehler treten auf, wenn das erwartete Ergebnis nicht mit dem Resultat übereinstimmt, resultieren aber in keiner Fehlermeldung.
Da Semantische Fehler keine Fehlermeldung, aber falsches Verhalten beinhalten, sind sie am schwierigsten zu finden.
Dazu kann man assertions, Tracing und debugging nutzen. 

Grundsätzlich unterscheidet man drei Fehlertypen:

| Fehlertyp               | Wann tritt er auf?                  | Beispiel           |
| ----------------------- | ----------------------------------- | ------------------ |
| **Syntaxfehler**        | Beim Parsen des Codes               | `if x = 5:`        |
| **Laufzeitfehler**      | Während der Programmausführung      | Division durch 0   |
| **Semantischer Fehler** | Programm läuft, Ergebnis ist falsch | Falsche Berechnung |


### Assert-statements (Zusicherungen)
Assertions prüfen Annahmen im Code (Vor- und Nachbedingungen). 

Format:
```py
assert bedingung
# oder mit Fehlermeldung
assert bedingung, "Fehlermeldung"
```
Die Bedingung kann wahr oder falsch sein.
```py
def verdopple(x):
    assert type(x) in [int, float], "x muss eine Zahl sein"
    return 2 *
```
Es wird überprüft, ob das Argument eine Zahl ist, denn auch Sequenzen oder boolsche ausdrücke (in dem fall dann 0 oder 1) würden ohne laufzeitfehler berechnet werden.

Wenn die Funktion mit einem Argument eines falschen Typs aufgerufen wird, verursacht die assert-Anweisung einen Programmabbruch mit einer Fehlermeldung.
```py
>>> verdopple('1')
Traceback (most recent call last):
    ...
    assert type(x) in [int, float]
AssertionError
```


Ein weiteres beispiel wäre 
```py
def entferne_min(s):
    'Entferne das Minimum in der Liste s.'
    assert isinstance(s, list), "s muss eine Liste sein"
    assert len(s) > 0, "s darf nicht leer sein"
    m = min(s)
    s.remove (m)
    return s
```

Assertions sind für Entwicklungszwecke gedacht und können mit python -O deaktiviert werden. Für produktive Zwecke eignen sich Exceptions deutlich besser.

### Tracing oder Logging
Während der Entwicklung werden oft print()Anweisungen genutzt. Professioneller ist das logging-Modul.
```py
import logging

logging.basicConfig(level=logging.DEBUG)

def berechne(x):
    logging.debug("Eingabewert: %s", x)
    return x * 2

```

| print()                    | logging                  |
| -------------------------- | ------------------------ |
| Immer sichtbar             | Level steuerbar          |
| Muss auskommentiert werden | Kann aktiv bleiben       |
| Keine Struktur             | Professionell einsetzbar |

Logging-Level:
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Tracing ist relevant während der Entwicklungsphase eines Programms. Unter Betrieb kommentiert man diese Überprüfungen dann aus.

Quicksort ist eine Methode, um eine Liste von Zahlen zu sortieren. Es funktioniert nach dem Prinzip "Teile und herrsche".
Die Grundidee
Einen Angelpunkt wählen (Pivot): Du nimmst eine Zahl aus der Liste (z.B. die erste Zahl) als Vergleichspunkt.
Liste aufteilen: Alle Zahlen, die kleiner sind als dein Angelpunkt, kommen in eine linke Liste. Alle, die größer oder gleich sind, in eine rechte Liste.
Dieselbe Methode wiederholen: Für beide neuen Listen machst du genau dasselbe - wieder Angelpunkt wählen, aufteilen usw. Die Listen werden dabei immer kleiner.

Zusammensetzen: Am Ende setzt du alles zusammen: sortierte linke Liste + Angelpunkt + sortierte rechte Liste = fertig sortierte Liste!

Ein quicksort beispiel mit tracing ist Ein quicksort beispiel mit tracing ist Ein quicksort beispiel mit tracing ist [hier](../exercises/Kapitel 13 Uebungen/quicksort.py) zu sehen. Wenn die Datei direkt ausgeführt wird, schreibt die Funktion etwas in die Standardausgabe und
dokumentiert so den Programmablauf. Wird es als Modul importiert, erfolgt keine Ausgabe.

[Dieses Programm](../exercises/Kapitel%2013%20Uebungen/sortierPerformance.py) zeigt die performance bzw laufzeit von zwei verschiedenen Sortieralgorithmen. Das Programm generiert 10000 Zufallszahlen zwischen 0 und 1.000.000 und sortiert diese mit quicksort und zum vergleich mit sorted(). Die Ausgabe zeigt, das quicksort deutlich schneller ist, als Pythons sorted().


### Debugging
VCCode bietet einen integrierten Debugger: Datei oeffnen, Breakpoint setzen (Klick neben die Zeilennummer), mit F5 starten und Python-Konfiguration waehlen.

| Typ                    | Beschreibung                        |
| ---------------------- | ----------------------------------- |
| Line Breakpoint        | Stoppt an einer bestimmten Zeile    |
| Conditional Breakpoint | Stoppt nur wenn Bedingung erfüllt   |
| Logpoint               | Gibt Nachricht aus, ohne zu stoppen |
| Exception Breakpoint   | Stoppt bei Exceptions               |

Beim Stop kannst du Variables, Watch und den Call Stack nutzen.
Mit F10/F11/Shift+F11 gehst du Schritt fuer Schritt weiter.
| Taste     | Funktion     |
| --------- | ------------ |
| F10       | Step Over    |
| F11       | Step Into    |
| Shift+F11 | Step Out     |
| Continue  | Weiterlaufen |

Bedingte Breakpoints und Logpoints helfen, ohne staendig zu stoppen.
“Pause on exceptions” zeigt Fehler genau an der Ursache.

Variables
Zeigt aktuelle Variabeln im aktuellen Scope.

Watch
Eigene Ausdrücke beobachten. Dies ist hilfreich bei Schleifen, Rekursion (wie bei Quicksort) und Zustandsänderungen.

Call Stack
Zeigt:
Welche Funktion welche aufgerufen hat. Dies ist besonders wichtig bei Rekursion. 

Debug Console
Die Debug-Console erlaubt es, Variablen zu verändern, Python-Code ausführen und somit Hypothesen zu testen.

Debug-Konfiguration (launch.json)
Beim ersten Debug-Start erzeugt VSCode eine launch.json.
Beispiel: 
{
  "name": "Python: Aktuelle Datei",
  "type": "python",
  "request": "launch",
  "program": "${file}",
  "console": "integratedTerminal"
}


### Wann welches tool

| Problem               | Werkzeug               |
| --------------------- | ---------------------- |
| Crash sofort          | Exception Breakpoint   |
| Falsches Ergebnis     | Debugger + Watch       |
| Schleifenproblem      | Conditional Breakpoint |
| Performanceproblem    | Profiler               |
| Vorbedingungen prüfen | assert                 |
| Dauerhafte Analyse    | logging                |
| Verhalten absichern   | Unit Tests                |

### Rückblick
Syntaxfehler werden vom Laufzeitsystem automatisch erkannt.
Bei einem Semantikfehler erfüllt das Programm nicht die erwartete Funktion.

Mit Zusicherungen (assert-Anweisungen) kannst du Vor- und Nachbedingungen einer Funktion überprüfen. Ist die Bedingung nicht erfüllt, stoppt der Interpreter die Ausführung des Programms und gibt eine Fehlermeldung aus.
Ein Debugger ist ein nützliches Werkzeug zur Suche nach semantischen Fehlern.
Ein Debugger ermöglicht es, ein Programm schrittweise durchzugehen und an kritischen Stellen Breakpunkte zu setzen, an denen der Programmlauf unterbrochen wird.

Ein Debugger visualisiert die Werte von Variablen und Execution Frames beim Aufruf von Funktionen.

## Objektorientierte Programmierung

Die Objektorientierte Programmierung kurz OOP organisiert Programme in Objekte, die Attrribute und Methoden bündeln.

Attribute und Methoden
Attribute sind Daten die den zustand beschreiben.
Methoden sind Operationen die das Verhalten steuern. 

Verteilte Zudständigkeiten
Objekte übernehmen bestimmte Aufgaben

Objekt und Klasse
Objekt ist eine Instanz einer Klasse.
Klasse ist ein Bauplan der festlegt, welche Attribute und Methoden für Objekte genztzt werden.

Bei der Planung von Klassen nutzt man für den Entwurf der Klassenstruktur UML-Klassendiagramme (Unified Model Language).

Beispiel: Klasse "Flasche"
Attribute: inhalt, max_inhalt, geöffnet
Methoden: öffnen(). schließen(), füllen(), leeren()

Durch die Planung erkennt man, wie das Objekt aussieht, bevor doe programmierung beginnt.

### Klassenstruktur in Python
class: definiert eine Klasse
__init__(): Initialisierungsmethode setzt Attribute auf startwerte
self: referenz auf das aktuelle Objekt
Instanziierung: erfolgt durch Klassenaufruf

### Polymorphie
Polymorphie bedeutet:

Derselbe Operator oder dieselbe Methode verhält sich je nach Objekt unterschiedlich.
Beispielsweise der + Operator wird für verschiedene Datentypen unterschiedlich definiert. Zahlen zählt er zusammen (addition), strings hängt er aneinander (verkettung). Intern nutzt Python da __add__()
Dies kann man nutzen um Operatoren für die eigenen Klassen selbst zu bauen, dies nennt man überladen. 
Einige Methoden sind gekennzeichnet durch  doppelte Unterstriche. Ein gutes Beispiel ist hier das zusammenzählen von punkt koordinaten. 
```py
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Punkt(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
```
Benutzung:
```py
p1 = Punkt(1, 2)
p2 = Punkt(3, 4)

print(p1 + p2)
```
Ergebnis:
(4, 6)

Dies kann man nutzen um das Verhalten von Klassen sauberer zu definieren.

| Methode | Erläuterung |
|---|---|
| `__add__(self, other)` | Überladen des Plusoperators `+` |
| `__bool__(self)` | Liefert für das Objekt einen Wahrheitswert. Die Methode sollte `True` zurückgeben, falls das Objekt als »wahr« angesehen wird, und sonst `False`. |
| `__eq__(self, other)` | Gleichheitsoperator `==`. Die Auswertung des Vergleichs `a == b` führt zum Methodenaufruf `a.__eq__(b)`. |
| `__ge__(self, other)` | Überladen des Größer-oder-gleich-Operators `>=` |
| `__gt__(self, other)` | Überladen des Größer-als-Operators `>` |
| `__le__(self, other)` | Überladen des Kleiner-oder-gleich-Operators `<=` |
| `__len__(self)` | Überladen der Standardfunktion `len()` |
| `__lt__(self, other)` | Überladen des Kleiner-als-Operators `<` |
| `__mod__(self, other)` | Überladen des Modulo-Operators `%` |
| `__mul__(self, other)` | Überladen des Multiplikationsoperators `*` |
| `__ne__(self, other)` | Überladen des Ungleich-Operators `!=` |
| `__str__(self)` | Liefert einen String, der das Objekt repräsentiert. Wird das Objekt mit einer `print()`-Funktion ausgegeben, so wird diese Methode aufgerufen. |

Polymorphie ist das Prinzip, dass für die “gleiche Schnittstelle, unterschiedliches Verhalten” möglich ist

### Vererbung
Vererbung beschreibt die Beziehung zwischen einer **Basisklasse** (Superklasse) und einer **Unterklasse** (Subklasse).
Die Unterklasse erbt alle Attribute und Methoden der Basisklasse und kann diese erweitern oder überschreiben.

**Syntax:**
```py
class Basisklasse:
    def methode(self):
        return "Basis"

class Unterklasse(Basisklasse):  # ← Erbt von Basisklasse
    def neue_methode(self):
        return "Neu"
```

**Was wird geerbt?**
- ✓ Alle Attribute
- ✓ Alle Methoden
- ✗ Der `__init__()` wird NICHT automatisch geerbt (muss explizit aufgerufen werden)

**Basisklasse-Methode aufrufen: `super()`**
```py
class Fahrzeug:
    def __init__(self, marke):
        self.marke = marke
    
    def info(self):
        return f"Fahrzeug: {self.marke}"

class Auto(Fahrzeug):
    def __init__(self, marke, tueren):
        super().__init__(marke)      # ← Ruft __init__ der Basisklasse auf
        self.tueren = tueren         # ← Neues Attribut
    
    def info(self):                  # ← Überschreibt Methode
        basis_info = super().info()  # ← Nutzt Basisklasse-Methode
        return f"{basis_info}, {self.tueren} Türen"
```

**Methoden überschreiben (Override)**
Unterklasse kann eine Methode anders definieren:
```py
class Tier:
    def laut(self):
        return "Tier macht Laut"

class Hund(Tier):
    def laut(self):                  # ← Überscheben
        return "Wau Wau!"

h = Hund()
print(h.laut())  # Ausgabe: Wau Wau!
```

**Mehrfach-Vererbung:**
Eine Klasse kann von mehreren Klassen erben:
```py
class Schwimmbar:
    def schwimmen(self):
        return "Schwimmt"

class Landtier:
    def rennen(self):
        return "Rennt"

class Ente(Schwimmbar, Landtier):
    pass

e = Ente()
print(e.schwimmen())  # Schwimmt
print(e.rennen())     # Rennt
```

**Vorteile:**
| Vorteil | Erklärung |
|---------|-----------|
| Code-Wiederverwendung | Keine Duplication von gemeinsamen Methoden |
| Hierarchie | Klare Struktur (z.B. Tier → Hund, Auto, Fahrrad) |
| Erweiterbarkeit | Neue Klassen einfach ableitbar |
| Überschreiben | Angepasstes Verhalten in Unterklassen |

### Rückblick

    In einer class-Definition legst du fest, welche Attribute und Methoden Objekte dieses Typs haben.
    Methoden sind Funktionen, die zu einem Objekt gehören und so aufgerufen werden: objekt.methode().
    In Methoden steht als erster Parameter fast immer self – das ist das aktuelle Objekt.
    Mit magischen (dunder) Methoden wie __add__() oder __str__() kannst du Operatoren und Standardfunktionen überladen (Polymorphie).
    Mit Vererbung kannst du neue Klassen aus bestehenden ableiten: class Unterklasse(Basisklasse):
    Mit super() rufst du Methoden der Basisklasse auf (z.B. super().__init__()).
    Mit Überschreiben (Override) definierst du Methoden neu in der Unterklasse.
    Vererbung ermöglicht Code-Wiederverwendung und klare Hierarchien.
