""" 
Entwickle ein Python-Programm, das ein Tkinter-Anwendungsfenster mit einer grafischen Benutzeroberfläche erstellt. 
Dein Programm soll folgende Elemente beinhalten und Funktionen ausführen:

a) Importiere das Tkinter-Modul korrekt und initialisiere das Hauptfenster der Anwendung. 
Benenne das Fenster als "Mein GUI".
b) Füge ein Label-Widget hinzu, das den Text "Willkommen zu deinem GUI!" in der Schriftart "Arial", Größe 16, 
in blauer Schrift auf gelbem Hintergrund anzeigt. Positioniere das Label zentral im Fenster.
c) Erstelle eine Schaltfläche (Button), die beschriftet ist mit "Klick mich!". 
Wenn der Button geklickt wird, soll der Text des Labels zu "Button wurde geklickt!" geändert werden. 
Achte darauf, dass die Schaltfläche und das Label gut sichtbar und nicht übereinander angeordnet sind.
d) Implementiere eine Funktion, die aufgerufen wird, wenn der Button geklickt wird und die den Text des Labels ändert. 
Verwende die Methode config des Label-Widgets, um den Text zu aktualisieren.
e) Stelle sicher, dass das Fenster eine feste Größe hat und nicht vom Benutzer in der Größe verändert werden kann.
f) Das Programm soll in einer Endlosschleife laufen, sodass das Fenster offen bleibt, bis der Benutzer es manuell schließt. 
 """

# Tkinter importieren
from tkinter import Tk, Label, Button

# Hauptfenster erstellen und konfigurieren
fenster = Tk()  # Fenster-Objekt erzeugen
fenster.title('Mein GUI')  # Fenstertitel setzen
fenster.geometry('400x200')  # Fenstergröße festlegen
fenster.resizable(False, False)  # Fenstergröße fixieren

# Label-Widget erstellen (Textanzeige)
label = Label(
    master = fenster, 
    text = 'Willkommen zu deinem GUI!', 
    font=('Arial', 16), 
    fg='blue', 
    bg='yellow'
    )
label.pack(pady=20)  # Label mittig platzieren

# Funktion, die beim Button-Klick ausgeführt wird
def button_klick():
    """Ändert den Text des Labels, wenn der Button geklickt wird."""
    label.config(text='Button wurde geklickt!')

# Button-Widget erstellen
button = Button(
    master=fenster, 
    text='Klick mich!', 
    command=button_klick)
button.pack(side='left', padx=10)  # Button links platzieren

# Hauptloop starten (Fenster bleibt offen)
fenster.mainloop()
