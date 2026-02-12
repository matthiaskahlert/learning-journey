""" Entwickle ein Python-Programm, das folgende Funktionalitäten umfasst:

a) Lese einen Text aus einer Datei, die Unicode-Zeichen enthält, und speichere den Text in einer Variablen. 
Verwende dazu die with-Anweisung und stelle sicher, dass die Datei korrekt geschlossen wird.
b) Verwende reguläre Ausdrücke, um alle Wörter im Text zu finden, die mit einem Großbuchstaben beginnen, 
und speichere diese Wörter in einer Liste.
c) Erstelle eine Funktion, die die Anzahl der Vorkommen jedes Wortes in der Liste aus b) zählt 
und diese in einem Dictionary speichert.
d) Speichere das Dictionary aus c) in einer JSON-Datei. Stelle sicher, dass Umlaute 
und Sonderzeichen korrekt gespeichert werden.
e) Lies die JSON-Datei, die du in d) erstellt hast, und gib den Inhalt in der Konsole aus. 
Verwende hierbei die richtige Kodierung, um Umlaute und Sonderzeichen korrekt darzustellen. """ 

# dateipfad mit unicode: python\exercises\Kapitel 9 Uebungen\unicode_text.txt
import re, json
# a) Text aus Datei lesen
DATEINAME = 'python/exercises/Kapitel 9 Uebungen/unicode_text.txt'
with open(DATEINAME, mode='r', encoding='utf-8') as datei:
    inhalt = datei.read()
    print(inhalt)
# b) Wörter mit Großbuchstaben finden
wörter = re.findall(r'\b[A-ZÄÖÜ][a-zäöüA-ZÄÖÜ]*\b', inhalt)
print(wörter) # ['Zusätzlich', 'Unicode', 'Zeichen', 'Griechisch', 'Mathematisch', 'Emojis', 'Arabisch', 'Chinesisch', 'Japanisch', 'Koreanisch']

# c) Anzahl der Vorkommen jedes Wortes zählen
def zähle_wörter(wort_liste):
    """

    Zählt die Anzahl der Vorkommen jedes Wortes in der Liste und gibt ein Dictionary zurück.
    Args:    wort_liste (List[str]): Eine Liste von Wörtern.
    Returns:    Dict[str, int]: Ein Dictionary mit Wörtern als Schlüssel und deren Vorkommen als Werte.

    """
    zählung = {}
    for wort in wort_liste:
        if wort in zählung:
            zählung[wort] += 1
        else:
            zählung[wort] = 1
            # die liste soll absteigend sortiert werden nach der Anzahl der Vorkommen
    return zählung

wort_zählung = zähle_wörter(wörter)
print(f'die Anzahl der Vorkommen jedes Wortes: {wort_zählung}')
#  {wort_zählung} soll auch als tabelle ausgegeben werden 
print(f'{"Wort":<15} | {"Vorkommen":<10}')
print('-' * 30)
for wort, vorkommen in wort_zählung.items():
    print(f'{wort:<15} | {vorkommen:<10}')

# d) Dictionary in JSON-Datei speichern
with open('python/exercises/Kapitel 9 Uebungen/wort_zaehlung.json', mode='w', encoding='utf-8') as json_datei:
    json.dump(wort_zählung, json_datei, ensure_ascii=False, indent=4)

# e) JSON-Datei lesen und Inhalt in der Konsole ausgeben
with open('python/exercises/Kapitel 9 Uebungen/wort_zaehlung.json', mode='r', encoding='utf-8') as json_datei:
    gelesene_daten = json.load(json_datei)
    print(f'Inhalt der JSON-Datei: {gelesene_daten}')
