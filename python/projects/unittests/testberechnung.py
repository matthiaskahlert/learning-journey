# Beispiel-Funktion: Durchschnitt berechnen
def berechne_durchschnitt(zahlen: list[float]) -> float | None:
    """Berechnet den Durchschnitt einer Liste von Zahlen. Gibt None zurück, wenn die Liste leer ist."""
    if len(zahlen) == 0:
        return None

    summe = 0
    anzahl = 0
    for zahl in zahlen:
        summe += zahl
        anzahl += 1
    return summe / anzahl


# --- Mini-Unit-Test ---
def test_berechne_durchschnitt():
    # Test 1: normale Liste
    assert berechne_durchschnitt([10, 20, 30]) == 20
    
    # Test 2: Liste mit einem Element
    assert berechne_durchschnitt([42]) == 42
    
    # Test 3: leere Liste
    assert berechne_durchschnitt([]) is None
    
    # Test 4: Liste mit negativen Zahlen
    assert berechne_durchschnitt([-10, 0, 10]) == 0
    
    print("Alle Tests bestanden ✅")


# Test starten
test_berechne_durchschnitt()
