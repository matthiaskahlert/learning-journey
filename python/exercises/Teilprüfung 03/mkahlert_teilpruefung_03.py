""" Entwickle ein Python-Programm, das folgende Funktionalitäten umfasst: 
a) Erstelle eine Funktion, die eine Liste von Namen aus einer Textdatei liest. 
Die Datei soll dabei so strukturiert sein, dass jeder Name in einer neuen Zeile steht. 
Verwende die with-Anweisung und try-except-Blöcke, um Fehler beim Lesen der Datei zu handhaben. 

b) Erweitere das Programm um eine Funktion, die die gelesenen Namen in ein JSON-Format umwandelt 
und in einer neuen Datei speichert. Stelle sicher, dass die Datei korrekt geschlossen wird, 
auch wenn beim Schreiben ein Fehler auftritt. 

c) Implementiere eine Benutzeroberfläche in der Konsole, die dem Benutzer erlaubt, 
zwischen den Funktionen zu wählen und entsprechende Eingaben zu machen. """

import json
TEXT_DATEI = 'namen.txt'
JSON_DATEI = 'namen.json'

def lade_daten():
    """
    Die Funktion liest eine Liste von Namen aus einer Textdatei ein. 
    Sie interpretiert jede Zeile als einen Namen. 
    Fehler beim Lesen der Datei werden durch try-except-Blöcke abgefangen.
    """
    try:
        daten = [] # erstellt eine leere liste die gefüllt werden soll
        with open(TEXT_DATEI, 'r',encoding='utf-8') as datei: # encoding für umlauthandling
            for zeile in datei:
                daten.append(zeile.strip()) # strip entfernt für whitespaceentfernung
    except IOError as e:
        print(f'Fehler beim Lesen der Datei: {e}')
    return daten # gibt die gefüllte liste zurück


def speichere_json(daten):
    """
    Wandelt die Namensliste in das JSON-Format um und speichert sie in einer Datei.
    Die Datei wird durch die with-Anweisung auch bei Fehlern automatisch geschlossen.
    """
    try:
        with open(JSON_DATEI, 'w', encoding='utf-8') as datei:
            json_daten = {
                "namen": daten
            }
            json.dump(json_daten, datei, indent=4, ensure_ascii=False) # einrückung um vier zeichen & kein unicode escape character im json falls umlaute in den namen vorhanden sind
            print(f'Daten erfolgreich im JSON-Format gespeichert in {JSON_DATEI}.')
    except IOError as e:
        print(f'Fehler beim Speichern der Daten: {e}')


def zeige_namen(daten):
    """
    Zeigt alle Namen aus der Liste an.
    """
    if not daten:
        print('Keine Namen vorhanden. Bitte erst Namen aus Textdatei laden!')
        return
    
    print('\n' + '='*50)
    print(f'GESPEICHERTE NAMEN (Anzahl: {len(daten)})')
    print('='*50)
    i = 1 
    for name in daten:
        print(f"{i}. {name}")
        i += 1
    print('='*50)


def hauptmenü():
    """
    Benutzeroberfläche zur Verwaltung von Namen
    """
    namen_liste = []
    
    while True:
        print('\n' + '='*50)
        print('BENUTZEROBERFLÄCHE - NAMENSVERWALTUNG')
        print('1. Namen aus Textdatei laden')
        print('2. Geladene Namen anzeigen')
        print('3. Namen als JSON speichern')
        print('4. Programm beenden')
        print('\n' + '='*50)
        
        wahl = input('Wähle eine Option (1-4): ')
        
        if wahl == '1':
            namen_liste = lade_daten()
            if namen_liste:
                print('Namen erfolgreich geladen!')
            else:
                print('Keine Namen geladen (Datei leer oder nicht vorhanden).')
            
        elif wahl == '2':
            zeige_namen(namen_liste)
            
        elif wahl == '3':
            if namen_liste:
                print('Namen wurden als JSON gespeichert!')
                speichere_json(namen_liste)
            else:
                print('Fehler: Keine Namen geladen. Bitte zuerst Option 1 wählen!')
                
        elif wahl == '4':
            print('Auf Wiedersehen!')
            print('Programm beendet.')
            print('='*50)
            break
            
        else:
            print('Ungültige Auswahl. Bitte nochmal versuchen.')



if __name__ == "__main__": # sorgt für ausführung per script aber nicht bei modulimport. dort wird der modulname gesetzt und der if block übersprungen
    TESTS_AKTIV = False # Setze auf True, um die automatischen Tests auszuführen
    if TESTS_AKTIV:
            print('========================= AUTOMATISCHE TESTS =========================\n')
            # OPTIONALE TESTDURCHLÄUFE
            # Test 1: namen aus textdatei laden
            print('Test 1: Lade Namen aus Textdatei')
            test_namen = lade_daten()
            
            # Test 2: geladene namen anzeigen
            print('Test 2: Zeige geladene Namen an')
            zeige_namen(test_namen)
            
            # Test 3: namen als JSON speichern
            if test_namen:
                print('Test 3: Speichere Namen als JSON')
                speichere_json(test_namen)
            else:
                print('Test 3: Übersprungen - Keine Namen zum Speichern vorhanden.')
                print('Die Datei "namen.txt" fehlt oder ist leer.')
            
            # teste menüstart
            print('\n' + '='*70)
            antwort = input('Interaktives Menü starten? (j/n): ').lower()
            if antwort == 'j':
                hauptmenü()
    else:
        hauptmenü()