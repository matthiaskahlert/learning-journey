from tkinter import Tk, Label, Button
from random import choice

NEON_FARBEN = [
    '#f000ff',  # Ultra Neon Lila
    '#00ff00',  # Laser Grün
    '#00ffff',  # Elektrisches Cyan
    '#ffea00',  # Highlighter Gelb
    '#ff3cff',  # Toxic Pink
    '#ff2fd6',  # Neon Pink
    '#00fff7',  # Neon Cyan
    '#ffe600',  # Neon Gelb
    '#39ff14',  # Neon Grün
    '#1e90ff',  # Neon Blau
    '#ff9900',  # Neon Orange    
    '#ff073a',  # Neon Rot
    '#ff00ff',  # Neon Magenta
    '#ccff00',  # Neon Limette
    '#00ff9f',  # Neon Mint
    '#00b3ff',  # Neon Sky Blue
    '#ff5f1f',  # Neon Koralle
    '#ff1493',  # Neon Hot Pink
    '#7fff00',  # Neon Chartreuse
    '#00ffcc',  # Neon Türkis
    '#ff00a6',  # Neon Fuchsia
]

# Funktion zum Ändern der Farben
def farben_ändern():
    for feld in felder:
        feld.config(bg=choice(NEON_FARBEN))

# Hauptprogramm
fenster = Tk()
felder = []

for i in range(5):
    for j in range(5):
        feld = Label(
            master=fenster,
            width=8,
            height=2,
            bg=choice(NEON_FARBEN)
        )
        feld.grid(column=i, row=j, padx=1, pady=1)
        felder.append(feld)

button = Button(
    master=fenster,
    text='Neue Farben',
    command=farben_ändern
)
button.grid(column=0, row=5, columnspan=5)

fenster.mainloop()