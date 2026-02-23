# farbtester.pyw Ein programm für einen interaktiven RGB Farbmischer
from tkinter import Button, Label, Tk, LEFT

class Taste(Button):
    """
    Klasse Taste erbt von: Button (Tkinter)
    Schaltfläche, die eine Hexadezimalziffer anzeigt
    Die Ziffernfolge ist 0123456789ABCDEF, die für die Farbcodierung in HTML verwendet wird.
    Die Methode drücken erhöht die Ziffer um 1, wobei nach F wieder bei 0 begonnen wird."""
    ziffern = '0123456789ABCDEF'
    def __init__(self, app):
        self.i = 0
        self.app = app
        Button.__init__(
            self, master=app,
            text=self.ziffern[self.i],
            command=self.drücken,
            font=('Arial', 16), width=3            
        )

    def drücken(self):
        self.i = (self.i + 1) % 16
        self.config(text=self.ziffern[self.i])
        self.app.farbe_anzeigen()
        
    def ziffer(self):
        return self.ziffern[self.i]

class App(Tk):
    """Anwendungsfenster
    die Klasse App erbt von: Tk (Tkinter-Hauptfenster)
    Das Fenster enthält drei Tasten, die jeweils eine Hexadezimalziffer anzeigen.
    Die Hintergrundfarbe des Fensters wird durch die Kombination der Ziffern der drei Tasten bestimmt."""
    
    def __init__(self):
        Tk.__init__(self)
        self.label=Label(master=self, width=20, height=6)
        self.tasten = [Taste(self) for i in range(3)]
        
        #Layout
        self.label.pack()
        for t in self.tasten:
            t.pack(side=LEFT, padx=5, pady=5)
        self.farbe_anzeigen()
        self.mainloop()
        
    def farbe_anzeigen(self):
        r, g, b = [t.ziffer() for t in self.tasten]
        code = '#' + r + g + b
        self.label.config(bg=code)

App()
