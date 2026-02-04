# Beispiel 1 mit try...except...finally
try:
    f = open('python/exercises/Kapitel 8 Uebungen/beispiel1.txt', 'w')
    f.write('Hallo Welt!')
except:
    print('Ein Fehler ist aufgetreten.')
finally:
    f.close()
""" 
Datei wird manuell geöffnet
Fehler beim Öffnen oder Schreiben werden abgefangen
finally sorgt dafür, dass die Datei immer geschlossen wird
Mehr Kontrolle, aber auch mehr Fehlerpotenzial
 """

# Beispiel 2 mit with-Anweisung
with open('python/exercises/Kapitel 8 Uebungen/beispiel2.txt', 'w') as f:
    f.write('Hallo Welt')
"""
Datei wird automatisch geöffnet

Datei wird immer geschlossen, auch bei Fehlern

Kein close(), kein finally

Kürzer, sicherer, übersichtlicher
"""


# versuch eine nichtexistente Datei zu öffnen
try:
    stream = open('text.txt', 'r')
    daten = stream.read()
    stream.close()
except:
    print('Fehler!')