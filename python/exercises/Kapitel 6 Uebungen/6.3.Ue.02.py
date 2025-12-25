""" 
a) Importiere das Modul random und verwende eine Funktion aus diesem Modul, um eine Zufallszahl zwischen 1 und 10 zu generieren. 
Speichere diese Zahl in einer Variablen.

b) Definiere eine Funktion namens berechne_quadrat, die einen Parameter nimmt, dessen Quadrat berechnet und das Ergebnis zurückgibt.

c) Verwende eine if-Kontrollstruktur, um zu überprüfen, ob die generierte Zufallszahl größer als 5 ist. 
Falls ja, rufe die Funktion berechne_quadrat mit der Zufallszahl als Argument auf und gib das Ergebnis aus. 
Falls nein, gib eine Nachricht aus, die besagt, dass die Zahl kleiner oder gleich 5 ist.

d) Implementiere eine Schleife, die von 1 bis zur generierten Zufallszahl läuft und dabei jedes Mal die aktuelle Zahl ausgibt.  """

import random
from math import sqrt
# a) 
zufallszahl = random.randint(1, 10) # Return random integer in range [a, b], including both end points.

# b)
def berechne_quadrat(x):
    ergebnis1 = sqrt(x)
    return ergebnis1

# c)
if zufallszahl >5:
    ergebnis2 = berechne_quadrat(zufallszahl)
    print(f"{zufallszahl} ist größer als 5. ")
    print(f"Die Quafratwurzel von {zufallszahl} ist {ergebnis2:.2f}")
else:
    print(f"{zufallszahl} ist kleiner als 5. ")

# d)
for i in range(1, zufallszahl + 1): # start ist inklusive stopwert ist eklusive, daher + 1
    print(i)