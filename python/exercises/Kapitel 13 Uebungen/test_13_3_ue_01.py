from uebung_13_3_ue_01 import filtere_gerade_zahlen, sortiere_liste

def test_filtere_gerade_zahlen():
    test_liste = [10, -4, 7, 0, -9, 2, -3, 8]
    assert filtere_gerade_zahlen(test_liste) == [10, -4, 0, 2, 8]

def test_sortiere_liste():
    assert sortiere_liste([10, -4, 0, 2, 8]) == [-4, 0, 2, 8, 10]