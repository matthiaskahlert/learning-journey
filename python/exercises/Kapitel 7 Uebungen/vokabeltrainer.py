from random import choice
def aufgabe(d):
    """
    Stellt eine zufällige Vokabelabfrage.

    Wählt zufällig einen englischen Begriff aus dem übergebenen Dictionary,
    fordert den Benutzer zur Eingabe einer deutschen Übersetzung auf und
    prüft die Antwort.

    - Bei falscher Antwort werden alle korrekten Übersetzungen ausgegeben.
    - Bei richtiger Antwort wird die Vokabel aus dem Dictionary entfernt.

    :param d: Dictionary mit englischen Vokabeln als Schlüssel und
              Listen deutscher Übersetzungen als Werte
    :type d: dict[str, list[str]]
    """
    vokabel = choice(list(d.keys()))
    print('Nennen Sie ein deutsches Wort für', vokabel + '!')
    antwort = input('Deutsches wort: ')
    if antwort not in d[vokabel]:
        print("Leider Falsch!")
        print(vokabel, 'bedeutet:', end=' ')#  end=' ' bewirkt, dass kein Zeilenumbruch erfolgt
        for wort in d[vokabel]:
            print(wort, end=' ')
        print('\n')
    else:
        print("Richtig!")
        print(vokabel, 'bedeutet:', end=' ')#  end=' ' bewirkt, dass kein Zeilenumbruch erfolgt
        for wort in d[vokabel]:
            print(wort, end=' ')
        print('\n')
        del d[vokabel]

d = {
'variable': ['Variable'],
'value': ['Wert'],
'key': ['Schlüssel'],
'type': ['Typ', 'Datentyp'],
'string': ['Zeichenkette', 'Text'],
'number': ['Zahl', 'Nummer'],
'integer': ['Ganzzahl', 'Integer'],
'float': ['Gleitkommazahl', 'Fließkommazahl'],
'boolean': ['Boolescher Wert', 'wahr/falsch', 'Bool'],
'expression': ['Ausdruck'],
'statement': ['Anweisung', 'Statement'],
'condition': ['Bedingung', 'Kondition'],
'loop': ['Schleife'],
'while': ['solange', 'während'],
'for': ['für'],
'if': ['wenn', 'falls'],
'else': ['sonst', 'dann'],
'elif': ['sonst wenn', 'else if', 'dann wenn'],
'break': ['abbrechen', 'unterbrechen', 'Beenden'],
'continue': ['fortfahren', 'weiter'],
'function': ['Funktion'],
'argument': ['Argument', 'Übergabewert'],
'parameter': ['Parameter', 'Übergabeparameter'],
'return': ['Rückgabewert'],
'call': ['aufrufen', 'Aufruf'],
'define': ['definieren'],
'module': ['Modul'],
'import': ['importieren', 'Import'],
'library': ['Bibliothek'],
'list': ['Liste'],
'tuple': ['Tupel'],
'dictionary': ['Wörterbuch', 'Dictionary'],
'item': ['Element', 'Eintrag', 'Item'],
'index': ['Index', 'Indexwert'],
'slice': ['Ausschnitt', 'Stück', 'Schnitt'],
'length': ['Länge'],
'error': ['Fehler', 'Bug'],
'exception': ['Ausnahme', 'Exception'],
'traceback': ['Fehlerrückverfolgung', 'Rückverfolgung'],
'syntax': ['Syntax'],
'runtime': ['Laufzeit'],
'bug': ['Fehler'],
'debug': ['debuggen', 'Fehler suchen'],
'test': ['Test'],
'output': ['Ausgabe'],
'input': ['Eingabe'],
'result': ['Ergebnis', 'Resultat'],
'expected': ['erwartet'],
'actual': ['tatsächlich', 'wirklich'],

}
while d: # Ein leeres Dictionary hat den Wahrheitswert False. Solange das Dictionary Einträge hat, ist der Wahrheitswert True.
    # Solange es true ist, wird das Dictionary d an die Funktion übergeben
    aufgabe(d)
print('Sie haben alle Vokabeln gelernt!') # wenn dictionary leer. geht es hier weiter
eingabe = input()