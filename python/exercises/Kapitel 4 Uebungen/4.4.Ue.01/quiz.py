""" Entwickle ein Python-Programm, das die Rolle eines einfachen Quizspiels übernimmt. 
Das Spiel soll aus drei Fragen bestehen, die nacheinander gestellt werden. 
Für jede Frage gibt es drei Antwortmöglichkeiten (a, b, c), von denen genau eine richtig ist. 
Nachdem der Spieler alle Fragen beantwortet hat, soll das Programm die Anzahl der richtig 
beantworteten Fragen ausgeben und eine Rückmeldung geben. 
Verwende für jede Frage eine if-elif-else-Struktur, um zu überprüfen, 
ob die Antwort des Spielers richtig oder falsch ist. 
Nutze zudem eine while-Schleife, um sicherzustellen, dass das Spiel nur fortgesetzt wird, 
wenn der Spieler eine gültige Antwort (a, b, oder c) eingegeben hat. 
Wenn eine ungültige Eingabe erfolgt, soll der Spieler erneut zur Eingabe aufgefordert werden, 
bis eine gültige Antwort gegeben wird. """

print("Willkommen zum Quizspiel!")
punkte = 0
# Frage 1
while True:
    antwort1 = input("Frage 1: Welche Figur ist das Maskottchen von SEGA?\n"
                     "a) Sonic the Hedgehog\n"
                     "b) Mario\n"
                     "c) Link\n"
                     "Deine Antwort (a, b, c): ").lower()
    if antwort1 == 'a':
        print("Richtig!")
        punkte += 1
        break
    elif antwort1 in ['b', 'c']:
        print("Falsch! Die richtige Antwort ist a) Sonic the Hedgehog.")
        break
    else:
        print("Ungültige Eingabe. Bitte wähle a, b oder c.")
# Frage 2
while True:
    antwort2 = input("Frage 2: Wie heißt die Kreatur, die in Minecraft explodiert, wenn sie dem Spieler zu nahe kommt?\n"
                     "a) Ghast\n"
                     "b) Creeper\n"
                     "c) Enderman\n"
                     "Deine Antwort (a, b, c): ").lower()
    if antwort2 == 'b':
        print("Richtig!")
        punkte += 1
        break
    elif antwort2 in ['a', 'c']:
        print("Falsch! Die richtige Antwort ist b) Creeper.")
        break
    else:
        print("Ungültige Eingabe. Bitte wähle a, b oder c.")
# Frage 3
while True:
    antwort3 = input("Frage 3: In welchem Spiel kommt die Figur „Geralt von Riva“ vor?\n"
                     "a) God of War\n"
                     "b) Dune Awakening\n"
                     "c) The Witcher\n"
                     "Deine Antwort (a, b, c): ").lower()
    if antwort3 == 'c':
        print("Richtig!")
        punkte += 1
        break
    elif antwort3 in ['a', 'b']:
        print("Falsch! Die richtige Antwort ist c) The Witcher.")
        break
    else:
        print("Ungültige Eingabe. Bitte wähle a, b oder c.")

# Endauswertung
print(f"\nDu hast {punkte} von 3 Punkten erreicht!")
