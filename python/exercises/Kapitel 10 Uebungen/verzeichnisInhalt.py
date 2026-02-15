import os

while True:
    cwd = os.getcwd()
    print(f"Arbeitsverzeichnis: {cwd}")
    print("Inhalt:")
    for item in os.listdir():
        print(item)
    verzeichnis = input("Gewünschtes Verzeichnis: ")
    if not verzeichnis:
        print("Auf Wiedersehen")
        break
    if os.path.isdir(verzeichnis):
        os.chdir(verzeichnis)
    else:
        print("Verzeichnis existiert nicht.")
