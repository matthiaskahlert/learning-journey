""" 
a) Importiere das Modul random und das Modul time.

b) Definiere eine Funktion wuerfeln(), die eine zufällige Zahl zwischen 1 und 6 generiert 
und diese zurückgibt. Verwende dafür die Funktion randint() aus dem Modul random.

c) Definiere eine Funktion aktueller_timestamp(), die den aktuellen Unix-Timestamp zurückgibt. 
Verwende dafür die Funktion time() aus dem Modul time.

d) Schreibe eine Hauptschleife, die fünfmal läuft. 
In jedem Durchlauf soll die Funktion wuerfeln() aufgerufen 
und das Ergebnis zusammen mit dem aktuellen Unix-Timestamp ausgegeben werden. 
Nutze dafür die Funktion aktueller_timestamp().

e) Sorge dafür, dass zwischen jedem Würfelwurf eine Pause von 2 Sekunden liegt. 
Verwende dafür die Funktion sleep() aus dem Modul time.  
"""
# a)
from random import randint, random
from time import time, sleep

# b)
def wuerfeln():
    """Generiert eine zufällige Zahl zwischen 1 und 6. """
    for i in range(5):
         zufallszahl = randint(1, 6)
         return zufallszahl
# testaufruf
print(wuerfeln())
# c)
def aktueller_timestamp():
    """ Gibt den aktuellen Unix-Timestanp zurück"""
    zeitpunkt = time()
    return zeitpunkt
# testaufruf
print(aktueller_timestamp())

# d)
durchlauf = 0
max_durchlaeufe = 5

while True:
    wurf = wuerfeln()
    timestamp = aktueller_timestamp()
    print(f"Wurf: {wurf}, Timestamp: {timestamp}")

    # e)
    sleep(2)

    
    durchlauf += 1
    if durchlauf >= max_durchlaeufe:
        print("Maximale Durchläufe erreicht, Schleife beendet.")
        break

