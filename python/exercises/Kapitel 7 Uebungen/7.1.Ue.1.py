# -*- coding: utf-8 -*-
""" 
a) Importiere das Modul random und verwende es, 
um eine Liste von 10 zufälligen Ganzzahlen zwischen 1 und 100 zu erzeugen.

b) Erstelle eine Funktion namens sortiere_und_zähle, die eine Liste von Zahlen als Argument nimmt. 
Die Funktion soll die Liste aufsteigend sortieren und die Anzahl der Elemente in der Liste zurückgeben.

c) Erstelle eine weitere Liste, die Tupel aus den ursprünglichen zufälligen Zahlen 
und dem Quadrat jeder Zahl enthält (z.B. [(Zahl, Quadrat der Zahl), ...]).

d) Verwende eine Schleife, um über die Liste der Tupel zu iterieren, 
und drucke für jedes Tupel eine formatierte Zeichenkette aus, 
die besagt: "Die Zahl X hat das Quadrat Y".

e) Schreibe eine Kontrollstruktur, die prüft, ob die Anzahl der Elemente in der sortierten Liste größer als 5 ist. 
Wenn ja, drucke "Mehr als 5 Elemente", ansonsten "5 oder weniger Elemente".  
"""
import random

# a)
zahlen = [random.randint(1,100) for n in range(10)] # randint gibt einen random integer in range 1, 100, 
# die funktion wird durch range(10) zehn mal durchlaufen
print("Zufällige Zahlen:", zahlen)
# b)
def sortiere_und_zähle(zahlen):
    """Sortiert die Liste und gibt die Anzahl der Elemente zurück."""
    sortierte_zahlen = sorted(zahlen)
    anzahl = len(sortierte_zahlen)
    return sortierte_zahlen, anzahl
sortierte_zahlen, anzahl = sortiere_und_zähle(zahlen)
print("Sortierte Zahlen:", sortierte_zahlen)
print("Anzahl der Elemente:", anzahl)

# c) [(Zahl, Quadrat der Zahl), ...]
quadrat_zahlen = [(zahl, zahl**2) for zahl in zahlen]
print("Zahl und Quadrat:", quadrat_zahlen)

# d) Formatierter Text
for zahl, quadrat in quadrat_zahlen:
    print(f"Die Zahl {zahl} hat das Quadrat {quadrat}")

# e) Kontrollstruktur
if anzahl > 5:
    print("Mehr als 5 Elemente")
else:
    print("5 oder weniger Elemente")