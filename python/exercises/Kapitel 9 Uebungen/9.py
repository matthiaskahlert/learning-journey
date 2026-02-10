# Unicode Zeichen
# ord(c) liefert zu einem einzelnen Schriftzeichen (String der Länge 1) die Unicode-Nummer als Dezimalzahl

for buchstabe in 'Abend':
    print(ord(buchstabe), end=' ') # 65 98 101 110 100 


print(f'\n{chr(65)}') # A  

print(chr(98)) # b


# Backslash und Anführungszeichen
print("Ein Backslash: \\ und ein \"Zitat\"")
# Ausgabe: Ein Backslash: \ und ein "Zitat"

# Zeilenumbruch
print("Erste Zeile\nZweite Zeile")
# Ausgabe:
# Erste Zeile
# Zweite Zeile

# Unicode-Zeichen mit Hexadezimalzahl
print('Pferd heißt auf Chinesisch \u99ac.')
# Ausgabe: Pferd hei��t auf Chinesisch 馬.
# UnicodeEncodeError: 'charmap' codec can't encode character '\u99ac' in position 27: character maps to <undefined>


# Unicode-Zeichen mit Namen
print('\N{GREEK CAPITAL LETTER DELTA}')
# Ausgabe: Δ


