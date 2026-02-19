# 11.11.A.01.pyw
""" 
Entwickle ein Python-Programm, das eine grafische Benutzeroberfläche (GUI) mit Tkinter erstellt. Dein Programm soll ein Anwendungsfenster mit folgenden Widgets und Funktionalitäten beinhalten:

a) Ein Eingabefeld (Entry-Widget), in den Benutzerinnen ihren Namen eingeben können.
b) Eine Schaltfläche (Button), die bei Klick eine Begrüßungsnachricht zusammen mit dem eingegebenen Namen in einem Label-Widget anzeigt.
c) Ein Radiobutton-Widget, mit dem Benutzerinnen ihre bevorzugte Begrüßungszeit auswählen können: "Guten Morgen", "Guten Tag", "Guten Abend". Die Auswahl soll die Begrüßungsnachricht beeinflussen.
d) Ein Text-Widget, das als Log dient, in dem jede durchgeführte Begrüßung mit Zeitstempel gespeichert wird.
e) Verwende das Raster-Layout (Grid), um die Widgets im Anwendungsfenster anzuordnen.
f) Implementiere eine Funktion, die die aktuelle Zeit und Datum als String zurückgibt, 
und verwende diese, um den Zeitstempel im Log zu generieren.
g) Gestalte das Anwendungsfenster und die Widgets ansprechend, indem du Größen, Farben und Schriftarten anpasst.  """

from tkinter import Tk, Label, Entry, Button, Radiobutton, StringVar, Text, END, font
from datetime import datetime

fenster = Tk()
fenster.title('Begrüßungs-GUI')
fenster.geometry('500x400')
fenster.config(bg='#222')

# Fonts
label_font = ('Arial', 14, 'bold')
entry_font = ('Arial', 12)
button_font = ('Arial', 12, 'bold')
log_font = ('Consolas', 10)

# a) Eingabefeld für Namen
name_label = Label(fenster, text='Name:', font=label_font, fg='white', bg='#222')
name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
name_entry = Entry(fenster, font=entry_font, width=20)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# c) Radiobuttons für Begrüßungszeit
zeit_var = StringVar(value='Guten Tag')
zeiten = ['Guten Morgen', 'Guten Tag', 'Guten Abend']
for i, zeit in enumerate(zeiten):
    Radiobutton(fenster, text=zeit, variable=zeit_var, value=zeit,
                font=entry_font, bg='#222', fg='white', selectcolor='#444').grid(row=1, column=i, padx=5, pady=5)

# b) Begrüßungsbutton und Label
begr_label = Label(fenster, text='', font=label_font, fg='#00fff7', bg='#222')
begr_label.grid(row=2, column=0, columnspan=3, pady=10)

def zeitstempel():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def begruessen():
    name = name_entry.get().strip()
    zeit = zeit_var.get()
    if name:
        msg = f'{zeit}, {name}!'
        begr_label.config(text=msg)
        log_entry = f'{zeitstempel()} - {msg}\n'
        log_text.insert(END, log_entry)
        log_text.see(END)
    else:
        begr_label.config(text='Bitte Namen eingeben.')

begr_button = Button(fenster, text='Begrüßen', command=begruessen,
                    font=button_font, bg='#ff2fd6', fg='black', activebackground='#ffe600')
begr_button.grid(row=3, column=0, columnspan=3, pady=10)

# d) Log-Textfeld
log_label = Label(fenster, text='Log:', font=label_font, fg='white', bg='#222')
log_label.grid(row=4, column=0, sticky='w', padx=10)
log_text = Text(fenster, font=log_font, width=50, height=8, bg='#111', fg='#39ff14')
log_text.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

fenster.mainloop()
