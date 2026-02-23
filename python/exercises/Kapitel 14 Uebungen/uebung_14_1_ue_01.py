""" 
Entwickle eine Python-Klasse Auto, die verschiedene Attribute wie marke, modell, baujahr und kilometerstand hat.
Die Klasse sollte folgende Methoden beinhalten: 

a) Eine Initialisierungsmethode, die es ermöglicht, bei der Erstellung eines Auto-Objekts 
die Marke, 
das Modell 
und das Baujahr anzugeben, 
während der Kilometerstand standardmäßig auf 0 gesetzt wird. 

b) Eine Methode fahren, die den Kilometerstand um die gefahrenen Kilometer erhöht, 
die als Parameter übergeben werden. 

c) Eine Methode anzeigen, die die Details des Autos (Marke, Modell, Baujahr, Kilometerstand) 
in einer lesbaren Form ausgibt.

Stelle sicher, dass du die Konzepte der objektorientierten Programmierung korrekt anwendest, 
insbesondere die Definition von Klassen, die Initialisierung von Objekten und das Aufrufen von Methoden. 
Teste deine Klasse, indem du mindestens zwei Auto-Objekte erstellst, 
mit der Methode fahren den Kilometerstand änderst 
und schließlich die Details jedes Autos mit der Methode anzeigen ausgibst. 
 """

# Klasse definieren

class Auto:
    """Die Auto Klasse"""
    # Initialisieren und startwerte festlegen
    def __init__(self, marke, modell, baujahr):
        """Initialisierungsmethode, die es ermöglicht, 
        bei der Erstellung eines Auto-Objekts 
        die Marke, 
        das Modell und 
        das Baujahr anzugeben, während der Kilometerstand standardmäßig auf 0 gesetzt wird."""
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = 0

    # Methoden - steuern das Verhalten der Klasse
    def fahren(self, kilometer):
        """Erhöht den Kilometerstand um die gefahrenen Kilometer."""
        self.kilometerstand += kilometer

    def anzeigen(self):
        """Gibt die Details des Autos in einer lesbaren Form aus."""
        print(f"Marke: {self.marke}")
        print(f"Modell: {self.modell}")
        print(f"Baujahr: {self.baujahr}")
        print(f"Kilometerstand: {self.kilometerstand}")


# Verwendung der Klasse
if __name__ == "__main__":
    # Erstellen von Auto-Objekten
    auto1 = Auto("Opel", "Astra", 2010)
    auto2 = Auto("Volkswagen", "Golf", 2015)

    # Ändern des Kilometerstands mit der Methode fahren
    auto1.fahren(15000)
    auto2.fahren(20000)

    # Anzeigen der Details jedes Autos mit der Methode anzeigen
    print("Details von Auto 1:")
    auto1.anzeigen()
    print("\nDetails von Auto 2:")
    auto2.anzeigen()
    