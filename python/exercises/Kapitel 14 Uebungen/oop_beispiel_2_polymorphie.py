"""
Einfaches Beispiel: Polymorphie
Thema: Spezielle Methoden mit doppelten Unterstrichen (__str__, __add__, etc.)
"""

class Geldbetrag:
    """Klasse für Geldbeträge mit polymorphen Methoden"""
    
    def __init__(self, euro):
        self.euro = euro
    
    # __str__() - definiert wie das Objekt als String dargestellt wird
    def __str__(self):
        return f"{self.euro}€"
    
    # __add__() - definiert wie zwei Objekte addiert werden
    def __add__(self, other):
        return Geldbetrag(self.euro + other.euro)
    
    # __sub__() - definiert wie zwei Objekte subtrahiert werden
    def __sub__(self, other):
        return Geldbetrag(self.euro - other.euro)
    
    # __eq__() - definiert wie zwei Objekte verglichen werden
    def __eq__(self, other):
        return self.euro == other.euro
    
    # __lt__() - definiert "kleiner als" Vergleich
    def __lt__(self, other):
        return self.euro < other.euro


class Punkt:
    """Klasse für 2D-Punkte"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # __str__() - lesbare Darstellung
    def __str__(self):
        return f"Punkt({self.x}, {self.y})"
    
    # __repr__() - technische Darstellung
    def __repr__(self):
        return f"Punkt(x={self.x}, y={self.y})"
    
    # __add__() - Vektoraddition
    def __add__(self, other):
        return Punkt(self.x + other.x, self.y + other.y)


# Verwendung
if __name__ == "__main__":
    print("=== Polymorphie Demo - Geldbetrag ===\n")
    
    # Objekte erstellen
    betrag1 = Geldbetrag(50)
    betrag2 = Geldbetrag(30)
    
    # __str__() wird automatisch beim print() aufgerufen
    print(f"Betrag 1: {betrag1}")
    print(f"Betrag 2: {betrag2}")
    
    # __add__() wird beim + Operator aufgerufen
    summe = betrag1 + betrag2
    print(f"Summe: {summe}")
    
    # __sub__() wird beim - Operator aufgerufen
    differenz = betrag1 - betrag2
    print(f"Differenz: {differenz}")
    
    # __eq__() wird beim == Operator aufgerufen
    print(f"Sind gleich? {betrag1 == betrag2}")
    
    # __lt__() wird beim < Operator aufgerufen
    print(f"Ist Betrag1 kleiner? {betrag1 < betrag2}")
    
    print("\n=== Polymorphie Demo - Punkt ===\n")
    
    p1 = Punkt(3, 4)
    p2 = Punkt(1, 2)
    
    print(f"Punkt 1: {p1}")
    print(f"Punkt 2: {p2}")
    
    # Addition von Punkten
    p3 = p1 + p2
    print(f"Summe: {p3}")
    
    print("\n=== Vorteile ===")
    print("Polymorphie erlaubt es, natürliche Operatoren (+, -, ==, etc.)")
    print("für eigene Klassen zu definieren.")
