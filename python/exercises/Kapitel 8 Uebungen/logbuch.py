from time import asctime
PFAD = 'python/exercises/Kapitel 8 Uebungen/log.txt'
MENUE = '''
n: Neuer Eintrag
l: Logbuch lesen
e: Ende
'''

def eintragen():
    with open(PFAD, 'a') as logbuch: # a → Anhängen (schreibt am Dateiende)
        eintrag = asctime() + ' '
        eintrag += input('Neuer Eintrag: ')
        logbuch.write(eintrag + '\n')

def lesen ():
    with open(PFAD, 'r') as logbuch: # r → Lesen (Text, Standard)
        text = logbuch.read()
    print(text)

auswahl = 'x'
while auswahl != 'e':
    print(MENUE)
    auswahl = input('Auswahl: ')
    if auswahl == 'n':
        eintragen()
    elif auswahl == 'l':
        lesen()
print('Auf Wiedersehen!')
input()