from tkinter import Tk, Label, Button
from random import choice
import random

# Funktionen
def zufallsfarbe():
    z = '0123456789abcdef'
    return '#' + choice(z) + choice(z) + choice(z)

def farben_ändern():
    for feld in felder:
        feld.config(bg=zufallsfarbe())

# Hauptprogramm
fenster = Tk()
felder = []
for i in range(5):
    for j in range(5):
        feld = Label(
            master=fenster,
            width=8,
            height=2
            )
        felder.append(feld)
        feld.grid(
            column=i,
            row=j,
            padx=1,
            pady=1
            )
button = Button(
    master=fenster,
    text='Neue Farben',
    command=farben_ändern
    )
button.grid(
    column=0,
    row=5,
    columnspan=5
    )
fenster.mainloop()
