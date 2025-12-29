print("Hallo Welt")
print(2+2)

# Python Grundtypen kompakt

# Integer (ganze Zahl)
i = 42          # Dezimal
b = 0b1010      # Binär → 10
h = 0x1f        # Hex → 31
o = 0o21        # Oktal → 17

# Float (Gleitkommazahl)
f1 = 3.14
f2 = 2e3        # 2000.0

# Complex (komplexe Zahl)
c = 2 + 3j

# String (Zeichenkette)
s = "Python"

# Tuple (unveränderbar)
t = (1, 'a', 3.14)

# List (veränderbar)
l = [1, 2, 3]
l[0] = 10       # ändern erlaubt

# Set (ungeordnet, keine Duplikate)
st = {1, 2, 3}
st.add(4)

# Dictionary (Schlüssel: Wert)
d = {'A': 65, 'B': 66}
d['C'] = 67     # hinzufügen erlaubt

# Bool (Wahrheitswert)
b1 = True
b2 = False
b3 = bool([])   # False, leere Liste → False

# NoneType
n = None        # kein Wert, bool(None) → False

# Ausgabe aller Typen
print("int:", i, b, h, o)
print("float:", f1, f2)
print("complex:", c)
print("str:", s)
print("tuple:", t)
print("list:", l)
print("set:", st)
print("dict:", d)
print("bool:", b1, b2, b3)
print("NoneType:", n)


xyz = 1
s = [('a', 1), ('b', 2)]
print(len(s))  # 2
print(s[0])  # ('a', 1) - Erstes element der Liste
print(s[0][0])  # a - erstes Element von s[0]
print(len([]))  # 0 - leere Liste keine Elemente
print('Tag ' + str(1))  # Tag 1 - string + string
stadt = 'Dortmund'
print(stadt[0] + stadt[1])  # Do  - erstes und zweites Element der Liste stadt
print(len(set('aaab')))  # 2 - set entfernt duplikate, daher ist die länge 2
print(bool([] + []))  # false - die leere liste ist false


first = "Matthias"
last = "Kahlert"
# anstatt dieses ausdrucks gibt es formatierte strungs mit geschweiften klammern
full1 = first + " " + last
print(full1)
full_formatted_string = f"{first} {last}"
print(full_formatted_string)
text = f"""
Name: {first} {last}
Status: Aktiv
"""
print(text)


s = "Hallo"  # pylint: disable=invalid-name
# s[0] = "X"   # ❌ Fehler: str is immutable

# Aber das geht:
s = "Hallo"
s = "X" + s[1:]   # 👍 neuer String wird erzeugt.
# man kann auch replace nutzen mit dot.notation:
s = s.replace("o", "X")
print(s)  # XallX

""" 
# fehler1.py2
ergebnis = a1 * 2
print(ergebnis)

# fehler2.py
a2 = input('Zahl: ')  # dies ist ein string, kein integer
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
ergebnis = a2 ** 2
print(ergebnis) """


print("-----------------------------------")
c = 42
print("Wert:", c, "Typ:", type(c), "ID:", id(c))

c = str(c)   # Typecast: int → str
print("Wert:", c, "Typ:", type(c), "ID:", id(c))


l = [1, 2, 3]
print(id(l))
print("Wert:", l, "Typ:", type(l), "ID:", id(l))

l.append(4)
# gleiche ID, da Liste veränderbar ist
print("Wert:", l, "Typ:", type(l), "ID:", id(l))


# lexikalische Ordnung
personen = [(23, 'Max'), (34, 'Markus'), (19, 'Tina')]
personen.sort()
print(personen) # [(19, 'Tina'), (23, 'Max'), (34, 'Markus')]
