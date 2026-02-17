""" Erstelle ein Python-Programm, das ein Tkinter-Anwendungsfenster mit folgenden Widgets und Funktionalitäten erzeugt:

a) Ein Label-Widget, das "Hallo Welt!" anzeigt. Verwende dabei eine Schriftart deiner Wahl mit einer Größe von 14 Punkten.
b) Ein Entry-Widget, in das Nutzer Text eingeben können.
c) Zwei Button-Widgets: Der erste Button soll den Text im Entry-Widget löschen, wenn er geklickt wird. 
Der zweite Button soll das Anwendungsfenster schließen.
d) Verwende Schleifen, um eine Liste von Tupeln zu erstellen, 
die jeweils die Texte für die Buttons und die zugehörigen Funktionen 
(zum Löschen des Textes und zum Schließen des Fensters) enthalten. 
Füge die Buttons basierend auf dieser Liste ins Anwendungsfenster ein.
e) Gestalte das Anwendungsfenster so, dass das Label oben erscheint, 
das Entry-Widget darunter und die Buttons am unteren Rand des Fensters angeordnet sind.
f) Verwende die pack()-Methode für das Layoutmanagement aller Widgets.
g) Schreibe Kommentare zu deinem Code, um die Funktionsweise der verschiedenen Teile zu erklären.
h) Stelle sicher, dass das Programm fehlerfrei läuft und alle Widgets wie beschrieben funktionieren.  """
from tkinter import Tk, Label, Entry, Button, Frame
from tkinter.font import BOLD

# Fenster erstellen
fenster = Tk()
fenster.title('Hallo Welt!')
fenster.geometry('400x200')

# a) Label oben anzeigen
label = Label(
    master=fenster,
    text='Hallo Welt!',
    font=('Courier', 14, BOLD),
    fg='blue',      # Schriftfarbe
    bg='gray',      # Hintergrundfarbe
    bd=5,           # Rahmenbreite
    relief='ridge'  # Rahmenstil
)
label.pack(side='top', fill='x', pady=10)

# b) Entry-Widget für Benutzereingabe
entry = Entry(master=fenster, font=('Arial', 12))
entry.pack(pady=10)

# c) Funktionen für Buttons
def clear_entry():
    """Löscht den Text im Entry-Widget"""
    entry.delete(0, 'end')

def close_window():
    """Schließt das Fenster"""
    fenster.destroy()

# d) Liste von Buttons mit Text und Funktion
buttons = [
    ('Text löschen', clear_entry),
    ('Fenster schließen', close_window)
]

# Frame für Buttons erstellen (unten)
button_frame = Frame(master=fenster)
button_frame.pack(side='bottom', pady=10)

# Buttons erstellen und in den Button-Frame packen
for text, command in buttons:
    button = Button(master=button_frame, text=text, command=command)
    button.pack(side='left', padx=10)  # horizontal nebeneinander

# h) Hauptloop starten
fenster.mainloop()
