""" 
Frage 1: Vorbedingungen
Die folgende Funktion entfernt das kleinste Element aus einer Liste von Zahlen:
Formuliere zwei sonnvolle assert statements, die als Vorbedingungen für diese Funktion dienen könnten. Führe die Funktion mit einem Beispiel aus, um zu zeigen, dass sie korrekt funktioniert.
 """


def entferne_min(s):
    'Entferne das Minimum in der Liste s.'
    assert isinstance(s, list), "s muss eine Liste sein"
    assert len(s) > 0, "s darf nicht leer sein"
    m = min(s)
    s.remove (m)
    return s

# Beispiel
zahlen = [3, 1, 4, 1, 5] # jetzt eine Liste
print("Vorher:", zahlen)
entferne_min(zahlen)
print("Nachher:", zahlen)

""" 
Vorher: (3, 1, 4, 1, 5)
Traceback (most recent call last):
  File "c:\\Users\\Matze\\repositories\\learning-journey\\python\\exercises\\Kapitel 13 Uebungen\\13.py", line 19, in <module>
    entferne_min(zahlen)
  File "c:\\Users\\Matze\\repositories\\learning-journey\\python\\exercises\\Kapitel 13 Uebungen\\13.py", line 10, in entferne_min
    assert isinstance(s, list), "s muss eine Liste sein"
AssertionError: s muss eine Liste sein
"""



