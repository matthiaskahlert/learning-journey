# -*- coding: utf-8 -*-
""" 
a) Gebe an, wie du das Modul math in Python importierst und verwende eine Funktion aus diesem Modul, 
um die Quadratwurzel von 256 zu berechnen.

b) Erstelle eine Variable radius mit dem Wert 7. 
Berechne den Umfang eines Kreises unter Verwendung der Variable radius und der Konstante pi aus dem Modul math. 
Schreibe das Ergebnis in eine neue Variable umfang und gib sie aus.

c) Beschreibe, wie du eine eigene Funktion namens fahrenheit_zu_celsius definierst, 
die eine Temperatur in Fahrenheit entgegennimmt und die entsprechende Temperatur in Celsius zurückgibt. 
Verwende diese Funktion anschließend, um die Temperatur 68°F in Celsius umzurechnen und das Ergebnis auszugeben.

d) Erkläre, wie eine einfache for-Schleife in Python aussieht, die die Zahlen von 1 bis einschließlich 5 ausgibt. 
Verwende dazu eine Schleife und die print-Funktion.

e) Benenne die zwei grundlegenden Arten, wie Funktionen aus Modulen in Python importiert werden können, 
und gib für jede Art ein Beispiel an. """

# a) Der Modulimport in python hat folgende optionen

# Standardimport braucht Dot-Notation:
import math
y = math.sin(math.radians(45))

# gezielter Import
from math import sin, radians
y = sin(radians(45))

# Alle Elemente importieren (nicht empfohlen kann zu Namenskonflikten führen)
from math import *
# quadratwurzel von 256
x=sqrt(256)
print(f"Das Ergebnis der Quadratwurzel von 256 lautet: {x}")

# b) Kreisumfang berechnen (U = 2 ⋅ π ⋅ r)
radius = 7
umfang = 2 * pi * radius
print(f"Kreisumfang mit Radius von: {radius} ist {umfang:.2f}")

# c) die Funktiuon zur Temparaturumrechnung braucht ein Argument: die temparatur in Fahrenheit
# Die Funktion hat als Rückgabewert die umgerechnete Temparatur
def fahrenheit_zu_celsius(fahrenheit):
    """Wandelt Fahrenheit in Celsius um"""
    return (fahrenheit - 32) * 5 / 9

temperatur_f = 68
temperatur_c = fahrenheit_zu_celsius(temperatur_f)

print(f"{temperatur_f} °F entsprechen {temperatur_c:.2f} °C")


# 68 °F entsprechen 20.00 °C

# d) 
x =  [1,2,3,4,5]
for i in x:
    print(i)
# die for schleife iteriert durch x und gibt mit jedem durchlauf den wert an der stelle des entsprechenden index aus.

# e)
# e) Zwei grundlegende Importarten in Python:

# 1. Import eines kompletten Moduls (Dot-Notation)
import math
print(math.sqrt(16))

# 2. Gezielter Import einzelner Funktionen/Konstanten
from math import sqrt
print(sqrt(16))
