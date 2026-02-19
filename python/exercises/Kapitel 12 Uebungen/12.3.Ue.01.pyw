
from tkinter import Canvas, StringVar, StringVar, Tk, Label, Entry, Button, Frame
from tkinter.ttk import Radiobutton


# Fenster erstellen
fenster = Tk()
fenster.title('Hallo Welt!')


# a) Label oben anzeigen
label = Label(
    master=fenster,
    text='Hallo Welt!',
    font=('Courier', 14, 'bold'),
    fg='pink',      # Schriftfarbe
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

def update_label():
    """Aktualisiert den Text im Label mit dem gewünschten Text."""
    new_text = entry.get()
    # new_text = 'Button wurde geklickt!'
    label.config(text=new_text)

# d) Liste von Buttons mit Text und Funktion
buttons = [
    ('Text aktualisieren', update_label),
    ('Text löschen', clear_entry),
    ('Fenster schließen', close_window)
    
]

# Frame für Buttons erstellen (unten)
button_frame = Frame(master=fenster) # erstellt einen container im hauptfenster
button_frame.pack(side='bottom', pady=10)

# Buttons erstellen und in den Button-Frame packen
for text, command in buttons:
    button = Button(master=button_frame, text=text, command=command)
    button.pack(side='left', padx=10)  # horizontal nebeneinander
# Füge einen Radiobutton hinzu, der es ermöglicht, zwischen zwei Farben für den Hintergrund des Labels zu wechseln: Rot und Blau. Die Auswahl des Radiobuttons soll sofort den Hintergrund des Labels entsprechend der Auswahl ändern.
def change_label_background():
    """Ändert die Hintergrundfarbe des Labels basierend auf der Auswahl des Radiobuttons."""
    selected_color = color_var.get()
    label.config(bg=selected_color)

color_var = StringVar(value='gray')  # Standardfarbe
radiobutton_frame = Frame(master=fenster)
radiobutton_frame.pack(side='bottom', pady=10)
colors = [('Rot', 'red'), ('Blau', 'blue')]
for text, color in colors:
    radiobutton = Radiobutton(
        master=radiobutton_frame,
        text=text,
        variable=color_var,
        value=color,
        command=change_label_background
    )
    radiobutton.pack(side='left', padx=10)

# Verwende ein Canvas-Widget, um eine einfache Linie und einen Kreis zu zeichnen.
canvas = Canvas(master=fenster, width=200, height=100, bg='white')
canvas.pack(pady=10)
# Linie zeichnen
canvas.create_line(10, 10, 190, 10, fill='black', width=2)
# Kreis zeichnen
canvas.create_oval(70, 20, 130, 80, fill='yellow', outline='black')
# Hauptloop starten
fenster.mainloop()
