# a)
t1 = [
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('d', 4),
    ('e', 5)
]

print("tuple:", t1)
# b) Schreibe eine Funktion, die prüft, ob ein bestimmtes Element
# (Tupel aus Buchstabe und Zahl) in der Liste vorhanden ist.
# Gib eine entsprechende Nachricht aus, z.B. "Element gefunden: (Buchstabe, Zahl)"
# oder "Element nicht gefunden".


def pruefung_element_vorhanden(element):
    return element in t1  # gibt true oder false zurück


def element_suchen():
    user_input = input(
        "Geben Sie ein Element ein (Format: buchstabe,zahl): ").lower()
    teile = user_input.split(",")  # trennt am Komma

    try:
        # teile[0] ist string, teile[1] in int umwandeln strip entfernt leerzeichen
        element = (teile[0].strip(), int(teile[1].strip()))
    except (IndexError, ValueError):
        print("Ungültiges Format. Bitte im Format buchstabe,zahl eingeben.")
        return

    if pruefung_element_vorhanden(element):  # ruft die funktion auf
        print("Element gefunden:", element)  # ausgabe wenn gefunden
    else:
        # ausgabe wenn nicht gefunden
        print("Element nicht gefunden:", element)


def zahl_eingeben_und_pruefen():

    # c)

    gegebene_zeichenkette = input("geben sie eine Zahl ein")
    print("Gegebene Zeichenkette:", gegebene_zeichenkette,
          type(gegebene_zeichenkette))  # gegebene_zeichenkette <class 'str'>
    zahl = int(gegebene_zeichenkette)
    # gegebene_zeichenkette <class 'int'>
    print("Konvertierte Ganzzahl:", zahl, type(zahl))

    # f) Füge eine Kontrollstruktur hinzu, die prüft, ob die umgewandelte Zahl positiv, negativ oder Null ist, und gib eine entsprechende Nachricht aus.
    if zahl > 0:
        print("Die Zahl ist positiv.")
    elif zahl < 0:
        print("Die Zahl ist negativ.")
    else:
        print("Die Zahl ist Null.")


"""e) benutzerinterface das die funktionen aufrufen kann also Eine echte Benutzerschnittstelle würde dem Nutzer ermöglichen, wiederholt Aktionen auszuwählen, z.B.:

1. Nach einem Element in der Liste suchen
2. Eine Zeichenkette in eine Zahl umwandeln
3. Programm beenden """

while True:
    print("\nWählen Sie eine Aktion:")
    print("1. Nach einem Element in der Liste suchen")
    print("2. Eine Zeichenkette in eine Zahl umwandeln")
    print("3. Programm beenden")
    auswahl = input("Ihre Wahl (1/2/3): ")

    if auswahl == '1':
        element_suchen()

    elif auswahl == '2':
        zahl_eingeben_und_pruefen()

    elif auswahl == '3':
        print("Programm wird beendet.")
        break

    else:
        print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
