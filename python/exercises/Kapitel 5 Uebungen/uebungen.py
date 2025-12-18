# lambda funktion mit einem input value

from curses.ascii import isdigit


multiplikation = lambda x: x*2 
print(multiplikation(2))
print("Die Nutzung der Multiplikations Lambda Funktion ergibt: ", multiplikation(2))  # 4
# lambda funtkion mit zwei input values
addiere = lambda x,y: x + y
print(addiere(5,3))


print("Die Nutzung der Additions Lambda Funktion ergibt: ", addiere(5, 3))  # 8


check = lambda i: i in "Python"


print(check("y"))  # True
print(check("z"))  # False

division = (lambda a, b: a/b)(10, 2)
print("Die Nutzung der Divisions Lambda Funktion ergibt: ", division)  # 5.0

prices = ['$12.50', '$9.99', '$100.00']  # liste von strings
p = '$12.50'
print(p.replace('$', ''))  # entfernen des dollarzeichens
print(float(p.replace('$', '')))  # Daten transformation in float

print(list(map(lambda p: float(p.replace('$', '')), prices)))
# map() wendet die Lambda-Funktion auf jedes Element in prices an
# list() konvertiert das map-Objekt in eine Liste
# [12.5, 9.99, 100.0]

# alle preise unter 100 entfernen:
prices2 = [120, 30, 150, 300, 80]

print(list(filter(lambda p2: p2 >= 100, prices2)))  # [120, 150, 300]
# filter() wendet die Lambda-Funktion auf jedes Element in prices2 an
# und behält nur die Elemente bei, für die die Funktion True zurückgibt
# list() konvertiert das filter-Objekt in eine Liste
# [120, 150, 300]

students = [
    ['Maria', 25],
    ['Tom', 22],
    ['Anna', 23]
]
# zeige nur Studierende mit alter größer 23
students[0][1] >= 23  # True
# [['Maria', 25], ['Anna', 23]]
print(list(filter(lambda row: row[1] >= 23, students)))
#zeige nur studierende die mit M beginnen
print(list(filter(lambda row: row[0].startswith('M'), students)))

tiere = ['Affe', 'Rentier', 'Fuchs']
wortlängen = map(len, tiere)
liste_wortlängen = list(wortlängen)
print(liste_wortlängen) # [4, 7, 5]


def add(x, y):
    return x + y

summe = map(add, [1, 2, 3], [4, 5, 6])
print(list(summe)) # [5, 7, 9]

summe = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print(list(summe)) #[5, 7, 9]

# imperatives programm:

a1 = float(input('a1: '))
b1 = float(input('b1: '))
ergebnis = a1 ** 2 + b1 ** 2
print(ergebnis)



# funktional verschachteltes programm:

a2 = float(input('a2: '))
b2 = float(input('b2: '))
print((lambda a,b: a ** 2 + b ** 2)(a2,b2))

# maximal verschachtelt
print("Maximal verschachtel", (lambda a,b: a ** 2 + b ** 2)(float(input('a: ')), float(input('b: '))))

# Übungen 5.14

def volumen_platte(l, b, d=2):
    """
    Berechnet das Volumen einer rechteckigen Platte.

    Parameter:
    l : Länge in cm
    b : Breite in cm
    d : Dicke in cm (optional, Standardwert=2)

    Rückgabe:
    Volumen in cm³
    """
    return l * b * d

# Beispiele
help(volumen_platte)
print(volumen_platte(10, 5))      # d=2 wird automatisch verwendet → 100
print(volumen_platte(10, 5, 3))   # d=3 → 150


# Schreibe eine Funktion ziffern(), die einen String als Argument übernimmt und 
# die Anzahl der Dezimalziffern (0, 1, ..., 9) in dem Text zählt und zurückgibt
str1 = input('Gib einen String ein. \n'
            'Die Funktion wird die Ziffern von 0 - 9 aus dem eingegebenen string heraussuchen und zurückgeben'
            ': ' )
def ziffern(s):
    result = []
    for i in s:
        if i.isdigit():
            result.append(int(i))
    return result
print(ziffern(str1))
