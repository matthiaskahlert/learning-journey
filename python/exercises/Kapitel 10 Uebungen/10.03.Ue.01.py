""" 
a) Erstelle eine Funktion erstelle_verzeichnis, die als Argument einen Verzeichnisnamen (String) nimmt. 
Die Funktion soll mithilfe des os-Moduls überprüfen, ob das Verzeichnis bereits existiert. 
Falls nicht, soll das Verzeichnis erstellt werden. 
Gib eine Bestätigung aus, dass das Verzeichnis erstellt wurde oder bereits existiert.

b) Erstelle eine Funktion speichere_text_in_datei, die zwei Argumente nimmt: 
den Dateinamen (String) und den zu speichernden Text (String). 
Die Funktion soll den Text in der angegebenen Datei speichern. 
Verwende die with-Anweisung, um die Datei zu öffnen und sicherzustellen, dass sie korrekt geschlossen wird.

c) Erstelle eine Funktion lese_datei, die als Argument einen Dateinamen (String) nimmt 
und den Inhalt der Datei ausgibt. 
Fange mögliche Ausnahmen ab, die beim Versuch, die Datei zu lesen, auftreten können 
(z.B. wenn die Datei nicht existiert), und gib eine entsprechende Fehlermeldung aus.

d) Erstelle eine Funktion liste_dateien_in_verzeichnis, die als Argument einen Verzeichnisnamen (String) nimmt 
und alle Dateien in diesem Verzeichnis auflistet. Verwende das os-Modul, um auf das Dateisystem zuzugreifen.

e) Schreibe ein Hauptprogramm, das die Funktionen in folgender Reihenfolge aufruft: 
erstelle_verzeichnis mit dem Verzeichnisnamen "MeineDaten", 
speichere_text_in_datei mit einem beliebigen Text in einer Datei namens "beispiel.txt" im Verzeichnis "MeineDaten", 
lese_datei für "beispiel.txt" und liste_dateien_in_verzeichnis für das Verzeichnis "MeineDaten". 
 """
import os
def erstelle_verzeichnis(verzeichnis):
    if not os.path.exists(verzeichnis):
        os.makedirs(verzeichnis)
        print(f"Verzeichnis '{verzeichnis}' wurde erstellt.")
    else:
        print(f"Verzeichnis '{verzeichnis}' existiert bereits.")

def speichere_text_in_datei(dateiname, text):
    with open(dateiname, 'w') as datei:
        datei.write(text)
    print(f"Text wurde in '{dateiname}' gespeichert.")

def lese_datei(dateiname):
    try:
        with open(dateiname, 'r') as datei:
            inhalt = datei.read()
            print(f"Inhalt der Datei '{dateiname}':\n{inhalt}")
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateiname}' existiert nicht.")

def liste_dateien_in_verzeichnis(verzeichnis):
    if os.path.exists(verzeichnis):
        dateien = os.listdir(verzeichnis)
        print(f"Dateien im Verzeichnis '{verzeichnis}':")
        for datei in dateien:
            print(datei)
    else:
        print(f"Fehler: Das Verzeichnis '{verzeichnis}' existiert nicht.")

# Hauptprogramm
if __name__ == "__main__":
    verzeichnis = "python/exercises/Kapitel 10 Uebungen/MeineDaten"
    erstelle_verzeichnis(verzeichnis)
    
    dateiname = os.path.join(verzeichnis, "beispiel.txt")
    text = "Dies ist ein neuer Beispieltext, der in die Datei geschrieben wird."
    speichere_text_in_datei(dateiname, text)
    lese_datei(dateiname)
    liste_dateien_in_verzeichnis(verzeichnis)
