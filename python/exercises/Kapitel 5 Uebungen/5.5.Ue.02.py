"""
Entwickle ein Python-Programm, das eine Funktion namens umrechner enthält, welche zwei Parameter akzeptiert: 
betrag und waehrung, wobei waehrung einen optionalen Parameter darstellt, der standardmäßig auf "USD" gesetzt ist. 
Die Funktion soll den betrag von Euro in die angegebene Währung umrechnen. 
Verwende für die Umrechnung folgende fiktive Wechselkurse: 1 Euro = 1,1 USD und 1 Euro = 0,9 GBP. 
Das Programm soll den Benutzer auffordern, einen Betrag und eine Währung einzugeben, und dann das Ergebnis der Umrechnung ausgeben. 
Implementiere zusätzlich eine Kontrollstruktur, die überprüft, ob die eingegebene Währung unterstützt wird, 
und eine entsprechende Nachricht ausgibt, falls dies nicht der Fall ist. 
Verwende Schleifen, um den Benutzer die Möglichkeit zu geben, mehrere Umrechnungen durchzuführen, 
bis er das Programm explizit beendet.

"""

def umrechner(betrag, waehrung='USD'):
    """
    Die Funktion soll einen Betrag von Euro in die angegebene Währung umrechnen.
    1 EUR = 1.1 USD
    1 EUR = 0.9 GBP
    Args:
        betrag: betrag ist die Summe in Euro, die umgerechnet werden soll
        waehrung: waehrung ist die Zielwährung, in die umgerechnet wird. es ist Standardmäßig USD, kann aber auch britische Pfund sein (GBP)

    Returns:
        result: Zurückgegeben wird die umgerechnete Summe in der Fremdwährung.
    """
    waehrung = waehrung.upper()  # Großbuchstaben zur Sicherheit

    if waehrung == 'USD':
        result_usd = betrag * 1.1
        return result_usd
    elif waehrung == 'GBP':
        result_gbp = betrag * 0.9
        return result_gbp
    else:
        return None

while True:
    print('Willkommen zum Währungs-Umrechner!')
    print('Gib "ende" ein, um das Programm zu beenden.\n')
    eingabe = input("Gib einen Betrag in EUR ein sowie die Zielwährung in die die Summe umgerechnet werden soll (z.B. '20 USD' oder '100 GBP'), oder 'ende' zum Beenden: ")
    if eingabe.lower() == 'ende':
        print('Programm beendet')
        break

    try:
        teile = eingabe.split() # macht aus "20 USD" -> ['20', 'USD']
        betrag = float(teile[0]) # macht ein float aus der betragseingabe.

        # Einheit optional, Standardwert USD
        if len(teile) == 2: # wenn die len von teile 2 ist, hat der user betrag und währung angegeben
            waehrung = teile[1].upper()
        else:
            waehrung = 'USD' # wenn nur betrag angegeben wird, wird die währung USD genutzt

        umgerechnet = umrechner(betrag, waehrung)

        if umgerechnet is not None:
            if waehrung == 'USD':
                print(f"{betrag} EUR entspricht {umgerechnet:.2f} USD\n")
            else:
                print(f"{betrag} EUR entspricht {umgerechnet:.2f} GBP\n")
        else:
            print("Bitte gib eine gültige Währung ('USD' oder 'GBP') ein.\n")

    except ValueError: # zb wenn der user keine zahl eingibt wirft python einen ValueError
        print("Bitte gib eine gültige Zahl für den Betrag ein.\n")