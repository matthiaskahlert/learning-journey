""" 
Entwickle ein Python-Programm, das eine Textdatei mit Kundenfeedback aus verschiedenen Ländern analysiert. 
Das Programm soll folgende Funktionen umfassen:

a) Lese die Textdatei feedback.txt, die Kundenkommentare in verschiedenen Sprachen enthält. 
Verwende die with-Anweisung und stelle sicher, dass die Datei korrekt geschlossen wird, nachdem sie gelesen wurde.

b) Verwende reguläre Ausdrücke, um alle Datumsangaben im Format DD.MM.YYYY aus dem Text zu extrahieren und speichere diese in einer Liste.

c) Zähle, wie oft jedes Datum vorkommt, und speichere die Ergebnisse in einem Dictionary, 
wobei das Datum der Schlüssel und die Anzahl der Vorkommen der Wert ist.

d) Identifiziere alle Kommentare, die das Wort "exzellent" in beliebiger Groß- oder Kleinschreibung enthalten. 
Speichere diese Kommentare in einer separaten Liste.

e) Nutze das json-Modul, um das Dictionary mit den Datumsvorkommen 
und die Liste der "exzellenten" Kommentare in zwei separaten Dateien (datums_vorkommen.json und exzellente_feedbacks.json) zu speichern.

f) Implementiere eine Fehlerbehandlung mit try und except, 
um elegante Lösungen für mögliche I/O-Fehler und Probleme beim Arbeiten mit Dateien zu bieten.

g) Verwende Unicode-Nummern, um spezielle Zeichen oder Emojis in die Ausgabe einzufügen, die den Erfolg der Operation signalisieren. 

h) Erstelle eine Textdatei entsprechend den obigen Punkten um deinen Code zu testen.
 """




import re
import json
# Konstanten für die Dateinamen
FEEDBACK_DATEI = 'feedback.txt'
DATUMS_JSON = 'datums_vorkommen.json'
EXZELLENTE_JSON = 'exzellente_feedbacks.json'
# a)
def lese_feedback():
    """
    Liest die Feedback-Datei ein und gibt den Inhalt zurück.
    Verwendet die with-Anweisung für sicheres Dateihandling.
    """
    try:
        with open(FEEDBACK_DATEI, 'r', encoding='utf-8') as datei:
            inhalt = datei.read()
            print(f'Feedback-Datei erfolgreich eingelesen.')
            return inhalt
    except FileNotFoundError:
        print(f'Fehler: Die Datei {FEEDBACK_DATEI} wurde nicht gefunden.')
        return None
    except IOError as e:
        print(f'Fehler beim Lesen der Datei: {e}')
        return None
# b)
def extrahiere_datumsangaben(text):
    """
    Extrahiert alle Datumsangaben im Format DD.MM.YYYY aus dem Text.
    Verwendet reguläre Ausdrücke für die Mustererkennung.
    """

    datum_muster = r'\b(\d{2}\.\d{2}\.\d{4})\b'     # Regex für DD.MM.YYYY
    datumsangaben = re.findall(datum_muster, text)
    print(f'{len(datumsangaben)} Datumsangaben gefunden.')
    return datumsangaben
# c)
def zaehle_datumsvorkommen(datumsangaben):
    """
    Zählt, wie oft jedes Datum vorkommt.
    Gibt ein Dictionary zurück mit Datum als Schlüssel und Anzahl als Wert.
    """
    datums_dict = {}
    for datum in datumsangaben:
        if datum in datums_dict:
            datums_dict[datum] += 1
        else:
            datums_dict[datum] = 1
    return datums_dict

def finde_exzellente_kommentare(text):
    """
    Findet alle Kommentare, die das Wort "exzellent" enthalten.
    Gibt eine Liste der Kommentare zurück.
    Fängt auch englischsprachige Kommentare ab.
    """
    kommentare = []
    zeilen = text.split('\n')
    
    # Durchsucht jede Zeile nach "exzellent", unabhängig von Groß- oder Kleinschreibung
    for zeile in zeilen:
        if re.search(r'\b(exzellent\w*|excellent)\b', zeile, re.IGNORECASE): # Fängt auch englischsprachige Bewertungen ab.
            kommentare.append(zeile.strip())
    
    print(f'{len(kommentare)} exzellente Kommentare gefunden.')
    return kommentare

   
def speichere_json(daten, dateiname):
    """
    Speichert die übergebenen Daten in einer JSON-Datei.
    Verwendet die with-Anweisung, damit die Datei korrekt geschlossen wird.
    """
    try:
        with open(dateiname, 'w', encoding='utf-8') as datei:
            json.dump(daten, datei, indent=4, ensure_ascii=False)
            print(f'Daten erfolgreich in {dateiname} gespeichert.')
    except IOError as e:
        print(f'Fehler beim Speichern der Datei {dateiname}: {e}')
    except Exception as e:
        print(f'Unerwarteter Fehler beim Speichern: {e}')



def hauptprogramm():
    """
    Hier werden alle funktionen in der richtigen Reihenfolge aufgerufen, um die Analyse durchzuführen.
    """
    # Feedback-Datei lesen
    feedback_text = lese_feedback()
    if feedback_text is None:
        print('Programm wird beendet. Kein Feedback vorhanden.')
        return
        
    datumsangaben = extrahiere_datumsangaben(feedback_text) # Datumsangaben extrahieren
    datums_vorkommen = zaehle_datumsvorkommen(datumsangaben) # Datumsvorkommen zählen
    exzellente_feedbacks = finde_exzellente_kommentare(feedback_text) # Exzellente Kommentare finden
    speichere_json(datums_vorkommen, DATUMS_JSON) # Ergebnisse in DATUMS_JSON speichern
    speichere_json(exzellente_feedbacks, EXZELLENTE_JSON) # Ergebnisse in EXZELLENTE_JSON speichern
    
    # Zusammenfassung anzeigen
    print(f'Gefundene Datumsangaben: {len(datumsangaben)}')
    print(f'Einzigartige Daten: {len(datums_vorkommen)} mit den folgenden Vorkommen: {datums_vorkommen}')
    print(f'Exzellente Kommentare: {len(exzellente_feedbacks)} mal wurde mit "exzellent" oder "excellent" bewertet.')
    print('\n\U0001F389 Analyse erfolgreich abgeschlossen! \U0001F389')
    print('='*60 + '\n')
if __name__ == "__main__":
    hauptprogramm()