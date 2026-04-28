import os


def ordnergroesse_pfad(pfad):
    """Berechnet rekursiv die Größe eines Ordners inkl. aller Unterordner."""
    gesamt = 0
    for wurzel, dirs, dateien in os.walk(pfad):
        for datei in dateien:
            try:
                gesamt += os.path.getsize(os.path.join(wurzel, datei))
            except (OSError, FileNotFoundError):
                pass
    return gesamt


def ordnerstruktur_mit_groesse(startpfad):
    """Gibt alle Ordner im Verzeichnisbaum mit ihrer Gesamtgröße aus."""
    for wurzel, dirs, _ in os.walk(startpfad):
        groesse = ordnergroesse_pfad(wurzel)
        print(f"{wurzel} -> {groesse/1024/1024:.2f} MB")


if __name__ == "__main__":
    pfad = input("Pfad zum Projektordner (z.B. flutter/exercises/bibliothek_dashboard): ")
    if not pfad:
        pfad = "flutter/exercises/bibliothek_dashboard"
    if not os.path.exists(pfad):
        print("Pfad existiert nicht!")
    else:
        print(f"Ordnergrößen für: {pfad}\n---------------------------")
        ordnerstruktur_mit_groesse(pfad)
