# Schreibe ein interaktives Programm, das das Volumen eines Hauses mit
# Satteldach berechnet.
try:
    höhe1 = float(input('Gib die Wandhöhe h1 in m ein: '))
    höhe2 = float(input('Gib die Dachhöhe h2 in m ein: '))
    breite = float(input('Gib die Breite a in m ein: '))
    länge = float(input('Gib die Länge b in m ein: '))
except ValueError:
    print("Fehlerhafte Eingabe: Bitte gültige Zahlen eingeben.")
    exit()  # Programm beenden
if höhe1 <= 0 or höhe2 <= 0 or breite <= 0 or länge <= 0:
    print("Fehlerhafte Eingabe: Alle Maße müssen größer als 0 sein.")
    exit()  # Programm beenden
# Verarbeitung: Berechnung des Volumens
volumen = (höhe1 * breite * länge) + ((höhe2 * breite * länge)/2)
print(f'Das Volumen des Hauses beträgt {volumen} m³.')
