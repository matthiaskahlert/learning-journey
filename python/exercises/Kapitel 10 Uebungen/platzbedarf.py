import os

BERICHT = '''
Ich habe {} Verzwichnisse durchsucht.
Der gesamte Speicherbedarf beträgt {} Bytes.'''

def berechne_platzbedarf(wurzel):
    durchlauf = os.walk(wurzel)
    anzahl = 0
    platz = 0
    for v, uv, d in durchlauf: # Verzeichnis, Unterverzeichnisse und Dateien
        anzahl +=1
        os.chdir(v)
        for datei in d:
            platz += os.path.getsize(datei)
            return anzahl, platz
        
# Hauptprogramm
wurzel = input('Wurzelverzeichnis z.B. /python): ')
if os.path.exists(wurzel):
    anz_verz, speicher = berechne_platzbedarf(wurzel)
    print(BERICHT.format(anz_verz, speicher))
else:
    print('Das Verzeichnis existiert nicht.')
input('Drücken Sie die Eingabetaste zum Beenden.')
