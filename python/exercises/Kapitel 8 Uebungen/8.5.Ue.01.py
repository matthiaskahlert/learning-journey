""" 
a) Definiere eine Funktion speichere_daten, die als Parameter eine Liste von Tupeln entgegennimmt. 
Jedes Tupel enthält zwei Werte: einen Namen (String) und ein Alter (Integer). 
Die Funktion soll diese Daten in einer Datei namens personen.txt speichern. 
Verwende dabei die with-Anweisung und den Modus 'w' zum Öffnen der Datei. 
Jedes Tupel soll in einer neuen Zeile in folgendem Format gespeichert werden: Name: Alter.

b) Definiere eine weitere Funktion lade_daten, die die zuvor gespeicherten Daten aus der Datei personen.txt liest 
und als Liste von Dictionaries zurückgibt, wobei jedes Dictionary einen Namen und ein Alter enthält.

c) Implementiere eine Fehlerbehandlung in beiden Funktionen, um mit möglichen Laufzeitfehlern umzugehen, z.B. wenn die Datei nicht existiert oder ein Schreib-/Lesefehler auftritt. Gib in solchen Fällen eine aussagekräftige Fehlermeldung aus.

d) Schreibe eine Kontrollstruktur, die überprüft, ob die zurückgegebene Liste von lade_daten leer ist oder nicht. 
Wenn sie nicht leer ist, gib die geladenen Daten formatiert in der Konsole aus. Verwende dazu eine Schleife.  """

# a)
def speichere_daten(daten):
    try:
        with open('python/exercises/Kapitel 8 Uebungen/personen.txt', 'w') as datei:
            for name, alter in daten:
                datei.write(f"{name}: {alter}\n")
    except Exception as e:
        print(f"Fehler beim Speichern der Daten: {e}")

# b + c)
def lade_daten():
    try:
        daten = []
        with open('python/exercises/Kapitel 8 Uebungen/personen.txt', 'r') as datei:
            for zeile in datei:
                name, alter = zeile.strip().split(': ')
                daten.append({'Name': name, 'Alter': int(alter)})
    except FileNotFoundError:
        print("Fehler: Die Datei wurde nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Laden der Daten: {e}")
    return daten

def main():
    daten = [('Anna', 36), ('Bernd', 55), ('Caspar', 19)]
    speichere_daten(daten)
    geladene_daten = lade_daten()
    if geladene_daten:
        for person in geladene_daten:
            print(f"Name: {person['Name']}, Alter: {person['Alter']}")
    else:
        print("Keine Daten geladen.")

if __name__ == "__main__": # sorgt für ausführung per script aber nicht bei modulimport. dort wird der modulname gesetzt und der if block übersprungen
    main()