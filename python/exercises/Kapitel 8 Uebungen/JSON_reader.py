import json, time
DATEINAME = 'python/exercises/Kapitel 8 Uebungen/messdaten.json'

try:
    with open(DATEINAME) as stream:
        messungen = json.load(stream)
except:
    print('Fehler')
for datum, messwert in messungen:
    print(datum, 'Temperatur: ', messwert, 'C')
