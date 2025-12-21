""" 
Entwickle eine Python-Funktion namens filtere_gerade_zahlen, 
die eine Liste von Zahlen als Argument nimmt 
und mithilfe der filter()-Funktion alle geraden Zahlen aus dieser Liste zurückgibt. 
Verwende eine Lambda-Funktion, um zu bestimmen, ob eine Zahl gerade ist. 
Die Funktion soll die gefilterten Zahlen als Liste zurückgeben. 
Teste deine Funktion mit einer Liste von Zahlen und gib das Ergebnis mit der print()-Funktion aus. 
Verwende für deine Tests die Liste [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
und stelle sicher, dass deine Funktion korrekt implementiert ist, indem du das Ergebnis überprüfst.  
"""

# b)
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def filtere_gerade_zahlen(zahlen):
    
    gefilterte_zahlen = list(
        filter(
            lambda zahl: zahl % 2 == 0, # diese lambda funktion wird von filter() genutzt um die elemente von "zahlen" abzugleichen
            zahlen
        )
    )
    return gefilterte_zahlen # enthält nur werte bei denen die lambda funktion true zurückgab

# mini test auf lowercase
print(filtere_gerade_zahlen(zahlen))
