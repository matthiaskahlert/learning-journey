""" 
Entwickle ein Python-Skript, das ein einfaches GUI (Graphical User Interface) mit Tkinter erstellt. 
Deine Anwendung soll ein kleines Quiz darstellen, in dem der Nutzer zwischen drei Optionen (A, B, C) mittels Radiobuttons wählen kann. 
Jede Option soll eine andere Farbe repräsentieren (Rot, Grün, Blau). 
Nach der Auswahl und einem Klick auf eine Schaltfläche "Bestätigen" soll das Hintergrundfarbe des 
Anwendungsfensters entsprechend der Auswahl geändert werden. Nutze dazu die Kontrollvariable der Radiobuttons, 
um die Auswahl zu ermitteln und die Hintergrundfarbe anzupassen. 
Implementiere zudem eine Funktion, die die Farbänderung durchführt. 
Die GUI soll außerdem eine Schaltfläche "Zurücksetzen" enthalten, die die Hintergrundfarbe auf die 
Standardfarbe zurücksetzt und die Auswahl der Radiobuttons aufhebt.

a) Definiere die GUI-Elemente und die notwendigen Variablen.
b) Implementiere die Funktion zur Änderung der Hintergrundfarbe basierend auf der Auswahl.
c) Füge Eventhandler für die Schaltflächen "Bestätigen" und "Zurücksetzen" hinzu.
d) Organisiere die Widgets im Fenster mithilfe des Raster-Layouts. 
 """
""" 
 """

# Tkinter importieren
from tkinter import *

# Hauptfenster erstellen und konfigurieren
fenster = Tk()  # Fenster-Objekt erzeugen
fenster.title('Farbauswahl')  # Fenstertitel setzen
default_bg = fenster.cget("bg")
farben = StringVar() # speichert den aktuell ausgewählten Wert der Radiobutton-Gruppe.
# Label-Widget erstellen (Textanzeige)
label = Label(
    master = fenster, 
    text = 'Wähle eine Hintergrundfarbe!', 
    font=('Arial', 16), 
    fg='black', 
    bg='darkgray'
    )
label.grid(row=0, column=0, columnspan=2, pady=20)  # Raster-Layout

# Funktion, die beim Button-Klick ausgeführt wird
def button_klick():
    """Ändert die Hintergrundfarbe des Fensters je nach Radiobuttonauswahl."""
    auswahl = farben.get()
    if auswahl == 'A':
        fenster.config(bg='red')
    elif auswahl == 'B':
        fenster.config(bg='green')
    elif auswahl == 'C':
        fenster.config(bg='blue')

def zuruecksetzen():
    """Setzt Hintergrundfarbe und Auswahl zurück."""
    fenster.config(bg=default_bg)
    farben.set(None)

# Button-Widget erstellen
rot = Radiobutton(
    master=fenster,
    text='Rot!',
    value='A', # Wert der gespeichert wird, wenn dieser button aktiv ist, analog bei grün und blau
    variable=farben) # Alle Buttons gehören zur gleichen Gruppe, da sie die gleiche Variable verwenden.
grün = Radiobutton(
    master=fenster,
    text='Grün!',
    value= 'B',
    variable=farben)
blau = Radiobutton(
    master=fenster,
    text='Blau!',
    value='C',
    variable=farben)

button = Button(
    master=fenster, 
    text='Bestätigen!', 
    command=button_klick)

Zurücksetzen = Button(
    master=fenster,
    text='Zurücksetzen!',
    command=zuruecksetzen
)

rot.grid(row=1, column=0, sticky="w", padx=10)
grün.grid(row=2, column=0, sticky="w", padx=10)
blau.grid(row=3, column=0, sticky="w", padx=10)

button.grid(row=4, column=0, padx=10, pady=10, sticky="w")
Zurücksetzen.grid(row=4, column=1, padx=10, pady=10, sticky="w")




# Hauptloop starten (Fenster bleibt offen)
fenster.mainloop()