""" 
Du arbeitest für ein Unternehmen, das eine Software zur Verwaltung von Büchereien entwickelt. 
Deine Aufgabe ist es, ein Python-Programm zu schreiben, das folgende Funktionalitäten bietet:

a) Buchsuche: Eine Funktion suche_buch(titel, autor=None), die Bücher nach Titel und optional nach Autor sucht. 
Die Funktion gibt eine Liste von Büchern zurück, die den Suchkriterien entsprechen. 
Wenn kein Autor angegeben ist, werden alle Bücher mit dem entsprechenden Titel zurückgegeben.

b) Buch hinzufügen: Eine Funktion fuege_buch_hinzu(titel, autor, jahr), die ein neues Buch zur Bücherei-Datenbank hinzufügt. 
Die Datenbank wird als Liste von Wörterbüchern dargestellt, wobei jedes Wörterbuch ein Buch repräsentiert.

c) Bücher nach Jahr filtern: 
Eine Funktion buecher_nach_jahr(jahr), die alle Bücher zurückgibt, die in einem bestimmten Jahr veröffentlicht wurden. 
Verwende die filter()-Funktion, um diese Aufgabe zu erfüllen.

d) Anzeige der Bücherei-Datenbank: 
Eine Funktion zeige_datenbank(), die den aktuellen Inhalt der Bücherei-Datenbank in einer formatierten Ausgabe anzeigt. 
Hierbei soll jeder Eintrag folgende Informationen enthalten: Titel, Autor, Erscheinungsjahr.

e) Interaktives Menü: 
Implementiere ein interaktives Menü, das es dem Benutzer ermöglicht, die oben genannten Funktionen auszuführen. 
Verwende eine Schleife mit while, um das Menü kontinuierlich anzuzeigen, bis der Benutzer sich entscheidet, das Programm zu beenden.

Datenbankstruktur (Beispiel):

buecherei_datenbank = [
    {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
    {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
    {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019}
]  
"""
buecherei_datenbank = [
    {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
    {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019},
    {"Titel": "Python lernen", "Autor": "Anna Schmidt", "Jahr": 2022},

    {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
    {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Max Mustermann", "Jahr": 2023},

    {"Titel": "Einführung in die Informatik", "Autor": "Peter Müller", "Jahr": 2018},
    {"Titel": "Einführung in die Informatik", "Autor": "Laura Becker", "Jahr": 2020},

    {"Titel": "Datenstrukturen und Algorithmen", "Autor": "Peter Müller", "Jahr": 2019},
    {"Titel": "Datenstrukturen und Algorithmen", "Autor": "Julia Weber", "Jahr": 2021},

    {"Titel": "Objektorientierte Programmierung", "Autor": "Thomas Klein", "Jahr": 2017},
    {"Titel": "Objektorientierte Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2020},

    {"Titel": "Webentwicklung mit Python", "Autor": "John Doe", "Jahr": 2021},
    {"Titel": "Webentwicklung mit Python", "Autor": "Anna Schmidt", "Jahr": 2023},

    {"Titel": "Datenanalyse mit Python", "Autor": "Max Mustermann", "Jahr": 2022},
    {"Titel": "Datenanalyse mit Python", "Autor": "Laura Becker", "Jahr": 2021}
]
# a)
def suche_buch(titel, autor=None):
    """
    Buchsuche: Eine Funktion, die Bücher nach Titel und optional nach Autor sucht. 
    Wenn kein Autor angegeben ist, werden alle Bücher mit dem entsprechenden Titel zurückgegeben.
    """
    gefunden_buecher = [] # Liste für Rückgabewerte
    for i in buecherei_datenbank:
        if i["Titel"].lower() == titel.lower():
            if autor is None or i["Autor"].lower() == autor.lower():
                print(f'Gefunden: {i["Titel"]} von {i["Autor"]} ({i["Jahr"]})')
                gefunden_buecher.append(i) # buch zur liste hinzufügen

    if not gefunden_buecher:
        if autor:
            print(f'Kein Buch mit dem Titel "{titel}" von "{autor}" gefunden')
        else:
            print(f'Kein Buch mit dem Titel "{titel}" gefunden')

    return gefunden_buecher

# testaufrufe
suche_buch("Datenanalyse mit Python") # mehr als ein autor für titel
suche_buch("Webentwicklung mit Python", "John Doe") # explizit mit autor
suche_buch("cskhbdckh") # titel nicht vorhanden

# b)
def fuege_buch_hinzu(titel, autor, jahr):
    """
    Eine Funktion, die ein neues Buch zur Bücherei-Datenbank hinzufügt.
    """
    neues_buch = {"Titel": titel, "Autor": autor, "Jahr": jahr}
    buecherei_datenbank.append(neues_buch)
    print(f'Ein neues Buch wurde der Bibliothek hinzugefügt: {titel} von {autor} aus dem Jahr {jahr}.')

# testaufrufe
fuege_buch_hinzu("Python für Dummies", "Max Mustermann", 2020) # fügt neues Buch hinzu
suche_buch("Python für Dummies") # prüft ob das buch hinzugefügt wurde

# c)
def buecher_nach_jahr(jahr):
    """
    Eine Funktion, die alle Bücher zurückgibt, die in einem bestimmten Jahr veröffentlicht wurden.   
    """
    gefilterte_buecher = list( # gibt das filterergebnis als liste wieder
        filter(
            lambda buch: buch["Jahr"] == jahr, # diese lambda funktion wird von filter() genutzt um die elemente von buecherei_datenbank abzugleichen
            buecherei_datenbank
        )
    )
    return gefilterte_buecher # enthält nur werte bei denen die lambda funktion true zurückgab

# testaufruf
ergebnis = buecher_nach_jahr(2018)
for buch in ergebnis:
    print(f' Das Suchergebnis lautet: {buch}')

# d)
def zeige_datenbank():
    """
    Eine Funktion, die die Bücherei-Datenbank formatiert mit festen Spaltenbreiten auf der Konsole ausgibt.
    """
    print('-' * 85)
    print(f'{"Titel":55} {"Autor":20} {"Jahr":5}') # 55, 20 und 5 sind die spaltenbreiten
    print('-' * 85)
    for buch in buecherei_datenbank:
        print(f'{buch["Titel"]:55} {buch["Autor"]:20} {buch["Jahr"]:5}')

# testaufruf
zeige_datenbank()

# e)
while True:
    print("\nWählen Sie eine Aktion:")
    print("1. Nach einem Buch in der Bibliothek suchen")
    print("2. Ein Buch hinzufügen")
    print("3. Bücher eines Jahres anzeigen")
    print("4. Datenbank anzeigen")
    print("5. Programm beenden")

    auswahl = input("Ihre Wahl (1/2/3/4/5)?: ")

    if auswahl == '1':
        buch_titel = input("Geben sie den Buchtitel ein: ")
        buch_autor = input("Geben sie den Autor ein oder drücken sie Enter: ")
        autor_gesucht = buch_autor if buch_autor != "" else None
        suche_buch(buch_titel, autor_gesucht)

    elif auswahl == '2':
        neuer_titel = input("Titel des Buches: ")
        neuer_autor = input("Autor: ")
        try:
            neues_jahr = int(input("Erscheinungsjahr: "))
            fuege_buch_hinzu(neuer_titel, neuer_autor, neues_jahr)
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl für das Jahr ein.")

    elif auswahl == '3':
        try:
            suche_jahr = int(input("Jahr eingeben: "))
            ergebnis = buecher_nach_jahr(suche_jahr)
            if ergebnis:
                for buch in ergebnis:
                    print(f'{buch["Titel"]} von {buch["Autor"]} ({buch["Jahr"]})')
            else:
                print(f"Keine Bücher aus dem Jahr {suche_jahr} gefunden.")
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein.")
    
    elif auswahl == '4':
        zeige_datenbank()

    elif auswahl == '5':
        print("Programm wird beendet.")
        break

    else:
        print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")