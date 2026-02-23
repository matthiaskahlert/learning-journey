""" 
Erstelle eine Klasse Auto, welche folgende Attribute besitzt: 
marke (String), 
modell (String), 
kilometerstand (Integer) 
und tankfüllung (in Prozent als Integer). 
Die Klasse soll zwei Methoden haben: fahren(kilometer) und tanken(prozent). 
Die Methode fahren(kilometer) soll den Kilometerstand um die gefahrenen Kilometer erhöhen 
und die Tankfüllung basierend auf einer Annahme, dass das Auto pro 100 Kilometer 5% des Tanks verbraucht, reduzieren. 
Die Methode tanken(prozent) soll die Tankfüllung um den angegebenen Prozentsatz erhöhen, darf aber 100% nicht überschreiten.
 """
class Auto:
    def __init__(self, marke, modell, kilometerstand, tankfüllung):
        self.marke = marke
        self.modell = modell
        self.kilometerstand = kilometerstand
        self.tankfüllung = tankfüllung


    def fahren(self, kilometer):
        self.kilometerstand += kilometer
        verbrauch = (kilometer / 100) * 5
        self.tankfüllung -= verbrauch
        if self.tankfüllung < 0:
            self.tankfüllung = 0
        print(f"Gefahrene Kilometer: {kilometer}. Verbleibende Tankfüllung: {self.tankfüllung}%.")


    def tanken(self, prozent):
        if self.tankfüllung + prozent > 100:
            self.tankfüllung = 100
        else:
            self.tankfüllung += prozent
        print(f"Getankte Menge: {prozent}%. Neue Tankfüllung: {self.tankfüllung}%.")


# Beispiel zur Nutzung der Klasse

mein_auto = Auto("Volkswagen", "Golf", 50000, 50)
mein_auto.fahren(200)
mein_auto.tanken(20)