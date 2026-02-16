""" 
a) Verwende das Modul os und json, um ein Verzeichnis namens meine_daten zu erstellen, falls es noch nicht existiert. 
Speichere in diesem Verzeichnis eine Datei namens daten.json, die eine Liste von Wörterbüchern (Dictionaries) enthält. 
Jedes Wörterbuch soll die Schlüssel name, alter und beruf mit entsprechenden Werten für drei fiktive Personen enthalten.

b) Lese die Datei daten.json aus dem Verzeichnis meine_daten und gib die Inhalte auf der Konsole aus. 
Verwende dazu die with-Anweisung und behandele mögliche Ausnahmen mit try und except.

c) Erweitere das Skript um eine Funktion aktualisiere_daten, die einen neuen Eintrag zu der Liste in daten.json hinzufügt. 
Der neue Eintrag soll durch Benutzereingabe über die Konsole gesammelt werden. 
Nutze dafür die Funktion input() für die Schlüssel name, alter, und beruf. 
Speichere die aktualisierten Daten wieder in daten.json. 
 """
import os
import json


#a) Verzeichnis erstellen und Daten speichern

verzeichnis = os.path.join('python', 'exercises', 'Kapitel 10 Uebungen', 'meine_daten')
os.makedirs(verzeichnis, exist_ok=True)
daten = [
    {'name': 'Max Mustermann', 'alter': 30, 'beruf': 'Ingenieur'},
    {'name': 'Erika Musterfrau', 'alter': 25, 'beruf': 'Architektin'},
    {'name': 'John Doe', 'alter': 40, 'beruf': 'Lehrer'}
]
dateipfad = os.path.join(verzeichnis, 'daten.json')
with open(dateipfad, 'w') as datei:
    json.dump(daten, datei, indent=4)


#b) Daten lesen und auf der Konsole ausgeben

try:
    with open(dateipfad, 'r') as datei:
        gelesene_daten = json.load(datei)
        print(gelesene_daten)
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")


#c) Daten aktualisieren

def aktualisiere_daten():
    name = input("Name: ")
    alter = input("Alter: ")
    beruf = input("Beruf: ")
    neuer_eintrag = {'name': name, 'alter': alter, 'beruf': beruf}

    try:
        with open(dateipfad, 'r+') as datei:
            daten = json.load(datei)
            daten.append(neuer_eintrag)
            datei.seek(0)
            json.dump(daten, datei, indent=4)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")
aktualisiere_daten()