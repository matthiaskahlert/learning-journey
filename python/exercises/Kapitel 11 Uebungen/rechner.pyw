# rechner.py
from tkinter import Tk, Label, Button, Entry, LEFT

def rechnen():
    ausdruck = eingabe.get()
    try:
        ergebnis = eval(ausdruck)
    except:
        ergebnis = 'Ungültiger Ausdruck'
    ausgabe.config(text=ergebnis)

fenster = Tk()
fenster.title('Rechner')

ausgabe = Label(master=fenster, width=20, height=2, font=('Arial', 12))
eingabe = Entry(master=fenster, font=('Arial', 12))
button = Button(master=fenster,
                text='Rechnen',
                font=('Arial', 12),
                command=rechnen)

ausgabe.pack()
eingabe.pack(side=LEFT, padx=5, pady=5)
button.pack(side=LEFT, padx=5, pady=5)

fenster.mainloop()
