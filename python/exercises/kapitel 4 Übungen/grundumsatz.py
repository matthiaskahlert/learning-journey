""" Python 3 K4.0002_3.0
94
• Bei einer if-Anweisung (einseitige Verzweigung) wird ein Anweisungsblock
nur dann ausgeführt, wenn eine bestimmte Bedingung erfüllt ist.
• Eine Bedingung ist ein logischer Ausdruck (boolescher Ausdruck), der
wahr oder falsch sein kann.
• Bei einer if...else-Anweisung (zweiseitige Verzweigung) wird ein
Anweisungsblock ausgeführt, wenn eine Bedingung erfüllt ist (if-Klausel).
Wenn die Bedingung nicht erfüllt ist, wird ein anderer Anweisungsblock
ausgeführt (else-Klausel).
• Für komplexe Fallunterscheidungen verwendet man if...elif...else-
Anweisungen.
• Bei einer bedingten Wiederholung (while-Anweisung) wird ein
Anweisungsblock so lange ausgeführt, wie eine bestimmte Bedingung
erfüllt ist.
• Bei einer Iteration (for-Anweisung) wird eine Kollektion (z.B. eine Liste oder
eine Menge) durchlaufen und für jedes Element der Kollektion ein
Anweisungsblock ausgeführt.
• Mit der Funktion range() können Zahlenfolgen erzeugt werden.
4.7 Übungen
Übung 1: Grundumsatz
Der Grundumsatz ist die Energie, die ein Mensch bei völliger Ruhe innerhalb von
24 Stunden zur Aufrechterhaltung der Körperfunktionen benötigt. Der
Grundumsatz kann näherungsweise nach der Harris-Benedict-Formel
berechnet werden: """

g = input('Geben Sie Ihr Geschlecht ein (m/w): ')
m = float(input('Geben Sie Ihr Gewicht in kg ein: '))
h = float(input('Geben Sie Ihre Größe in cm ein: '))
a = int(input('Geben Sie Ihr Alter in Jahren ein: '))
if g == 'w':
    geschlecht = 'Frau'
    # Frauen (häufig verwendet)
    grundumsatz_frauen = 655.1 + (9.6 * m) + (1.8 * h) - (4.7 * a)
else:
    geschlecht = 'Mann'
    # Männer (korrigiert)
    grundumsatz_maenner = 66.47 + (13.7 * m) + (5.0 * h) - (6.8 * a)


print('Als', geschlecht, 'beträgt Ihr Grundumsatz:')
if g == 'w':
    print(round(grundumsatz_frauen, 2), 'kcal pro Tag')
else:
    print(round(grundumsatz_maenner, 2), 'kcal pro Tag')
