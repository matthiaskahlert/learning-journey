# Meine Markdown Notes – Woche 3



## 📅 Tagesnotizen
## 🗓️ Tag 11 – Module in Python
### Kurze Zusammenfassung:

Module sind spezifische Sammlungen von temenfokussierten funktionen, beispielsweise die Module Math mit mathematischen Funktionen, random mit Zufallsfunktionen oder das Modul time mit Funktionen zu Datum und Zeit.
Module werden importiert, wntweder als ganzes z.B. import Math oder nur bestimmte modulfunktionen. bei beiden Vartianten wird das Schlüsselwort import genutzt.
man kann module
### 6.1 Warum Module?

Module
Module ermöglichen das Nutzen von erweiterten Funktionalitäten. Zum Beispiel:
- Grafiktools (siehe Modul turtle)
- Mathematischen Funktionen / Konstanten (siehe Modul math)
•odule ermöglichen zudem die einfache Wiederverwendung von eigenen Funktionalitäten.

Einbindung einzelner Objekte. In einer Anweisung können auch mehrere Namen importiert werden
Beispiel: 
```py
from math import pi, sin
print sin(pi/2)
```

Einbindung aller Objekte aus einem Modul
Beispiel: 
```py
from math import *
print sin(pi/2)
```
Einbindung eines kompletten Moduls mit Prefix
Beispiel: 
```py
import math
print math.sin(math.pi/2)
```

Einbindung eines kompletten Moduls unter anderem Prefix-Namen
Beispiel: 
```py
import math as M
print M.sin(M.pi/2)
```
Man kann auch dioe help Funktion nutzen:
```py
import math
help(math)
```

### 6.2 Das math Modul
| Funktion / Konstante | Erklärung |
|---------------------|-----------|
| `cos(x)`            | Kosinus von x |
| `degrees(x)`        | Liefert zum Bogenmaß x den Winkel in Grad |
| `e`                 | Eulersche Zahl e ≈ 2,71 |
| `log(x)`            | Natürlicher Logarithmus von x (Basis e) |
| `log10(x)`          | Dekadischer Logarithmus von x (Basis 10) |
| `pi`                | Kreiszahl π ≈ 3,14 |
| `radians(a)`        | Bogenmaß des Winkels a |
| `sin(x)`            | Sinus von x |
| `sqrt(x)`           | Quadratwurzel von x (engl. *square root*) |
| `tan(x)`            | Tangens von x |


Bei trigonometrischen Funktionen wie Sinus, Kosinus und Tangens wird kein Winkel in Grad übergeben, sondern ein Wert im Bogenmaß. Dieses liegt im Bereich von 0 bis 2π, also ungefähr zwischen 0 und 6,28.

Beispiel:
```py
from math import *
sin(pi/2) # 1.0
```

### Importmöglichkeiten

#### 1. Standardimport (Dot-Notation)
```python
import math

y = math.sin(math.radians(45))
```

    Vorteil: Übersichtlich, klar, dass Funktion aus math stammt

    Empfohlen für größere Projekte

2. Gezielt importieren
```py
from math import sin, radians

y = sin(radians(45))
```
    Vorteil: Kürzer, keine math.-Prefix

    Nachteil: Weniger klar, woher Funktion stammt

3. Alles importieren (nicht empfohlen)
```py
from math import *

y = sin(radians(45))
```
    Funktioniert, kann aber zu Namenskonflikten führen

Merksatz

    Eigenen Dateien niemals wie Standardmodule nennen (z. B. math.py) – sonst werden Funktionen nicht korrekt gefunden.

Namensraum import math
┌─────────────┐
│ math        │ ──> [sin, cos, tan, pi, e, ...] (alles im math-Modul)
└─────────────┘

    Du hast nur math im aktuellen Namensraum

    Alle Funktionen/Konstanten von math musst du mit **math.** aufrufen


Namensraum from math import sin, pi
┌─────────────┐
│ sin         │ ──> math.sin
│ pi          │ ──> math.pi
└─────────────┘

    sin und pi sind direkt im Namensraum

    Kein Präfix nötig

    Aber du siehst nicht sofort, dass sie aus math stammen

### 6.3 Das random Modul

| Funktion       | Erklärung                                                                                  |
|----------------|--------------------------------------------------------------------------------------------|
| `choice(seq)`  | Liefert ein zufälliges Element aus der Sequenz `seq`.                                       |
| `randint(a, b)`| Liefert eine ganze Zufallszahl zwischen `a` und `b`.                                       |
| `random()`     | Liefert eine Zufallszahl zwischen 0 und 1 als Dezimalbruch (Kommazahl).                   |
| `shuffle(x)`   | Die Liste `x` wird „gemischt“ – die Elemente werden in eine zufällige Reihenfolge gebracht. |

man kann mit random beispielsweise einen Würfel würfeln lassen:
```py
from random import randint # vom Modul random wird die Funktion randint() importiert
for i in range(5):
    zufallszahl = randint(1, 6)
    print(zufallszahl, end ='')
```

Aus einer Liste von Namen wird ein Name nach dem Zufallsprinzip ausgewählt und auf dem Bildschirm ausgegeben.

```py
from random import choice
personen = ['Alex', 'Tina', 'Annelie', 'Tom']
person = choice(personen)
print(person, 'wurde zufallig gewählt.')
```

### 6.4 Das time Modul

Das Modul time enthält Funktionen, die mit Datum und Uhrzeit zu tun haben.

| Funktion      | Erklärung |
|---------------|-----------|
| `asctime()`   | Liefert einen String, der die augenblickliche Ortszeit beschreibt, z.B. `'Sun Apr 19 12:19:57 2020'`. |
| `localtime()` | Liefert ein „Zeit-Objekt“, das aus mehreren Teilen besteht und die aktuelle Ortszeit mit Zahlen beschreibt, z.B. `(tm_year=2020, tm_mon=11, tm_mday=17, tm_hour=18, tm_min=31, tm_sec=41, tm_wday=1, tm_yday=322, tm_isdst=0)`. |
| `sleep(t)`    | Der Lauf des Programms hält für `t` Sekunden an. |
| `time()`      | Liefert die sogenannte Unix-Zeit. Das ist die Anzahl der Sekunden seit dem 1.1.1970 als Gleitpunktzahl (z.B. `1587909684.232469`). Vor allem nützlich, um Zeitunterschiede zu messen. |

### localtime()

Die Funktion localtime() liefert ein Objekt, das den aktuellen Zeitpunkt über neun Attribute beschreibt. Diese Attribute enthalten numerische Werte für Jahr, Monat, Tag, Stunde, Minute, Sekunde usw.

Tabelle für die localtime()-Attribute und ihre Bedeutungen/Werte:
| Attribut   | Bedeutung                    | Werte                       |
|------------|-----------------------------|----------------------------|
| `tm_year`  | Jahr                         | z.B. 2021                  |
| `tm_mon`   | Monat                        | 1 … 12                     |
| `tm_mday`  | Tag im Monat                 | 1 … 31                     |
| `tm_hour`  | Stunde                       | 0 … 23                     |
| `tm_min`   | Minute                       | 0 … 59                     |
| `tm_sec`   | Sekunde                      | 0 … 59                     |
| `tm_wday`  | Wochentag (0 = Montag)       | 0 … 6                      |
| `tm_yday`  | Tag im Jahr                  | 1 … 366                    |
| `tm_isdst` | Sommerzeit (daylight saving) | 0 (nein) / 1 (ja)          |

Obige Attribute werden mit objekt.attribut angewendet:
```py
from time import *
zeitpunkt = localtime()
print(zeitpunkt.tm_year) # 2025
print(zeitpunkt.tm_mon) # 12
```
Dieses Programm zählt printet die uhrzeit alle zehn Sekunden bis die abbruchbedingung erfüllt ist: 
```py
from time import localtime, sleep
durchlauf = 0
max_durchlaeufe = 5

while True:
    zeit = localtime()
    print(zeit.tm_hour, 'Uhr', zeit.tm_min, 'und',zeit.tm_sec, 'Sekunden')
    
    durchlauf += 1
    if durchlauf >= max_durchlaeufe:
        print("Maximale Durchläufe erreicht, Schleife beendet.")
        break

    sleep(10)
```
sleep() nimmt immer Sekunden als Argument. Bruchteile von Sekunden sind erlaubt, also z. B. sleep(0.25) = 250 Millisekunden

| Zeitangabe      | Argument für sleep()      | Bemerkung                               |
|-----------------|--------------------------|----------------------------------------|
| 1 Sekunde       | 1                        | Standardangabe in Sekunden             |
| 0,5 Sekunden    | 0.5                      | 500 Millisekunden                       |
| 1 Minute        | 60                       | 60 Sekunden                             |
| 5 Minuten       | 300                      | 5 × 60 Sekunden                         |
| 1 Stunde        | 3600                     | 60 × 60 Sekunden                        |
| 0,1 Sekunde     | 0.1                      | 100 Millisekunden                        |


### Modulimport


Jede Python-Datei ist ein Modul und kann importiert werden (import modulname)

Vorteil: Funktionen lassen sich wiederverwenden (z. B. Volumenberechnung geometrischer Körper)

Beispiel volumen.py:
```py

from math import pi

def kuppel(hoehe, radius):
    """Volumen einer halben Rotationsellipsoiden-Kuppel"""
    return 2/3 * pi * radius**2 * hoehe

def quader(laenge, breite, hoehe):
    """Volumen eines Quaders"""
    return laenge * breite * hoehe

if __name__ == "__main__":
    print(kuppel(1,1))
    print(quader(2,3,2))
```

Code in if __name__ == "__main__": wird nur ausgeführt, wenn das Skript direkt gestartet wird, nicht beim Import.

Interaktives Programm, das das Modul nutzt:
```py
from volumen import *

# Abfrage
eingabe = input('(Q)uader, (K)uppel, (E)nde: ')
```

Voraussetzungen: Moduldatei und Hauptprogramm im gleichen Verzeichnis

Python erzeugt beim Import automatisch einen Ordner __pycache__ 
mit __pycache__ enthält von Python erzeugten Bytecode (.pyc) zur Beschleunigung von Imports.
Der Ordner ist automatisch, harmlos und kann ignoriert werden sollte man aber in git.ignore erwähnen:

```gitignore
__pycache__/
*.pyc
```

### 6.6 Module aus dem Python Package Index (PyPI)

PyPI ist ein frei zugängliches Online-repo mit Third-Party-Modulen zu verschiedenen Themen.

Installation eines Moduls modul aus PyPI erfolgt über die Konsole:
```shell
pip install modul
```