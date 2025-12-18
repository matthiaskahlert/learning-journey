# Uebung 5.5.Ue.01

def temperatur_umrechner(temperatur, einheit='C'):
    """
    Wandelt eine Temperatur zwischen Celsius und Fahrenheit um.
    
    Args:
        temperatur (float): Wert der Temperatur
        einheit (str): 'C' für Celsius, 'F' für Fahrenheit  (optional, Standard: 'C')
    
    Returns:
        float: umgerechnete Temperatur
    """
    einheit = einheit.upper()  # Großbuchstaben zur Sicherheit

    if einheit == 'C':
        fahrenheit = temperatur * 9/5 + 32
        return fahrenheit
    elif einheit == 'F':
        celsius = (temperatur - 32) * 5/9
        return celsius
    else:
        return None



while True:
    print('Willkommen zum Temperatur-Umrechner!')
    print('Gib "ende" ein, um das Programm zu beenden.\n')
    eingabe = input("Gib eine Temperatur mit Einheit ein (z.B. '20 C' oder '100 F'), oder 'ende' zum Beenden: ")
    if eingabe.lower() == 'ende':
        print('Programm beendet')
        break

    try:
        teile = eingabe.split() # macht aus "20 C" -> ['20', 'C']
        temperatur = float(teile[0]) # macht ein float aus der temparaturangabe

        # Einheit optional, Standardwert C
        if len(teile) == 2: # wenn die len von teile 2 ist, hat der user temparatur und einheit angegeben
            einheit = teile[1].upper()
        else:
            einheit = 'C' # wenn nur temparatur angegeben wird, wird die einheit selsius gebutzt

        umgerechnet = temperatur_umrechner(temperatur, einheit)

        if umgerechnet is not None:
            if einheit == 'C':
                print(f"{temperatur} °C entspricht {umgerechnet:.2f} °F\n")
            else:
                print(f"{temperatur} °F entspricht {umgerechnet:.2f} °C\n")
        else:
            print("Bitte gib eine gültige Einheit ('C' oder 'F') ein.\n")

    except ValueError: # zb wenn der user keine zahl eingibt wirft python einen ValueError
        print("Bitte gib eine gültige Zahl für die Temperatur ein.\n")