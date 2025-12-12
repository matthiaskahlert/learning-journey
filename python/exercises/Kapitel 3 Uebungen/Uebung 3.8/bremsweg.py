# Das Programm fragt nach Geschwindigkeit und
# Bremsverzögerung und berechnet den Bremsweg.
# Autor:mkahlert
# Letzte Änderung:10.12.25


# Eingabe: Geschwindigkeit und Bremsverzögerung
print('Berechnung des Bremswegs')
try:
    geschwindigkeit = float(input('Gib die Geschwindigkeit in m/s ein :'))
except ValueError:
    print("Fehlerhafte Eingabe: Bitte eine Zahl für die Geschwindigkeit eingeben.")
    exit()  # Programm beenden

verzoegerung = input(
    'Ist es nass oder trocken auf dem Asphalt (n/t)? :').lower()
if verzoegerung not in ['n', 't']:
    print("Fehlerhafte Eingabe: Bitte 'n' für nass oder 't' für trocken eingeben.")
    exit()  # Programm beenden

geschwindigkeit_kmh = geschwindigkeit * 3.6

print(
    f"""Du hast angegeben es ist {'nass' if verzoegerung == 'n' else 'trocken'} auf dem Asphalt.
    Deine Geschwindigkeit von {geschwindigkeit} m/s entspricht  {geschwindigkeit_kmh} km/h."""
)
print('Die Bremsverzögerung ist auf trockenem Asphalt 8 m/s² und auf nassem Asphalt 7 m/s²')


# Verarbeitung: Berechnung des Bremsweges
if verzoegerung == 'n':
    bremsweg = geschwindigkeit ** 2 / (2*7)
else:
    bremsweg = geschwindigkeit ** 2 / (2*8)

# Ausgabe: Berechneten Bremsweg ausgeben auf zwei Nachkommastellen gerundet
bremsweg = round(bremsweg, 2)
print(f'Der Bremsweg beträgt demnach {bremsweg} Meter.')
