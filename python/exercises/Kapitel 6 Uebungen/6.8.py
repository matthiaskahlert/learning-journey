"""Entwickle ein interaktives Programm, das die Höhe eines Baums berechnen
kann. Es sollen folgende Daten eingegeben werden: Entfernung zum Baum,
Augenhöhe, Blickwinkel alpha zur Spitze des Baums."""

from math import tan, radians

# Eingabe
entfernung = float(input("Entfernung zum Baum (m): "))
augenhoehe = float(input("Augenhöhe (m): "))
alpha = float(input("Blickwinkel (Grad): "))

# Verarbeitung
hoehe_baum = augenhoehe + entfernung * tan(radians(alpha))

# Ausgabe
print(f"Höhe des Baums: {hoehe_baum:.2f} m")
