"""
Einfaches Beispiel: Vererbung
Thema: Basisklasse, Unterklasse, Erweiterung, Überschreiben
"""

# Basisklasse (Superklasse, Elternklasse)
class Fahrzeug:
    """Allgemeine Fahrzeug-Klasse"""
    
    def __init__(self, marke, geschwindigkeit=0):
        self.marke = marke
        self.geschwindigkeit = geschwindigkeit
    
    def beschleunigen(self, wert):
        """Erhöht die Geschwindigkeit"""
        self.geschwindigkeit += wert
        print(f"{self.marke} beschleunigt auf {self.geschwindigkeit} km/h")
    
    def bremsen(self):
        """Stoppt das Fahrzeug"""
        self.geschwindigkeit = 0
        print(f"{self.marke} gestoppt")
    
    def info(self):
        """Zeigt Informationen an"""
        return f"Fahrzeug: {self.marke}, {self.geschwindigkeit} km/h"


# Unterklasse 1 - erbt von Fahrzeug
class Auto(Fahrzeug):
    """Auto-Klasse erbt von Fahrzeug"""
    
    def __init__(self, marke, anzahl_tueren):
        # Ruft __init__ der Basisklasse auf
        super().__init__(marke)
        # Fügt neues Attribut hinzu
        self.anzahl_tueren = anzahl_tueren
    
    # Überschreibt die info() Methode
    def info(self):
        return f"Auto: {self.marke}, {self.anzahl_tueren} Türen, {self.geschwindigkeit} km/h"
    
    # Fügt neue Methode hinzu
    def hupen(self):
        print("Mööp Mööp!")


# Unterklasse 2 - erbt von Fahrzeug
class Fahrrad(Fahrzeug):
    """Fahrrad-Klasse erbt von Fahrzeug"""
    
    def __init__(self, marke, gang=1):
        super().__init__(marke)
        self.gang = gang
    
    # Überschreibt beschleunigen() mit eigener Logik
    def beschleunigen(self, wert):
        # Fahrräder sind langsamer
        self.geschwindigkeit += wert // 2
        print(f"{self.marke} (Fahrrad) beschleunigt auf {self.geschwindigkeit} km/h")
    
    # Neue Methode
    def gang_wechseln(self, neuer_gang):
        self.gang = neuer_gang
        print(f"Gang gewechselt zu {self.gang}")


# Unterklasse 3 - erbt von Auto (mehrstufige Vererbung)
class Elektroauto(Auto):
    """Elektroauto erbt von Auto"""
    
    def __init__(self, marke, anzahl_tueren, batteriekapazitaet):
        super().__init__(marke, anzahl_tueren)
        self.batteriekapazitaet = batteriekapazitaet
        self.batteriestand = 100  # Prozent
    
    def info(self):
        return f"Elektroauto: {self.marke}, {self.anzahl_tueren} Türen, {self.geschwindigkeit} km/h, Batterie: {self.batteriestand}%"
    
    def laden(self):
        self.batteriestand = 100
        print("Batterie vollständig geladen!")


# Verwendung
if __name__ == "__main__":
    print("=== Vererbung Demo ===\n")
    
    # Basisklasse verwenden
    print("--- Allgemeines Fahrzeug ---")
    f = Fahrzeug("Generic")
    f.beschleunigen(50)
    print(f.info())
    f.bremsen()
    
    print("\n--- Auto (erbt von Fahrzeug) ---")
    auto = Auto("VW Golf", 5)
    auto.beschleunigen(80)
    print(auto.info())
    auto.hupen()  # Nur Auto hat diese Methode
    
    print("\n--- Fahrrad (erbt von Fahrzeug) ---")
    rad = Fahrrad("Canyon")
    rad.beschleunigen(40)  # Überschriebene Methode
    rad.gang_wechseln(3)
    print(rad.info())
    
    print("\n--- Elektroauto (erbt von Auto) ---")
    tesla = Elektroauto("Tesla Model 3", 4, 75)
    tesla.beschleunigen(100)
    print(tesla.info())
    tesla.hupen()  # Von Auto geerbt
    tesla.laden()  # Eigene Methode
    
    print("\n=== Vorteile der Vererbung ===")
    print("✓ Code-Wiederverwendung (beschleunigen, bremsen)")
    print("✓ Erweiterbarkeit (neue Attribute und Methoden)")
    print("✓ Überschreiben (angepasstes Verhalten)")
    print("✓ Klare Hierarchie (Fahrzeug → Auto → Elektroauto)")
