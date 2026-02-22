"""
Du sollst eine Python-Funktion namens verbessere_quicksort schreiben, die den Quicksort-Algorithmus implementiert 
und zusätzlich eine Verbesserung beinhaltet: Bevor die eigentliche Sortierung beginnt, soll überprüft werden, 
ob die Liste bereits sortiert ist. 
Ist dies der Fall, gibt die Funktion die Liste direkt zurück, ohne den Quicksort-Algorithmus durchzuführen. 
Diese Überprüfung soll durch eine Zusicherung (assert) realisiert werden, die sicherstellt, 
dass die Funktion nur dann den Quicksort-Algorithmus ausführt, wenn die Liste nicht bereits sortiert ist. 
Implementiere außerdem eine einfache Debugging-Ausgabe, die den Zustand der Liste vor und nach der Sortierung in die Konsole schreibt, 
sofern die Umgebungsvariable DEBUG auf True gesetzt ist.
 """
import os


def ist_sortiert(s):
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))


def verbessere_quicksort(liste):
    """Sortiert die uebergebene Liste mit einer verbesserten Quicksort-Implementierung."""
    debug = os.getenv("DEBUG", "False") == "True"

    if ist_sortiert(liste):
        if debug:
            print("Die Liste ist bereits sortiert:", liste)
        return liste

    assert not ist_sortiert(liste), "Die Liste ist bereits sortiert"

    if debug:
        print("Vor der Sortierung:", liste)

    def quicksort(s):
        if len(s) <= 1:
            return s
        pivot = s[0]
        s1 = [x for x in s[1:] if x < pivot]
        s2 = [x for x in s[1:] if x >= pivot]
        return quicksort(s1) + [pivot] + quicksort(s2)

    sorted_list = quicksort(liste)

    if debug:
        print("Nach der Sortierung:", sorted_list)

    return sorted_list
    
    # Beispielaufruf
if __name__ == "__main__":
    import os
    os.environ['DEBUG'] = 'True'  # Setze DEBUG auf True für Debugging-Ausgaben
    test_liste = [3, 6, 8, 10, 1, 2, 1]
    print("Sortierte Liste:", verbessere_quicksort(test_liste))