""" Aufgabe:  Fehler finden
a) Schreibe ein Python-Skript, das eine Liste von Ganzzahlen definiert 
und die Summe sowie den Durchschnitt dieser Zahlen berechnet. Kommentiere jeden Schritt deines Skripts, um zu erklären, was gemacht wird.

b) Erstelle ein Python-Skript, das eine Zeichenkette (String) von einem Benutzer einliest 
und anschließend prüft, ob es sich um eine Ganzzahl (int) oder eine Gleitkommazahl (float) handelt. 
Gib das Ergebnis aus und erkläre den Prozess in Kommentaren.

c) Definiere ein Python-Skript, das ein einfaches Beispiel für das EVA-Prinzip demonstriert: 
Es soll vom Benutzer zwei Zahlen einlesen (Eingabe), diese multiplizieren (Verarbeitung) 
und das Ergebnis ausgeben (Ausgabe). Kommentiere jeden Schritt im Skript.

d) Finde und korrigiere die Fehler im folgenden Python-Skript. Kommentiere, was falsch war und wie du es behoben hast. 

print("Willkommen zum Fehlerfindungs-Quiz!")
zahl1 = input("Bitte gib eine Zahl ein: ")
zahl2 = input("Bitte gib eine andere Zahl ein: ")
ergebnis = zahl1 + zahl2
print("Das Ergebnis der Addition ist: ", ergebnis) """

# a)
liste = [5, 10, 15, 20, 25, 30]  # Definieren einer Liste von Ganzzahlen
summe = sum(liste)  # Berechnung der Summe der Zahlen in der Liste
durchschnitt = summe / len(liste)  # Berechnung des Durchschnitts der Zahlen
# Ausgabe der Summe und des Durchschnitts
print(f'Summe: {summe}, Durchschnitt: {durchschnitt}')

# b)
eingabe = input('Gib eine Zahl ein: ')  # Einlesen der Eingabe vom Benutzer.
# input() liefert immer einen String.
try:
    # wenn Wert nicht in den erwarteten Typ konvertiert dann error
    wert_int = int(eingabe)
    # Ausgabe, wenn es eine Ganzzahl ist
    print(f'Die Eingabe ist eine Ganzzahl: {wert_int}')
except ValueError:
    # wenn error bei konvertierung, prüfe float
    try:
        # wenn Wert nicht in den erwarteten Typ konvertiert dann error
        wert_float = float(eingabe)
        # Ausgabe, wenn es eine Gleitkommazahl ist
        print(f'Die Eingabe ist eine Gleitkommazahl: {wert_float}')
    except ValueError:
        # Ausgabe, wenn es weder noch ist
        print('Die Eingabe ist weder eine Ganzzahl noch eine Gleitkommazahl.')
# c)
# Eingabe: Zwei Zahlen vom Benutzer einlesen
zahl1 = float(input("Bitte die erste Zahl eingeben: "))
zahl2 = float(input("Bitte die zweite Zahl eingeben: "))
# Verarbeitung: Multiplikation der beiden Zahlen
ergebnis = zahl1 * zahl2
# Ausgabe: Ergebnis der Multiplikation ausgeben
print("Das Ergebnis der Multiplikation ist: ", ergebnis)

# d)
# die eingaben sind strings, müssen in int umgewandelt werden
print("Willkommen zum gefixten-Quiz!")
zahl1 = int(input("Bitte gib eine Zahl ein: "))
zahl2 = int(input("Bitte gib eine andere Zahl ein: "))
ergebnis = zahl1 + zahl2
print("Das Ergebnis der Addition ist: ", ergebnis)
