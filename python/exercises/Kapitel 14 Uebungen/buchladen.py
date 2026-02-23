"""
Entwickle ein Python-Programm, das eine einfache Simulation eines Online-Buchladens durchführt.
Der Buchladen soll Bücher in verschiedenen Kategorien (z.B. Roman, Sachbuch, Wissenschaft) führen.
Jedes Buch hat einen Titel, einen Autor, eine Kategorie und einen Preis.

a) Definiere eine Klasse Buch mit den Attributen titel, autor, kategorie und preis.
Implementiere eine __init__-Methode, die diese Attribute initialisiert,
und eine __str__-Methode, die eine repräsentative Zeichenkette für das Buchobjekt zurückgibt.

b) Definiere eine Klasse Buchladen mit einem Attribut inventar, das eine Liste von Buchobjekten speichert.
Implementiere Methoden für das Hinzufügen eines Buches zum Inventar,
das Durchsuchen des Inventars nach Kategorie
und das Berechnen des Gesamtpreises einer Buchauswahl.

c) Erstelle ein paar Buchobjekte und füge sie zum Inventar des Buchladens hinzu.
Teste anschließend die Funktionalitäten des Buchladens,
indem du Bücher nach Kategorie durchsuchst
und den Gesamtpreis für eine Auswahl von Büchern berechnest.
"""


# a) Klasse Buch
class Buch:
    """Repräsentiert ein Buch mit Titel, Autor, Kategorie und Preis."""

    def __init__(self, titel, autor, kategorie, preis):
        """Initialisiert ein Buch mit Titel, Autor, Kategorie und Preis."""
        self.titel = titel
        self.autor = autor
        self.kategorie = kategorie
        self.preis = preis

    def __str__(self):
        """Gibt eine lesbare Darstellung des Buchs zurück."""
        return f'"{self.titel}" von {self.autor} ({self.kategorie}) - {self.preis:.2f} €'


# b) Klasse Buchladen
class Buchladen:
    """Repräsentiert einen Buchladen mit einem Inventar an Büchern."""

    def __init__(self):
        """Initialisiert den Buchladen mit einem leeren Inventar."""
        self.inventar = []

    def buch_hinzufuegen(self, buch):
        """Fügt ein Buch zum Inventar hinzu."""
        self.inventar.append(buch)

    def suche_nach_kategorie(self, kategorie):
        """Gibt alle Bücher der angegebenen Kategorie zurück."""
        return [buch for buch in self.inventar if buch.kategorie == kategorie]

    def gesamtpreis(self, buecher):
        """Berechnet den Gesamtpreis einer Liste von Büchern."""
        return sum(buch.preis for buch in buecher)


# c) Buchobjekte erstellen und testen
if __name__ == "__main__":
    # Buchladen erstellen
    laden = Buchladen()

    # Bücher erstellen und zum Inventar hinzufügen
    laden.buch_hinzufuegen(Buch("Der Alchimist", "Paulo Coelho", "Roman", 12.99))
    laden.buch_hinzufuegen(Buch("1984", "George Orwell", "Roman", 10.99))
    laden.buch_hinzufuegen(Buch("Eine kurze Geschichte der Zeit", "Stephen Hawking", "Wissenschaft", 14.99))
    laden.buch_hinzufuegen(Buch("Sapiens", "Yuval Noah Harari", "Sachbuch", 16.99))
    laden.buch_hinzufuegen(Buch("Das Universum in der Nussschale", "Stephen Hawking", "Wissenschaft", 13.99))

    # Bücher nach Kategorie durchsuchen
    print("Bücher in der Kategorie 'Roman':")
    for buch in laden.suche_nach_kategorie("Roman"):
        print(" ", buch)

    print("\nBücher in der Kategorie 'Wissenschaft':")
    wissenschaft_buecher = laden.suche_nach_kategorie("Wissenschaft")
    for buch in wissenschaft_buecher:
        print(" ", buch)

    # Gesamtpreis berechnen
    print(f"\nGesamtpreis der Wissenschaftsbücher: {laden.gesamtpreis(wissenschaft_buecher):.2f} €")
    print(f"Gesamtpreis aller Bücher: {laden.gesamtpreis(laden.inventar):.2f} €")
