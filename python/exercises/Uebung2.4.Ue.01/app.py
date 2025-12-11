""" 
Übung 2.4.Ü.01
Du hast die Aufgabe, ein kleines Python-Programm zu schreiben, das folgende Anforderungen erfüllt:

a) Erstelle eine Liste mit den Namen deiner fünf besten Freunde.

b) Füge der Liste zwei neue Namen hinzu, indem du die append() Methode verwendest.

c) Entferne einen Namen aus der Liste mit der remove() Methode.

d) Erstelle ein Tupel, das drei verschiedene Ganzzahlen enthält.

e) Konvertiere das Tupel in eine Liste und füge eine weitere Ganzzahl hinzu.

f) Erstelle eine Menge mit mindestens drei deiner Lieblingsfrüchte.

g) Füge der Menge eine neue Frucht hinzu, die noch nicht in der Menge enthalten ist.

h) Erstelle ein Dictionary, dass drei verschiedene Länder als Schlüssel und deren Hauptstädte als Werte enthält. 
  """


namen = ["Peter", "Tim", "Nordi", "Georg", "Gregor"]  # a)
print("a:", namen)
# b) mit append kann ich nur ein element hinzufügen, mit extend mehrere
namen.extend(["Max Mustermann", "Erika Musterfrau"])
print("b:", namen)
namen.remove("Nordi")  # c)
print("c:", namen)
t0 = (2, 4, 6)  # d)
print("d:", t0)
t0_list = list(t0)  # Convert tuple to list
t0_list.append(8)  # Append 8 to the list
t0 = tuple(t0_list)  # Convert back to tuple
print("e:", t0)
frucht_set = {"Erdbeere", "Mango", "Kirsche"}  # f)
print("f:", frucht_set)
frucht_set.add("Banane")  # g)
print("g:", frucht_set)
laender_dict = {"Deutschland": "Berlin",
                "Frankreich": "Paris", "Italien": "Rom"}  # h)
print("h:", laender_dict)
