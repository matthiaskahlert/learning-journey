G = {
    1: [2, 4], 
    2: [1, 3, 5], 
    3: [2, 5], 
    4: [1, 5], 
    5: [4, 2, 3, 6], 
    6: [5]
    }
"""
Das Dictionary beschreibt ein Knotenpunktsystem eines Fahrradnetzes. 
Die Schlüssel sind die Knotenpunkte, während die Werte die direkt 
verbundenen Knotenpunkte angeben.
"""

def kuerzester_weg(start, ziel):
    """
    Bestimmt den kürzesten Weg zwischen zwei Knotenpunkten in einem Graphen.

    Der Graph ist als Dictionary G gegeben, wobei jeder Schlüssel einen
    Knotenpunkt darstellt und der zugehörige Wert eine Liste der direkt
    verbundenen Nachbarknoten ist.

    Die Funktion verwendet eine Breitensuche (Breadth-First Search, BFS),
    um den kürzesten Weg (mit der geringsten Anzahl an Kanten) vom
    Startknoten zum Zielknoten zu finden.

    :param start: Startknotenpunkt (Ganzzahl)
    :param ziel: Zielknotenpunkt (Ganzzahl)
    :return: Eine Liste der Knotenpunkte, die den kürzesten Weg vom Start 
    zum Ziel beschreibt, oder None, falls kein Weg existiert
    """
    warteschlange = [[start]]   # Liste von Wegen
    besucht = []

    while warteschlange:
        weg = warteschlange.pop(0)   # erstes Element holen (FIFO)
        aktuell = weg[-1]

        if aktuell == ziel:
            return weg

        if aktuell not in besucht:
            besucht.append(aktuell)

            for nachbar in G[aktuell]:
                neuer_weg = weg + [nachbar]
                warteschlange.append(neuer_weg)

    return None

while True:
    start = int(input("Startknotenpunkt: "))
    ziel = int(input("Zielknotenpunkt: "))
    weg = kuerzester_weg(start, ziel)
    print("Kürzester Weg:", weg)

