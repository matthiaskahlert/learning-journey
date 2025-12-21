"""a) Eine Funktion durchschnittspreis, die den Durchschnittspreis aus einer Liste von Produkt-Preisen berechnet. 
Die Funktion nimmt eine Liste von Preisen als Argument und gibt den Durchschnittspreis zurück.

b) Eine Funktion produkt_filter, die eine Liste von Produktnamen 
und einen Buchstaben als Argumente nimmt und alle Produkte zurückgibt, 
die mit diesem Buchstaben beginnen, unter Verwendung der filter()-Funktion.

c) Eine rekursive Funktion max_preis, 
die den höchsten Preis in einer Liste von Preisen findet. 
Wenn die Liste leer ist, soll die Funktion None zurückgeben.

d) Eine Funktion preis_mit_steuer, die den Preis eines Produkts inklusive Mehrwertsteuer berechnet. 
Die Funktion nimmt zwei Argumente: den Preis ohne Steuer und den Steuersatz (als optionalen Parameter mit einem Default-Wert von 19%).

e) Eine Lambda-Funktion, die zusammen mit der map()-Funktion verwendet wird, 
um die Preise einer Liste von Produkten um einen bestimmten Prozentsatz zu erhöhen. 
Die Prozentsatzerhöhung soll als Argument übergeben werden.

f) Eine Funktion drucke_produktliste, die eine Liste von Produktnamen schön formatiert auf der Konsole ausgibt. 
Verwende die print()-Funktion, um jedes Produkt in einer neuen Zeile auszugeben. """


produkte = [
    {"name": "Laptop", "preis": 999.00},
    {"name": "Smartphone", "preis": 599.00},
    {"name": "Kopfhörer", "preis": 149.00},
    {"name": "Smartwatch", "preis": 249.00},
    {"name": "Tablet", "preis": 399.00},
    {"name": "E-Book-Reader", "preis": 129.00},
    {"name": "Fitness-Tracker", "preis": 79.00},
    {"name": "Bluetoothlautsprecher", "preis": 89.00},
    {"name": "Powerbank", "preis": 39.00},
    {"name": "Webcam", "preis": 59.00}
]


# a) durchschnitspreise
def durchschnittspreis(preise):
    if len(preise) == 0:  # prüft, ob die Liste leer ist
        # wenn die Liste nicht leer ist wird nicht None returned sondern der durchschnitt berechnet
        return None
    return sum(preise) / len(preise)


# Alle Produktnamen extrahieren
namen = []

for p in produkte:
    namen.append(p["name"])# p ist z. B. {"name": "Laptop", "preis": 999.00} 
    # p["name"] ist demzurfolge "Laptop"

# Alle Preise extrahieren
preise = []
for p in produkte:
    preise.append(p["preis"]) # p["preis"] ist zb 999.00



# a)
print(f"Durchschnittspreis: {durchschnittspreis(preise):.2f} €") # Durchschnittspreis: 279.00 €

# b)
def produkt_filter(namen, buchstabe):
    buchstabe = buchstabe.lower() # alles in lowercase, auch gleich in der lambda 
    gefilterte_namen = list(
        filter(
            lambda name: name.lower().startswith(buchstabe), # diese lambda funktion wird von filter() genutzt um die elemente von "namen" abzugleichen
            namen
        )
    )
    return gefilterte_namen # enthält nur werte bei denen die lambda funktion true zurückgab

# mini test auf lowercase
print(produkt_filter(namen, "S"))
print(produkt_filter(namen, "s"))

# c)
def max_preis(preise):
    # Abbruchfall 1: leere Liste
    if len(preise) == 0:
        return
    # Abbruchfall 2: Liste mit nur einem Eintrag / Wert um den rückweg der rekursion zu initiieren
    if len(preise) == 1:
        return preise[0]
   
    # rekursiver Schritt: höchste Zahl im Rest der Liste
    max_rest = max_preis(preise[1:])
    
    # Vergleich mit erstem Element
    if preise[0] > max_rest:
        return preise[0]
    else:
        return max_rest

print(max_preis(preise))

# d)
def preis_mit_steuer(preis, mwst_satz = 19):
    mwst = preis  * (mwst_satz / 100)
    return preis + mwst
print("Orginal Preis mit Mehrwertsteuer",preis_mit_steuer(produkte[0]["preis"]))

# e)
def preise_erhoehen(preise, prozent):
    return list(
    map(lambda p: round(p * (1 + prozent / 100),2), preise) # gerundet auf 2 stellen, punkt vor strichrechnung - (1 + prozent / 100) = 1 + 10 / 100 = 1 + 0.10 = 1.10
    )
print("Orginalpreise:",preise)
print("Erhöhte Preise:",preise_erhoehen(preise, 10))

# map() wendet die Lambda-Funktion auf jedes Element in prices an
# list() konvertiert das map-Objekt in eine Liste


# f)
def drucke_produktliste(produkte):
    print("Produktliste:")
    for produkt in produkte:
        print(f"- {produkt}\n")
drucke_produktliste(produkte)


# bonus
# preise inkl. mwstr ausgeben

def drucke_produktliste_mit_mwst(produkte, mwst_satz=19):
    print("Produktliste (inkl. MwSt):")
    for produkt in produkte:
        name = produkt["name"]
        preis_netto = produkt["preis"]
        preis_brutto = preis_mit_steuer(preis_netto, mwst_satz)
        print(f"- {name}: {preis_brutto:.2f} €")

drucke_produktliste_mit_mwst(produkte)


produkte_erhoeht = []

for p in produkte:
    name = p["name"]
    preis_erhoeht = round(p["preis"] * 1.10, 2)  # 10 % Erhöhung
    produkte_erhoeht.append({"name": name, "preis": preis_erhoeht})


drucke_produktliste_mit_mwst(produkte_erhoeht)