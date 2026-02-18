""" 
Entwickle ein Python-Programm, das ein Tkinter-Anwendungsfenster erstellt. 
In diesem Fenster sollen user aus drei verschiedenen Obstsorten (Äpfel, Bananen, Orangen) über Radiobuttons auswählen können. 
Nach der Auswahl und einem Klick auf eine Schaltfläche "Bestätigen" soll der ausgewählte Wert in einem Label angezeigt werden. 
Zusätzlich soll eine Funktion implementiert werden, die es ermöglicht, über eine Dialogbox eine Textdatei zu öffnen, 
deren Inhalt dann in einem Text-Widget dargestellt wird. 
Die Anwendung soll auch einen Button zum Schließen des Fensters enthalten. 
Berücksichtige die Verwendung von Threads, um sicherzustellen, dass die GUI reaktionsfähig bleibt, 
während die Datei geladen wird. 
 """

# Tkinter importieren
from tkinter import Text, filedialog, Tk, Label, Button, Radiobutton, StringVar
import threading

# Datei laden (thread)

def inhalt_laden(dateipfad):
    try:
        with open(dateipfad, 'r', encoding = 'utf-8') as datei:
            inhalt = datei.read()
            fenster.after(0, lambda: textfeld.insert('1.0', inhalt))  # Inhalt im Text-Widget anzeigen
    except Exception as e:
        fenster.after(0, lambda: textfeld.insert('1.0', f"Fehler beim Laden der Datei: {e}"))


def datei_öffnen():
    """Öffnet eine Dialogbox zum Auswählen einer Textdatei und zeigt deren Inhalt im Text-Widget an."""
    dateipfad = filedialog.askopenfilename(
        filetypes=[("Textdateien", "*.txt")]
    )
    if dateipfad:
        textfeld.delete(1.0, 'end')  # Vorherigen Inhalt löschen
        thread = threading.Thread(
            target=inhalt_laden, 
            args=(dateipfad,)
        )
        thread.start()


# Hauptfenster erstellen und konfigurieren
fenster = Tk()  # Fenster-Objekt erzeugen
fenster.title('Obstauswahl')  # Fenstertitel setzen
obstwahl = StringVar() # speichert den aktuell ausgewählten Wert der Radiobutton-Gruppe.
# Label-Widget erstellen (Textanzeige)
label = Label(
    master = fenster, 
    text = 'Wähle eine Obstsorte!', 
    font=('Arial', 16), 
    fg='black', 
    bg='darkgray'
    )
label.grid(row=0, column=0, columnspan=2, pady=20)  # Raster-Layout

# Funktion, die beim Button-Klick ausgeführt wird
def button_klick():
    """Ändert den Labeltext je nach Radiobuttonauswahl."""
    auswahl = obstwahl.get()
    if auswahl == 'A':
        label.config(text='Äpfel!')
    elif auswahl == 'B':
        label.config(text='Bananen!')
    elif auswahl == 'C':
        label.config(text='Orangen!')


# Button-Widget erstellen
eins = Radiobutton(
    master=fenster,
    text='Äpfel!',
    value='A', # Wert der gespeichert wird, wenn dieser button aktiv ist, analog bei grün und blau
    variable=obstwahl) # Alle Buttons gehören zur gleichen Gruppe, da sie die gleiche Variable verwenden.
zwei = Radiobutton(
    master=fenster,
    text='Bananen!',
    value= 'B',
    variable=obstwahl)
drei = Radiobutton(
    master=fenster,
    text='Orangen!',
    value='C',
    variable=obstwahl)

file_button = Button(
    fenster, 
    text="Datei öffnen", 
    command=datei_öffnen
    )

confirm_button = Button(
    master=fenster, 
    text='Bestätigen!', 
    command=button_klick
    )

close_button = Button(
    master=fenster,
    text='Fenster schließen',
    command=fenster.destroy
    )

# Textfeld: 
textfeld = Text(fenster, width=50, height=10)

textfeld.grid(row=7, column=0, columnspan=2, pady=10)
eins.grid(row=1, column=0, sticky="w", padx=10)
zwei.grid(row=2, column=0, sticky="w", padx=10)
drei.grid(row=3, column=0, sticky="w", padx=10)

confirm_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")
file_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")
close_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")


# Hauptloop starten (Fenster bleibt offen)
fenster.mainloop()
