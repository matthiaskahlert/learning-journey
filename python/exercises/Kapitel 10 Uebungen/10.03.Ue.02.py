""" 
a) Erstelle eine Funktion erstelle_datei, die eine neue Textdatei mit einem vorgegebenen Namen und Inhalt 
in einem spezifischen Verzeichnis erstellt. 
Verwende dazu die with-Anweisung und stelle sicher, dass Fehler, wie z.B. fehlende Schreibberechtigungen, 
mit try und except abgefangen werden.
b) Implementiere eine Funktion listdir_filter, die alle Dateien eines Verzeichnisses auflistet, 
die eine bestimmte Dateiendung haben (z.B. .txt). Nutze dazu das Modul os und eine List Comprehension.
c) Schreibe eine Funktion umbenennen_dateien, die alle Dateien eines Verzeichnisses, 
die eine bestimmte Endung haben, umbenennt, indem sie ein Präfix hinzufügt. Verwende dazu das Modul os.
d) Entwickle eine Funktion json_speichern, die eine Liste von Dictionaries in eine Datei im JSON-Format speichert. 
Verwende dazu das Modul json.
e) Implementiere eine Funktion json_laden, die eine JSON-Datei liest und den Inhalt als Python-Objekt zurückgibt.
f) Erstelle eine Funktion regex_suche, die in allen .txt-Dateien eines Verzeichnisses nach einem 
regulären Ausdruck sucht und die Namen der Dateien zurückgibt, in denen die Suche erfolgreich war.
Für jede dieser Funktionen sollst du ein kurzes Beispiel für deren Aufruf und Verwendung schreiben. 
 """
import os
import json
import re

def erstelle_datei(verzeichnis, dateiname, inhalt):
	"""Erstellt eine Textdatei mit gegebenem Namen und Inhalt im angegebenen Verzeichnis."""
	pfad = os.path.join(verzeichnis, dateiname)
	try:
		with open(pfad, 'w', encoding='utf-8') as f:
			f.write(inhalt)
		print(f"Datei '{pfad}' wurde erstellt.")
	except Exception as e:
		print(f"Fehler beim Erstellen der Datei: {e}")

def listdir_filter(verzeichnis, endung):
	"""Listet alle Dateien mit bestimmter Endung im Verzeichnis auf."""
	return [f for f in os.listdir(verzeichnis) if f.endswith(endung) and os.path.isfile(os.path.join(verzeichnis, f))]

def umbenennen_dateien(verzeichnis, endung, praefix):
	"""Benennt alle Dateien mit bestimmter Endung um, indem ein Präfix hinzugefügt wird."""
	for f in os.listdir(verzeichnis):
		if f.endswith(endung):
			alt = os.path.join(verzeichnis, f)
			neu = os.path.join(verzeichnis, praefix + f)
			os.rename(alt, neu)
			print(f"Umbenannt: {alt} -> {neu}")

def json_speichern(liste, dateiname):
	"""Speichert eine Liste von Dictionaries als JSON-Datei."""
	try:
		with open(dateiname, 'w', encoding='utf-8') as f:
			json.dump(liste, f, ensure_ascii=False, indent=2)
		print(f"JSON gespeichert in {dateiname}")
	except Exception as e:
		print(f"Fehler beim Speichern: {e}")

def json_laden(dateiname):
	"""Lädt eine JSON-Datei und gibt das Python-Objekt zurück."""
	try:
		with open(dateiname, 'r', encoding='utf-8') as f:
			return json.load(f)
	except Exception as e:
		print(f"Fehler beim Laden: {e}")
		return None

def regex_suche(verzeichnis, muster):
	"""Sucht in allen .txt-Dateien eines Verzeichnisses nach einem regulären Ausdruck."""
	treffer = []
	for f in os.listdir(verzeichnis):
		if f.endswith('.txt'):
			pfad = os.path.join(verzeichnis, f)
			try:
				with open(pfad, 'r', encoding='utf-8') as datei:
					inhalt = datei.read()
					if re.search(muster, inhalt):
						treffer.append(f)
			except Exception as e:
				print(f"Fehler beim Lesen von {f}: {e}")
	return treffer

# Beispielaufrufe
if __name__ == "__main__":
	verzeichnis = r"C:\Users\Matze\repositories\learning-journey\python\exercises\Kapitel 10 Uebungen\testverzeichnis"
	os.makedirs(verzeichnis, exist_ok=True)
	erstelle_datei(verzeichnis, "a.txt", "Hallo Welt!")
	erstelle_datei(verzeichnis, "b.txt", "Python ist toll.")
	erstelle_datei(verzeichnis, "c.md", "Markdown Datei.")
	print(".txt-Dateien:", listdir_filter(verzeichnis, ".txt"))
	umbenennen_dateien(verzeichnis, ".txt", "NEU_")
	daten = [{"name": "Max", "alter": 25}, {"name": "Anna", "alter": 30}]
	json_datei = os.path.join(verzeichnis, "daten.json")
	json_speichern(daten, json_datei)
	print("Geladen:", json_laden(json_datei))
	print("Regex-Suche (Welt):", regex_suche(verzeichnis, r"Welt"))
