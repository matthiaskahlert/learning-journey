""" a) Definiere eine Variable text, die einen mehrzeiligen String speichert. 
Der String soll mindestens ein Unicode-Zeichen, eine Escape-Sequenz und variable Teile enthalten, 
die durch die format() Methode ersetzt werden. Verwende für das Unicode-Zeichen ein Emoji und für die Escape-Sequenz einen Zeilenumbruch.
b) Verwende die print() Funktion, um den String auszugeben.
c) Lese eine Textdatei namens beispiel.txt, die du zuvor selbst erstellen musst, mit der with-Anweisung und utf-8 Encoding. 
Speichere den Inhalt der Datei in einer Variablen und gib ihn aus.
d) Schreibe eine Funktion speichere_json, die ein Python-Objekt 
(z.B. ein Dictionary mit einigen Schlüssel-Wert-Paaren) in eine Datei im JSON-Format speichert. 
Verwende dazu das Modul json.
e) Verwende die try und except Blöcke, um Fehler beim Lesen einer nicht existierenden Datei zu behandeln. 
Gib eine benutzerfreundliche Nachricht aus, wenn die Datei nicht gefunden wird.  """
import json

# a) Variable text mit format()
text = "Guten Tag! \U0001F600\nName: {name}\nAlter: {alter}\nStadt: {stadt}"
ausgabe = text.format(name="Max Mustermann", alter=30, stadt="Hamburg")
print(ausgabe)

# c) Textdatei lesen
DATEINAME = 'python/exercises/Kapitel 9 Uebungen/beispiel.txt'
with open(DATEINAME, mode='r', encoding='utf-8') as datei:
    inhalt = datei.read()
    print(inhalt)

# d) JSON speichern
def speichere_json(objekt, dateiname):
    with open(dateiname, mode='w', encoding='utf-8') as datei:
        json.dump(objekt, datei, ensure_ascii=False, indent=4)

beispiel_dict = {
    "name": "Max Mustermann",
    "alter": 30,
    "stadt": "Hamburg"
}
speichere_json(beispiel_dict, 'python/exercises/Kapitel 9 Uebungen/beispiel.json')

# e) Fehlerbehandlung
try:
    with open('nicht_existierende_datei.txt', mode='r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden. Bitte überprüfe den Dateinamen und den Pfad.")
