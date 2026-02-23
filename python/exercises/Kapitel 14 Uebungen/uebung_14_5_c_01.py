""" Aufgabe: Objektorientierte Programmierung

Du arbeitest als Softwareentwickler in einem Unternehmen, das sich auf die Entwicklung von Unternehmenssoftware spezialisiert hat. 
Dein aktuelles Projekt beinhaltet die Entwicklung einer Anwendung zur Verwaltung von Mitarbeiterdaten. 
Die Anwendung soll es ermöglichen, Mitarbeiterdaten zu erfassen, zu aktualisieren, zu löschen und zu durchsuchen. 
Die Mitarbeiterdaten umfassen Name, Position, Abteilung, Gehalt und Einstellungsdatum. 
Du sollst eine objektorientierte Lösung in Python entwerfen, die folgende Anforderungen erfüllt:

a) Entwerfe eine Klasse Mitarbeiter, die die Attribute Name, Position, Abteilung, Gehalt und Einstellungsdatum speichert. 
Implementiere Methoden zum Setzen und Abrufen dieser Attribute 
sowie eine Methode zeige_daten(), die alle Daten eines Mitarbeiters in einem formatierten String ausgibt.

b) Entwickle eine Klasse MitarbeiterVerwaltung, die eine Liste von Mitarbeiter-Objekten verwaltet. 
Diese Klasse soll Methoden zum Hinzufügen, 
Aktualisieren (basierend auf dem Namen), 
Löschen (basierend auf dem Namen) 
und Suchen (basierend auf dem Namen oder der Abteilung) von Mitarbeitern beinhalten.

c) Implementiere eine einfache Benutzeroberfläche unter Verwendung des tkinter-Moduls, 
die es dem Benutzer ermöglicht, Mitarbeiterdaten einzugeben, zu aktualisieren, zu löschen und zu durchsuchen. 
Die Benutzeroberfläche sollte auch eine Ausgabebereich haben, in dem die Ergebnisse von Suchoperationen 
oder die Daten eines neu hinzugefügten oder aktualisierten Mitarbeiters angezeigt werden. """

import tkinter as tk


# a) Klasse Mitarbeiter
class Mitarbeiter:
    def __init__(self, name, position, abteilung, gehalt, einstellungsdatum):
        self.name = name
        self.position = position
        self.abteilung = abteilung
        self.gehalt = gehalt
        self.einstellungsdatum = einstellungsdatum

    def zeige_daten(self):
        return (f"Name: {self.name}, "
                f"Position: {self.position}, "
                f"Abteilung: {self.abteilung}, "
                f"Gehalt: {self.gehalt}, "
                f"Einstellungsdatum: {self.einstellungsdatum}")


# b) Klasse MitarbeiterVerwaltung
class MitarbeiterVerwaltung:
    def __init__(self):
        self.liste = []

    def hinzufuegen(self, mitarbeiter):
        self.liste.append(mitarbeiter)

    def aktualisieren(self, name, position, abteilung, gehalt, datum):
        for m in self.liste:
            if m.name == name:
                m.position = position
                m.abteilung = abteilung
                m.gehalt = gehalt
                m.einstellungsdatum = datum
                return True
        return False

    def loeschen(self, name):
        for m in self.liste:
            if m.name == name:
                self.liste.remove(m)
                return True
        return False

    def suchen(self, suchbegriff):
        return [m.zeige_daten() for m in self.liste
                if suchbegriff.lower() in m.name.lower()
                or suchbegriff.lower() in m.abteilung.lower()]


# c) Einfache GUI
class App:
    def __init__(self, root):
        self.verwaltung = MitarbeiterVerwaltung()
        self.root = root
        self.root.title("Mitarbeiterverwaltung")

        # Eingabefelder
        tk.Label(root, text="Name").grid(row=0)
        tk.Label(root, text="Position").grid(row=1)
        tk.Label(root, text="Abteilung").grid(row=2)
        tk.Label(root, text="Gehalt").grid(row=3)
        tk.Label(root, text="Einstellungsdatum").grid(row=4)

        self.name = tk.Entry(root)
        self.position = tk.Entry(root)
        self.abteilung = tk.Entry(root)
        self.gehalt = tk.Entry(root)
        self.datum = tk.Entry(root)

        self.name.grid(row=0, column=1)
        self.position.grid(row=1, column=1)
        self.abteilung.grid(row=2, column=1)
        self.gehalt.grid(row=3, column=1)
        self.datum.grid(row=4, column=1)

        # Buttons
        tk.Button(root, text="Hinzufügen", command=self.hinzufuegen).grid(row=5, column=0)
        tk.Button(root, text="Aktualisieren", command=self.aktualisieren).grid(row=5, column=1)
        tk.Button(root, text="Löschen", command=self.loeschen).grid(row=6, column=0)
        tk.Button(root, text="Suchen", command=self.suchen).grid(row=6, column=1)

        # Ausgabefeld
        self.output = tk.Text(root, height=8, width=60)
        self.output.grid(row=7, column=0, columnspan=2)

    def hinzufuegen(self):
        m = Mitarbeiter(
            self.name.get(),
            self.position.get(),
            self.abteilung.get(),
            self.gehalt.get(),
            self.datum.get()
        )
        self.verwaltung.hinzufuegen(m)
        self.zeige_text("Hinzugefügt:\n" + m.zeige_daten())

    def aktualisieren(self):
        erfolg = self.verwaltung.aktualisieren(
            self.name.get(),
            self.position.get(),
            self.abteilung.get(),
            self.gehalt.get(),
            self.datum.get()
        )
        self.zeige_text("Aktualisiert" if erfolg else "Nicht gefunden")

    def loeschen(self):
        erfolg = self.verwaltung.loeschen(self.name.get())
        self.zeige_text("Gelöscht" if erfolg else "Nicht gefunden")

    def suchen(self):
        ergebnisse = self.verwaltung.suchen(self.name.get())
        if ergebnisse:
            self.zeige_text("\n\n".join(ergebnisse))
        else:
            self.zeige_text("Keine Ergebnisse")

    def zeige_text(self, text):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, text)


# Start
root = tk.Tk()
app = App(root)
root.mainloop()