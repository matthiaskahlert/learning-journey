# waehrungsrechner.pyw
from tkinter import *
D = {'USD' : 1.22, 'GBP' :0.91, 'JPY' :126.7}

def berechnen():
    euros = float(eingabe.get())
    ergebnis = euros * D[währung.get()] # währung.get() → liefert z. B. 'USD' - D['USD'] → liefert 1.22 - Multiplikation mit Euro-Betrag
    ausgabetext = '{} {}'.format(ergebnis, währung.get())
    ausgabe.config(text=ausgabetext)

fenster = Tk()
fenster.title('Wahrungsrechner')
währung = StringVar() # speichert den aktuell ausgewählten Wert der Radiobutton-Gruppe.
usd = Radiobutton(
    master=fenster,
    text='Dollar',
    value='USD', # Wert der gespeichert wird, wenn dieser button aktiv ist, analog bei GBP und JPY
    variable=währung) # Alle Buttons gehören zur gleichen Gruppe, da sie die gleiche Variable verwenden.
gbp = Radiobutton(
    master=fenster,
    text='Britisches Pfund',
    value= 'GBP',
    variable=währung)
jpy = Radiobutton(
    master=fenster,
    text='Japanischer Yen',
    value='JPY',
    variable=währung)
ausgabe = Label (
    master=fenster,
    bg='blue',
    fg='white',
    font=('Arial', 25),
    width=15)
label = Label(
    master=fenster,
    text='Euros: '
)
usd.select() # Damit ist „Dollar“ beim Start automatisch aktiv.
eingabe = Entry(master=fenster)
button = Button(
    master=fenster,
    text='Rechnen',
    command=berechnen)
ausgabe. pack()
usd.pack (anchor=W)
gbp.pack(anchor=W)
jpy.pack (anchor=W)
label.pack(side=LEFT)
eingabe.pack(side=LEFT)
button.pack(side=LEFT)
fenster.mainloop()
