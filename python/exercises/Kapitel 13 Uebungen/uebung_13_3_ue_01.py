""" 
a) Definiere eine Funktion filtere_gerade_zahlen, die eine Liste von Zahlen als Argument nimmt 
und eine neue Liste zurückgibt, die nur die geraden Zahlen enthält. Verwende dazu eine Schleife, 
um durch die Liste zu iterieren.

b) Füge am Anfang der Funktion eine Zusicherung ein, die sicherstellt, dass das übergebene Argument eine Liste ist. 
Falls das Argument keine Liste ist, soll das Programm mit einer AssertionError enden.

c) Schreibe eine zweite Funktion sortiere_liste, die eine Liste von Zahlen nimmt und diese mit dem Quicksort-Algorithmus sortiert. 
Du kannst die Implementierung des Quicksort-Algorithmus selbst wählen, achte aber darauf, dass du den Algorithmus korrekt implementierst.

d) Verwende die Funktion filtere_gerade_zahlen, um eine Liste von Zahlen zu filtern, 
und verwende dann die Funktion sortiere_liste, um die gefilterte Liste zu sortieren. 
Gib das Ergebnis aus.

e) Füge am Ende des Skripts eine Testroutine ein, die deine Funktionen mit einer vorgegebenen Liste von Zahlen testet. 
Die Liste soll sowohl positive als auch negative Zahlen sowie Null enthalten. 
 """
#a)
def filtere_gerade_zahlen(liste):
    """Filtert gerade Zahlen aus der übergebenen Liste."""
    #b)
    assert isinstance(liste, list), "Das Argument muss eine Liste sein" # prüft, ob das Argument eine Liste ist und gibt fehlermneldung aus, wenn nicht
    gerade_zahlen = []
    for zahl in liste:
        if zahl % 2 == 0:
            gerade_zahlen.append(zahl)
    return gerade_zahlen

def sortiere_liste(liste):
    """Sortiert die übergebene Liste mit dem Quicksort-Algorithmus."""
    if len(liste) <= 1:
        return liste
    else:
        pivot = liste[0]
        s1 = [x for x in liste[1:] if x < pivot]
        s2 = [x for x in liste[1:] if x >= pivot]
        return sortiere_liste(s1) + [pivot] + sortiere_liste(s2)
    
#d)
zahlen = [3, -1, 4, 0, -5, 2, -3]
gefilterte_zahlen = filtere_gerade_zahlen(zahlen)
sortierte_zahlen = sortiere_liste(gefilterte_zahlen)
print("Liste von Zahlen:", zahlen)
print("Gefilterte gerade Zahlen:", gefilterte_zahlen)
print("Sortierte gerade Zahlen:", sortierte_zahlen)


#e)

if __name__ == "__main__":
    test_liste = [10, -4, 7, 0, -9, 2, -3, 8]

    assert filtere_gerade_zahlen(test_liste) == [10, -4, 0, 2, 8]
    assert sortiere_liste([10, -4, 0, 2, 8]) == [-4, 0, 2, 8, 10]

    print("Alle Tests erfolgreich bestanden.")