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

from re import findall
text = 'Witten 58452 Berlin 10115 Hamburg 20255'
reg = r'\d\d\d\d\d'
gefunden = findall(reg, text)
print(gefunden) # ['58452', '10115', '20255']





# Gib reguläre Ausdrücke an, die zu den folgenden Beispielen passen: 
""" 
1. Positive Gleitkommazahlen als Dezimalbrüche (Python-
Syntax)
- 15.23
0.1234

2. Fünfstellige positive oder negative Zahlen
58454
-38812
Anrede
 - Frau, Herr

3. Kleingeschriebene Wörter, die auf en enden. 
laufen, hören

4. Gleitkommazahlen als Dezimalbrüche (Python-Syntax)
-15.23
0.1234
5. Gleitkommazahlen in Exponentialschreibweise (Python-
Syntax)
-I.23e4
I.2345E-19
6. Inlandstelefonnummern mit Vorwahl nach DINn 5008
(optional ein Leerzeichen nach der Vorwahl und ein Bin-
destrich vor der Durchwahl)
0201 89775
0201 89775
031 78455-53 """

#1, 
reg1 = r'-?\d+\.\d+'
#2,
reg2 = r'-?\d{5}'
#3,
reg3 = r'\b\w+en\b'
#4,
reg4 = r'-?\d+\.\d+'
#5,
reg5 = r'-?\d+\.\d+[eE]-?\d+'
#6,
reg6 = r'\b\d{3,4}\s?-?\d{5,}\b'


# Beispiel für greedy vs. non-greedy matching
text = 'Das ist ein <greedy> Beispiel für <greedy> Matching.'   
reg_greedy = r'<.*>'  # Greedy: Erfasst alles zwischen dem ersten < und dem letzten >
reg_non_greedy = r'<.*?>'  # Non-greedy: Erfasst nur das, was zwischen den ersten < und > liegt
print(findall(reg_greedy, text))  # Ausgabe: ['<greedy> Beispiel für <greedy> Matching.']
print(findall(reg_non_greedy, text))  # Ausgabe: ['<greedy>', '<greedy>']

from re import findall
text = '''<h1>Python</h1>
Python ist eine Programmiersprache. '''
reg = r' <. *>'
gefunden = findall(reg, text)
print(gefunden)

text = '''{gewinner} hat {preis} Euro gewonnen.
Herzlichen Glückwunsch, {gewinner}!'''
print(text.format(preis=1000, gewinner='Tom'))
""" Tom hat 1000 Euro gewonnen.
Herzlichen Glückwunsch, Tom! """


text2 = '{:3} {:6}'
print('='*25)
print('TABELLE DER KUBIKZAHLEN')
print('='*25)
for n in range(5):
    print(text2.format(n, n ** 3))
