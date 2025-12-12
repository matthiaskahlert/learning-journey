""" Entwickle ein Python-Skript, das folgende Funktionen ausführt:

a) Frage den Benutzer nach seiner aktuellen Stimmung (z.B. "glücklich", "traurig", "müde"). 
Speichere die Eingabe in einer Variablen.

b) Überprüfe die Eingabe des Benutzers. 
Wenn der Benutzer "glücklich" eingibt, soll das Programm ausgeben: 
"Es ist toll zu hören, dass du glücklich bist!". 
Wenn der Benutzer "traurig" eingibt, soll das Programm ausgeben: 
"Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht dir bald besser!". 
Bei der Eingabe von "müde" soll das Programm ausgeben: 
"Vielleicht solltest du dich etwas ausruhen. Ruhe ist wichtig.". 
Für alle anderen Eingaben soll das Programm ausgeben: 
"Interessant! Ich weiß nicht viel über diese Stimmung."

c) Füge einen Kommentar über jede Kontrollstruktur hinzu, um zu erklären, was sie tut.

d) Verwende eine while-Schleife, um den Benutzer zu fragen, ob er das Programm beenden möchte ("Ja" oder "Nein"). 
Wenn der Benutzer "Nein" eingibt, wiederhole die Schritte a) bis c).  """

print("Willkommen zum mood-check!")
# Frage den Benutzer nach seiner aktuellen Stimmung
while True:
    mood = input(
        "Wie ist deine Stimmung? (glücklich, traurig, müde): ").lower()
    if mood == "glücklich":
        # Ausgabe für glücklich
        print("Es ist toll zu hören, dass du glücklich bist!")

    elif mood == "traurig":
        # Ausgabe für traurig
        print("Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht dir bald besser!")

    elif mood == "müde":
        # Ausgabe für müde
        print("Vielleicht solltest du dich etwas ausruhen. Ruhe ist wichtig.")

    else:
        # Ausgabe für alle anderen Stimmungen
        print("Interessant! Ich weiß nicht viel über diese Stimmung.")
    # Frage den Benutzer, ob er das Programm beenden möchte
    beenden = input(
        "Möchtest du das Programm beenden (Ja oder Nein): ").lower()
    if beenden == "ja":
        print("Auf Wiedersehen!")
        break  # Beende die Schleife und das Programm
    elif beenden == "nein":
        continue  # Wiederhole die Schleife
    else:
        print("Ungültige Eingabe. Das Programm wird beendet.")
        break  # Beende die Schleife und das Programm bei ungültiger Eingabe
