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

def suche_weg(aktuell, ziel, besucht):
    """
    Die Funktion versucht, einen Weg von aktuell nach ziel zu finden.
    Es findet allerdings nicht immer den kürzesten Weg, die Funktion nutzt Tiefensuche (DFS)
    
    :param aktuell: aktueller Knoten
    :param ziel: gesuchter Knoten
    :param besucht: Liste der bereits besuchten Knoten (gegen Endlosschleifen)
    :return: eine Liste der Knoten (der Weg), oder None, wenn kein Weg gefunden wurde
    """
    besucht = besucht + [aktuell]
    if aktuell == ziel:
        return besucht # Abbruch der Rekursion wenn ziel gefunden
    else:
        for nachbar in G[aktuell]: # alle Nachbarn des aktuellen Knotens anschauen
            if not nachbar in besucht: # besuchte knoten überspringen
                weg = suche_weg(nachbar, ziel, besucht) # Versuche, von diesem Nachbarn aus einen Weg zum Ziel zu finden.
                if weg is not None: # Wenn ein Weg gefunden wurde brich alles ab und...
                    return weg # ...gib den weg nach oben weiter
        return None # Abbruch der Rekursion wenn kein ziel gefunden

while True:
    start = int(input('Startknotenpunkt: '))
    ziel = int(input('Zielknotenpunkt: '))
    weg = suche_weg(start, ziel, [])
    print('Gefundener Weg:', weg)
