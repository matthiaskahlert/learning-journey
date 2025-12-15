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
```py
def fallhoehe(t: float, g: float = 9.81) -> float:
    return 0.5 * g * t**2
```

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
