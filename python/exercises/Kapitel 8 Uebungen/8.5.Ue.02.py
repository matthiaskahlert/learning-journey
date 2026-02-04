""" 
a) Definiere eine Funktion speichere_daten, die als Parameter eine Liste von Tupeln entgegennimmt. 
Jedes Tupel soll Daten eines Studenten repräsentieren, bestehend aus (Name, Matrikelnummer, Studiengang). 
Die Funktion soll diese Daten in einer Textdatei namens studentendaten.txt speichern. 
Verwende die with-Anweisung, um sicherzustellen, dass die Datei korrekt geöffnet und geschlossen wird. 
Jeder Student soll in einer neuen Zeile in folgendem Format gespeichert werden: 
"Name: [Name], Matrikelnummer: [Matrikelnummer], Studiengang: [Studiengang]".

b) Definiere eine zweite Funktion lade_daten, die die gespeicherten Daten aus der Datei studentendaten.txt liest 
und als Liste von Dictionaries zurückgibt, wobei jedes Dictionary die Daten eines Studenten enthält.

c) Implementiere eine einfache Fehlerbehandlung in beiden Funktionen, um den Fall zu behandeln, 
dass die Datei nicht geöffnet oder gefunden werden kann. 
Gib in diesem Fall eine entsprechende Fehlermeldung aus.
"""
def speichere_daten(daten):
    try:
        with open('python/exercises/Kapitel 8 Uebungen/studentendaten.txt', 'w') as datei:
            for name, matrikelnummer, studiengang in daten:
                datei.write(f"Name: {name}, Matrikelnummer: {matrikelnummer}, Studiengang: {studiengang}\n")
    except Exception as e:
        print(f"Fehler beim Speichern der Daten: {e}")

def lade_daten():
    try:
        daten = []
        with open('python/exercises/Kapitel 8 Uebungen/studentendaten.txt', 'r') as datei:
            for zeile in datei:
                teile = zeile.strip().split(', ')
                name = teile[0].split(': ')[1]
                matrikelnummer = teile[1].split(': ')[1]
                studiengang = teile[2].split(': ')[1]
                daten.append({'Name': name, 'Matrikelnummer': matrikelnummer, 'Studiengang': studiengang})
    except FileNotFoundError:
        print("Fehler: Die Datei wurde nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Laden der Daten: {e}")
    return daten

def main():
    daten = [
        ('Max Mustermann', '234567', 'BWL'),
        ('Erika Musterfrau', '345678', 'Informatik'),
        ('Hans Meier', '5465860', 'Maschinenbau und Produktionstechnik')
    ]
    speichere_daten(daten)
    geladene_daten = lade_daten()
    for datensatz in geladene_daten:
        print(datensatz)

if __name__ == "__main__":
    main()
