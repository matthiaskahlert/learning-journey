"""
a) Definiere eine Variable, die einen Text in Form eines Strings speichert.
Dieser Text soll mindestens ein Unicode-Zeichen enthalten, welches nicht auf einer normalen Tastatur zu finden ist.
Verwende dazu die Funktion chr() mit einer Unicode-Nummer deiner Wahl.
b) Füge dem Text eine Escape-Sequenz hinzu, die einen Zeilenumbruch darstellt.
c) Verwende eine Stringmethode, um zu zählen, wie oft ein bestimmtes Zeichen in deinem Text vorkommt.
d) Erstelle eine Liste mit mehreren Strings.
Verwende die Methode .join(), um einen neuen String zu erstellen, der die Elemente der Liste durch ein Komma getrennt enthält.
e) Speichere den Text aus a) in einer Datei.
Verwende dazu die with-Anweisung und den Modus 'w' für das Schreiben in Dateien.
f) Lies den Text aus der Datei, die du in e) erstellt hast, und gib ihn auf der Konsole aus.
Verwende dazu ebenfalls die with-Anweisung, diesmal mit dem Modus 'r' für das Lesen aus Dateien.
g) Fange mögliche Ausnahmen, die beim Lesen der Datei auftreten können, mit try und except ab.
h) Verwende das JSON-Format, um eine einfache Datenstruktur (z.B. ein Dictionary mit einigen Schlüssel-Wert-Paaren)
in einer Datei zu speichern und wieder zu laden.
"""
import json

textvariable = 'Ich bin ein string.'
print('Variable mit einem String: ')
print(textvariable)
textvariable += ' ' + chr(128512)  # Füge ein Unicode-Zeichen hinzu (😀)
print('\nDie gleiche Variable, erweitert mit unicodezeichen: ')
print(textvariable)
textvariable += '\nDies ist eine neue Zeile, erzeugt durch einen escape character "\\n".'  # Füge einen Zeilenumbruch hinzu
print('\nDie gleiche Variable, erweitert mit unicodezeichen und neuer Zeile: ')
print(textvariable)
zeichen_zaehler = textvariable.count('e')  # Zähle, wie oft 'e' im Text vorkommt
print(f'\nDas Zeichen "e" kommt {zeichen_zaehler} mal in dem Text vor.')
stringListe = ['Hallo', 'Welt', 'Python']
print('\nListe mit mehreren Strings: ')
print(stringListe)
neuerString = ', '.join(stringListe)  # Verbinde die Elemente der Liste mit einem Komma
print('\nStringliste getrennt durch Komma: ')
print(neuerString)
try:
    with open('python/exercises/Kapitel 9 Uebungen/text97Ue03.txt', 'w', encoding='utf-8') as file:
        file.write(textvariable)  # Speichere den Text in einer Datei
    with open('python/exercises/Kapitel 9 Uebungen/text97Ue03.txt', 'r', encoding='utf-8') as file:
        gelesenerText = file.read()  # Lese den Text aus der Datei
        print('\nEingelesener Text aus der erstellten Datei: ')
        print(gelesenerText)
except Exception as e:
    print(f'Fehler beim Lesen der Datei: {e}')
#e)
daten = {
    'Name': 'Max Mustermann',
    'Alter': 33,
    'Beruf': 'Softwareentwickler'
}
# Speichern der Daten im JSON-Format
try:
    with open('python/exercises/Kapitel 9 Uebungen/daten97UE03.json', 'w', encoding='utf-8') as json_file:
        json.dump(daten, json_file, ensure_ascii=False, indent=4)
    # Laden der Daten aus der JSON-Datei
    with open('python/exercises/Kapitel 9 Uebungen/daten97UE03.json', 'r', encoding='utf-8') as json_file:
        geladene_daten = json.load(json_file)
        print('\nGeladene Daten aus JSON-Datei: ')
        print(geladene_daten)
except Exception as e:
    print(f'Fehler beim Umgang mit der JSON-Datei: {e}')    