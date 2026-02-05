""" 
Du arbeitest als Entwickler in einem Unternehmen, das eine Software zur Verwaltung von Kundenkontakten entwickelt. 
Deine Aufgabe ist es, ein Python-Modul zu erstellen, das folgende Funktionalitäten umfasst:

a) Erstelle eine Funktion speichere_kontakt, die als Parameter die Daten eines Kontakts (Name, E-Mail, Telefonnummer) entgegennimmt 
und diese in einer JSON-Datei speichert. Verwende dabei das JSON-Format. 
Achte darauf, dass bei jedem Aufruf der Funktion ein neuer Kontakt zur Datei hinzugefügt wird, 
ohne die bestehenden Daten zu überschreiben.

b) Implementiere eine Funktion lade_kontakte, die die gespeicherten Kontaktdaten aus der JSON-Datei liest 
und als Liste von Dictionaries zurückgibt. Jedes Dictionary in der Liste soll die Daten eines Kontakts repräsentieren.

c) Erstelle eine Fehlerbehandlung für beide Funktionen, um sicherzustellen, 
dass das Programm nicht abstürzt, falls die Datei nicht existiert oder beschädigt ist. 
Gib in solchen Fällen eine entsprechende Fehlermeldung aus.

d) Schreibe eine einfache Benutzeroberfläche (CLI), über die ein Benutzer neue Kontakte hinzufügen 
und die gespeicherten Kontakte anzeigen lassen kann. 
Verwende dazu die Funktionen speichere_kontakt und lade_kontakte. """

import json
# Dateipfad als globale Variable
DATEINAME = 'python/exercises/Kapitel 8 Uebungen/kontakte.json'


# a)
def speichere_kontakt(kontaktname, email, telefonnummer):
    """
    Speichert einen neuen Kontakt in der JSON-Datei.
    Prüft auf Duplikate, basierend auf der E-Mail Adresse.
    
    Args:
        kontaktname (str): Name des Kontakts
        email (str): E-Mail-Adresse
        telefonnummer (str): Telefonnummer
    """

    # vorhandene kontakte laden
    try:
        with open(DATEINAME, 'r') as stream:
            kontakte = json.load(stream)
    except (FileNotFoundError, json.JSONDecodeError):
        kontakte =  [] # array wird erstellt, falls datei nicht existiert
    
    # duplikatprüfung
    for kontakt in kontakte:
        if kontakt.get("E-Mail") == email:
            print(f"Kontakt mit der E-Mail {email} existiert bereits.")
            return
    # neue kontakte hinzufügen   
    kontakt = {
        'Name': kontaktname,
        'E-Mail': email,
        'Telefonnummer': telefonnummer
        }
    kontakte.append(kontakt)

    # alles speichern
    try:
        with open(DATEINAME, 'w') as stream:
            json.dump(kontakte, stream, indent=4) # indent kommt von indentation, das ist der einzug, hier vier leerzeichen
    except (IOError):
        print("Fehler beim Speichern der Kontakte.")


def lade_kontakte():
    """
    Lädt alle Kontakte aus der JSON-Datei.
    
    Returns:
        list: Liste von Kontakt-Dictionaries
    """
    try:
        with open(DATEINAME, 'r') as stream:
            kontakte = json.load(stream)
        return kontakte
    except FileNotFoundError:
        print("Die Kontaktdatei existiert noch nicht.")
        return []
    except json.JSONDecodeError:
        print("Die Kontaktdatei ist beschädigt.")
        return []

# hilfsfunktion zum anzeigen der kontakte
def zeige_kontakte():
    """
    Zeigt alle gespeicherten Kontakte an
    """
    kontakte = lade_kontakte()
    
    if not kontakte:
        print("\nKeine Kontakte vorhanden.")
        return
    
    print(f"\n{'='*70}")
    print(f"Gespeicherte Kontakte ({len(kontakte)}):")
    print(f"{'='*70}")

    for kontakt in lade_kontakte():
        print('Name: ', kontakt['Name'],'E-Mail: ', kontakt['E-Mail'], 'Telefonnummer: ', kontakt['Telefonnummer'])

def hauptmenü():
    """
    Einfache CLI zur Verwaltung von Kontakten
    """
    while True:
        print("\n" + "="*70)
        print("KONTAKTVERWALTUNG")
        print("\n" + "="*70)
        print("1. Neuen Kontakt hinzufügen")
        print("2. Alle Kontakte anzeigen")
        print("3. Programm Beenden")
        print("\n" + "="*70)
        
        wahl = input("\nWähle eine Option (1-3): ")
        
        if wahl == '1':
            print("\n--- Neuen Kontakt hinzufügen ---")
            kontaktname = input("Name: ")
            email = input("E-Mail: ")
            telefonnummer = input("Telefonnummer: ")

            if kontaktname and email and telefonnummer:
                speichere_kontakt(kontaktname, email, telefonnummer)
            else:
                print("Fehler: Alle Felder müssen ausgefüllt werden!")
            
        elif wahl == '2':
            zeige_kontakte()
        elif wahl == '3':
            print("\nAuf Wiedersehen!")
            print("Programm beendet.")
            print("="*60)
            break
        else:
            print("Ungültige Auswahl. Bitte versuche es erneut.")

#Testbereich
if __name__ == "__main__":
    print("=== AUTOMATISCHE TESTS ===\n")

    # kontakte speichern
    print("Füge Testkontakte hinzu...\n")
    speichere_kontakt("Anna", "anna@mail.de", "+49151 12 34 567") # kontakte.json wurde erstellt und kontakt hinzugefügt
    speichere_kontakt("Bernd", "bernd@mail.de", "+49151 23 45 678") # test ob der erste kontakt in Liste verbleibt

    # 

    # testdaten zum entgegennehmen:

    daten = [
        ('Max', 'max@mail.de', '+49161 12 34 567'),
        ('Erika', 'erika@mail.de', '+49161 23 45 678'),
        ('Hans', 'hans@mail.de', '+49161 34 56 789')
        ]
    for i in daten:
        speichere_kontakt(i[0], i[1], i[2])
    
    # kontakte anzeigen
    zeige_kontakte()

        # Starte interaktives Menü (optional auskommentieren)
    print("\n" + "="*60)
    antwort = input("Möchten Sie das interaktive Menü starten? (j/n): ").lower()
    if antwort == 'j':
        hauptmenü()