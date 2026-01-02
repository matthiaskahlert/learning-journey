""" 
a) Importiere das Modul random und das Modul math.

b) Erstelle eine Funktion namens erzeuge_zufallszahlen_liste, die zwei Parameter akzeptiert: 
anzahl (die Anzahl der Zufallszahlen in der Liste) und 
max_wert (der maximale Wert einer Zufallszahl).
Die Funktion soll eine Liste von anzahl Zufallszahlen generieren, 
wobei jede Zufallszahl zwischen 1 und max_wert (inklusive) liegt. 
Nutze die Funktion randint aus dem Modul random zur Generierung der Zufallszahlen.

c) Erstelle eine Funktion namens berechne_durchschnitt, die eine Liste von Zahlen als Parameter akzeptiert 
und den Durchschnittswert dieser Zahlen zurückgibt.

d) Erstelle eine Funktion namens sortiere_und_teile, die eine Liste von Zahlen akzeptiert 
und die Liste in zwei Hälften teilt. Die Funktion soll zunächst die Liste aufsteigend sortieren. 
Dann soll die Funktion zwei Listen zurückgeben: die erste Hälfte und die zweite Hälfte der ursprünglichen Liste. 
Wenn die Liste eine ungerade Anzahl von Elementen hat, soll das mittlere Element zur ersten Hälfte hinzugefügt werden.

e) Verwende die Funktion erzeuge_zufallszahlen_liste, um eine Liste mit 10 Zufallszahlen zu erzeugen, 
wobei max_wert 100 ist.

f) Gib die erzeugte Liste aus.

g) Berechne und gib den Durchschnittswert der Zufallszahlenliste mit der Funktion berechne_durchschnitt aus.

h) Verwende die Funktion sortiere_und_teile, um die Zufallszahlenliste zu sortieren und in zwei Hälften zu teilen. 
Gib beide Hälften aus. 
 """
# a)
import random, math


# b)
def erzeuge_zufallszahlen_liste(anzahl, max_wert):
    """ Die Funktion soll eine Liste von anzahl Zufallszahlen generieren, 
    wobei jede Zufallszahl zwischen 1 und max_wert (inklusive) liegt"""
    return [random.randint(1, max_wert) for _ in range(anzahl)] #using _ instead to indicate that the variable is intentionally unused for better readability.
# e)
zahlen = erzeuge_zufallszahlen_liste(10, 100)
# f)
print(zahlen)

# c)
def berechne_durchschnitt(zahlen):
    """Die Funktion soll den Durchschnittswert dieser Zahlen zurückgeben."""
    return sum(zahlen) / len(zahlen) # die summe durch die anzahl der zahlen ergibt den durchschnitt

durchschnitt = berechne_durchschnitt(zahlen)
print(durchschnitt)

# d)


def sortiere_und_teile(zahlen):
    """Die Funktion soll zunächst die Liste aufsteigend sortieren. 
    Dann soll die Funktion zwei Listen zurückgeben: die erste Hälfte und die zweite Hälfte der ursprünglichen Liste. 
    Wenn die Liste eine ungerade Anzahl von Elementen hat, soll das mittlere Element zur ersten Hälfte hinzugefügt werden."""
    sortierte_zahlen = sorted(zahlen) # sortiert die liste aufsteigend
    # mitte ist die Anzahl der Elemente, die in die erste Hälfte sollen.
    # bei ungeraden zahlen wird mit math.ceil aufgerundet
    # dadurch ist in der variable mitte der Index direkt NACH dem mittleren Element
    mitte = math.ceil(len(sortierte_zahlen) / 2) 
    erste_haelfte = sortierte_zahlen[:mitte]
    zweite_haelfte = sortierte_zahlen[mitte:]
    return erste_haelfte, zweite_haelfte
erste_haelfte, zweite_haelfte = sortiere_und_teile(zahlen)
# h)
print(f"Erste Hälfte: {erste_haelfte} \
      Zweite Hälfte: {zweite_haelfte}")

# g)
durchschnitt_erste_haelfte = berechne_durchschnitt(erste_haelfte)
print(durchschnitt_erste_haelfte)

durchschnitt_zweite_haelfte = berechne_durchschnitt(zweite_haelfte)
print(durchschnitt_zweite_haelfte)


