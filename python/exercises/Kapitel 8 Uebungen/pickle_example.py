import pickle

liste = [
    {"name": "Anna", "alter": 26},
    {"name": "Bernd", "alter": 59},
    {"name": "Caspar", "alter": 19},
    {"name": "Doro", "alter": 29},
]

with open('python/exercises/Kapitel 8 Uebungen/liste.dat', 'wb') as stream:
    pickle.dump(liste, stream)

print("Datei erfolgreich gespeichert!")
""" 
Es wird eine Binärdatei liste.dat erzeugt
Die Liste wird in Bytes umgewandelt und gespeichert
Durch with wird die Datei automatisch geschlossen """


# das öffnen der datei erfolgt folgendermaßen:
with open('python/exercises/Kapitel 8 Uebungen/liste.dat', 'rb') as stream:
    geladene_liste = pickle.load(stream)
print(geladene_liste)
