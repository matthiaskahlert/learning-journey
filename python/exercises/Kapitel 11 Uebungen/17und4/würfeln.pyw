from tkinter import *
from random import randint
summe = 0

def würfeln():
    global summe
    text = label.cget('text')
    zahl = randint(1, 6)
    summe += zahl # Zur Summe der bereits „gewürfelten“ Zahlen wird die neue Zahl hinzuaddiert
    label.config(text=text + ' ' + str(zahl))
    if summe > 21:
        label.config(bg='yellow')

def löschen():
    global summe
    summe = 0
    label.config(text='', bg='white')

# Widgets
fenster = Tk()
bild_würfel = PhotoImage(file=r'python\exercises\Kapitel 11 Uebungen\17und4\würfel.png')
bild_löschen = PhotoImage(file=r'python\exercises\Kapitel 11 Uebungen\17und4\eimer.png')
label = Label(
    master=fenster, width=16,
    font=('Arial', 30),
    text='',
    bg='white'
    )
b_würfeln = Button(
    master=fenster, image=bild_würfel,
    command=würfeln
)
b_löschen = Button(
    master=fenster, image=bild_löschen,
    command=löschen
)


# Layout
label.pack ()
b_würfeln.pack(side=LEFT, padx=30, pady=10)
b_löschen.pack(side=RIGHT, padx=30, pady=10)
fenster.mainloop()