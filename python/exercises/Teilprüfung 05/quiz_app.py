""" 
Entwickle eine Python-Anwendung, die eine grafische Benutzeroberfläche (GUI) mit Tkinter erstellt. 
Diese Anwendung soll ein einfaches Quiz mit Fragen und mehreren Antwortmöglichkeiten über Radiobuttons darstellen. 
Zudem soll sie die Möglichkeit bieten, die Ergebnisse in einer Datei zu speichern und frühere Ergebnisse zu laden. 
Die Anwendung soll auch Threads verwenden, um den Timer für jede Frage zu handhaben, ohne die GUI zu blockieren.

a) Definiere ein Python-Modul quiz_app.py, das eine Klasse QuizApp enthält. 
Diese Klasse soll das Hauptfenster mit einem Titel, einem Bereich für die Frage, 
Radiobuttons für die Antwortmöglichkeiten, einem Timer-Label, einem "Nächste Frage"-Button 
und einem "Ergebnisse speichern"-Button erstellen.

b) Implementiere die Funktionalität, um Fragen und Antwortmöglichkeiten anzuzeigen. 
Verwende für jede Frage ein Dictionary, das die Frage und eine Liste von Antwortmöglichkeiten enthält. 
Die richtige Antwort soll ebenfalls in diesem Dictionary markiert sein.

c) Füge einen Timer hinzu, der für jede Frage 30 Sekunden läuft. 
Verwende Threads, um den Timer parallel zur GUI laufen zu lassen, sodass die GUI während des Countdowns reaktionsfähig bleibt.

d) Implementiere Eventhandler für die "Nächste Frage"- und "Ergebnisse speichern"-Buttons. 
Der "Nächste Frage"-Button soll die nächste Frage laden und den Timer zurücksetzen. 
Der "Ergebnisse speichern"-Button soll die Ergebnisse in einer Datei speichern 
und die Möglichkeit bieten, diese Ergebnisse bei einem späteren Programmstart zu laden.

e) Verwende Dialogboxen, um den Pfad für das Speichern und Laden der Ergebnisse auszuwählen. 
 """

import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import time
import json

# mkahlert_teilpruefung_05
# Hinweis zu quiz_app.py:Aufgabe a) sieht die Verwendung einer Klasse vor.
# Da Klassen im Lehrplan erst nach Kapitel 12 eingeführt werden (uns zwar in Kapitel 14),
# wurde die vorliegende Lösung ohne objektorientierte Struktur umgesetzt.

fragen_liste = [
    {
        "frage": "Welche Sprache wird häufig für Data Science verwendet?",
        "optionen": ["Python", "HTML", "CSS", "Markdown"],
        "richtige_antwort": 0
    },
    {
        "frage": "Wofür steht GUI?",
        "optionen": ["General User Input", "Graphical User Interface", "Git User Interface", "Graph Unit Index"],
        "richtige_antwort": 1
    },
    {
        "frage": "Was macht ein Thread?",
        "optionen": ["Speichert Dateien", "Läuft parallel zum Rest des Programms", "Macht Grafiken", "Ist ein Radiobutton"],
        "richtige_antwort": 1
    },
]

FRAGE_DAUER = 30 # in Sekunden


# Variablen

aktuelle_frage_nummer = 0
punkte = 0
alle_antworten = []
verbleibende_zeit = FRAGE_DAUER


# Fenster
fenster = tk.Tk()
fenster.title("Quizfragen")
fenster.geometry("600x400")

ausgewaehlte_antwort = tk.IntVar() # Variable für die radiobuttons, speichert die Nummer der ausgewählten Antwort
ausgewaehlte_antwort.set(None) # Keine Antwort ausgewählt


# GUI

frage_text = tk.Label(master = fenster, font=("Arial", 12, 'bold'), wraplength=500, bg="lightblue", padx=10, pady=10) # wraplength sorgt für RTextumbruch nach 500 pixeln
frage_text.pack(pady=10)

radio1 = tk.Radiobutton( master = fenster, variable=ausgewaehlte_antwort, value=0)
radio1.pack(anchor="w", padx=20)
radio2 = tk.Radiobutton( master = fenster, variable=ausgewaehlte_antwort, value=1)
radio2.pack(anchor="w", padx=20)
radio3 = tk.Radiobutton( master = fenster, variable=ausgewaehlte_antwort, value=2)
radio3.pack(anchor="w", padx=20)
radio4 = tk.Radiobutton(master = fenster, variable=ausgewaehlte_antwort, value=3)
radio4.pack(anchor="w", padx=20)

zeit_text = tk.Label(master = fenster, font=("Arial", 12, "bold"))
zeit_text.pack(pady=10)


# Funktionen

def frage_anzeigen():
    """ Zeigt die aktuelle Frage und die Antwortmöglichkeiten an. Setzt den Timer zurück. """
    global verbleibende_zeit

    frage = fragen_liste[aktuelle_frage_nummer]

    frage_text.config(text=frage["frage"])

    radio1.config(text=frage["optionen"][0])
    radio2.config(text=frage["optionen"][1])
    radio3.config(text=frage["optionen"][2])
    radio4.config(text=frage["optionen"][3])

    ausgewaehlte_antwort.set(None) # Keine Antwort ausgewählt

    verbleibende_zeit = FRAGE_DAUER
    zeit_text.config(text="Zeit: " + str(verbleibende_zeit))


def antwort_pruefen(zeit_abgelaufen=False):
    """ Prüft die ausgewählte Antwort und aktualisiert die Punkte. """
    global punkte

    gewaehlte_nummer = ausgewaehlte_antwort.get()
    richtige_nummer = fragen_liste[aktuelle_frage_nummer]["richtige_antwort"]

    ist_richtig = (gewaehlte_nummer == richtige_nummer) and not zeit_abgelaufen

    if ist_richtig:
        punkte += 1

    alle_antworten.append({
        "frage": fragen_liste[aktuelle_frage_nummer]["frage"],
        "gewaehlt": gewaehlte_nummer,
        "richtig": richtige_nummer,
        "korrekt": ist_richtig
    })


def naechste_frage(zeit_abgelaufen=False):
    """ Geht zur nächsten Frage über. """
    global aktuelle_frage_nummer

    antwort_pruefen(zeit_abgelaufen)

    aktuelle_frage_nummer += 1

    if aktuelle_frage_nummer >= len(fragen_liste):
        messagebox.showinfo("Fertig!", "Du hast " + str(punkte) + " Punkte erreicht.")
    else:
        frage_anzeigen()
        timer_starten()


# Timer

def timer_thread():
    """ Führt den Timer im Hintergrund aus. """
    global verbleibende_zeit

    while verbleibende_zeit > 0:
        fenster.after(0, lambda: zeit_text.config(text="Zeit: " + str(verbleibende_zeit))) # aktualisiert Timer im Hauptthread
        time.sleep(1) # warte eine sekunde
        verbleibende_zeit -= 1 # reduziert die verbleibende Zeit um 1 Sekunde

    fenster.after(0, lambda: naechste_frage(True)) # Zeit abgelaufen, dann nächste frage anzeigen


def timer_starten():
    """ Startet den Timer in einem separaten Thread. """
    thread = threading.Thread(target=timer_thread) # Erstellt einen neuen Thread. wenn du startest, führe timer_thread aus
    thread.daemon = True # dies verhindert, dass der Timer beim beenden des programms weiterläuft und somit schließen des Fensters verhindert
    thread.start() # hauptthread und timerthread laufen jetzt gleichzeitig


# Speichern / Laden

def ergebnisse_speichern():
    """ Speichert die Ergebnisse in einer JSON-Datei. """
    dateipfad = filedialog.asksaveasfilename(defaultextension=".json")
    if not dateipfad:
        return

    daten = {
        "punkte": punkte,
        "gesamt": len(fragen_liste),
        "antworten": alle_antworten
    }
    try:
        with open(dateipfad, "w", encoding="utf-8") as datei:
            json.dump(daten, datei, indent=2, ensure_ascii=False)
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Speichern der Ergebnisse: {e}")


def ergebnisse_laden():
    """ Lädt die Ergebnisse aus einer JSON-Datei und zeigt sie an. """
    dateipfad = filedialog.askopenfilename()
    if not dateipfad:
        return

    try:
        with open(dateipfad, "r", encoding="utf-8") as datei:
            daten = json.load(datei)
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Laden der Ergebnisse: {e}")
        return

    messagebox.showinfo("Geladen",
                        "Gespeicherte Punkte: "
                        + str(daten["punkte"])
                        + " von "
                        + str(daten["gesamt"]))


# Buttons

tk.Button(master = fenster, text="Nächste Frage", command=naechste_frage).pack(pady=10)
tk.Button(master = fenster, text="Ergebnisse speichern", command=ergebnisse_speichern).pack(pady=10)
tk.Button(master = fenster, text="Ergebnisse laden", command=ergebnisse_laden).pack(pady=10)



# Start

if __name__ == "__main__": 
    frage_anzeigen()
    timer_starten()
    fenster.mainloop()
