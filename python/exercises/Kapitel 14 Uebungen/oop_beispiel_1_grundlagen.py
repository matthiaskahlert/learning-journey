"""
Einfaches Beispiel: Klassen-Grundlagen
Thema: Attribute, Methoden, __init__, self, Instanziierung
"""

# Klasse definieren
class Flasche:
    """Eine einfache Flaschen-Klasse"""
    
    # Initialisierungsmethode - setzt Startwerte für Attribute
    def __init__(self, max_inhalt):
        self.inhalt = 0              # Attribute: aktueller Inhalt
        self.max_inhalt = max_inhalt # Attribute: maximaler Inhalt
        self.geoeffnet = False       # Attribute: Zustand (offen/geschlossen)
    
    # Methoden - steuern das Verhalten
    def oeffnen(self):
        """Öffnet die Flasche"""
        self.geoeffnet = True
        print("Flasche geöffnet")
    
    def schliessen(self):
        """Schließt die Flasche"""
        self.geoeffnet = False
        print("Flasche geschlossen")
    
    def fuellen(self, menge):
        """Füllt eine bestimmte Menge in die Flasche"""
        if not self.geoeffnet:
            print("Fehler: Flasche ist geschlossen!")
            return
        
        if self.inhalt + menge > self.max_inhalt:
            print(f"Fehler: Zu viel! Maximal {self.max_inhalt}ml möglich.")
        else:
            self.inhalt += menge
            print(f"Gefüllt: {menge}ml. Aktueller Inhalt: {self.inhalt}ml")
    
    def leeren(self):
        """Leert die Flasche komplett"""
        if not self.geoeffnet:
            print("Fehler: Flasche ist geschlossen!")
            return
        
        self.inhalt = 0
        print("Flasche geleert")


# Verwendung der Klasse
if __name__ == "__main__":
    print("=== Objektorientierte Programmierung Demo ===\n")
    
    # Instanziierung - Objekt von der Klasse erstellen
    meine_flasche = Flasche(max_inhalt=500)
    
    print(f"Flasche erstellt: max. {meine_flasche.max_inhalt}ml\n")
    
    # Methoden aufrufen
    meine_flasche.oeffnen()
    meine_flasche.fuellen(200)
    meine_flasche.fuellen(150)
    meine_flasche.fuellen(200)  # Zu viel!
    meine_flasche.schliessen()
    meine_flasche.leeren()      # Geht nicht - ist geschlossen
    
    print("\n=== Zweites Objekt ===\n")
    
    # Weiteres Objekt erstellen - unabhängig vom ersten
    andere_flasche = Flasche(max_inhalt=1000)
    andere_flasche.oeffnen()
    andere_flasche.fuellen(750)
    
    print(f"\nMeine Flasche: {meine_flasche.inhalt}ml")
    print(f"Andere Flasche: {andere_flasche.inhalt}ml")
