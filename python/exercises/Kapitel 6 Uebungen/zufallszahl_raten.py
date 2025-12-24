import random

# Zufallszahl generieren
zufall = random.randint(1, 100)  # 1 bis 100 inklusiv
# print(f"Die erzeugte Zahl ist {zufall}")  # Kontrolle als Test

input_str = input(
    "Bitte gib eine Zahl zwischen 1 und 100 ein oder 'exit', um das Spiel zu beenden: "
)

while input_str.lower() != "exit":
    try:
        geratene_zahl = int(input_str)  # für den Zahlenvergleich
    except ValueError:
        print("Ungültige Eingabe! Bitte eine Zahl eingeben oder 'exit' zum Beenden.")
        input_str = input("Neue Eingabe: ")
        continue

    if geratene_zahl == zufall:
        print(f"Herzlichen Glückwunsch, du hast richtig geraten! "
              f"Deine Eingabe {geratene_zahl} entspricht der generierten Zahl {zufall}!\n"
              "Ich hoffe es hat Spaß gemacht, vielen Dank für das Spiel!")
        break
    elif geratene_zahl > zufall:
        print(f"Deine Eingabe {geratene_zahl} ist zu hoch!")
    else:
        print(f"Deine Eingabe {geratene_zahl} ist zu niedrig!")

    input_str = input("Neue Eingabe oder 'exit' zum Beenden: ")

if input_str.lower() == "exit":
    print("Du hast 'exit' eingegeben. Ich hoffe es hat Spaß gemacht, vielen Dank für das Spiel!")
