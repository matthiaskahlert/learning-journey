""" 
Erstelle ein Python-Skript, das folgende Aufgaben erfüllt:

a) Definiere eine Variable alter und weise ihr dein Alter als Ganzzahl zu.

b) Definiere eine Liste hobbies mit mindestens drei deiner Hobbies als Strings.

c) Definiere ein Tupel lieblingsfarben mit mindestens drei deiner Lieblingsfarben als Strings.

d) Schreibe eine Schleife, die für jedes Hobby in hobbies ausgibt: "Eines meiner Hobbies ist: [Hobby]."

e) Definiere eine Funktion jahre_bis_rente, die das Alter als Parameter annimmt und berechnet, 
wie viele Jahre du bis zur Rente (angenommen mit 65 Jahren) hast. Die Funktion soll das Ergebnis zurückgeben.

f) Importiere das Modul json und speichere die Daten aus hobbies und lieblingsfarben in einem Dictionary 
mit den Schlüsseln "Hobbies" und "Lieblingsfarben" in einer JSON-Datei namens persoenliche_daten.json.

g) Verwende eine try-except-Block, um die Datei zu öffnen und sicherzustellen, 
dass eine Nachricht "Fehler beim Speichern der Daten" ausgegeben wird, falls ein Fehler auftritt.

h) Verwende die with-Anweisung, um sicherzustellen, dass die Datei korrekt geschlossen wird, 
nachdem der Schreibvorgang abgeschlossen oder ein Fehler aufgetreten ist. 
 """
import json

alter = 45
hobbies = ['gaming', 'kickern', 'hiking']
lieblingsfarben = ('blau', 'türkis', 'schwarz')

for i in hobbies:
    print(f'Eines meiner hobbies ist: {i}.')

def jahre_bis_rente(alter):
    rentenalter = 65
    return rentenalter - alter

DATEINAME = 'python/exercises/Kapitel 8 Uebungen/persoenliche_daten.json'

# Dictionary erstellen (f) Teil 1)
daten = {
    'Hobbies':hobbies,
    'Lieblingsfarben':lieblingsfarben
}
# In JSON-Datei speichern (f) Teil 2)
try:
    with open(DATEINAME, 'w', encoding='utf-8') as stream: # encoding für umlaute in 'türkis' und: Die with-Anweisung garantiert, dass die Datei automatisch geschlossen wird
        json.dump(daten, stream, indent=4, ensure_ascii=False) # einrückung vier zeichen & kein unicode escape character im json
    print("Erfolgreich gespeichert")
except (IOError):
    print("Fehler beim Speichern der Daten")

