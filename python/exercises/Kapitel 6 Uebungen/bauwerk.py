# bauwerk.py
from volumen_modul import *
summe = 0
eingabe = input('(Q)uader, (K)uppel, (E)nde:').lower()
while eingabe in ('k', 'q'): # nur diese zeichen erlauben einen weiteren schleifendurchlauf
    if eingabe in 'k':
        h = float(input('Höhe (m): '))
        r = float(input('Radius (m):'))
        n = int(input('Anzahl dieser Kuppeln: '))
        summe += n * kuppel(h, r)
    elif eingabe in 'q':
        l = float(input('Länge (m): '))
        b = float(input('Breite (m): '))
        h = float(input('Höhe (m): '))
        n = int(input('Anzahl dieser Quader: '))
        summe += n * quader(l, b, h)
    eingabe = input('(Q)uader, (K)uppel, (E)nde:').lower()
print('Das Volumen des Gebaudes ist ', round(summe, 2), 'm³ ' )