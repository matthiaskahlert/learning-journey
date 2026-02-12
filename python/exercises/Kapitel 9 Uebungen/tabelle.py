# tabelle.py
ZEILE = '{:15} | {:10}'

def häufigste_wörter(text, minlänge, anzahl):
    """
    Ermittelt die häufigsten Wörter im Text, die mindestens eine bestimmte Länge haben.
    Entfernt Satzzeichen, zählt die Häufigkeit und gibt die Top-N als Liste von Tupeln (Vorkommen, Wort) zurück.
    Args:
        text (str): Der zu analysierende Text.
        minlänge (int): Minimale Wortlänge.
        anzahl (int): Anzahl der häufigsten Wörter, die zurückgegeben werden.
    Returns:
        List[Tuple[int, str]]: Liste der häufigsten Wörter und ihrer Vorkommen.
    """
    for ch in '${}<>., ;: / ?! " -_ []':
        text = text.replace(ch, ' ')
    wortliste = text.split()
    wortmenge = set(wortliste)
    häufigkeiten = [(text.count(wort), wort)
                    for wort in wortmenge
                    if len(wort) >= minlänge]
    häufigkeiten.sort()
    häufigkeiten.reverse()
    return häufigkeiten[0:anzahl]

def ausgabe (häufigkeiten):
    """
    Gibt eine Tabelle der Wörter und ihrer Vorkommen aus.
    Args:
        häufigkeiten (List[Tuple[int, str]]): Liste der häufigsten Wörter und ihrer Vorkommen.
    """
    print(ZEILE.format('Wort','Vorkommen'))
    print(26*'-')
    for vorkommen, wort in häufigkeiten:
        print(ZEILE.format(wort, vorkommen))

# Hauptprogramm
dateiname = input('Dateiname: ')
minlänge = int(input('Minimale Wortlänge: '))
anzahl = int(input('Länge der Tabelle: '))
f = open(dateiname, 'r', encoding='utf-8')
text=f.read()
f.close()
tabelle = häufigste_wörter(text, minlänge, anzahl)
ausgabe (tabelle)
input()
