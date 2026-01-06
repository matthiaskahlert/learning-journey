"""
Schreibe ein Programm, das die Ermittlung der Verkehrsdichte an einer Straße
unterstützt. Der Benutzer zählt jedes vorbeikommende Auto, jedes Fahrrad und
jede Person durch Eingabe der Buchstaben f, a und p. Nach einer Minute wird
die Zählung beendet und das Ergebnis ausgegeben. 
"""
import time

def verkehrszaehler(dauer=60):
    verkehr = {'fahrrad':0, 'auto':0, 'person':0}
    beginn = time.time()
    print("Zählen Sie die vorbeikommenden Fahrzeuge und Personen.")
    print("Geben Sie 'f' für Fahrrad, 'a' für Auto und 'p' für Person ein.")
    print(f"Die Zählung endet automatisch nach {dauer} Sekunden")

    while time.time() - beginn < dauer:
        eingabe = input("Eingabe (f/a/p/): ").strip().lower()
        if eingabe == 'f':
            verkehr['fahrrad'] +=1
        elif eingabe == 'a':
            verkehr['auto'] +=1
        elif eingabe == 'p':
            verkehr['person'] +=1
        else:
            print("Ungültige Eingabe.")
    return verkehr

ergebnis = verkehrszaehler(60)

print("\nErgebnis der Verkehrszählung:")
print(f"Autos: {ergebnis['auto']}")
print(f"Fahrräder: {ergebnis['fahrrad']}")
print(f"Personen: {ergebnis['person']}")
