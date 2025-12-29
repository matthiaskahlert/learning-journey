TEL = [('Mathias', '0201 461487'), # Konstante in Uppercase
('Bea', '0201 334100'),
('Marius', '0177 3543488')]

MENÜ = '''
(T)elefonnummer suchen
(N)ame suchen
(E)nde'''

def suche_nummern(suchwort):
    for name, nummer in TEL:
        if suchwort in name:
            print(name, nummer)

def suche_namen(ziffern):
    for name, nummer in TEL:
        if ziffern in nummer:
            print(name, nummer)

print(MENÜ)
eingabe = input('Auswahl (t, n, e): ')

while eingabe != 'e':
    if eingabe == 'n':
        suchwort = input('Suchwort: ')
        suche_nummern(suchwort)
    elif eingabe == 't':
        ziffern = input('Ziffern: ')
        suche_namen(ziffern)
    print(MENÜ)
    eingabe = input('Auswahl (t, n, e): ')

print('Bis bald!')