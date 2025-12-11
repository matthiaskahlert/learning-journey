# Fehlerbehandlung (Basis)

# Falsche Eingaben abfangen, damit der Code nicht abstürzt:

while True:
    try:
        zahl = float(input("Bitte eine Zahl eingeben: "))
        break
    except ValueError:
        print("❌ Ungültige Eingabe, bitte eine Zahl eingeben!")
