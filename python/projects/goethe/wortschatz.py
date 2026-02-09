# Textquelle: faust.txt von https://github.com/martinth/mobverdb
# Original: https://github.com/martinth/mobverdb/blob/master/faust.txt

PFAD = 'python/projects/goethe/faust.txt'
f = open(PFAD, mode='r', encoding='utf-8')  #2
text = f.read()  #3
f.close()

# Nur den Text zwischen den Markern verwenden
start_marker = '*** START OF THIS PROJECT GUTENBERG EBOOK'
end_marker = '*** END OF THIS PROJECT GUTENBERG EBOOK'

start_pos = text.find(start_marker)
end_pos = text.find(end_marker)

if start_pos != -1:
    # Text nach dem Start-Marker beginnen
    text = text[start_pos + len(start_marker):]
    
if end_pos != -1:
    # Text vor dem End-Marker beenden
    text = text[:end_pos - start_pos - len(start_marker)]

text = text.lower()  #4

# Alle Satzzeichen durch Leerzeichen ersetzen
for p in '.,:;-?!()_/[]':  #5
    text = text.replace(p, ' ')

wortliste = text.split()  #6
wortmenge = set(wortliste)  #7
print('=' * 70)
print('Wörter insgesamt:', len(wortliste))
print('Unterschiedliche Wörter:', len(wortmenge))
print('=' * 70)
print('Erste 50 unterschiedliche Wörter: ')
print(list(wortmenge)[:50])  #8 - Erste 50 unterschiedliche Wörter
print('=' * 70)
print('Erste 50 unterschiedliche Wörter (alphabetisch sortiert): ')
print(sorted(wortmenge)[:50])
print('=' * 70)

#2:** Datei im Lesemodus (`'r'`) mit UTF-8 Kodierung öffnen
#3:** Gesamten Dateiinhalt als String einlesen
#4:** Alle Buchstaben in Kleinbuchstaben umwandeln
#5:** Schleife über alle Satzzeichen, die entfernt werden sollen
#6:** Text in Liste von Wörtern aufteilen (bei Leerzeichen)
#7:** Menge erstellen → automatisches Entfernen von Duplikaten
#8:** Erste 50 unterschiedliche Wörter ausgeben

