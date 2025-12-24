from math import pi

def kuppel (hoehe:float, radius: float)-> float:
    """Volumen einer halben Rotationsellipsoiden-Kuppel"""
    return 2/3 * pi * radius ** 2 * hoehe

def quader(laenge:float, breite:float, hoehe: float)-> float:
    """Volumen eines Quaders"""
    return laenge * breite * hoehe

def main():
    print ('Kuppel mit Radius 1 und Höhe 1 ', kuppel(1, 1))
    print('Quader mit den Seitenlangen 2, 3, 2: ', quader(2, 3, 2))


# folgecode wird nur ausgeführt, wenn die Datei direkt gestartet wird, nicht, wenn sie importiert wird.
if __name__== '__main__': 
    main()
