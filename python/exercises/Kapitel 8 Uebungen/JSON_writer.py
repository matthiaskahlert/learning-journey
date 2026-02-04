# writer.py
import json, time
DATEINAME = 'python/exercises/Kapitel 8 Uebungen/messdaten.json'

try:
    with open(DATEINAME) as stream:
        messungen = json.load(stream)
except:
    messungen = []
print('Zum Beenden der Eingabe ENTER drücken.')

eingabe = input('Temperatur in C: ')
while eingabe:
    eintrag = [time.asctime(), round(float(eingabe), 3)]
    messungen. append(eintrag)
    eingabe = input('Temperatur in C: ')

with open(DATEINAME, 'w') as stream:
    json.dump(messungen, stream)
