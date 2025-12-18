"""Entwickle ein Python-Programm, das eine Funktion namens berechne_durchschnitt definiert, 
welche eine Liste von Zahlen als Parameter akzeptiert und den Durchschnittswert dieser Zahlen zurückgibt. 
Dein Programm sollte folgende Anforderungen erfüllen:

a) Definiere die Funktion berechne_durchschnitt, die eine Liste von Zahlen entgegennimmt. 
Die Funktion soll den Durchschnitt dieser Zahlen berechnen und das Ergebnis zurückgeben.

b) Verwende eine for-Schleife innerhalb der Funktion, um durch die Liste zu iterieren und die Summe der Zahlen zu berechnen.

c) Außerhalb der Funktion, definiere eine Liste von Zahlen und weise sie einer Variablen zu. 
Verwende dann diese Liste als Argument, um die Funktion berechne_durchschnitt aufzurufen.

d) Gib das Ergebnis des Funktionsaufrufs mit einer aussagekräftigen Nachricht mithilfe der print()-Funktion aus.

e) Stelle sicher, dass dein Programm auch mit einer leeren Liste umgehen kann, ohne einen Fehler zu verursachen. 
In diesem Fall soll die Funktion None zurückgeben. """


def berechne_durchschnitt(zahlen):
    """
    Berechnet den Durchschnitt einer Liste von Zahlen.
    Gibt None zurück, wenn die Liste leer ist.
    """
    if len(zahlen) == 0: # e) None zurückgeben, wenn liste leer
        return None

    summe = 0
    anzahl = 0

    for zahl in zahlen:      
        summe += zahl
        anzahl += 1

    durchschnitt = summe / anzahl
    return durchschnitt
zahlen_liste = [11, 22, 33, 44, 55]
ergebnis = berechne_durchschnitt(zahlen_liste) # c) Funktion berechne_durchschnitt aufrufen mit liste als argument
if ergebnis is not None:
    print(f"Der Durchschnitt der Zahlen ist: {ergebnis}")
else:
    print("Die Liste ist leer, kein Durchschnitt berechenbar.")


# --- Mini-Unit-Test ---
def test_berechne_durchschnitt():
    # Test 1: normale Liste
    assert berechne_durchschnitt([10, 20, 30]) == 20 # assert <Bedingung>: Prüft, ob die Bedingung wahr ist, wenn nicht, wird ein fehler geworfen
    
    # Test 2: Liste mit einem Element
    assert berechne_durchschnitt([42]) == 42
    
    # Test 3: leere Liste
    assert berechne_durchschnitt([]) is None
    
    # Test 4: Liste mit negativen Zahlen
    assert berechne_durchschnitt([-10, 0, 10]) == 0

    print("Happy path: Alle Tests bestanden ✅")


# Test starten
test_berechne_durchschnitt()


def test_fail_example():
    # Erwartet fälschlicherweise 25 statt 20
    assert berechne_durchschnitt([10, 20, 30]) == 25
    print("unhappy - path: Alle Tests bestanden ✅")
# Test starten
test_fail_example()