import os


def ordnergroesse_pfad(zielpfad):
    """Berechnet rekursiv die Größe eines Ordners inkl. aller Unterordner."""
    gesamt = 0
    for wurzel, _, dateien in os.walk(zielpfad):
        for datei in dateien:
            try:
                gesamt += os.path.getsize(os.path.join(wurzel, datei))
            except (OSError, FileNotFoundError):
                pass
    return gesamt


def ordnerstruktur_mit_groesse(startpfad, ausgabepfad):
    """Schreibt alle Ordner im Verzeichnisbaum sortiert nach Größe als Tabelle in eine Textdatei."""
    eintraege = []
    for wurzel, _, _ in os.walk(startpfad):
        groesse = ordnergroesse_pfad(wurzel)
        eintraege.append((wurzel, groesse))

    eintraege.sort(key=lambda eintrag: eintrag[1], reverse=True)

    if not eintraege:
        with open(ausgabepfad, "w", encoding="utf-8") as datei:
            datei.write("Keine Ordner gefunden.\n")
        return

    breite_ordner = max(len("Ordner"), max(len(pfad) for pfad, _ in eintraege))
    header = f"{'Ordner':<{breite_ordner}} | {'MB':>10} | {'Bytes':>12}"
    zeilen = [header, "-" * len(header)]

    for ordnerpfad, groesse in eintraege:
        groesse_mb = groesse / 1024 / 1024
        zeilen.append(f"{ordnerpfad:<{breite_ordner}} | {groesse_mb:>10.2f} | {groesse:>12,d}")

    with open(ausgabepfad, "w", encoding="utf-8") as datei:
        datei.write("\n".join(zeilen) + "\n")


if __name__ == "__main__":
    pfad = input("Pfad zum Projektordner (z.B. flutter/exercises/bibliothek_dashboard): ")
    if not pfad:
        pfad = "flutter/exercises/bibliothek_dashboard"
    if not os.path.exists(pfad):
        print("Pfad existiert nicht!")
    else:
        ausgabedatei = os.path.join(os.path.dirname(__file__), "ordnergroessen_report.txt")
        ordnerstruktur_mit_groesse(pfad, ausgabedatei)
        print(f"Ausgabe gespeichert in: {os.path.abspath(ausgabedatei)}")
