from geld import Geld
from tkinter import Button, Tk, Text, LEFT, END

class App():
    def __init__(self):
        self.fenster = Tk()
        self.text = Text(master=self.fenster, width=30, height=6)
        self.button = Button(master=self.fenster, text='Abrechnen', command=self.abrechnen)
        self.text.pack()
        self.button.pack(side=LEFT, padx=5, pady=5)
        self.fenster.mainloop()
    
    def abrechnen(self):
        text = self.text.get(1.0, END)
        zeilen = text.split('\n')
        summe = Geld('EUR', 0)
        for z in zeilen:
            try:
                währung, betrag = z.split()
                summe = summe + Geld(währung, betrag)
            except:
                pass
        self.text.insert(END, '\n\nSumme: ' + str(summe))
""" 
trägt man in das widget nun unterschiedliche währungen wie 
EUR 120
USD 70
USD 12.30
ein, so werden sie zusammengerechnet.
 """
App()