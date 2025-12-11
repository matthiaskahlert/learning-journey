# Einfacher Taschenrechter der die grund operatoren nutzt, unter eingabe von zwei zahlen.
zahl1 = float(input("Bitte die erste Zahl eingeben: "))
operator = input("Bitte Operator eingeben (+,-,*, /): ")
zahl2 = float(input("Bitte die zweite Zahl eingeben: "))
if operator == "+":
    ergebnis = zahl1 + zahl2
    print("Ergebnis lautet: ", ergebnis)
elif operator == "-":
    ergebnis = zahl1 - zahl2
    print("Ergebnis lautet: ", ergebnis)
elif operator == "*":
    ergebnis = zahl1 * zahl2
    print("Ergebnis lautet: ", ergebnis)
elif operator == "/":
    if zahl2 == 0:
        print("Teilen durch null ist nicht erlaubt.")
    else:
        ergebnis = zahl1/zahl2
        print("Ergebnis lautet: ", ergebnis)
else:
    print("Ungültiger Operator. Bitte einen der folgenden Operatoren eingeben: +, -, *, /")
