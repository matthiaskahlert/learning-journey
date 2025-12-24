""" a) Importiere das Modul random und das Modul math.

b) Definiere eine Variable zahl, die eine zufällige Ganzzahl zwischen 1 und 100 speichert.

c) Schreibe eine Funktion quadratwurzel, die die Quadratwurzel einer Zahl berechnet und zurückgibt. Verwende dafür eine Funktion aus dem Modul math.

d) Verwende eine if-else-Kontrollstruktur, um zu überprüfen, ob Variable zahl größer als 50 ist. 
Wenn ja, rufe die Funktion quadratwurzel mit zahl als Argument auf und drucke das Ergebnis aus. 
Andernfalls drucke "Zahl ist 50 oder kleiner".

e) Erstelle eine for-Schleife, die Zahlen von 1 bis 5 durchläuft, 
und für jede Zahl die Funktion quadratwurzel aufruft und das Ergebnis ausdruckt.  """

# a)
from math import sqrt
import random

# b)
# randint(a, b)`| Liefert eine ganze Zufallszahl zwischen `a` und `b`.
zahl = random.randint(1, 100)
print(zahl) # test

# c)
def quadratwurzel(x):
    """
    Docstring for quadratwurzel
    
    :param x: Description
    """
    return sqrt(x)

# d)
if zahl > 50:
    print(f"Quadratwurzel von {zahl} ist {quadratwurzel(zahl)}")
else:
    print("Zahl ist 50 oder kleiner")

# e)
x =  [1,2,3,4,5]
for i in x:     # es ginge auch ohne x und mit "for i in range(1, 6):"
    print(quadratwurzel(i))
