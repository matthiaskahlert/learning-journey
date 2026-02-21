""" 
Erstelle ein Python-Skript, das ein Tkinter-Fenster mit folgenden Widgets und Funktionalitäten enthält:

a) Ein Label, das "Wähle deine Lieblingsfarbe:" anzeigt.
b) Drei Radiobuttons zur Auswahl zwischen "Rot", "Grün" und "Blau".
c) Ein Button mit der Beschriftung "Bestätigen", der bei Klick eine Funktion ausführt, die den Namen der ausgewählten Farbe in einem separaten Label anzeigt.
d) Ein Canvas-Widget, das bei Auswahl einer Farbe und Klick auf den "Bestätigen"-Button, den Hintergrund des Canvas entsprechend der ausgewählten Farbe ändert.
e) Verwende für die Radiobuttons eine gemeinsame Kontrollvariable.
f) Stelle sicher, dass das Fenster ein Raster-Layout verwendet, um die Widgets zu organisieren. 
 """

from tkinter import *

def farbe_anzeigen():
    ausgewaehlte_farbe = farbwahl.get()
    farbanzeige_label.config(text=f"Ausgewählte Farbe: {ausgewaehlte_farbe}")
    canvas.config(bg=ausgewaehlte_farbe.lower())

fenster = Tk()
fenster.title("Farbwahl")

farbwahl = StringVar()
farbwahl.set("Rot")  # Standardauswahl

# Widgets
label = Label(fenster, text="Wähle deine Lieblingsfarbe:")
label.grid(row=0, column=0, columnspan=2)

rot_rb = Radiobutton(fenster, text="Rot", variable=farbwahl, value="Rot")
rot_rb.grid(row=1, column=0)

gruen_rb = Radiobutton(fenster, text="Grün", variable=farbwahl, value="Grün")
gruen_rb.grid(row=1, column=1)

blau_rb = Radiobutton(fenster, text="Blau", variable=farbwahl, value="Blau")
blau_rb.grid(row=1, column=2)

bestaetigen_button = Button(fenster, text="Bestätigen", command=farbe_anzeigen)
bestaetigen_button.grid(row=2, column=0, columnspan=3)

farbanzeige_label = Label(fenster, text="Ausgewählte Farbe: Rot")
farbanzeige_label.grid(row=3, column=0, columnspan=3)

canvas = Canvas(fenster, width=200, height=100, bg="red")
canvas.grid(row=4, column=0, columnspan=3)

fenster.mainloop()