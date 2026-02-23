"""
Komplettes OOP-Beispiel: Alle Konzepte zusammen
Thema: Klassen, Polymorphie, Vererbung in einem realitätsnahen Beispiel
"""

# Basisklasse
class Konto:
    """Bankkonto-Basisklasse"""
    
    # Klassenattribut (für alle Instanzen gleich)
    bank_name = "MeineBank AG"
    
    def __init__(self, inhaber, kontonummer):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.saldo = 0.0
    
    def einzahlen(self, betrag):
        """Geld einzahlen"""
        if betrag > 0:
            self.saldo += betrag
            print(f"Eingezahlt: {betrag}€. Neuer Saldo: {self.saldo}€")
        else:
            print("Betrag muss positiv sein!")
    
    def abheben(self, betrag):
        """Geld abheben"""
        if betrag > self.saldo:
            print("Nicht genug Guthaben!")
        else:
            self.saldo -= betrag
            print(f"Abgehoben: {betrag}€. Neuer Saldo: {self.saldo}€")
    
    # Polymorphie: __str__
    def __str__(self):
        return f"Konto {self.kontonummer} ({self.inhaber}): {self.saldo}€"


# Unterklasse 1: Girokonto
class Girokonto(Konto):
    """Girokonto mit Dispo-Kredit"""
    
    def __init__(self, inhaber, kontonummer, dispo=500):
        super().__init__(inhaber, kontonummer)
        self.dispo = dispo  # Neues Attribut
    
    # Überschreibt abheben() mit erweiterter Logik
    def abheben(self, betrag):
        """Abheben mit Dispo-Möglichkeit"""
        if betrag > self.saldo + self.dispo:
            print(f"Nicht genug Guthaben! (Max: {self.saldo + self.dispo}€)")
        else:
            self.saldo -= betrag
            print(f"Abgehoben: {betrag}€. Neuer Saldo: {self.saldo}€")
            if self.saldo < 0:
                print(f"Achtung!⚠️  Im Dispo: {abs(self.saldo)}€")
    
    def __str__(self):
        return f"Girokonto {self.kontonummer} ({self.inhaber}): {self.saldo}€ (Dispo: {self.dispo}€)"


# Unterklasse 2: Sparkonto
class Sparkonto(Konto):
    """Sparkonto mit Zinsen"""
    
    def __init__(self, inhaber, kontonummer, zinssatz=1.5):
        super().__init__(inhaber, kontonummer)
        self.zinssatz = zinssatz
    
    # Neue Methode
    def zinsen_gutschreiben(self):
        """Berechnet und schreibt Zinsen gut"""
        zinsen = self.saldo * (self.zinssatz / 100)
        self.saldo += zinsen
        print(f"Zinsen gutgeschrieben: {zinsen:.2f}€. Neuer Saldo: {self.saldo:.2f}€")
    
    # Überschreiben: Sparkonto erlaubt nur Abheben wenn Saldo > 0
    def abheben(self, betrag):
        """Bei Sparkonto kein Minus erlaubt"""
        if betrag > self.saldo:
            print("Sparkonto darf nicht ins Minus gehen!")
        else:
            super().abheben(betrag)
    
    def __str__(self):
        return f"Sparkonto {self.kontonummer} ({self.inhaber}): {self.saldo:.2f}€ (Zinssatz: {self.zinssatz}%)"


# Verwendung
if __name__ == "__main__":
    print(f"=== Willkommen bei {Konto.bank_name} ===\n")
    
    # Verschiedene Konten erstellen
    girokonto = Girokonto("Max Mustermann", "DE123", dispo=1000)
    sparkonto = Sparkonto("Max Mustermann", "DE456", zinssatz=2.0)
    
    print("--- Girokonto ---")
    girokonto.einzahlen(500)
    girokonto.abheben(300)
    girokonto.abheben(400)  # Geht ins Dispo
    print(girokonto)
    
    print("\n--- Sparkonto ---")
    sparkonto.einzahlen(1000)
    sparkonto.zinsen_gutschreiben()
    sparkonto.abheben(500)
    sparkonto.abheben(700)  # Zu viel!
    print(sparkonto)
    
    print("\n=== Alle Konten im Überblick ===")
    konten = [girokonto, sparkonto]
    for konto in konten:
        print(f'\n{konto}')  # Nutzt __str__() - Polymorphie!
    
    print("\n=== OOP-Konzepte in diesem Beispiel ===")
    print("✓ Klassen: Konto, Girokonto, Sparkonto")
    print("✓ Vererbung: Girokonto und Sparkonto erben von Konto")
    print("✓ Polymorphie: __str__() für verschiedene Darstellungen")
    print("✓ Überschreiben: abheben() in Unterklassen angepasst")
    print("✓ Erweiterung: zinsen_gutschreiben() nur bei Sparkonto")
    print("✓ Klassenattribute: bank_name für alle gleich")
