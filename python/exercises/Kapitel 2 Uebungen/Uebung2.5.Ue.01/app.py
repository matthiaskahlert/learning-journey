""" Erstelle ein Python-Skript, das folgende Aufgaben ausführt:

a) Definiere Variablen für jeden der folgenden Datentypen: int, float, complex, str, tuple, list und set. 
Verwende für die Definition dieser Variablen Werte deiner Wahl, aber achte darauf, 
dass die Werte repräsentativ für den jeweiligen Datentyp sind.

b) Für jede der definierten Variablen, verwende die Funktion type() und drucke den Datentyp der Variable in der Konsole aus.

c) Konvertiere die int Variable in einen float und einen str Datentyp und drucke das Ergebnis aus.

d) Erstelle eine neue Liste, die aus den ersten zwei Elementen der ursprünglichen Liste 
und dem letzten Element der Tupel-Variable besteht. 
Prüfe, ob das letzte Element des Tupels bereits in der neuen Liste vorhanden ist, 
bevor du es hinzufügst. Drucke die neue Liste aus.

e) Verwende die set Variable, um ein Element hinzuzufügen, das bereits existiert, 
und ein neues Element, das noch nicht in der Menge vorhanden ist. 
Drucke die veränderte Menge aus.   """

# Python Grundtypen kompakt

# Integer (ganze Zahl)
i1 = 42          # Dezimal

# Float (Gleitkommazahl)
f1 = 3.14

# Complex (komplexe Zahl)
c1 = 2 + 3j

# String (Zeichenkette)
s1 = "Python"

# Tuple (unveränderbar)
t1 = (1, 'a', 3.14)

# List (veränderbar)
l1 = [1, 2, 3]

# Set (ungeordnet, keine Duplikate)
st1 = {1, 2, 3}

# Ausgabe aller Typen
print("int:", i1, "Datentyp", type(i1))
print("float:", f1, "Datentyp", type(f1))
print("complex:", c1, "Datentyp", type(c1))
print("str:", s1, "Datentyp", type(s1))
print("tuple:", t1, "Datentyp", type(t1))
print("list:", l1, "Datentyp", type(l1))
print("set:", st1, "Datentyp", type(st1))

# c) Konvertiere die int Variable in einen float und einen str Datentyp und drucke das Ergebnis aus.
i_float = float(i1)
i_string = str(i_float)
print("Konvertierter float:", i_float, "Datentyp", type(i_float))
print("Konvertierter str:", i_string, "Datentyp", type(i_string))

# l1_neu = [l1[0], l1[1]] ginge auch aber besser mit slicing
l1_neu = l1[:2]  # Erste zwei Elemente der Liste denn liste[start:stop:step]
print("Neue Liste vor dem Hinzufuegen des Tupel-Elements:", l1_neu)
t1_letztes_element = t1[-1]
if t1_letztes_element not in l1_neu:
    # Der +-Operator funktioniert nur zwischen Liste + Liste
    l2 = l1_neu + [t1_letztes_element]
else:
    # falls Element bereits existiert: einfach die ursprüngliche Liste übernehmen
    l2 = l1_neu

print("Neue Liste nach dem Hinzufuegen des Tupel-Elements:", l2)


# e) Verwende die set Variable, um ein Element hinzuzufügen, das bereits existiert,

st1.add(2)   # existiert bereits → wird nicht erneut eingefügt
st1.add(4)   # neues Element → wird hinzugefügt

print(st1)
