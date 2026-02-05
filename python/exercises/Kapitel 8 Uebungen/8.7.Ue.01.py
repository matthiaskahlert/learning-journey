""" 
Erstelle ein Python-Skript, das folgende Aufgaben ausführt:

a) Definiere eine Liste mit Namen einkaufsliste und fülle sie mit mindestens fünf verschiedenen Lebensmitteln (als Strings).

b) Schreibe eine Funktion einkauf_hinzufuegen, die ein neues Lebensmittel zur einkaufsliste hinzufügt. 
Die Funktion soll überprüfen, ob das Lebensmittel bereits in der Liste vorhanden ist. 
Ist dies der Fall, soll eine entsprechende Nachricht ausgegeben werden ("Lebensmittel bereits in der Liste!"), 
andernfalls soll das Lebensmittel hinzugefügt werden.

c) Nutze eine Schleife, um den Benutzer bis zu drei Mal nach neuen Lebensmitteln zu fragen, die zur Liste hinzugefügt werden sollen. 
Verwende die Funktion einkauf_hinzufuegen für jeden Eingabewert.

d) Speichere die endgültige einkaufsliste in einer Datei namens einkaufsliste.txt mithilfe der with-Anweisung und dem write-Modus. 
Achte darauf, jedes Lebensmittel in einer neuen Zeile zu speichern.

e) Fange mögliche Laufzeitfehler ab, die beim Öffnen, Schreiben oder Schließen der Datei auftreten können, 
indem du try und except Blöcke verwendest.

f) Lies die einkaufsliste.txt Datei und gib ihren Inhalt Zeile für Zeile in der Konsole aus. 
Verwende dabei ebenfalls die with-Anweisung und den read-Modus. """
DATEINAME = 'python/exercises/Kapitel 8 Uebungen/einkaufsliste.txt'
# a)
einkaufsliste = ['Milch', 'Brot', 'Wurst', 'Käse', 'Kaffee']

# b)
def einkauf_hinzufuegen(lebensmittel):
    """
    Fügt ein Lebensmittel zur Einkaufsliste hinzu.
    Prüft vorher, ob es bereits vorhanden ist.
    
    Args:
        lebensmittel (str): Das hinzuzufügende Lebensmittel
    """
    if lebensmittel in einkaufsliste:
        print(f"{lebensmittel} ist bereits in der Liste.")
    else:
        einkaufsliste.append(lebensmittel)
        print(f"{lebensmittel} wurde der Liste hinzugefügt.")

# c) Benutzer bis zu 3x nach neuen Lebensmitteln fragen
print("=" * 60)
print("EINKAUFSLISTEN-VERWALTUNG")
print("=" * 60)
print(f"\nAktuelle Einkaufsliste: {', '.join(einkaufsliste)}")
print("\nSie können bis zu 3 neue Lebensmittel hinzufügen.")
print("(Drücken Sie ENTER ohne Eingabe zum vorzeitigen Beenden)\n")
for i in range(3):
    neues_lebensmittel = input(f'{i+1}. Geben sie ein neues Lebensmittel ein (oder drücken sie ENTER zum beenden): ')
    if not neues_lebensmittel:
        print("Eingabe beendet.")
        break
    einkauf_hinzufuegen(neues_lebensmittel)
# d) und e)
try:
    with open(DATEINAME, 'w') as stream:
        for item in einkaufsliste:
            stream.write(f'{item}\n')
            print(f"Einkaufsliste erfolgreich in '{DATEINAME}' gespeichert.\n")
except (IOError):
    print("Fehler beim Speichern der items.")

    # f)
print("=" * 60)
print("GESPEICHERTE EINKAUFSLISTE (aus Datei gelesen):")
print("=" * 60)
try:
    with open(DATEINAME, 'r') as stream:
        for line in stream:
            print(line.strip())
except (IOError):
    print("Fehler beim Lesen der Datei.")

print("=" * 60)
print("Programm beendet.")