""" Schreibe ein Python-Skript, das folgende Aufgaben erfüllt:

a) Erstelle eine Liste mit den Namen von fünf Freunden.
b) Speichere diese Liste in einer Datei mit dem Namen "freunde.txt" 
unter Verwendung des JSON-Formats.
c) Lies die Liste aus der Datei "freunde.txt" und weise sie einer neuen Variablen zu.
d) Füge der Liste in der Datei einen weiteren Namen hinzu, ohne die ursprüngliche Liste im Skript zu ändern.

e) Fang mögliche Laufzeitfehler beim Öffnen, Schreiben und Lesen der Datei ab 
und gib eine benutzerfreundliche Fehlermeldung aus.

f) Stelle sicher, dass die Datei in jedem Fall korrekt geschlossen wird, auch wenn Fehler auftreten. """

import json
# a)
namen = ["Peter", "Tim", "Nordi", "Georg", "Gregor"]

# b)
DATEINAME = 'python/exercises/Kapitel 8 Uebungen/freunde.txt'
try:
    with open(DATEINAME, 'w') as datei:
        json.dump(namen, datei, indent=4)
        print(f'Liste erfolgreich in "{DATEINAME}" gespeichert.')
except IOError as e:
    print(f'Fehler beim Speichern der Liste: {e}')

# c)
try:
    with open(DATEINAME, 'r') as datei:
        geladene_namen = json.load(datei)
        print(f'Liste erfolgreich aus "{DATEINAME}" geladen: {geladene_namen}')
except IOError as e:
    print(f'Fehler beim Laden der Liste: {e}')

# d)
try:
    with open(DATEINAME, 'r') as stream:
        geladene_namen = json.load(stream)
    
    neuer_name = input('Gib einen neuen Namen ein: ')
    geladene_namen.append(neuer_name)
    
    with open(DATEINAME, 'w') as stream:
        json.dump(geladene_namen, stream, indent=4)
    print(f'Neuer Name "{neuer_name}" wurde der Liste hinzugefügt und in "{DATEINAME}" gespeichert.')
    
except FileNotFoundError:
    print(f'Fehler: Die Datei "{DATEINAME}" wurde nicht gefunden.')
except json.JSONDecodeError:
    print(f'Fehler: Die Datei "{DATEINAME}" enthält ungültige JSON-Daten.')
except IOError as e:
    print(f'Fehler beim Lesen oder Schreiben der Datei: {e}')