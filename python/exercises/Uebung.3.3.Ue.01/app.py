""" a) Benenne die vier Hauptdatentypen in Python und gib für jeden Datentyp ein Beispiel an.

b) Erstelle eine Liste mit mindestens drei verschiedenen Datentypen 
und zeige, wie man den Typ jedes Elements in der Liste bestimmt.

c) Beschreibe, wie man eine Ganzzahl (int) in eine Gleitkommazahl (float) umwandelt und gib ein Beispiel dafür.

d) Erkläre, was ein Tupel ist und vergleiche es kurz mit einer Liste hinsichtlich der Änderbarkeit der Elemente.

e) Schreibe ein kurzes Python-Programm, das eine Zeichenkette (str) und eine Ganzzahl (int) nimmt, die Ganzzahl in eine Zeichenkette umwandelt und beide Zeichenketten zusammenfügt. Kommentiere jede Zeile deines Codes, um das EVA-Prinzip (Eingabe, Verarbeitung, Ausgabe) zu demonstrieren """
# a) Vier Hauptdatentypen in Python mit Beispielen:
# 1. Ganzzahl (int): Beispiel: 42
# 2. Gleitkommazahl (float): Beispiel: 3.14
# 3. Zeichenkette (str): Beispiel: "Hallo, Welt!"
# 4. Boolescher Wert (bool): Beispiel: True
# b) Liste mit verschiedenen Datentypen und Bestimmung des Typs:
# Liste mit int, float, str, bool
daten_liste = [42, 3.14, "Hallo, Welt!", True]
for i in daten_liste:
    # Ausgabe des Typs jedes Elements i
    print(f'Das Element {i} ist vom Typ {type(i)}')
# c) Umwandlung einer Ganzzahl (int) in eine Gleitkommazahl (float):
ganzzahl = 10  # Eine Ganzzahl
gleitkommazahl = float(ganzzahl)  # Umwandlung in float
# Ausgabe
print(f'Die Ganzzahl {ganzzahl} als Gleitkommazahl ist {gleitkommazahl}')
# d) Ein Tupel ist eine Sammlung von Daten, die nicht veränderbar ist.
# Also Tupel nach ihrer Erstellung nicht mehr änderbar, man kann sie aber in eine iste konvertieren um sie zu ändern.
# Tupel werden mit runden Klammern () definiert,
# während Listen mit eckigen Klammern [] definiert werden.
# Listen sind veränderbar, Tupel nicht.

# Beispiel für ein Tupel:
mein_tupel = (1, 2, 3)  # Ein Tupel mit drei Ganzzahlen
# Beispiel für eine Liste:
meine_liste = [1, 2, 3]  # Eine Liste mit drei Ganzzahlen

# e) Kurzes Python-Programm zur Umwandlung und Verkettung:
# Eingabe: String und Zahl
str1 = input('Gib eine Zeichenkette ein: ')
zahl1 = int(input('Gib eine ganze Zahl ein: '))
# Verarbeitung: Umwandlung der Ganzzahl in eine Zeichenkette und konkatenation
zahl_str = str(zahl1)  # Umwandlung der Ganzzahl in eine Zeichenkette
ergebnis = str1 + zahl_str  # Verkettung der beiden Zeichenketten
# Ausgabe: Ergebnis ausgeben
print(f'Das Ergebnis der lautet: {ergebnis}')
