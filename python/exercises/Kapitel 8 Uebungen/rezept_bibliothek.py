from urllib.request import urlopen # import der urlopen funktion
BIB = {
    'r': ('http://www.textfiles.com/food/richbred.txt', 'Rich Bread'),
    'a': ('http://www.textfiles.com/food/arcadian.txt', 'Arcadian Eight Bean Chili'),
    'o': ('http://www.textfiles.com/food/oakwood.txt', 'Oakwood Feed Store Chili')
    } # buchstaben werden den urls zugeordnet

def lesen(url):
    with urlopen(url)as stream: # datei wird heruntergeladen und dem stream zugeordnet
        rohdaten = stream. read()
    text = rohdaten. decode() # aus dem bytestring wird ein string gewonnen
    print()
    print(text)
    print()

def auswahlmenü():
    print('Rezepte')
    print('-' * 20)
    for schlüssel in BIB.keys():
        url, titel = BIB[schlüssel]
        print(schlüssel + ': ' + titel )
    print('e: Ende')

# Hauptprogramm
auswahl = 'x'
while auswahl != 'e':
    auswahlmenü()
    auswahl = input('Auswahl: ')
    if auswahl in BIB.keys():
        url, titel = BIB[auswahl] # aus dem dictionary wird das zum schlüssel zugehörige tupel geholt
        lesen(url)

print('Bis bald')