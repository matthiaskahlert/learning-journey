""" Entwickle ein Python-Skript, das folgende Aufgaben erfüllt:

a) Lese eine Textdatei namens "tagebuch.txt", die in UTF-8 kodiert ist, und speichere den Inhalt in einer Variablen. 
Verwende die with-answeisung und try-except-Blöcke, um Fehler beim Dateizugriff zu handhaben.
b) Verwende eine Funktion, um alle Vorkommen eines bestimmten Wortes im Text zu zählen. 
Das Wort soll als Parameter an die Funktion übergeben werden.
c) Ersetze in dem Text alle Vorkommen des Wortes "traurig" durch "glücklich" 
und speichere das Ergebnis in einer neuen Datei namens "tagebuch_neu.txt".

d) Schreibe eine weitere Funktion, die den aktualisierten Text nimmt und eine Liste von Sätzen zurückgibt, 
wobei jeder Satz ein Element der Liste ist. Verwende dazu eine geeignete String-Methode.

e) Konvertiere die Liste von Sätzen in ein JSON-Format und speichere 
diese Daten in einer Datei namens "tagebuch_saetze.json".

Stelle sicher, dass dein Skript modular aufgebaut ist und du Import-Module für JSON-Funktionalitäten 
und andere benötigte Funktionen verwendest.   """

import json
def zähle_wort(text, wort):
    return text.lower().count(wort.lower())
def ersetze_wort(text, alt, neu):
    return text.replace(alt, neu)
def teile_in_sätze(text):
    return text.split('.')
def speichere_als_json(dateiname, daten):
    with open(dateiname, 'w', encoding='utf-8') as file:
        json.dump(daten, file, ensure_ascii=False, indent=4)
try:
    with open('tagebuch.txt', 'r', encoding='utf-8') as file:
        inhalt = file.read()
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")
else:
    wort_vorkommen = zähle_wort(inhalt, 'traurig')
    print(f"Das Wort 'traurig' kommt {wort_vorkommen} Mal vor.")
    
    aktualisierter_text = ersetze_wort(inhalt, 'traurig', 'glücklich')
    
    with open('tagebuch_neu.txt', 'w', encoding='utf-8') as neue_datei:
        neue_datei.write(aktualisierter_text)
    
    sätze = teile_in_sätze(aktualisierter_text)
    speichere_als_json('tagebuch_sätze.json', sätze)