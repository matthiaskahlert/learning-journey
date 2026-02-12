""" a) Definiere eine Variable text, die einen mehrzeiligen String speichert, welcher Sonderzeichen und Unicode-Zeichen enthält. 
Verwende mindestens drei verschiedene Escape-Sequenzen und zwei Unicode-Zeichen 
Emn(z.B. ein Emoji und ein Zeichen aus einem anderen Schriftsystem).
b) Zähle, wie oft ein bestimmtes Wort in text vorkommt. Das Wort soll als Eingabe über die Konsole gegeben werden.
c) Ersetze in text alle Vorkommen eines bestimmten Wortes (ebenfalls über die Konsole eingegeben) 
durch ein anderes Wort (auch über die Konsole eingegeben) und gib den neuen Text aus.
d) Speichere den modifizierten Text in einer Datei mit dem Namen modifizierter_text.txt unter Verwendung der with-Anweisung.
e) Dies eine Datei namens daten.json, die eine Liste von Dictionaries enthält, ein. 
Verwende das JSON-Modul, um die Datei zu laden. Gib anschließend die Daten in der Konsole aus. """ 

import json

# a) Mehrzeiliger String mit Escape-Sequenzen und Unicode-Zeichen
text = """
Zeile 1: Hallo\nDas ist ein mehrzeiliger Text.\tHier ist ein Tab.
Zeile 2: Ein Backslash: \\ und ein Anführungszeichen: \".
Zeile 3: Emoji: 😊, Chinesisches Zeichen: 汉
Zeile 4: Noch ein Emoji: 🚀
"""

# b) Wort zählen
wort = input("Welches Wort soll gezählt werden? ")
anzahl = text.count(wort)
print(f"Das Wort '{wort}' kommt {anzahl} mal vor.")

# c) Wort ersetzen
zu_ersetzen = input("Welches Wort soll ersetzt werden? ")
ersatz = input("Wodurch soll es ersetzt werden? ")
text_modifiziert = text.replace(zu_ersetzen, ersatz)
print("\nModifizierter Text:")
print(text_modifiziert)

# d) Modifizierten Text speichern
with open("python\exercises\Kapitel 9 Uebungen\modifizierter_text.txt", "w", encoding="utf-8") as f:
	f.write(text_modifiziert)

# e) JSON-Datei laden und ausgeben
try:
	with open("python\exercises\Kapitel 9 Uebungen\daten.json", "r", encoding="utf-8") as f:
		daten = json.load(f)
	print("\nDaten aus daten.json:")
	print(daten)
except FileNotFoundError:
	print("daten.json nicht gefunden.")
	
   
