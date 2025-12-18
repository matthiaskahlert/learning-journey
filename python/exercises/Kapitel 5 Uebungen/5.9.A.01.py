"""Entwickle ein Python-Programm, das folgende Funktionen umfasst:

a) Eine Funktion buch_daten_speichern, die als Parameter den Titel eines Buches (String), den Namen des Autors (String), 
das Veröffentlichungsjahr (Integer), und optional die Anzahl der Seiten (Integer, Defaultwert 0) erhält. 
Die Funktion soll alle diese Daten in einem Dictionary speichern, wobei die Schlüssel titel, autor, jahr, und seiten sind. 
Die Funktion gibt dieses Dictionary zurück.

b) Eine Funktion buecher_sammlung, die eine Liste von Bücher-Dictionaries (erstellt von buch_daten_speichern) als Parameter erhält 
und die Gesamtanzahl der Seiten aller Bücher in der Liste berechnet. Die Funktion gibt die Gesamtseitenzahl zurück.

c) Verwende eine Schleife, um den Benutzer zur Eingabe von Daten für drei verschiedene Bücher aufzufordern. 
Nutze dabei die Funktion buch_daten_speichern für jedes Buch und speichere jedes resultierende Dictionary in einer Liste.

d) Nachdem alle Bücher eingegeben wurden, rufe die Funktion buecher_sammlung mit der Liste der Bücher-Dictionaries als Argument auf, 
um die Gesamtanzahl der Seiten aller Bücher zu berechnen.

e) Gib die Gesamtanzahl der Seiten aller Bücher aus. """

def buch_daten_speichern(
        titel: str,
        autor: str,
        jahr: int,
        seiten: int = 0 # optionale Seitenzahl, Standardwert = 0
        )-> dict: # -> dict ist quasi eine empfehlung, python prüft dies nicht explizit aber es besagt: dir funktion gibt ein dictionary zurück
    return {
        "titel": titel,
        "autor": autor,
        "jahr": jahr,
        "seiten": seiten
        }

def buecher_sammlung(buecher):
    gesamt_seiten = 0 # initial Zähler für Gesamtseitenzahl
    for buch in buecher: # Iteriert über alle Bücher in der Liste
        gesamt_seiten += buch["seiten"]
    return gesamt_seiten
    
buecher_liste = [] # Liste, in der alle Bücher gespeichert werden

for i in range(3): # Schleife für die Eingabe von drei Büchern
    print(f"\nBuch {i + 1}")

    titel = input("Titel: ")
    autor = input("Autor: ")

    # Erscheinungsjahr abfragen, mit Fehlerbehandlung
    while True:
        try:
            jahr = int(input("Erscheinungsjahr: "))
            break # Schleife verlassen, wenn die Eingabe gültig ist
        except ValueError:
            print("Bitte eine gültige Jahreszahl eingeben.")

    # Seitenzahl ist optional
    while True:
        seiten_eingabe = input("Seitenzahl (Enter = 0): ")
        if seiten_eingabe == "":
            seiten = 0
            break
        try: # typkonvertierung da input ein string ist
            seiten = int(seiten_eingabe)
            break
        except ValueError:
            print("Bitte eine gültige Seitenzahl eingeben.")

    buch = buch_daten_speichern(titel, autor, jahr, seiten) # Erzeugt ein Buch-Dictionary mit der Funktion
    buecher_liste.append(buch) # Fügt das Buch der Bücherliste hinzu


gesamt = buecher_sammlung(buecher_liste) # Berechnt die Gesamtanzahl der Seiten aller Bücher
print(f"\nGesamtanzahl der Seiten aller Bücher: {gesamt}")
