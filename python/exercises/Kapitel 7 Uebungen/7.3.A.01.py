"""
Entwickle ein Python-Programm, das folgende Funktionalitäten umfasst:

a) Importiere das Modul random und das Modul math. 
Verwende aus dem Modul random die Funktion randint und aus math die Funktion sqrt.

b) Erstelle eine Funktion erzeuge_zufallszahlen_liste(n), 
die eine Liste mit n zufälligen ganzen Zahlen zwischen 1 und 100 zurückgibt.

c) Erstelle eine Funktion berechne_wurzeln(liste), 
die für jede Zahl in der übergebenen Liste die Quadratwurzel berechnet 
und die Wurzeln in einer neuen Liste speichert. Gib diese Liste zurück.

d) Erstelle eine Funktion sortiere_und_erzeuge_tupel(liste), 
die die Liste von Quadratwurzeln aufsteigend sortiert und ein Tupel aus (Originalzahl, Quadratwurzel) 
für jede Zahl in der ursprünglichen Liste erzeugt. 
Speichere diese Tupel in einer Liste und gib sie zurück.

e) Erstelle eine Funktion erstelle_dictionary(tupel_liste), die ein Dictionary erstellt, 
wobei der Schlüssel die Originalzahl und der Wert die Quadratwurzel ist. 
Gib dieses Dictionary zurück.

f) Verwende alle oben erstellten Funktionen in einer Hauptfunktion main(), 
um eine Liste mit 10 zufälligen Zahlen zu erzeugen, die Quadratwurzeln zu berechnen, 
die Liste zu sortieren, das Tupel zu erstellen und schließlich das Dictionary zu erstellen und auszugeben.

g) Gib am Ende des Programms das erstellte Dictionary aus. 
"""


# a) Imports
from random import randint
from math import sqrt


# b) Zufallszahlen erzeugen
def erzeuge_zufallszahlen_liste(n):
    """
    Erzeugt eine Liste mit n zufälligen ganzen Zahlen zwischen 1 und 100.
    """
    return [randint(1, 100) for _ in range(n)]


# c) Quadratwurzeln berechnen
def berechne_wurzeln(liste):
    """
    Berechnet für jede Zahl in der Liste die Quadratwurzel und gibt eine neue Liste zurück.
    """
    return [sqrt(zahl) for zahl in liste]


# d) Sortieren und Tupel erzeugen
def sortiere_und_erzeuge_tupel(zahlen):
    """
    Sortiert die Zahlen aufsteigend und erzeugt eine Liste von Tupeln der Form (Originalzahl, Quadratwurzel).
    """
    sortierte_zahlen = sorted(zahlen)
    return [(zahl, sqrt(zahl)) for zahl in sortierte_zahlen]


# e) Dictionary erstellen
def erstelle_dictionary(tupel_liste):
    """
    Erstellt ein Dictionary mit der Originalzahl als Schlüssel und der Quadratwurzel als Wert.
    """
    return {zahl: wurzel for zahl, wurzel in tupel_liste}


# f) Hauptfunktion
def main():
    zahlen = erzeuge_zufallszahlen_liste(10)
    print("Zufällige Zahlen:", zahlen)

    wurzeln = berechne_wurzeln(zahlen)
    print("Quadratwurzeln:", wurzeln)

    tupel_liste = sortiere_und_erzeuge_tupel(zahlen)
    print("Tupel (Zahl, Wurzel):", tupel_liste)

    dictionary = erstelle_dictionary(tupel_liste)
    print("Ergebnis-Dictionary:")
    print(dictionary)


# g) Programm start von main inkls. ausgabe des dictionary
if __name__ == "__main__":
    main()




