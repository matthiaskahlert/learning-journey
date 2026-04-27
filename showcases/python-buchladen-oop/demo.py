"""Simple demo runner for the bookstore showcase."""

from bookstore import baue_demo_inventar


if __name__ == "__main__":
    laden = baue_demo_inventar()

    for kategorie in ["Sachbuch", "Roman", "Wissenschaft"]:
        print(f"Bucher in der Kategorie '{kategorie}':")
        gefundene_buecher = laden.suche_nach_kategorie(kategorie)
        for buch in gefundene_buecher:
            print(f"  {buch}")
        print()

    wissenschaft_buecher = laden.suche_nach_kategorie("Wissenschaft")
    print(f"Gesamtpreis der Wissenschaftsbucher: {laden.gesamtpreis(wissenschaft_buecher):.2f} EUR")
    print(f"Gesamtpreis aller Bucher: {laden.gesamtpreis(laden.inventar):.2f} EUR")
