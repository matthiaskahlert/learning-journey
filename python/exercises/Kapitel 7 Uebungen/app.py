t = ('Radiergummi', 0.45)
artikel, preis = t # hier findet das sogenannte unpacking statt
print(artikel) # Radiergummi
print(preis) # 0.45


print(3 * 'Hoch') # HochHochHoch
wort = 'Raumschiff'
print(wort[0:4]) # Raum
print(wort[2:4]) # um
print(max(wort)) # u
zahlen = [1, 2] + [1, 2]
print(zahlen) # [1, 2, 1, 2]
print(zahlen.count(1)) # 2
s=[(1,2),(3,4),(5,6)]
print(s[0]) # (1, 2)
print(s[0] [1]) # 2
print('Quadrat' [0]) # Q
s = [[]]
print(len(s)) # 1


zahlen = [234,6,7,1]
zahlen.sort()
zahlen.reverse()
print(zahlen) # [234, 7, 6, 1]


# List Comprehension
lc1 = [n ** 2 for n in range(10)]
print(lc1) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List Comprehension mit Bedingung
lc2 = [x ** 2 for x in range(20) if (x ** 2) % 2 == 0]
print(lc2) # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

# • Liste von Zahlen zwischen 0 und 100, die durch 4 teilbar sind
lc3 = [x for x in range(101) if x % 4 == 0] # range(n) liefert ein range-Objekt, das eine Zahlenfolge von 0 bis n-1 enthält
print(lc3)

# • Es sei s eine Liste von Wörtern. Gesucht ist die Liste der Anfangsbuchstaben der Wörter in s.
# Für jedes Item der Kollektion kollektion wird einmal der Ausdruck ausdruck
# ausgewertet und das resultierende Objekt der neuen Liste hinzugefügt
s = ['Sambuca', 'Bier', 'Saftschorle', 'Wasser', 'Eierlikör', 'Anfang', 'Anker', 'alt']
lc4 = [wort[0] for wort in s]
print(lc4) # ['S', 'B', 'S', 'W', 'E']

# • Es sei s eine Liste von Wörtern. Gesucht ist die Liste der Wörter, die mit a oder A beginnen.
lc5 = [wort for wort in s if wort.startswith('a') or wort.startswith('A')]
print(lc5) # ['Anfang', 'Anker', 'alt']
