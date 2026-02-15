import os, time
import sys
# Suchen und Eigenschften ermitteln
print('Unterverzeichnisse des Arbeitsverzeichnisses:')
inhalt = os.listdir() # ohne angabe eines Pfades wird das aktuelle Arbeitsverzeichnis durchsucht
for item in inhalt:
    if os.path.isdir(item):
        print(item)

        
# angabe eines expliziten Pfades
zielverzeichnis = "C:/Users/Matze/repositories/learning-journey/python/exercises"  # Pfad zu einem beliebigen Verzeichnis
print('Unterverzeichnisse in', zielverzeichnis)
inhalt = os.listdir(zielverzeichnis)
for item in inhalt:
    pfad = os.path.join(zielverzeichnis, item)
    if os.path.isdir(pfad):
        print(item)

aktuellesVerzeichnis = os.getcwd() # aktuelles Arbeitsverzeichnis
print(aktuellesVerzeichnis) # Ausgabe des aktuellen Arbeitsverzeichnisses
def prüfe_verzeichnis(pfad):
    if os.path.exists(pfad):
        print(f'Das Verzeichnis {pfad} existiert.')
    else:
        print(f'Das Verzeichnis {pfad} existiert nicht!')


def datei_größe(dateipfad):
    print('Die Datei', dateipfad, 'hat die Größe von', os.path.getsize(dateipfad), 'Bytes')
    return os.path.getsize(dateipfad)

def datei_zugriff(dateipfad):
    
    # ich bekomme mit os.path.getatime die zeit in millisekunden seit dem 1.1.1970. 
    # deshalb könnte man das noch in ein lesbares Format umwandeln, mit der Funktion time.ctime() aus dem Modul time
    zugriffsZeit = os.path.getatime(dateipfad)
    lesbareZeit = time.ctime(zugriffsZeit)
    print('Die Datei', dateipfad, 'hat die letzte Zugriffszeit von', lesbareZeit) # Zugriffszeit von Sun Feb 15 11:48:30 2026
    return lesbareZeit

dateipfad = "python\exercises\Kapitel 9 Uebungen\daten97UE03.json"
dateiname, dateiendung = os.path.splitext(dateipfad)
print("Dateiname:", dateiname)      # Ausgabe: beispiel
print("Dateiendung:", dateiendung)  # Ausgabe: .txt

ordner = "C:/Users/Matze/repositories/learning-journey/python/exercises/Kapitel 10 Uebungen"
for datei in os.listdir(ordner):
    pfad = os.path.join(ordner, datei)
    if os.path.isfile(pfad):
        name, endung = os.path.splitext(datei)
        print(f"Dateiname: {name}\tEndung: {endung}")


# Funktion, die eine Datei in Name und Endung aufteilt
def split_text(dateipfad):
    dateiname, dateiendung = os.path.splitext(dateipfad)
    return dateiname, dateiendung
# Funktion, die alle Dateien eines Ordners tabellarisch ausgibt
def tabellarische_ausgabe_verzeichnis(verzeichnis):
    print(f"{'Dateiname':<40} {'Endung':<10}")
    print("=" * 50)
    for datei in os.listdir(verzeichnis):
        pfad = os.path.join(verzeichnis, datei)
        if os.path.isfile(pfad):
            name, endung = split_text(datei)
            print(f"{name:<40} {endung:<10}")


# Beispielaufrufe
prüfe_verzeichnis('C:/Users/Matze/repositories/learning-journey/python/exercises')  
prüfe_verzeichnis('F:\Dokumente\Python beispiele')
datei_größe('c:\\Users\\Matze\\repositories\\learning-journey\\python\\exercises\\Kapitel 10 Uebungen\\10.py')
datei_zugriff('c:\\Users\\Matze\\repositories\\learning-journey\\python\\exercises\\Kapitel 10 Uebungen\\10.py')
tabellarische_ausgabe_verzeichnis('C:/Users/Matze/repositories/learning-journey/python/exercises/Kapitel 9 Uebungen')


print(os.walk('C:/Users/Matze/repositories/learning-journey/python/exercises/Kapitel 9 Uebungen'))
for ordnername, unterverzeichnisse, dateien in os.walk('C:/Users/Matze/repositories/learning-journey/python/exercises/Kapitel 9 Uebungen'):
    print(f"Ordner: {ordnername}")
    print(f"Unterverzeichnisse: {unterverzeichnisse}")
    print(f"Dateien: {dateien}")
    print("=" * 40)

v4 = [i[0] for i in os.walk('C:/Users/Matze/repositories/learning-journey/python/exercises')]
print(v4)

# plattform.py

print('Ihre Systemplattform ist', sys.platform)
print('Python-Version:')
print('Python '+ sys.version)

if sys.platform == 'win32':
    from winsound import Beep
    Beep(770, 1000)
else:
    print('Beep!')

sys.path