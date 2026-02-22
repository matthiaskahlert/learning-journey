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