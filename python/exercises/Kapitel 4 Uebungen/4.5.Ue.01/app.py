eingabe = input("Bitte geben sie eine ganze Zahl ein: ")  # Eingabe
zahl = int(eingabe)

if zahl > 10:  # Verarbeitung
    print("Die Zahl ist größer als 10.")  # Ausgabe
elif zahl < 10:
    print("Die Zahl ist kleiner als 10.")
else:
    print("Die Zahl ist gleich 10.")

for i in range(1, zahl + 1):  # for schleife mit range startwert 1 und stopwert eingegebener wert +1
    print(i)
print("Ende des Programms.")
