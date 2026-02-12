""" Entwickle ein Python-Programm, das eine Textdatei mit einer Liste von Produkten und deren Preisen verarbeitet. 
Die Datei soll in folgendem Format vorliegen:

Produkt,Preis
Milch,1.29
Brot,2.49
Äpfel,3.19

a) Lese die Datei ein und speichere die Daten in einer geeigneten Datenstruktur. 
Verwende dabei die with-Anweisung und stelle sicher, dass Fehler beim Lesen der Datei ordnungsgemäß 
behandelt werden.
b) Füge eine Funktion hinzu, die die Mehrwertsteuer für jedes Produkt berechnet. 
Die Mehrwertsteuer beträgt 19%. Speichere die Ergebnisse in einer neuen Datenstruktur, 
die sowohl den Originalpreis als auch den Preis inklusive Mehrwertsteuer enthält.
c) Erweitere das Programm, sodass es eine neue Datei erstellt, die neben dem Produktnamen 
und dem Originalpreis auch den Preis inklusive Mehrwertsteuer enthält. 
Das Format soll wie folgt sein:

Produkt,Preis,MwSt
Milch,1.29,1.54
Brot,2.49,2.96
Äpfel,3.19,3.80

d) Implementiere eine Fehlerbehandlung für den Fall, dass die Eingabedatei Produkte 
mit ungültigen Preisen enthält (z.B. nicht-numerische Werte). 
In solchen Fällen soll eine Warnmeldung ausgegeben und das betroffene Produkt übersprungen werden.
e) Verwende reguläre Ausdrücke, um zu überprüfen, ob die Produktbezeichnungen gültig sind 
(bestehend aus Buchstaben, Zahlen und ggf. Leerzeichen). 
Ungültige Produktbezeichnungen sollen ähnlich wie bei d) behandelt werden. """


# --- Import für Regex ---
import re

# --- Funktion zur Berechnung der Mehrwertsteuer ---
def berechne_mwst(preis):
    return round(preis * 1.19, 2)

# --- Funktion zur Preisprüfung ---
def ist_gueltiger_preis(preis):
    try:
        float(preis)
        return True
    except ValueError:
        return False

# --- Funktion zur Namensprüfung (Regex) ---
def ist_gueltiger_name(name):
    return bool(re.match(r'^[\w\s]+$', name))

# --- Einlesen, Prüfen und Verarbeiten der Datei ---
produkte = []
try:
    with open('python/exercises/Kapitel 9 Uebungen/produktliste.txt', 'r', encoding='utf-8') as file:
        header = next(file)  # Überspringe Kopfzeile
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 2:
                print(f"Warnung: Ungültige Zeile übersprungen: {line.strip()}")
                continue
            produkt, preis_str = parts
            if not ist_gueltiger_preis(preis_str):
                print(f"Warnung: Ungültiger Preis für {produkt}. Überspringe Produkt.")
                continue
            if not ist_gueltiger_name(produkt):
                print(f"Warnung: Ungültiger Produktname '{produkt}'. Überspringe Produkt.")
                continue
            preis = float(preis_str)
            produkte.append((produkt, preis, berechne_mwst(preis)))

    # Schreibe neue Datei mit MwSt
    with open('python/exercises/Kapitel 9 Uebungen/produkte_mit_mwst.txt', 'w', encoding='utf-8') as file:
        file.write('Produkt,Preis,MwSt\n')
        for produkt in produkte:
            file.write(f"{produkt[0]},{produkt[1]:.2f},{produkt[2]:.2f}\n")


except IOError:
    print("Fehler beim Lesen oder Schreiben der Datei.")

# Ausgabe der eingelesenen und verarbeiteten Produkte (optional)
print("Produktliste:", produkte)


