# umbenennen.py
import os

EXTENSIONS = ['.png', '.bmp', '.jpg']

def umbenennen(präfix, verzeichnis):
	anzahl = 0
	os.chdir(verzeichnis)
	for name in os.listdir():
		_, ext = os.path.splitext(name)
		if ext.lower() in EXTENSIONS:
			neuer_name = präfix + name
			os.rename(name, neuer_name)
			anzahl += 1
	return anzahl

# Hauptprogramm
if __name__ == "__main__":
	präfix = input('Geben Sie ein Präfix an: ')
	verzeichnis = input('Zielverzeichnis: ')
	while not os.path.exists(verzeichnis):
		print('Pfad existiert nicht.')
		verzeichnis = input('Zielverzeichnis: ')
	n = umbenennen(präfix, verzeichnis)
	print('Es wurden {} Dateien umbenannt.'.format(n))
