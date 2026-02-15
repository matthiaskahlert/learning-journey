"""
Entwickle ein Python-Programm, das eine Textdatei mit Kundenfeedback aus verschiedenen Ländern analysiert.

Das Programm soll folgende Funktionen umfassen:
a) Lese die Textdatei feedback.txt mit der with-Anweisung
b) Extrahiere alle Datumsangaben im Format DD.MM.YYYY mit regulären Ausdrücken
c) Zähle die Datumsvorkommen und speichere sie in einem Dictionary
d) Identifiziere alle Kommentare mit dem Wort "exzellent" (case-insensitive)
e) Speichere die Ergebnisse in JSON-Dateien
f) Implementiere Fehlerbehandlung mit try-except
g) Verwende Unicode-Emojis für Erfolgsausgaben
h) Teste das Programm mit der erstellten Textdatei
"""

import re
import json

# Konstanten für Dateinamen
FEEDBACK_DATEI = 'feedback.txt'
DATUMS_JSON = 'datums_vorkommen.json'
EXZELLENTE_JSON = 'exzellente_feedbacks.json'


def lese_feedback():
    """
    Liest die Feedback-Datei und gibt den Inhalt zurück.
    Verwendet die with-Anweisung für sicheres Dateihandling.
    """
    try:
        with open(FEEDBACK_DATEI, 'r', encoding='utf-8') as datei:
            inhalt = datei.read()
            print(f'\u2713 Feedback-Datei erfolgreich gelesen! \U0001F4C4')
            return inhalt
    except FileNotFoundError:
        print(f'\u274C Fehler: Die Datei {FEEDBACK_DATEI} wurde nicht gefunden.')
        return None
    except IOError as e:
        print(f'\u274C Fehler beim Lesen der Datei: {e}')
        return None


def extrahiere_datumsangaben(text):
    """
    Extrahiert alle Datumsangaben im Format DD.MM.YYYY aus dem Text.
    Verwendet reguläre Ausdrücke für die Mustererkennung.
    """
    try:
        # Regulärer Ausdruck für das Format DD.MM.YYYY
        datum_muster = r'\b(\d{2}\.\d{2}\.\d{4})\b'
        datumsangaben = re.findall(datum_muster, text)
        print(f'\u2713 {len(datumsangaben)} Datumsangaben gefunden! \U0001F4C5')
        return datumsangaben
    except Exception as e:
        print(f'\u274C Fehler beim Extrahieren der Datumsangaben: {e}')
        return []


def zaehle_datumsvorkommen(datumsangaben):
    """
    Zählt, wie oft jedes Datum vorkommt.
    Gibt ein Dictionary zurück mit Datum als Schlüssel und Anzahl als Wert.
    """
    try:
        datums_dict = {}
        for datum in datumsangaben:
            if datum in datums_dict:
                datums_dict[datum] += 1
            else:
                datums_dict[datum] = 1
        print(f'\u2713 Datumsvorkommen gezählt! \U0001F522')
        return datums_dict
    except Exception as e:
        print(f'\u274C Fehler beim Zählen der Datumsvorkommen: {e}')
        return {}


def finde_exzellente_kommentare(text):
    """
    Findet alle Kommentare, die das Wort "exzellent" enthalten (case-insensitive).
    Gibt eine Liste der Kommentare zurück.
    """
    try:
        kommentare = []
        # Teilt den Text in Zeilen auf
        zeilen = text.split('\n')
        
        # Durchsucht jede Zeile nach "exzellent" (case-insensitive)
        for zeile in zeilen:
            if re.search(r'\bexzellent\b', zeile, re.IGNORECASE):
                kommentare.append(zeile.strip())
        
        print(f'\u2713 {len(kommentare)} exzellente Kommentare gefunden! \u2B50')
        return kommentare
    except Exception as e:
        print(f'\u274C Fehler beim Suchen nach exzellenten Kommentaren: {e}')
        return []


def speichere_json(daten, dateiname):
    """
    Speichert die übergebenen Daten in einer JSON-Datei.
    Verwendet die with-Anweisung für sicheres Dateihandling.
    """
    try:
        with open(dateiname, 'w', encoding='utf-8') as datei:
            json.dump(daten, datei, indent=4, ensure_ascii=False)
            print(f'\u2713 Daten erfolgreich in {dateiname} gespeichert! \U0001F4BE')
    except IOError as e:
        print(f'\u274C Fehler beim Speichern der Datei {dateiname}: {e}')
    except Exception as e:
        print(f'\u274C Unerwarteter Fehler beim Speichern: {e}')


def hauptprogramm():
    """
    Hauptfunktion, die alle Schritte koordiniert.
    """
    print('\n' + '='*60)
    print('KUNDENFEEDBACK-ANALYSE \U0001F50D')
    print('='*60 + '\n')
    
    # Schritt 1: Feedback-Datei lesen
    print('Schritt 1: Lese Feedback-Datei...')
    feedback_text = lese_feedback()
    
    if feedback_text is None:
        print('\u274C Programm wird beendet.')
        return
    
    # Schritt 2: Datumsangaben extrahieren
    print('\nSchritt 2: Extrahiere Datumsangaben...')
    datumsangaben = extrahiere_datumsangaben(feedback_text)
    
    # Schritt 3: Datumsvorkommen zählen
    print('\nSchritt 3: Zähle Datumsvorkommen...')
    datums_vorkommen = zaehle_datumsvorkommen(datumsangaben)
    
    # Schritt 4: Exzellente Kommentare finden
    print('\nSchritt 4: Suche exzellente Kommentare...')
    exzellente_feedbacks = finde_exzellente_kommentare(feedback_text)
    
    # Schritt 5: Ergebnisse in JSON-Dateien speichern
    print('\nSchritt 5: Speichere Ergebnisse...')
    speichere_json(datums_vorkommen, DATUMS_JSON)
    speichere_json(exzellente_feedbacks, EXZELLENTE_JSON)
    
    # Zusammenfassung anzeigen
    print('\n' + '='*60)
    print('ZUSAMMENFASSUNG \U0001F4CA')
    print('='*60)
    print(f'Gefundene Datumsangaben: {len(datumsangaben)}')
    print(f'Einzigartige Daten: {len(datums_vorkommen)}')
    print(f'Exzellente Kommentare: {len(exzellente_feedbacks)}')
    print('\n\U0001F389 Analyse erfolgreich abgeschlossen! \U0001F389')
    print('='*60 + '\n')


if __name__ == "__main__":
    hauptprogramm()
