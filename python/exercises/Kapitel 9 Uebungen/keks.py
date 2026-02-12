from random import choice

AUFFORDERUNGEN = [
    "Begrüße", "Achte", "Genieße", "Entdecke", "Erkenne", "Feiere", "Schätze"
]
OBJEKTE = [
    "die Leidenschaft", "das Leben", "die Freundschaft", "den Moment", "die Freude", "die Natur"
]

def glueckskeks():
    print(f"{choice(AUFFORDERUNGEN)} {choice(OBJEKTE)}!")

while True:
    glueckskeks()
    antwort = input("(N)euer Glückskeks (E)nde: ").strip().lower()
    if antwort == "e":
        print("Bis bald!")
        break