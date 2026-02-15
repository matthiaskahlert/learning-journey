import os, time

def finde_alte_programme(p):
    """
    Sucht rekursiv alle Python-Dateien (.py) in einem Verzeichnis,
    die älter als 30 Tage sind.
    Parameter:
        p (str): Pfad zum Startverzeichnis
    Rückgabe:
        list: Liste von Tupeln (vollständiger Dateipfad, Alter in Tagen)
    """
    ergebnis = []
    jetzt = time.time()
    for name in os.listdir(p):
        pfad = os.path.join(p, name)
        if os.path.isfile(pfad) and name.endswith('.py'):
            mtime = os.path.getmtime(pfad)
            alter_tage = (jetzt - mtime) / (60 * 60 * 24)
            if alter_tage > 30:
                ergebnis.append((pfad, alter_tage))
    return ergebnis

# Hauptprogramm
if __name__ == "__main__":
    pfad = input('Verzeichnis: ')
    if os.path.exists(pfad) and os.path.isdir(pfad):
        alt = finde_alte_programme(pfad)
        for programm, alter in alt:
            print(programm, round(alter), 'Tage alt')
        print(len(alt), 'Dateien gefunden')
    else:
        print('Ungültiger Pfad')