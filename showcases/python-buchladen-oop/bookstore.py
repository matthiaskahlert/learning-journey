"""Core domain model for the bookstore showcase."""

from dataclasses import dataclass


@dataclass
class Buch:
    """Represents a book in the store inventory."""

    titel: str
    autor: str
    kategorie: str
    preis: float

    def __str__(self) -> str:
        return f'"{self.titel}" von {self.autor} ({self.kategorie}) - {self.preis:.2f} EUR'


class Buchladen:
    """Represents a bookstore with an in-memory inventory."""

    def __init__(self) -> None:
        self.inventar: list[Buch] = []

    def buch_hinzufuegen(self, buch: Buch) -> None:
        self.inventar.append(buch)

    def suche_nach_kategorie(self, kategorie: str) -> list[Buch]:
        kategorie_normalized = kategorie.strip().lower()
        return [
            buch
            for buch in self.inventar
            if buch.kategorie.strip().lower() == kategorie_normalized
        ]

    def gesamtpreis(self, buecher: list[Buch]) -> float:
        return sum(buch.preis for buch in buecher)


def baue_demo_inventar() -> Buchladen:
    """Creates a ready-to-run demo inventory."""

    laden = Buchladen()
    laden.buch_hinzufuegen(Buch("Der Alchimist", "Paulo Coelho", "Roman", 17.99))
    laden.buch_hinzufuegen(Buch("1984", "George Orwell", "Roman", 15.99))
    laden.buch_hinzufuegen(
        Buch("Eine kurze Geschichte der Zeit", "Stephen Hawking", "Wissenschaft", 19.99)
    )
    laden.buch_hinzufuegen(
        Buch("Mit Pflanzen die Welt retten", "Bernhard Kegel", "Sachbuch", 25.00)
    )
    laden.buch_hinzufuegen(
        Buch(
            "Natur auf dem Teller: Weil Pizza und Pommes nicht auf Baumen wachsen",
            "Lisa Voisard",
            "Wissenschaft",
            20.00,
        )
    )
    return laden
