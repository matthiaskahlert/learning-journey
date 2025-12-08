""" 
a) Definiere eine Variable für jeden der vier Standard-Datentypen: int, float, complex und str. 
Für den Datentyp int wähle eine Dezimalzahl, 
für float eine Zahl mit Nachkommastellen, 
für complex eine komplexe Zahl und 
für str eine Zeichenkette deiner Wahl.

b) Verwende die Funktion type() für jede dieser Variablen, um den Datentyp zu überprüfen. 
Gib das Ergebnis mit einer print()-Anweisung aus, die auch den Namen der Variable enthält, 
damit klar ist, zu welcher Variable der Datentyp gehört.

c) Berechne die Summe der int- und float-Variablen und speichere das Ergebnis in einer neuen Variable. 
Überprüfe den Datentyp des Ergebnisses mit der Funktion type() und gib das Ergebnis aus.

d) Füge der Zeichenkette (str) die Zeichenfolge " - Python Basics" hinzu 
und speichere das Ergebnis in einer neuen Variable. 
Verwende die print()-Funktion, um das Ergebnis auszugeben.  """

a = 2
b = 2.567
c = 12 + 3j
d = "yay python"

print("a:", type(a))
print("b:", type(b))
print("c:", type(c))
print("d:", type(d))
ergebnis = a + b
print("ergebnis:", ergebnis, "Typ von ergebnis:", type(ergebnis))
e = " - Python Basics"
f = d + e
print(f)
