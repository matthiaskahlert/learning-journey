"""a) Eine Funktion durchschnittspreis, die den Durchschnittspreis aus einer Liste von Produkt-Preisen berechnet. 
Die Funktion nimmt eine Liste von Preisen als Argument und gibt den Durchschnittspreis zurück.

b) Eine Funktion produkt_filter, die eine Liste von Produktnamen und einen Buchstaben als Argumente nimmt 
und alle Produkte zurückgibt, die mit diesem Buchstaben beginnen, unter Verwendung der filter()-Funktion.

c) Eine rekursive Funktion max_preis, die den höchsten Preis in einer Liste von Preisen findet. 
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
    if not preise:  # prüft, ob die Liste leer ist.
        return None
    return sum(preise) / len(preise)


# Alle Produktnamen extrahieren
namen = [p["name"] for p in produkte]
preise = [p["preis"] for p in produkte]

# a)
print(f"Durchschnittspreis: {durchschnittspreis(preise):.2f} €")