""" Entwickle ein Python-Programm, das als Taschenrechner für einfache mathematische Operationen 
(Addition, Subtraktion, Multiplikation, Division) fungiert. 
Das Programm soll den Benutzer zuerst fragen, welche Operation durchgeführt werden soll. 
Anschließend fragt es nach zwei Zahlen, führt die gewählte Operation mit diesen Zahlen durch 
und gibt das Ergebnis aus. 
Beachte dabei die korrekte Anwendung von Datentypen, 
die Implementierung von Kontrollstrukturen sowie die korrekte Verwendung von Kommentaren im Code. 

a) Fordere den Benutzer auf, eine Operation auszuwählen, 
indem er einen der folgenden Buchstaben eingibt: 
A für Addition, S für Subtraktion, M für Multiplikation, D für Division.

b) Frage den Benutzer nach zwei Zahlen.

c) Führe die ausgewählte Operation mit diesen Zahlen durch und gib das Ergebnis aus.

d) Implementiere eine Fehlerbehandlung für den Fall, dass bei der Division durch Null versucht wird 
oder ein ungültiger Operator eingegeben wird.

e) Verwende Kommentare im Code, um die Logik hinter den einzelnen Schritten zu erklären.  """

while True:
    berechnung = input("Frage: Welche mathematische Operation möchten Sie durchführen?\n"
                       "Addition (A)\n"
                       "Subtraktion (S)\n"
                       "Multiplikation (M)\n"
                       "Division (D)\n"
                       # Sicherstellung, dass uppercase Eingabe erfolgt für if-Anweisungen
                       "Deine Antwort (A, S, M, D): ").upper()
    if berechnung == 'A':
        print("Addition!")
        # korrekte Anwendung von Datentypen durch Typkonvertierung zu float
        zahl1 = float(input("Bitte die erste Zahl eingeben: "))  # Eingabe
        zahl2 = float(input("Bitte die zweite Zahl eingeben: "))
        ergebnis = zahl1 + zahl2  # Verarbeitung
        print("Ergebnis lautet: ", ergebnis)  # Ausgabe
    elif berechnung == 'S':
        print("Subtraktion!")
        zahl1 = float(input("Bitte die erste Zahl eingeben: "))
        zahl2 = float(input("Bitte die zweite Zahl eingeben: "))
        ergebnis = zahl1 - zahl2
        print("Ergebnis lautet: ", ergebnis)
    elif berechnung == 'M':
        print("Multiplikation!")
        zahl1 = float(input("Bitte die erste Zahl eingeben: "))
        zahl2 = float(input("Bitte die zweite Zahl eingeben: "))
        ergebnis = zahl1 * zahl2
        print("Ergebnis lautet: ", ergebnis)
    elif berechnung == 'D':
        print("Division!")
        zahl1 = float(input("Bitte die erste Zahl eingeben: "))
        zahl2 = float(input("Bitte die zweite Zahl eingeben: "))
        # Kontrollstruktur zur Fehlerbehandlung bei Division durch Null
        if zahl2 == 0:
            print("Teilen durch null ist nicht erlaubt.")
        else:
            ergebnis = zahl1/zahl2
            print("Ergebnis lautet: ", ergebnis)
    else:
        # Kontrollstruktur zur Fehlerbehandlung bei ungültiger Operatoreneingabe
        print("Ungültiger Operator. Bitte einen der folgenden Operatoren eingeben: (A, S, M, D)")
        continue
    # Frage, ob das Programm beendet werden soll
    beenden = input("Möchten Sie das Programm beenden? (ja/nein): ").lower()
    if beenden == "ja":
        print("Auf Wiedersehen!")
        break
    elif beenden == "nein":
        continue
    else:
        print("Ungültige Eingabe. Das Programm wird beendet.")
        break
