"""
Schreibe ein Programm, das die Ziehung der Lottozahlen simuliert (6 aus 49).
Verwende die Funktion choice() aus dem Modul random. Der Aufruf choice(s)
liefert ein zufälliges Element aus der Sequenz s.
"""
from random import choice
def ziehung():
    """Die Funktion simuliert die Ziehung der Lottozahlen (6 aus 49).
    
    :return: eine Liste mit 6 verschiedenen gezogenen Lottozahlen
    """
    s = list(range(1, 50))  # Erstelle eine Liste der Zahlen von 1 bis 49
    gezogen = []  # Liste für die gezogenen Zahlen
    while len(gezogen) < 6:
        zahl = choice(s)  # Ziehe eine zufällige Zahl
        if zahl not in gezogen:  # Stelle sicher, dass die Zahl noch nicht gezogen wurde
            gezogen.append(zahl)  # Füge die Zahl zur Liste der gezogenen Zahlen hinzu
    return gezogen

print(ziehung())
