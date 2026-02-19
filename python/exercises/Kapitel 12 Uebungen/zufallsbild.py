# ad_reinhardt.pyw
from canvasvg import saveall
from tkinter import *
from random import choice
from time import asctime

def neue_farbe():
    Z= '0123456789ABCDEF'
    return '#' + choice(Z) + choice(Z) + choice(Z)

def malen():
    global id0, id1, id2
    id0 = bild.create_rectangle(
        0,0,250,300,
        fill=neue_farbe(),
        outline='')
    id1= bild.create_rectangle(
        100,0,150,300,
        fill=neue_farbe(),
        outline='')
    id2 = bild.create_rectangle(
        0,100,250,200,
        fill=neue_farbe(),
        outline='')

def löschen():
    bild.delete(id0)
    bild.delete(id1)
    bild.delete(id2)

def speichern():
    zeitstempel=asctime()
    for ch in ' :. ':
        zeitstempel = zeitstempel.replace(ch, '')
    saveall(r'python\exercises\Kapitel 11 Uebungen\Kapitel 12 Uebungen\bild'+zeitstempel+'.svg', bild) # der parameter r sorgt dafür, dass die backslashes nicht als escape zeichen interpretiert werden

fenster = Tk()
button_malen = Button(
    master=fenster,
    text='Malen', command=malen)
button_löschen = Button(
    master=fenster,
    text='Löschen', command=löschen)
button_speichern = Button(
    master=fenster,
    text='Speichern', command=speichern)
bild = Canvas(
    master=fenster,
    width = 250,
    height = 300)

button_malen.pack(side=LEFT)
button_löschen.pack(side=LEFT)
button_speichern.pack(side=LEFT)
bild.pack()
fenster.mainloop()